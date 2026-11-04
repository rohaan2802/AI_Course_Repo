#!/usr/bin/env python3


import copy, math, random, time, os, sys
from itertools import product as cartesian_product

try:
    import dearpygui.dearpygui as dpg
except ImportError:
    print("ERROR: Dear PyGui not installed.  Run:  pip install dearpygui")
    sys.exit(1)

#  SECTION 1 — PROBABILITY TABLES  (stored as data structures, not inline magic)

# 9-sided combat die → 6 outcome groups
COMBAT_OUTCOMES = [
    dict(id="fail_pen",  prob=0.20, otype="fail",    e_loss=1, advance=False, bonus=0),
    dict(id="fail_free", prob=0.15, otype="fail",    e_loss=0, advance=False, bonus=0),
    dict(id="partial",   prob=0.16, otype="partial", e_loss=0, advance=False, bonus=0),
    dict(id="part_adv",  prob=0.12, otype="partial", e_loss=0, advance=True,  bonus=0),
    dict(id="full",      prob=0.26, otype="full",    e_loss=0, advance=False, bonus=0),
    dict(id="critical",  prob=0.11, otype="critical",e_loss=0, advance=False, bonus=2),
]
assert abs(sum(o["prob"] for o in COMBAT_OUTCOMES) - 1.0) < 1e-9, "Combat probs must sum to 1"

# 4-sided minefield event
MINE_OUTCOMES = [
    dict(id="safe",     prob=0.40, e_loss=0, disable=0, detonate=False),
    dict(id="drain",    prob=0.30, e_loss=3, disable=0, detonate=False),
    dict(id="disabled", prob=0.20, e_loss=0, disable=2, detonate=False),
    dict(id="detonate", prob=0.10, e_loss=5, disable=0, detonate=True),
]

# Environmental event names (4 drawn uniformly)
ENV_EVENTS = ["supply_drop", "earthquake", "reinforcement", "fog_of_war"]

#  CONSTANTS

EMPTY     = "."
OBSTACLE  = "X"
FORTRESS  = "F"
MINEFIELD = "M"
AGENTS    = ["A", "B", "C"]
DIRS      = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # N S W E

#  SECTION — AGENT CONFIGS  (structural asymmetry, NOT if-else on agent ID)

class AgentCfg:
    """Base config – subclassed to enforce per-agent capability."""
    aid       = ""
    label     = ""
    depth     = 0
    obs_range = None   # None = full board, int = radius
    branches  = "all"  # "all" | "top2"
    eval_lvl  = 1      # 1=greedy  3=intermediate  5=expert
    use_tt    = False  # transposition table

class ExpertCfg(AgentCfg):
    aid="A"; label="Expert";       depth=4; obs_range=None; branches="all";  eval_lvl=5; use_tt=True #7

class IntermCfg(AgentCfg):
    aid="B"; label="Intermediate"; depth=3; obs_range=5;    branches="all";  eval_lvl=3; use_tt=False#5

class NoviceCfg(AgentCfg):
    aid="C"; label="Novice";       depth=2; obs_range=3;    branches="top2"; eval_lvl=1; use_tt=False#3

#These are the normal values 
#These are the dev/testing values (bottom)

#class ExpertCfg(AgentCfg):
  #  aid="A"; label="Expert";       depth=3; obs_range=None; branches="all";  eval_lvl=5; use_tt=True

#class IntermCfg(AgentCfg):
   # aid="B"; label="Intermediate"; depth=2; obs_range=5;    branches="all";  eval_lvl=3; use_tt=False

#class NoviceCfg(AgentCfg):
  #  aid="C"; label="Novice";       depth=2; obs_range=3;    branches="top2"; eval_lvl=1; use_tt=False

CFGS = {"A": ExpertCfg(), "B": IntermCfg(), "C": NoviceCfg()}

#  SECTION — GAME STATE CLASSES


class Unit:
    __slots__ = ("aid", "idx", "pos", "disabled")
    def __init__(self, aid, idx, pos):
        self.aid = aid
        self.idx = idx
        self.pos = pos          # (row, col)
        self.disabled = 0       # turns remaining disabled (minefield)

    def clone(self):
        u = Unit(self.aid, self.idx, self.pos)
        u.disabled = self.disabled
        return u


class AgentState:
    __slots__ = ("aid", "energy", "score", "units", "alive")
    def __init__(self, aid, start_pos):
        self.aid    = aid
        self.energy = 20
        self.score  = 0
        self.units  = [Unit(aid, 0, start_pos), Unit(aid, 1, start_pos)]
        self.alive  = True

    def clone(self):
        a = AgentState.__new__(AgentState)
        a.aid    = self.aid
        a.energy = self.energy
        a.score  = self.score
        a.units  = [u.clone() for u in self.units]
        a.alive  = self.alive
        return a


class GameState:
    """Complete mutable game state."""
    def __init__(self):
        self.N = 0; self.M = 0; self.R = 30
        self.base_grid = []         # original grid rows (read-only reference)
        self.cell      = {}         # (r,c) → current cell type
        self.owner     = {}         # (r,c) → aid | None
        self.defense   = {}         # (r,c) → int
        self.agents    = {}         # aid   → AgentState
        self.round     = 1
        self.turn_idx  = 0          # 0=A, 1=B, 2=C
        self.temp_f    = {}         # supply-drop temp fortress: (r,c)→rounds_left
        self.over      = False
        self.winner    = None
        self.log       = []         # shared list – per-move reports
        self.move_num  = 0

    @property
    def cur(self):
        return AGENTS[self.turn_idx]

    def clone(self):
        s = GameState.__new__(GameState)
        s.N = self.N; s.M = self.M; s.R = self.R
        s.base_grid = self.base_grid            # shared, read-only
        s.cell      = dict(self.cell)
        s.owner     = dict(self.owner)
        s.defense   = dict(self.defense)
        s.agents    = {k: v.clone() for k, v in self.agents.items()}
        s.round     = self.round
        s.turn_idx  = self.turn_idx
        s.temp_f    = dict(self.temp_f)
        s.over      = self.over
        s.winner    = self.winner
        s.log       = self.log          # shared reference
        s.move_num  = self.move_num
        return s

    # ── helpers 
    def ok(self, r, c):
        return 0 <= r < self.N and 0 <= c < self.M

    def passable(self, r, c):
        return self.ok(r, c) and self.cell.get((r, c)) != OBSTACLE

    def owned_by(self, aid):
        return [p for p, a in self.owner.items() if a == aid]

    def non_obstacle(self):
        return [p for p, t in self.cell.items() if t != OBSTACLE]

    def round_pts(self, aid):
        return sum(3 if self.cell.get(p) == FORTRESS else 1
                   for p in self.owned_by(aid))

    def get_hash(self):
        return hash((
            self.round, self.turn_idx,
            tuple(sorted(self.owner.items())),
            tuple(sorted(self.defense.items())),
            tuple(sorted(
                (aid, ag.energy, tuple(u.pos for u in ag.units))
                for aid, ag in self.agents.items()
            ))
        ))


#  SECTION — BOARD LOADING

def load_board(filename="board.txt"):
    with open(filename) as f:
        lines = [l.rstrip() for l in f.readlines() if l.strip()]
    idx = 0
    N, M, R = map(int, lines[idx].split()); idx += 1
    base = []
    for r in range(N):
        base.append(list(lines[idx + r]))
    idx += N
    starts = {}
    for aid in AGENTS:
        x, y = map(int, lines[idx].split()); idx += 1
        starts[aid] = (y, x)   # board.txt gives col(x) then row(y)

    s = GameState()
    s.N = N; s.M = M; s.R = R; s.base_grid = base

    for r in range(N):
        for c in range(M):
            ch  = base[r][c]
            pos = (r, c)
            if ch == OBSTACLE:
                s.cell[pos]  = OBSTACLE
            elif ch == FORTRESS:
                s.cell[pos]  = FORTRESS
                s.owner[pos] = None
                s.defense[pos] = 2
            elif ch == MINEFIELD:
                s.cell[pos]  = MINEFIELD
            else:
                s.cell[pos]  = EMPTY

    for aid, pos in starts.items():
        s.agents[aid] = AgentState(aid, pos)
        if s.cell.get(pos) not in (OBSTACLE, FORTRESS, MINEFIELD):
            s.owner[pos]   = aid
            s.defense[pos] = 1

    s.log = []; s.move_num = 0
    return s


#  SECTION — ACTION GENERATION

def unit_actions(state, aid, unit):
    """All legal single-unit actions."""
    if unit.disabled > 0:
        return [("wait",)]
    ag = state.agents[aid]
    if ag.energy <= 0:
        return [("wait",)]    # locked to wait (free cost)

    r, c = unit.pos
    acts = [("wait",)]

    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if not state.passable(nr, nc):
            continue
        pos2 = (nr, nc)
        own2 = state.owner.get(pos2)

        # Move: to any non-own cell
        if own2 != aid:
            acts.append(("move", dr, dc))

        # Attack (stay in place): opponent-owned adjacent
        if own2 is not None and own2 != aid:
            acts.append(("attack", dr, dc))

        # Fortify: own adjacent cell with room to grow
        if own2 == aid and state.defense.get(pos2, 1) < 3:
            acts.append(("fortify", dr, dc))

    return acts


def unit_actions_pruned(state, aid, unit):
    """
    Generate unit actions and keep only the top-4 by quick heuristic.
    This reduces the joint action Cartesian product from ~25 to ~16 max.
    Improves pruning efficiency significantly at deeper depths.
    """
    acts = unit_actions(state, aid, unit)
    if len(acts) <= 4:
        return acts   # already small enough, no filtering needed

    def quick_score(a):
        if a[0] == "attack":
            dr, dc  = a[1], a[2]
            pos2    = (unit.pos[0] + dr, unit.pos[1] + dc)
            def_val = state.defense.get(pos2, 1)
            ctype   = state.cell.get(pos2, EMPTY)
            score   = 5 - def_val   # lower defense = better target
            if ctype == FORTRESS: score += 4
            return score
        elif a[0] == "move":
            dr, dc = a[1], a[2]
            pos2   = (unit.pos[0] + dr, unit.pos[1] + dc)
            ctype  = state.cell.get(pos2, EMPTY)
            if ctype == FORTRESS: return 4
            if ctype == MINEFIELD: return -1   # deprioritise mines
            # Reward moving toward nearest fortress
            fortresses = [p for p, t in state.cell.items() if t == FORTRESS]
            if fortresses:
                curr_d = min(manhattan(unit.pos, fp) for fp in fortresses)
                new_d  = min(manhattan(pos2, fp) for fp in fortresses)
                if new_d < curr_d: return 3   # getting closer to fortress
            return 1
        elif a[0] == "fortify":
            dr, dc = a[1], a[2]
            pos2   = (unit.pos[0] + dr, unit.pos[1] + dc)
            # Only fortify if opponent unit is nearby (actual threat)
            opp_nearby = any(
                manhattan(pos2, u.pos) <= 2
                for o in AGENTS if o != aid
                for u in state.agents[o].units
            )
            return 2 if opp_nearby else 0
        else:  # wait
            return -2   # wait is last resort

    return sorted(acts, key=quick_score, reverse=True)[:4]


def joint_actions(state, aid):
    """All legal joint (unit0, unit1) action pairs — pruned to top actions."""
    ag = state.agents[aid]
    if not ag.alive:
        return [((("wait",), ("wait",)))]
    a0 = unit_actions_pruned(state, aid, ag.units[0])
    a1 = unit_actions_pruned(state, aid, ag.units[1])
    return list(cartesian_product(a0, a1))

def action_str(jact):
    """Human-readable joint action string."""
    parts = []
    for a in jact:
        if a[0] == "wait":
            parts.append("Wait")
        elif a[0] == "fortify":
            dr, dc = a[1], a[2]
            direction = {(-1,0):"N",(1,0):"S",(0,-1):"W",(0,1):"E"}.get((dr,dc),"?")
            parts.append(f"Fortify({direction})")
        elif a[0] == "move":
            dr, dc = a[1], a[2]
            direction = {(-1,0):"↑",(1,0):"↓",(0,-1):"←",(0,1):"→"}.get((dr,dc),"?")
            parts.append(f"Move{direction}")
        elif a[0] == "attack":
            dr, dc = a[1], a[2]
            direction = {(-1,0):"↑",(1,0):"↓",(0,-1):"←",(0,1):"→"}.get((dr,dc),"?")
            parts.append(f"Attack{direction}")
    return " | ".join(parts)

#  SECTION  — STATE TRANSITIONS

def weighted_sample(outcomes):
    """Sample one outcome dict by probability weight."""
    r = random.random()
    cumul = 0.0
    for oc in outcomes:
        cumul += oc["prob"]
        if r < cumul:
            return oc
    return outcomes[-1]


def apply_combat_outcome(s, aid, unit, target_pos, oc, stay_put):
    
    ag = s.agents[aid]
    otype = oc["otype"]

    # Attacker energy loss
    if oc["e_loss"] > 0:
        ag.energy = max(0, ag.energy - oc["e_loss"])

    if otype == "fail":
        pass  # defender unchanged

    elif otype == "partial":
        ctype = s.cell.get(target_pos, EMPTY)
        s.owner[target_pos] = None
        if ctype == FORTRESS:
            s.defense[target_pos] = 2   # unowned fortress resets
        else:
            s.defense.pop(target_pos, None)
        if oc["advance"] and not stay_put:
            unit.pos = target_pos

    elif otype in ("full", "critical"):
        cur_def = s.defense.get(target_pos, 1)
        new_def = cur_def - 1
        if new_def <= 0:
            s.owner[target_pos]   = aid
            ctype = s.cell.get(target_pos, EMPTY)
            s.defense[target_pos] = 2 if ctype == FORTRESS else 1
            ag.score += oc["bonus"]
        else:
            s.defense[target_pos] = new_def


def apply_joint_action_with_outcome(state, aid, jact, combat_oc=None):
    
    s = state.clone()
    ag = s.agents[aid]
    first_combat_done = False

    for i, act in enumerate(jact):
        unit = ag.units[i]

        if unit.disabled > 0:
            unit.disabled = max(0, unit.disabled - 1)
            continue

        atype = act[0]

        if atype == "wait":
            if ag.energy > 0:
                ag.energy -= 1
            continue

        # All non-wait actions cost 1 energy (unless already 0)
        if ag.energy > 0:
            ag.energy -= 1

        if atype == "fortify":
            dr, dc = act[1], act[2]
            pos2 = (unit.pos[0] + dr, unit.pos[1] + dc)
            s.defense[pos2] = min(3, s.defense.get(pos2, 1) + 1)

        elif atype in ("move", "attack"):
            dr, dc = act[1], act[2]
            pos2 = (unit.pos[0] + dr, unit.pos[1] + dc)
            own2 = s.owner.get(pos2)

            if own2 is not None and own2 != aid:
                # Combat — use provided outcome for first combat, else sample
                if combat_oc is not None and not first_combat_done:
                    oc = combat_oc
                    first_combat_done = True
                else:
                    oc = weighted_sample(COMBAT_OUTCOMES)
                apply_combat_outcome(s, aid, unit, pos2, oc, stay_put=(atype == "attack"))

            elif atype == "move":
                ctype = s.cell.get(pos2, EMPTY)
                if ctype == MINEFIELD:
                    unit.pos = pos2
                    # Mine resolved in real game only (Q&A #5 — not in search tree)
                elif own2 is None:
                    unit.pos = pos2
                    if ctype not in (OBSTACLE, FORTRESS):
                        s.owner[pos2]   = aid
                        s.defense[pos2] = 1
                    elif ctype == FORTRESS and s.owner.get(pos2) is None:
                        # Entering unowned fortress doesn't capture yet
                        unit.pos = pos2

    return s


def has_combat(state, aid, jact):
    """True if jact will trigger at least one combat."""
    ag = state.agents[aid]
    for i, act in enumerate(jact):
        if act[0] in ("move", "attack"):
            unit = ag.units[i]
            dr, dc = act[1], act[2]
            pos2 = (unit.pos[0] + dr, unit.pos[1] + dc)
            own2 = state.owner.get(pos2)
            if own2 is not None and own2 != aid:
                return True
    return False


def get_chance_branches(state, aid, jact, branch_mode="all"):
    """
    Returns list of (probability, outcome_dict) — NO state clones yet.
    States are created lazily inside expectiminimax only when needed.
    """
    if not has_combat(state, aid, jact):
        return [(1.0, None)]   # None = no combat outcome, apply directly

    outcomes = list(COMBAT_OUTCOMES)
    if branch_mode == "top2":
        outcomes = sorted(outcomes, key=lambda o: o["prob"], reverse=True)[:2]
        total    = sum(o["prob"] for o in outcomes)
        outcomes = [dict(o, prob=o["prob"] / total) for o in outcomes]

    return [(oc["prob"], oc) for oc in outcomes]



#  SECTION 8 — EVALUATION FUNCTIONS

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def evaluate(state, searcher, cfg):
    """
    Heuristic board evaluation for `searcher`.
    Complexity scales with cfg.eval_lvl:
      1 = greedy (score differential only)        — Novice
      3 = 3 factors                               — Intermediate
      5 = full 5-factor function                  — Expert
    """
    ag = state.agents[searcher]
    if not ag.alive:
        return -1e6

    opponents = [a for a in AGENTS if a != searcher and state.agents[a].alive]
    n_opp = max(len(opponents), 1)

    # ── Factor 1: Score differential 
    opp_avg_score = sum(state.agents[o].score for o in opponents) / n_opp
    score_diff = ag.score - opp_avg_score

    if cfg.eval_lvl == 1:   # Novice – greedy
        return float(score_diff)

    # ── Factor 2: Territory control 
    my_cells    = state.owned_by(searcher)
    f_count     = sum(1 for p in my_cells if state.cell.get(p) == FORTRESS)
    territory   = len(my_cells) + 2.0 * f_count

    # ── Factor 3: Energy advantage 
    opp_avg_e = sum(state.agents[o].energy for o in opponents) / n_opp
    e_adv     = ag.energy - opp_avg_e

    if cfg.eval_lvl == 3:   # Intermediate – 3 factors
        return 2.5 * score_diff + 1.5 * territory + 0.6 * e_adv

    # ── Factor 4: Positional advantage (proximity to Fortress tiles) ──────────
    fortresses = [p for p, t in state.cell.items() if t == FORTRESS]
    pos_adv = 0.0
    for unit in ag.units:
        for fp in fortresses:
            d = manhattan(unit.pos, fp)
            if d == 0:
                pos_adv += 5.0
            elif d <= 4:
                pos_adv += max(0.0, 4.0 - d) * 0.8

    # ── Factor 5: Threat assessment (opponent units adjacent to owned cells) ──
    opp_unit_pos = set()
    for o in opponents:
        for u in state.agents[o].units:
            opp_unit_pos.add(u.pos)

    threat = 0.0
    for p in my_cells:
        for dr, dc in DIRS:
            if (p[0] + dr, p[1] + dc) in opp_unit_pos:
                threat += 1.0

    # Expert – full 5 factors
    return (3.0 * score_diff
            + 2.0 * territory
            + 0.8 * pos_adv
            - 1.2 * threat
            + 0.5 * e_adv)


#  SECTION  EXPECTIMINIMAX WITH ALPHA-BETA PRUNING

class SearchStats:
    def __init__(self):
        self.nodes  = 0
        self.pruned = 0


def expectiminimax(state, depth, alpha, beta, searcher, cfg, stats, tt):
    
    # ── Transposition table lookup (Expert only) 
    h = None
    if tt is not None:
        h = state.get_hash()
        if h in tt and tt[h][0] >= depth:
            return tt[h][1], tt[h][2]

    # ── Terminal / depth-limit 
    if depth == 0 or state.over:
        stats.nodes += 1
        return evaluate(state, searcher, cfg), None

    cur    = state.cur
    jacts  = joint_actions(state, cur)
    if not jacts:
        stats.nodes += 1
        return evaluate(state, searcher, cfg), None

    # ── Move ordering: attacks first, then moves, then wait (improves pruning) ─
    def move_priority(ja):
        p = 0
        for a in ja:
            if a[0] == "attack":  p += 3
            elif a[0] == "move":  p += 2
            elif a[0] == "fortify": p += 1
        return -p

    jacts.sort(key=move_priority)

    is_max   = (cur == searcher)
    best_val = -math.inf if is_max else math.inf
    best_act = jacts[0]

    for ji, jact in enumerate(jacts):
        stats.nodes += 1

        # ── CHANCE NODE: probability-weighted sum (NO pruning inside) ─────────
        branches = get_chance_branches(state, cur, jact, cfg.branches)
        expected  = 0.0
        for prob, combat_oc in branches:
            # Create state clone HERE (lazily) — only when we actually need it
            ns = apply_joint_action_with_outcome(state, cur, jact, combat_oc)

            # Advance the turn pointer
            ns.turn_idx = (ns.turn_idx + 1) % 3

            # End of round handling
            if ns.turn_idx == 0:
                ns.round += 1
                if ns.round > ns.R:
                    ns.over = True
                else:
                    for a in AGENTS:
                        if ns.agents[a].alive:
                            ns.agents[a].score += ns.round_pts(a)

            _check_victory(ns)

            child_val, _ = expectiminimax(
                ns, depth - 1, alpha, beta, searcher, cfg, stats, tt
            )
            expected += prob * child_val

        # ── MAX / MIN update 
        if is_max:
            if expected > best_val:
                best_val = expected
                best_act = jact
            alpha = max(alpha, best_val)
        else:
            if expected < best_val:
                best_val = expected
                best_act = jact
            beta = min(beta, best_val)

        # ── Alpha-Beta cut (MAX/MIN only, NOT inside chance node) 
        if beta <= alpha:
            remaining = len(jacts) - ji - 1
            stats.pruned += remaining
            break

    # ── Store in transposition table 
    if tt is not None and h is not None:
        tt[h] = (depth, best_val, best_act)

    return best_val, best_act


def _check_victory(state):
    """Check all win conditions: 60% territory and round limit."""
    if state.over:
        # Already marked over — just ensure winner is declared
        if not state.winner:
            alive = [a for a in AGENTS if state.agents[a].alive]
            candidates   = alive if alive else AGENTS
            state.winner = max(candidates, key=lambda a: state.agents[a].score)
        return

    non_obs   = state.non_obstacle()
    total     = len(non_obs)
    threshold = 0.60 * total if total > 0 else 0

    # Condition: 60% territory dominance
    for aid in AGENTS:
        if not state.agents[aid].alive:
            continue
        if len(state.owned_by(aid)) > threshold:
            state.over   = True
            state.winner = aid
            return

    # Condition: round limit reached
    if state.round >= state.R:
        state.over   = True
        alive        = [a for a in AGENTS if state.agents[a].alive]
        candidates   = alive if alive else AGENTS
        state.winner = max(candidates, key=lambda a: state.agents[a].score)


def apply_observation_mask(state, aid):
   
    cfg = CFGS[aid]
    if cfg.obs_range is None:
        return state.clone()

    s = state.clone()
    unit_positions = [u.pos for u in state.agents[aid].units]

    def in_range(pos):
        return any(manhattan(pos, up) <= cfg.obs_range for up in unit_positions)

    for r in range(s.N):
        for c in range(s.M):
            pos = (r, c)
            if not in_range(pos):
                own = s.owner.get(pos)
                if own is not None and own != aid:
                    s.owner[pos] = None
                    ctype = s.cell.get(pos)
                    if ctype not in (FORTRESS, MINEFIELD, OBSTACLE):
                        s.cell[pos] = EMPTY
    return s


def get_best_action(state, aid):
    """
    Run Expectiminimax for `aid`.
    Returns (best_joint_action, utility_value, SearchStats).
    """
    cfg        = CFGS[aid]
    stats      = SearchStats()
    tt         = {} if cfg.use_tt else None
    search_st  = apply_observation_mask(state, aid)
    search_st.turn_idx = AGENTS.index(aid)

    val, act = expectiminimax(
        search_st,
        cfg.depth,
        -math.inf, math.inf,
        aid, cfg, stats, tt
    )
    if act is None:
        jacts = joint_actions(state, aid)
        act   = jacts[0] if jacts else (("wait",), ("wait",))
    return act, val, stats


#  SECTION : ENVIRONMENTAL & MINEFIELD EVENTS  (real gameplay only)

def resolve_env_event(state):
    """Draw and apply one environmental event. Mutates state in-place."""
    event = random.choice(ENV_EVENTS)

    if event == "supply_drop":
        empties = [p for p, t in state.cell.items() if t == EMPTY]
        if empties:
            pos = random.choice(empties)
            state.cell[pos]    = FORTRESS
            state.owner[pos]   = None
            state.defense[pos] = 2
            state.temp_f[pos]  = 3   # reverts after 3 rounds
        return f"Supply Drop at {pos}"

    elif event == "earthquake":
        owned = [(p, a) for p, a in state.owner.items() if a is not None]
        if owned:
            pos, prev_own = random.choice(owned)
            cur_def = state.defense.get(pos, 1)
            new_def = cur_def - 1
            if new_def <= 0:
                state.owner[pos] = None
                state.defense.pop(pos, None)
                if state.cell.get(pos) == FORTRESS:
                    state.defense[pos] = 2
            else:
                state.defense[pos] = new_def
            return f"Earthquake at {pos} (def {cur_def}→{new_def})"
        return "Earthquake: no owned cells"

    elif event == "reinforcement":
        scores = {aid: state.agents[aid].score for aid in AGENTS
                  if state.agents[aid].alive}
        if scores:
            weakest = min(scores, key=scores.get)
            # Extra unit effect: give +5 energy instead (simplified; real impl would add temp unit)
            state.agents[weakest].energy = min(20, state.agents[weakest].energy + 3)
            return f"Reinforcement → {weakest} gets +3 energy"
        return "Reinforcement: no agents"

    elif event == "fog_of_war":
        return "Fog of War: observable range halved this turn"

    return f"Unknown event: {event}"


def resolve_mine_event(state, aid, unit):
    """Resolve a minefield event. Mutates state in-place."""
    oc = weighted_sample(MINE_OUTCOMES)
    ag = state.agents[aid]
    pos = unit.pos

    if oc["e_loss"] > 0:
        ag.energy = max(0, ag.energy - oc["e_loss"])
    if oc["disable"] > 0:
        unit.disabled = oc["disable"]
    if oc["detonate"]:
        state.cell[pos] = OBSTACLE
        state.owner.pop(pos, None)
        state.defense.pop(pos, None)
    return oc["id"]


def tick_temp_fortresses(state):
    expired = []
    for pos, turns_left in state.temp_f.items():
        if turns_left <= 1:
            expired.append(pos)
        else:
            state.temp_f[pos] = turns_left - 1
    for pos in expired:
        del state.temp_f[pos]
        if state.owner.get(pos) is None:
            state.cell[pos] = EMPTY
            state.defense.pop(pos, None)


def check_eliminations(state):
    
    for aid in AGENTS:
        ag = state.agents[aid]
        if not ag.alive:
            continue

        # Check if all units are somehow off the board
      
        active_units = [u for u in ag.units if u.pos is not None]
        if len(active_units) == 0:
            ag.alive  = False
            # Give elimination bonus to all surviving agents
            for other in AGENTS:
                if other != aid and state.agents[other].alive:
                    state.agents[other].score += 5
            state.log.append({
                "move": state.move_num,
                "agent": aid,
                "label": CFGS[aid].label,
                "action": "ELIMINATED (no units remaining)",
                "nodes": 0, "pruned": 0, "pct": 0,
                "val": 0, "time": 0,
                "events": [f"💀 Agent {aid} eliminated! Opponents get +5 pts"],
                "env": None
            })

    # Check if only one agent remains, that agent wins immediately
    alive_agents = [a for a in AGENTS if state.agents[a].alive]
    if len(alive_agents) == 1:
        state.over   = True
        state.winner = alive_agents[0]
    elif len(alive_agents) == 0:
        state.over   = True
        state.winner = max(AGENTS, key=lambda a: state.agents[a].score)



#  SECTION 11 — GAME LOOP

def run_one_move(state):
    if state.over:
        return state, None, None

    aid   = state.cur
    ag    = state.agents[aid]

    # ── Search 
    t0             = time.time()
    jact, val, sts = get_best_action(state, aid)
    elapsed        = time.time() - t0

    # ── Apply action to real game state 
    ns = apply_joint_action_with_outcome(state, aid, jact)

    # ── Detect what happened (combat result, mine, env) 
    event_notes = []

    # Check if any action was an attack or move-onto-enemy
    for i, act in enumerate(jact):
        if act[0] in ("attack", "move"):
            unit_orig = state.agents[aid].units[i]
            dr, dc    = act[1], act[2]
            target    = (unit_orig.pos[0] + dr, unit_orig.pos[1] + dc)
            prev_own  = state.owner.get(target)
            new_own   = ns.owner.get(target)
            if prev_own is not None and prev_own != aid:
                # Combat happened — figure out result
                if new_own == aid:
                    ctype = ns.cell.get(target, ".")
                    label = "Fortress" if ctype == FORTRESS else "Cell"
                    event_notes.append(f"⚔ Captured {label} at {target}!")
                elif new_own is None:
                    event_notes.append(f"⚔ Cell {target} neutralised (partial hit)")
                else:
                    prev_def = state.defense.get(target, 1)
                    new_def  = ns.defense.get(target, prev_def)
                    if new_def < prev_def:
                        event_notes.append(f"⚔ Attack hit! Defense {prev_def}→{new_def} at {target}")
                    else:
                        event_notes.append(f"⚔ Attack failed at {target}")

    # ── Mine events 
    mine_results = []
    for i, act in enumerate(jact):
        if act[0] == "move":
            unit = ns.agents[aid].units[i]
            if ns.cell.get(unit.pos) == MINEFIELD:
                mine_result = resolve_mine_event(ns, aid, unit)
                labels = {
                    "safe":     "💨 Mine: Safe passage",
                    "drain":    "💥 Mine: Energy drained -3",
                    "disabled": "🚫 Mine: Unit disabled 2 turns",
                    "detonate": "💣 Mine: DETONATED! Cell destroyed, -5 energy"
                }
                mine_results.append(labels.get(mine_result, f"Mine: {mine_result}"))
    event_notes.extend(mine_results)

    # ── Advance turn 
    ns.move_num += 1
    ns.turn_idx  = (ns.turn_idx + 1) % 3

    env_msg = None
    if ns.turn_idx == 0:
        ns.round += 1
        tick_temp_fortresses(ns)
        for a in AGENTS:
            if ns.agents[a].alive:
                ns.agents[a].score += ns.round_pts(a)
        if ns.round > ns.R:
            ns.over   = True
            ns.round  = ns.R        # cap display at 30, not 31
        else:
            env_msg = resolve_env_event(ns)   # no env event after final round

    # Check eliminations every turn (not just end of round)
    check_eliminations(ns)

    # Check all victory conditions
    _check_victory(ns)

    # ── Log entry 
    pct   = (sts.pruned / max(sts.nodes + sts.pruned, 1)) * 100
    cfg   = CFGS[aid]
    entry = {
        "move":    ns.move_num,
        "agent":   aid,
        "label":   cfg.label,
        "action":  action_str(jact),
        "nodes":   sts.nodes,
        "pruned":  sts.pruned,
        "pct":     pct,
        "val":     val,
        "time":    elapsed,
        "events":  event_notes,
        "env":     env_msg,
    }
    ns.log.append(entry)

    state.__dict__.update(ns.__dict__)
    return state, jact, entry

def format_log_entry(e):
    lines = [
        f"Move {e['move']:>3} | Agent {e['agent']} ({e['label']:<13}) | Action: {e['action']}",
        f"  Expectiminimax nodes explored : {e['nodes']:>8,}",
        f"  Nodes pruned (Alpha-Beta)     : {e['pruned']:>8,}  ({e['pct']:.1f}%)",
        f"  Chosen action value (utility) : {e['val']:>8.3f}",
    ]
    return "\n".join(lines)


def write_results(state, filename="results.txt"):
    with open(filename, "w") as f:
        f.write("=" * 65 + "\n")
        f.write("  Assignment 3 — Per-Move Node Reports\n")
        f.write("=" * 65 + "\n\n")
        for e in state.log:
            f.write(format_log_entry(e) + "\n\n")

        f.write("=" * 65 + "\n")
        f.write("  SUMMARY TABLE\n")
        f.write("=" * 65 + "\n")
        f.write(f"{'Agent':<15} {'Moves':>6} {'Tot Nodes':>12} {'Tot Pruned':>12} {'Efficiency':>11}\n")
        f.write("-" * 60 + "\n")
        for aid in AGENTS:
            entries = [e for e in state.log if e["agent"] == aid]
            tn = sum(e["nodes"] for e in entries)
            tp = sum(e["pruned"] for e in entries)
            pct = tp / max(tn + tp, 1) * 100
            cfg = CFGS[aid]
            f.write(f"{aid} ({cfg.label:<13}) {len(entries):>6} {tn:>12,} {tp:>12,} {pct:>10.1f}%\n")

        f.write("\n" + "=" * 65 + "\n")
        f.write("  FINAL SCORES\n")
        f.write("=" * 65 + "\n")
        for aid in AGENTS:
            ag = state.agents[aid]
            f.write(f"  Agent {aid} ({CFGS[aid].label}): {ag.score} pts | "
                    f"cells owned: {len(state.owned_by(aid))} | energy: {ag.energy}\n")
        winner = state.winner or max(AGENTS, key=lambda a: state.agents[a].score)
        f.write(f"\n  WINNER: Agent {winner} ({CFGS[winner].label})\n")
    print(f"[results.txt written]")


#  SECTION 12 — DEAR PYGUI INTERFACE

# GUI colour palette
COLOURS = {
    "A":        (70,  130, 180, 255),   # steel blue  – Expert
    "B":        (60,  179, 113, 255),   # medium sea green – Intermediate
    "C":        (205, 133,  63, 255),   # peru – Novice
    OBSTACLE:   (50,   50,  50, 255),   # dark grey
    FORTRESS:   (218, 165,  32, 255),   # goldenrod
    MINEFIELD:  (178,  34,  34, 255),   # firebrick
    EMPTY:      (220, 220, 220, 255),   # light grey
    "unit":     (255, 255,   0, 255),   # yellow unit dot
    "bg":       (30,   30,  30, 255),
    "unowned_f":(180, 140,  20, 255),   # darker gold for unowned fortress
}

CELL_SZ = 48    # pixels per cell
PANEL_W = 340   # side-panel width

_gui_state  = {}   # mutable GUI data shared via closures

#GUI CODE
def build_gui(game_state):
    dpg.create_context()

    N  = game_state.N
    M  = game_state.M
    BW = M * CELL_SZ        # board pixel width
    BH = N * CELL_SZ        # board pixel height
    VP_W = BW + PANEL_W + 40
    VP_H = max(BH + 80, 660)

    _gui_state["gs"]         = game_state
    _gui_state["running"]    = False
    _gui_state["run_speed"]  = 0.3
    _gui_state["last_entry"] = None

    # ── textures / font (default) 
    with dpg.font_registry():
        pass   # use default font

    # ── Main window 
    with dpg.window(label="Stochastic Battlefield", tag="main_win",
                    width=VP_W, height=VP_H, no_resize=False):

        with dpg.group(horizontal=True):
            # ── Left: board canvas 
            with dpg.child_window(tag="board_panel", width=BW + 10, height=BH + 40,
                                  no_scrollbar=True):
                dpg.add_text("Board", color=(200, 200, 200))
                with dpg.drawlist(tag="board_dl", width=BW, height=BH):
                    _draw_board(game_state)

            # ── Right: side panel 
            with dpg.child_window(tag="side_panel", width=PANEL_W, height=VP_H - 20):
                # Agent stats
                dpg.add_text("── Agent Status ──", color=(200,200,100))
                dpg.add_separator()
                for aid in AGENTS:
                    ag  = game_state.agents[aid]
                    cfg = CFGS[aid]
                    col = COLOURS[aid]
                    dpg.add_text(
                        f"{aid} ({cfg.label})",
                        tag=f"stat_{aid}_hdr",
                        color=col
                    )
                    dpg.add_text(
                        f"  Score: {ag.score}  Energy: {ag.energy}  "
                        f"Cells: {len(game_state.owned_by(aid))}",
                        tag=f"stat_{aid}"
                    )
                    dpg.add_spacer(height=4)

                dpg.add_separator()
                dpg.add_text("── Round / Turn ──", color=(200,200,100))
                dpg.add_text("Round: 1 / 30   Turn: A", tag="round_lbl")

                dpg.add_separator()
                dpg.add_text("── Last Move ──", color=(200,200,100))
                dpg.add_text("(none yet)", tag="last_move_lbl", wrap=PANEL_W - 20)

                dpg.add_separator()
                dpg.add_text("── Node Stats ──", color=(200,200,100))
                dpg.add_text("Nodes: —   Pruned: —   (—%)", tag="node_stat_lbl")

                dpg.add_separator()
                dpg.add_text("── Move Log ──", color=(200,200,100))
                with dpg.child_window(tag="log_panel", width=PANEL_W - 10,
                                      height=220, horizontal_scrollbar=False):
                    dpg.add_text("", tag="log_text", wrap=PANEL_W - 30)

                dpg.add_separator()
                dpg.add_text("── Controls ──", color=(200,200,100))
                with dpg.group(horizontal=True):
                    dpg.add_button(label="Next Move",
                                   callback=lambda: _step_once(), width=110)
                    dpg.add_button(label="Run / Pause",
                                   callback=lambda: _toggle_run(), width=110)
                dpg.add_text("Speed (s/move):", color=(180,180,180))
                dpg.add_slider_float(tag="speed_slider", default_value=0.3,
                                     min_value=0.05, max_value=2.0,
                                     callback=lambda s, d: _gui_state.update(run_speed=d))
                dpg.add_separator()
                dpg.add_text("", tag="winner_lbl", color=(255, 215, 0))

    # ── Viewport 
    dpg.create_viewport(title="Assignment 3 – Stochastic Battlefield",
                        width=VP_W + 20, height=VP_H + 40)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("main_win", True)

    _last_auto = [time.time()]
    while dpg.is_dearpygui_running():
        gs = _gui_state["gs"]
        if _gui_state["running"] and not gs.over:
            if time.time() - _last_auto[0] >= _gui_state["run_speed"]:
                _step_once()
                _last_auto[0] = time.time()
        dpg.render_dearpygui_frame()

    write_results(_gui_state["gs"])
    dpg.destroy_context()


#helpeers
def _step_once():
    gs = _gui_state["gs"]
    if gs.over:
        _show_winner(gs)
        return
    gs, jact, entry = run_one_move(gs)
    _gui_state["gs"]         = gs
    _gui_state["last_entry"] = entry
    _refresh_gui(gs, entry)


def _toggle_run():
    _gui_state["running"] = not _gui_state["running"]


def _refresh_gui(gs, entry):
    """Redraw board and update all labels."""
    # Redraw board
    dpg.delete_item("board_dl", children_only=True)
    with dpg.mutex():
        pass
    dpg.push_container_stack("board_dl")
    _draw_board(gs)
    dpg.pop_container_stack()

    # Agent stats
    for aid in AGENTS:
        ag = gs.agents[aid]
        status = "LOCKED" if ag.energy <= 0 else f"Energy: {ag.energy}"
        alive  = "" if ag.alive else "  [ELIMINATED]"
        dpg.set_value(f"stat_{aid}",
            f"  Score: {ag.score}  {status}  Cells: {len(gs.owned_by(aid))}{alive}")

    # Round / turn
    dpg.set_value("round_lbl",
        f"Round: {gs.round} / {gs.R}   Turn: {gs.cur}  (move #{gs.move_num})")

    # Last move — full detail with events and env
    if entry:
        lines = [f"{entry['agent']} ({entry['label']}): {entry['action']}"]
        for ev in entry.get("events", []):
            lines.append(f"  {ev}")
        if entry.get("env"):
            lines.append(f"  🌍 {entry['env']}")
        dpg.set_value("last_move_lbl", "\n".join(lines))
        dpg.set_value("node_stat_lbl",
            f"Nodes: {entry['nodes']:,}   Pruned: {entry['pruned']:,}"
            f"   ({entry['pct']:.1f}%)   [{entry['time']:.2f}s]")

    # Move log — action + combat result + env event on separate lines
    log_lines = []
    for e in gs.log[-12:]:
        # Main action line
        line = f"M{e['move']:>3} {e['agent']}({e['label'][0]}) {e['action'][:28]}"
        log_lines.append(line)
        # Combat/mine events
        for ev in e.get("events", []):
            log_lines.append(f"      {ev[:45]}")
        # Environmental event
        if e.get("env"):
            log_lines.append(f"      🌍 {e['env'][:40]}")

    dpg.set_value("log_text", "\n".join(log_lines))

    if gs.over:
        _show_winner(gs)


def _show_winner(gs):
    winner = gs.winner or max(AGENTS, key=lambda a: gs.agents[a].score)
    cfg    = CFGS[winner]
    ag     = gs.agents[winner]

    # Update the label in side panel
    dpg.set_value("winner_lbl",
        f"WINNER: {winner} ({cfg.label})  Score: {ag.score}")

    # Show a popup window on top if not already shown
    if not dpg.does_item_exist("winner_popup"):
        scores = sorted(AGENTS, key=lambda a: gs.agents[a].score, reverse=True)
        lines  = []
        medals = ["1st", "2nd", "3rd"]
        for rank, a in enumerate(scores):
            lines.append(
                f"{medals[rank]}  Agent {a} ({CFGS[a].label})"
                f"  —  Score: {gs.agents[a].score}"
                f"  |  Cells: {len(gs.owned_by(a))}"
            )

        with dpg.window(
            label="Game Over",
            tag="winner_popup",
            modal=True,
            no_close=False,
            width=420, height=200,
            pos=(150, 180)
        ):
            dpg.add_text(
                f"GAME OVER — Round {gs.R} Complete",
                color=(255, 215, 0)
            )
            dpg.add_separator()
            dpg.add_text(
                f"WINNER:  Agent {winner} ({cfg.label})",
                color=(100, 255, 100)
            )
            dpg.add_separator()
            for line in lines:
                dpg.add_text(line)
            dpg.add_separator()
            dpg.add_button(
                label="Close",
                callback=lambda: dpg.delete_item("winner_popup"),
                width=100
            )

    _gui_state["running"] = False


def _draw_board(gs):
    """Draw all cells and unit markers onto the board drawlist."""
    unit_pos = {}
    for aid in AGENTS:
        for u in gs.agents[aid].units:
            unit_pos.setdefault(u.pos, []).append(aid)

    for r in range(gs.N):
        for c in range(gs.M):
            pos   = (r, c)
            ctype = gs.cell.get(pos, EMPTY)
            owner = gs.owner.get(pos)
            x0    = c * CELL_SZ
            y0    = r * CELL_SZ
            x1    = x0 + CELL_SZ - 1
            y1    = y0 + CELL_SZ - 1

            # Cell background
            if ctype == OBSTACLE:
                fill = COLOURS[OBSTACLE]
            elif ctype == FORTRESS:
                fill = COLOURS[owner] if owner else COLOURS["unowned_f"]
            elif ctype == MINEFIELD:
                fill = COLOURS[MINEFIELD]
            elif owner:
                fill = COLOURS[owner]
            else:
                fill = COLOURS[EMPTY]

            dpg.draw_rectangle((x0, y0), (x1, y1),
                                fill=fill, color=(80, 80, 80), thickness=1)

            # Cell type labels
            mid_x = x0 + CELL_SZ // 2 - 5
            mid_y = y0 + CELL_SZ // 2 - 7
            if ctype == FORTRESS:
                dpg.draw_text((x0 + 4, y0 + 4), "F",
                              color=(255, 255, 180), size=14)
            elif ctype == MINEFIELD:
                dpg.draw_text((x0 + 4, y0 + 4), "M",
                              color=(255, 200, 200), size=14)
            elif ctype == OBSTACLE:
                dpg.draw_text((x0 + 4, y0 + 4), "X",
                              color=(120, 120, 120), size=14)

            # Defense value badge
            if pos in gs.defense and gs.defense[pos] > 0:
                dv = gs.defense[pos]
                dpg.draw_text((x0 + CELL_SZ - 14, y0 + 2),
                              str(dv), color=(255, 255, 255), size=11)

            # Owner label
            if owner:
                dpg.draw_text((x0 + CELL_SZ // 2 - 4, y0 + CELL_SZ - 16),
                              owner, color=(255, 255, 255), size=12)

            # Unit dots
            if pos in unit_pos:
                agents_here = unit_pos[pos]
                for k, a in enumerate(agents_here):
                    cx = x0 + 8 + k * 14
                    cy = y0 + CELL_SZ // 2
                    dpg.draw_circle((cx, cy), 6,
                                    fill=COLOURS[a], color=(0, 0, 0), thickness=1)


#  SECTION 13 — MAIN ENTRY POINT

def main():
    board_file = "board.txt"
    if len(sys.argv) > 1:
        board_file = sys.argv[1]

    if not os.path.exists(board_file):
        # Write the provided example board if none found
        example = (
            "8 8 30\n"
            "........\n"
            ".X..F...\n"
            "....X...\n"
            "..M.....\n"
            ".......M\n"
            "...X....\n"
            "..F..X..\n"
            "........\n"
            "0 0\n"
            "7 0\n"
            "3 7\n"
        )
        with open(board_file, "w") as f:
            f.write(example)
        print(f"[Created default {board_file}]")

    print(f"Loading board from {board_file} ...")
    state = load_board(board_file)
    print(f"Board: {state.N}×{state.M}, Rounds: {state.R}")
    for aid in AGENTS:
        ag = state.agents[aid]
        print(f"  Agent {aid} ({CFGS[aid].label}): starts at "
              f"{ag.units[0].pos}, depth={CFGS[aid].depth}")

    print("\nLaunching Dear PyGui interface ...")
    print("  • Click 'Next Move' to step one turn at a time.")
    print("  • Click 'Run / Pause' to auto-play.")
    print("  • results.txt is written when the window closes.\n")

    build_gui(state)


if __name__ == "__main__":
    main()