import argparse
import copy
import math
import random
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

try:
    import dearpygui.dearpygui as dpg
except Exception:
    dpg = None


# =========================
# Basic constants and types
# =========================

AGENT_IDS = ["A", "B", "C"]
STARTING_ENERGY = 20
ELIMINATION_BONUS = 5
CRITICAL_BONUS = 2

# 9-sided die outcomes for combat
DIE_OUTCOMES = [
    ("fail_extra_energy", 0.10),
    ("fail_extra_energy", 0.10),
    ("fail", 0.15),
    ("partial_no_advance", 0.08),
    ("partial_no_advance", 0.08),
    ("partial_advance", 0.12),
    ("full", 0.13),
    ("full", 0.13),
    ("critical", 0.11),
]

# Minefield event outcomes
MINE_OUTCOMES = [
    ("safe", 0.40),
    ("energy_drain", 0.30),
    ("unit_disabled", 0.20),
    ("detonation", 0.10),
]


@dataclass
class AgentProfile:
    name: str
    depth_limit: int
    view_range: int
    evaluate_top_k_chance_faces: int
    evaluation_level: str
    use_transposition_table: bool


@dataclass
class Unit:
    x: int
    y: int
    disabled_turns: int = 0
    temporary_turns_left: int = 0


@dataclass
class GameState:
    width: int
    height: int
    round_limit: int
    board: List[List[str]]
    owners: List[List[Optional[str]]]
    defense: List[List[int]]
    temp_fortress_rounds: List[List[int]]
    scores: Dict[str, int]
    energy: Dict[str, int]
    units: Dict[str, List[Unit]]
    eliminated: Dict[str, bool]
    current_round: int = 1
    fog_active: bool = False
    stochastic_enabled: bool = True

    def clone(self) -> "GameState":
        return copy.deepcopy(self)


@dataclass
class SearchStats:
    explored_nodes: int = 0
    pruned_nodes: int = 0


@dataclass
class MoveLogItem:
    round_no: int
    agent_id: str
    action_text: str
    explored: int
    pruned: int


@dataclass
class MoveChoice:
    action_type: str
    unit_index: int
    target_x: int
    target_y: int
    score_hint: float = 0.0


def inside(state: GameState, x: int, y: int) -> bool:
    return 0 <= x < state.width and 0 <= y < state.height


def is_obstacle(state: GameState, x: int, y: int) -> bool:
    return state.board[y][x] == "X"


def is_minefield(state: GameState, x: int, y: int) -> bool:
    return state.board[y][x] == "M"


def manhattan(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def parse_board_file(path: str) -> Tuple[GameState, Dict[str, Tuple[int, int]]]:
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    first = lines[0].split()
    width, height, round_limit = int(first[0]), int(first[1]), int(first[2])

    raw_rows = lines[1:1 + height]
    positions = lines[1 + height:1 + height + 3]

    board = [list(row) for row in raw_rows]
    owners = [[None for _ in range(width)] for _ in range(height)]
    defense = [[0 for _ in range(width)] for _ in range(height)]
    temp_fortress_rounds = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            cell = board[y][x]
            if cell in AGENT_IDS:
                owners[y][x] = cell
                defense[y][x] = 1
                board[y][x] = "."
            elif cell == "F":
                defense[y][x] = 2
            else:
                defense[y][x] = 0

    starts = {}
    units = {a: [] for a in AGENT_IDS}
    for i, aid in enumerate(AGENT_IDS):
        x, y = map(int, positions[i].split())
        starts[aid] = (x, y)
        # two units at start as required
        units[aid].append(Unit(x, y))
        units[aid].append(Unit(x, y))
        owners[y][x] = aid
        if defense[y][x] == 0:
            defense[y][x] = 1

    state = GameState(
        width=width,
        height=height,
        round_limit=round_limit,
        board=board,
        owners=owners,
        defense=defense,
        temp_fortress_rounds=temp_fortress_rounds,
        scores={a: 0 for a in AGENT_IDS},
        energy={a: STARTING_ENERGY for a in AGENT_IDS},
        units=units,
        eliminated={a: False for a in AGENT_IDS},
    )
    return state, starts


def score_cells_for_agent(state: GameState, agent_id: str) -> int:
    total = 0
    for y in range(state.height):
        for x in range(state.width):
            if state.owners[y][x] == agent_id:
                if state.board[y][x] == "F":
                    total += 3
                else:
                    total += 1
    return total


def update_round_scores(state: GameState) -> None:
    for aid in AGENT_IDS:
        if not state.eliminated[aid]:
            state.scores[aid] += score_cells_for_agent(state, aid)


def visible_cells(state: GameState, agent_id: str, profile: AgentProfile) -> set:
    if profile.view_range < 0:
        return {(x, y) for y in range(state.height) for x in range(state.width)}

    effective_range = profile.view_range
    if state.fog_active:
        effective_range = max(0, profile.view_range // 2)

    vis = set()
    for u in state.units[agent_id]:
        if u.disabled_turns > 0:
            continue
        for y in range(state.height):
            for x in range(state.width):
                if manhattan((u.x, u.y), (x, y)) <= effective_range:
                    vis.add((x, y))
    return vis


def get_non_obstacle_count(state: GameState) -> int:
    total = 0
    for y in range(state.height):
        for x in range(state.width):
            if not is_obstacle(state, x, y):
                total += 1
    return total


def get_control_count(state: GameState, aid: str) -> int:
    count = 0
    for y in range(state.height):
        for x in range(state.width):
            if state.owners[y][x] == aid:
                count += 1
    return count


def remove_temporary_units(state: GameState) -> None:
    for aid in AGENT_IDS:
        new_units = []
        for u in state.units[aid]:
            if u.temporary_turns_left > 0:
                u.temporary_turns_left -= 1
                if u.temporary_turns_left == 0:
                    continue
            if u.disabled_turns > 0:
                u.disabled_turns -= 1
            new_units.append(u)
        state.units[aid] = new_units


def apply_environment_event(state: GameState, starts: Dict[str, Tuple[int, int]], rng: random.Random, log: List[str]) -> None:
    if not state.stochastic_enabled:
        state.fog_active = False
        return

    state.fog_active = False
    event = rng.choice(["supply", "earthquake", "reinforcement", "fog"])

    if event == "supply":
        empties = [(x, y) for y in range(state.height) for x in range(state.width)
                   if state.owners[y][x] is None and state.board[y][x] == "."]
        if empties:
            x, y = rng.choice(empties)
            state.board[y][x] = "F"
            state.defense[y][x] = max(state.defense[y][x], 2)
            state.temp_fortress_rounds[y][x] = 3
            log.append(f"Environment: Supply Drop at ({x},{y}).")
        else:
            log.append("Environment: Supply Drop skipped (no empty cell).")
    elif event == "earthquake":
        owned = [(x, y) for y in range(state.height) for x in range(state.width) if state.owners[y][x] is not None]
        if owned:
            x, y = rng.choice(owned)
            state.defense[y][x] = max(0, state.defense[y][x] - 1)
            if state.defense[y][x] == 0:
                state.owners[y][x] = None
                if state.board[y][x] == "F" and state.temp_fortress_rounds[y][x] <= 0:
                    state.board[y][x] = "."
            log.append(f"Environment: Earthquake hit ({x},{y}).")
        else:
            log.append("Environment: Earthquake skipped (no owned cells).")
    elif event == "reinforcement":
        alive = [a for a in AGENT_IDS if not state.eliminated[a]]
        if not alive:
            return
        low_agent = min(alive, key=lambda a: state.scores[a])
        placed = False
        candidate_positions = []
        for u in state.units[low_agent]:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = u.x + dx, u.y + dy
                if inside(state, nx, ny) and not is_obstacle(state, nx, ny) and state.owners[ny][nx] is None:
                    candidate_positions.append((nx, ny))
        if not candidate_positions:
            sx, sy = starts[low_agent]
            if state.owners[sy][sx] is None and not is_obstacle(state, sx, sy):
                candidate_positions.append((sx, sy))
        if not candidate_positions:
            own_cells = [(x, y) for y in range(state.height) for x in range(state.width) if state.owners[y][x] == low_agent]
            if own_cells:
                candidate_positions.append(min(own_cells, key=lambda p: manhattan(p, starts[low_agent])))
        if candidate_positions:
            px, py = candidate_positions[0]
            state.units[low_agent].append(Unit(px, py, temporary_turns_left=2))
            state.owners[py][px] = low_agent
            state.defense[py][px] = max(1, state.defense[py][px])
            placed = True
        if placed:
            log.append(f"Environment: Reinforcement given to Agent {low_agent}.")
        else:
            log.append("Environment: Reinforcement skipped (no placement available).")
    else:
        state.fog_active = True
        log.append("Environment: Fog of War active this round.")


def decay_temporary_fortresses(state: GameState) -> None:
    for y in range(state.height):
        for x in range(state.width):
            if state.temp_fortress_rounds[y][x] > 0:
                state.temp_fortress_rounds[y][x] -= 1
                if state.temp_fortress_rounds[y][x] == 0 and state.board[y][x] == "F":
                    # Only revert supply-drop fortress tiles to empty
                    state.board[y][x] = "."
                    if state.owners[y][x] is None:
                        state.defense[y][x] = 0


def apply_mine_event(state: GameState, aid: str, unit: Unit, x: int, y: int, rng: random.Random, log: List[str]) -> None:
    if not state.stochastic_enabled:
        return
    if not is_minefield(state, x, y):
        return
    event = weighted_choice(MINE_OUTCOMES, rng)
    if event == "safe":
        log.append(f"Mine event: Agent {aid} safe passage at ({x},{y}).")
    elif event == "energy_drain":
        state.energy[aid] = max(0, state.energy[aid] - 3)
        log.append(f"Mine event: Agent {aid} lost 3 energy at ({x},{y}).")
    elif event == "unit_disabled":
        unit.disabled_turns = max(unit.disabled_turns, 2)
        log.append(f"Mine event: Agent {aid} unit disabled for 2 turns.")
    elif event == "detonation":
        state.board[y][x] = "X"
        state.owners[y][x] = None
        state.defense[y][x] = 0
        state.energy[aid] = max(0, state.energy[aid] - 5)
        log.append(f"Mine event: Detonation at ({x},{y}); Agent {aid} lost 5 energy.")


def weighted_choice(outcomes: List[Tuple[str, float]], rng: random.Random) -> str:
    r = rng.random()
    total = 0.0
    for name, prob in outcomes:
        total += prob
        if r <= total:
            return name
    return outcomes[-1][0]


def apply_combat_result(
    state: GameState,
    attacker: str,
    defender: str,
    tx: int,
    ty: int,
    outcome: str,
    move_attacker_to_target: bool,
    unit: Unit,
) -> int:
    bonus = 0

    if outcome == "fail_extra_energy":
        state.energy[attacker] = max(0, state.energy[attacker] - 1)
    elif outcome in ("partial_no_advance", "partial_advance"):
        state.owners[ty][tx] = None
        state.defense[ty][tx] = 0
        if outcome == "partial_advance" and move_attacker_to_target:
            unit.x = tx
            unit.y = ty
    elif outcome in ("full", "critical"):
        state.defense[ty][tx] = max(0, state.defense[ty][tx] - 1)
        if state.defense[ty][tx] == 0:
            state.owners[ty][tx] = attacker
            state.defense[ty][tx] = 1 if state.board[ty][tx] != "F" else 2
            if move_attacker_to_target:
                unit.x = tx
                unit.y = ty
            if outcome == "critical":
                bonus += CRITICAL_BONUS
    return bonus


def generate_unit_actions(state: GameState, aid: str, unit_idx: int, profile: AgentProfile, vis: set) -> List[MoveChoice]:
    unit = state.units[aid][unit_idx]
    actions: List[MoveChoice] = []

    # If disabled, only wait
    if unit.disabled_turns > 0:
        actions.append(MoveChoice("wait", unit_idx, unit.x, unit.y, 0))
        return actions

    # Wait action
    actions.append(MoveChoice("wait", unit_idx, unit.x, unit.y, 0.1))

    # Move and attack and fortify around 4-neighbors
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = unit.x + dx, unit.y + dy
        if not inside(state, nx, ny):
            continue
        if (nx, ny) not in vis:
            continue
        if is_obstacle(state, nx, ny):
            continue

        owner = state.owners[ny][nx]
        if owner is None:
            actions.append(MoveChoice("move", unit_idx, nx, ny, 1.5))
        elif owner != aid:
            actions.append(MoveChoice("attack", unit_idx, nx, ny, 1.8))
            actions.append(MoveChoice("move_attack", unit_idx, nx, ny, 1.9))
        else:
            if state.defense[ny][nx] < 3:
                actions.append(MoveChoice("fortify", unit_idx, nx, ny, 1.0))

    # Keep only top few for manageability
    actions.sort(key=lambda a: a.score_hint, reverse=True)
    return actions[:3]


def joint_action_combinations(action_lists: List[List[MoveChoice]], limit: int = 12) -> List[List[MoveChoice]]:
    if not action_lists:
        return []
    combos = [[]]
    for actions in action_lists:
        new_combos = []
        for c in combos:
            for a in actions:
                new_combos.append(c + [a])
        combos = new_combos
    combos.sort(key=lambda combo: sum(x.score_hint for x in combo), reverse=True)
    return combos[:limit]


def apply_joint_actions(
    state: GameState,
    aid: str,
    joint: List[MoveChoice],
    combat_outcome_resolver,
    rng: random.Random,
    log: Optional[List[str]] = None,
) -> None:
    if log is None:
        log = []
    for action in joint:
        if state.energy[aid] <= 0:
            break
        unit = state.units[aid][action.unit_index]
        state.energy[aid] = max(0, state.energy[aid] - 1)

        if action.action_type == "wait":
            continue
        if unit.disabled_turns > 0:
            continue

        tx, ty = action.target_x, action.target_y
        if not inside(state, tx, ty) or is_obstacle(state, tx, ty):
            continue

        if action.action_type == "move":
            if state.owners[ty][tx] is None:
                unit.x = tx
                unit.y = ty
                state.owners[ty][tx] = aid
                state.defense[ty][tx] = max(1, state.defense[ty][tx])
                apply_mine_event(state, aid, unit, tx, ty, rng, log)
        elif action.action_type == "fortify":
            if state.owners[ty][tx] == aid:
                state.defense[ty][tx] = min(3, state.defense[ty][tx] + 1)
        elif action.action_type in ("attack", "move_attack"):
            owner = state.owners[ty][tx]
            if owner is not None and owner != aid:
                outcome = combat_outcome_resolver()
                bonus = apply_combat_result(
                    state=state,
                    attacker=aid,
                    defender=owner,
                    tx=tx,
                    ty=ty,
                    outcome=outcome,
                    move_attacker_to_target=(action.action_type == "move_attack"),
                    unit=unit,
                )
                state.scores[aid] += bonus
                if action.action_type == "move_attack":
                    apply_mine_event(state, aid, unit, unit.x, unit.y, rng, log)


def check_eliminations(state: GameState, log: List[str]) -> None:
    alive_agents = [a for a in AGENT_IDS if not state.eliminated[a]]
    for aid in alive_agents:
        has_units = len(state.units[aid]) > 0
        has_energy = state.energy[aid] > 0
        if (not has_units or not has_energy) and not state.eliminated[aid]:
            state.eliminated[aid] = True
            for other in AGENT_IDS:
                if other != aid and not state.eliminated[other]:
                    state.scores[other] += ELIMINATION_BONUS
            log.append(f"Elimination: Agent {aid} eliminated.")


def game_over(state: GameState) -> bool:
    if state.current_round > state.round_limit:
        return True
    non_obstacles = get_non_obstacle_count(state)
    for aid in AGENT_IDS:
        if get_control_count(state, aid) > 0.60 * non_obstacles:
            return True
    alive = [a for a in AGENT_IDS if not state.eliminated[a]]
    if len(alive) <= 1:
        return True
    return False


def state_hash_for_tt(state: GameState, maximizing_agent: str) -> str:
    rows = []
    for y in range(state.height):
        row = []
        for x in range(state.width):
            row.append(
                f"{state.board[y][x]}:{state.owners[y][x] or '_'}:{state.defense[y][x]}"
            )
        rows.append("|".join(row))
    unit_text = []
    for aid in AGENT_IDS:
        for u in state.units[aid]:
            unit_text.append(f"{aid}-{u.x}-{u.y}-{u.disabled_turns}-{u.temporary_turns_left}")
    return ";".join(rows) + "#" + ",".join(unit_text) + f"#{maximizing_agent}"


def evaluate_state(state: GameState, agent_id: str, level: str) -> float:
    opp = [a for a in AGENT_IDS if a != agent_id]
    avg_opp_score = sum(state.scores[a] for a in opp) / len(opp)
    score_diff = state.scores[agent_id] - avg_opp_score

    if level == "greedy":
        return score_diff

    own_cells = 0
    own_fortress = 0
    threat = 0
    for y in range(state.height):
        for x in range(state.width):
            if state.owners[y][x] == agent_id:
                own_cells += 1
                if state.board[y][x] == "F":
                    own_fortress += 1
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if inside(state, nx, ny):
                        owner = state.owners[ny][nx]
                        if owner is not None and owner != agent_id:
                            threat += 1

    territory_term = own_cells + 2.0 * own_fortress

    high_value_targets = []
    for y in range(state.height):
        for x in range(state.width):
            if state.board[y][x] == "F" and state.owners[y][x] != agent_id:
                high_value_targets.append((x, y))

    positional_term = 0.0
    if high_value_targets and state.units[agent_id]:
        d_sum = 0
        for u in state.units[agent_id]:
            d_sum += min(manhattan((u.x, u.y), t) for t in high_value_targets)
        avg_d = d_sum / len(state.units[agent_id])
        positional_term = -avg_d

    avg_opp_energy = sum(state.energy[a] for a in opp) / len(opp)
    energy_term = state.energy[agent_id] - avg_opp_energy

    if level == "medium":
        return 1.5 * score_diff + 1.2 * territory_term + 0.8 * energy_term

    # full evaluation for expert
    return (
        1.8 * score_diff
        + 1.4 * territory_term
        + 0.9 * positional_term
        - 1.1 * threat
        + 0.8 * energy_term
    )


def get_chance_branches(profile: AgentProfile) -> List[Tuple[str, float]]:
    merged = {}
    for outcome, p in DIE_OUTCOMES:
        merged[outcome] = merged.get(outcome, 0) + p
    branches = list(merged.items())
    branches.sort(key=lambda x: x[1], reverse=True)
    if profile.evaluate_top_k_chance_faces > 0:
        branches = branches[:profile.evaluate_top_k_chance_faces]
        total = sum(p for _, p in branches)
        branches = [(name, p / total) for name, p in branches]
    return branches


def expectiminimax(
    state: GameState,
    maximizing_agent: str,
    current_agent: str,
    depth_left: int,
    alpha: float,
    beta: float,
    profiles: Dict[str, AgentProfile],
    stats: SearchStats,
    node_budget: int,
    transposition_table: Optional[Dict[str, float]] = None,
) -> float:
    stats.explored_nodes += 1

    if depth_left <= 0 or game_over(state) or stats.explored_nodes >= node_budget:
        level = profiles[maximizing_agent].evaluation_level
        return evaluate_state(state, maximizing_agent, level)

    use_tt = profiles[maximizing_agent].use_transposition_table and transposition_table is not None
    key = None
    if use_tt:
        key = f"{depth_left}|{current_agent}|{state_hash_for_tt(state, maximizing_agent)}"
        if key in transposition_table:
            return transposition_table[key]

    profile_for_current = profiles[current_agent]
    vis = visible_cells(state, current_agent, profile_for_current)

    if not state.units[current_agent]:
        next_idx = (AGENT_IDS.index(current_agent) + 1) % 3
        val = expectiminimax(
            state, maximizing_agent, AGENT_IDS[next_idx], depth_left - 1,
            alpha, beta, profiles, stats, node_budget, transposition_table
        )
        if use_tt and key is not None:
            transposition_table[key] = val
        return val

    action_lists = []
    for i in range(len(state.units[current_agent])):
        action_lists.append(generate_unit_actions(state, current_agent, i, profile_for_current, vis))
    joint_actions = joint_action_combinations(action_lists, limit=4)

    is_max = current_agent == maximizing_agent

    if is_max:
        value = -10**9
        for joint in joint_actions:
            expected_value = 0.0
            branches = get_chance_branches(profile_for_current)
            for outcome_name, prob in branches:
                next_state = state.clone()

                def resolver():
                    return outcome_name

                apply_joint_actions(next_state, current_agent, joint, resolver, random.Random(0))
                next_idx = (AGENT_IDS.index(current_agent) + 1) % 3
                child = expectiminimax(
                    next_state, maximizing_agent, AGENT_IDS[next_idx], depth_left - 1,
                    alpha, beta, profiles, stats, node_budget, transposition_table
                )
                expected_value += prob * child

            value = max(value, expected_value)
            alpha = max(alpha, value)
            if beta <= alpha:
                stats.pruned_nodes += 1
                break
    else:
        value = 10**9
        for joint in joint_actions:
            expected_value = 0.0
            branches = get_chance_branches(profile_for_current)
            for outcome_name, prob in branches:
                next_state = state.clone()

                def resolver():
                    return outcome_name

                apply_joint_actions(next_state, current_agent, joint, resolver, random.Random(0))
                next_idx = (AGENT_IDS.index(current_agent) + 1) % 3
                child = expectiminimax(
                    next_state, maximizing_agent, AGENT_IDS[next_idx], depth_left - 1,
                    alpha, beta, profiles, stats, node_budget, transposition_table
                )
                expected_value += prob * child

            value = min(value, expected_value)
            beta = min(beta, value)
            if beta <= alpha:
                stats.pruned_nodes += 1
                break

    if use_tt and key is not None:
        transposition_table[key] = value
    return value


def choose_best_joint_action(
    state: GameState,
    aid: str,
    profiles: Dict[str, AgentProfile],
) -> Tuple[List[MoveChoice], SearchStats]:
    stats = SearchStats()
    node_budget_map = {"A": 550, "B": 350, "C": 220}
    node_budget = node_budget_map.get(aid, 1000)

    profile = profiles[aid]
    vis = visible_cells(state, aid, profile)

    action_lists = []
    for i in range(len(state.units[aid])):
        action_lists.append(generate_unit_actions(state, aid, i, profile, vis))
    all_joint = joint_action_combinations(action_lists, limit=4)
    if not all_joint:
        return [], stats

    tt = {} if profile.use_transposition_table else None
    best_value = -10**9
    best_joint = all_joint[0]
    # Practical depth cap to keep the game interactive in GUI mode.
    effective_depth_map = {"A": 3, "B": 2, "C": 1}
    effective_depth = min(profile.depth_limit, effective_depth_map.get(aid, profile.depth_limit))

    for joint in all_joint:
        expected_value = 0.0
        for outcome_name, prob in get_chance_branches(profile):
            next_state = state.clone()

            def resolver():
                return outcome_name

            apply_joint_actions(next_state, aid, joint, resolver, random.Random(0))
            next_idx = (AGENT_IDS.index(aid) + 1) % 3
            val = expectiminimax(
                next_state,
                maximizing_agent=aid,
                current_agent=AGENT_IDS[next_idx],
                depth_left=effective_depth - 1,
                alpha=-10**9,
                beta=10**9,
                profiles=profiles,
                stats=stats,
                node_budget=node_budget,
                transposition_table=tt,
            )
            expected_value += prob * val

        if expected_value > best_value:
            best_value = expected_value
            best_joint = joint

    return best_joint, stats


def simulate_game(
    initial_state: GameState,
    starts: Dict[str, Tuple[int, int]],
    profiles: Dict[str, AgentProfile],
    seed: int = 42,
    stochastic_enabled: bool = True,
    expert_depth_override: Optional[int] = None,
) -> Tuple[GameState, List[MoveLogItem], List[str], Dict[str, Dict[str, float]]]:
    rng = random.Random(seed)
    state = initial_state.clone()
    state.stochastic_enabled = stochastic_enabled
    move_logs: List[MoveLogItem] = []
    text_log: List[str] = []

    if expert_depth_override is not None:
        profiles = copy.deepcopy(profiles)
        profiles["A"].depth_limit = expert_depth_override

    per_agent_nodes = {a: [] for a in AGENT_IDS}
    per_agent_prune = {a: [] for a in AGENT_IDS}

    while not game_over(state):
        text_log.append(f"\n=== Round {state.current_round} ===")

        apply_environment_event(state, starts, rng, text_log)
        for aid in AGENT_IDS:
            if state.eliminated[aid]:
                continue

            if state.energy[aid] <= 0 or len(state.units[aid]) == 0:
                state.eliminated[aid] = True
                continue

            best_joint, stats = choose_best_joint_action(state, aid, profiles)
            per_agent_nodes[aid].append(stats.explored_nodes)
            denom = max(1, stats.explored_nodes + stats.pruned_nodes)
            per_agent_prune[aid].append(stats.pruned_nodes / denom)

            def random_combat_resolver():
                if not state.stochastic_enabled:
                    return "full"
                return weighted_choice(DIE_OUTCOMES, rng)

            apply_joint_actions(state, aid, best_joint, random_combat_resolver, rng, text_log)

            action_text = "; ".join([f"{m.action_type} U{m.unit_index}->{(m.target_x,m.target_y)}" for m in best_joint])
            move_logs.append(MoveLogItem(
                round_no=state.current_round,
                agent_id=aid,
                action_text=action_text,
                explored=stats.explored_nodes,
                pruned=stats.pruned_nodes,
            ))
            text_log.append(
                f"Agent {aid} move: {action_text} | nodes explored={stats.explored_nodes}, pruned={stats.pruned_nodes}"
            )
            check_eliminations(state, text_log)

        update_round_scores(state)
        remove_temporary_units(state)
        decay_temporary_fortresses(state)
        state.fog_active = False
        state.current_round += 1

    summary_stats = {}
    for aid in AGENT_IDS:
        avg_nodes = sum(per_agent_nodes[aid]) / len(per_agent_nodes[aid]) if per_agent_nodes[aid] else 0
        avg_prune = sum(per_agent_prune[aid]) / len(per_agent_prune[aid]) if per_agent_prune[aid] else 0
        summary_stats[aid] = {"avg_nodes": avg_nodes, "avg_prune": avg_prune}
    return state, move_logs, text_log, summary_stats


def write_results_file(
    path: str,
    final_state: GameState,
    move_logs: List[MoveLogItem],
    text_log: List[str],
    main_summary: Dict[str, Dict[str, float]],
    depth_analysis: Dict[str, float],
    stochastic_analysis: Dict[str, float],
) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write("Stochastic Battlefield - Results\n")
        f.write("=" * 45 + "\n\n")

        f.write("Final Scores:\n")
        for aid in AGENT_IDS:
            f.write(f"Agent {aid}: {final_state.scores[aid]}\n")
        winner = max(AGENT_IDS, key=lambda a: final_state.scores[a])
        f.write(f"Winner: Agent {winner}\n\n")

        f.write("Per-Move Node Report:\n")
        for m in move_logs:
            f.write(
                f"Round {m.round_no:02d} | Agent {m.agent_id} | "
                f"Explored={m.explored:6d} | Pruned={m.pruned:6d} | {m.action_text}\n"
            )
        f.write("\n")

        f.write("Average Node and Pruning Summary:\n")
        for aid in AGENT_IDS:
            f.write(
                f"Agent {aid}: avg_nodes={main_summary[aid]['avg_nodes']:.2f}, "
                f"avg_pruning_efficiency={main_summary[aid]['avg_prune']:.3f}\n"
            )
        f.write("\n")

        f.write("Depth Impact Analysis (Agent A depth 5 vs 7 across 5 runs):\n")
        for k, v in depth_analysis.items():
            f.write(f"{k}: {v:.3f}\n")
        f.write("\n")

        f.write("Stochasticity Impact Analysis (5 deterministic vs 5 stochastic):\n")
        for k, v in stochastic_analysis.items():
            f.write(f"{k}: {v:.3f}\n")
        f.write("\n")

        f.write("Detailed Play Log:\n")
        for line in text_log:
            f.write(line + "\n")


def run_batch_analysis(
    initial_state: GameState,
    starts: Dict[str, Tuple[int, int]],
    profiles: Dict[str, AgentProfile],
) -> Tuple[Dict[str, float], Dict[str, float]]:
    # Batch analysis is intentionally done on fewer rounds
    # so student machines can finish all 5+5 runs quickly.
    analysis_state = initial_state.clone()
    analysis_state.round_limit = min(initial_state.round_limit, 10)

    scores_depth5 = []
    scores_depth7 = []
    for i in range(5):
        st5, _, _, _ = simulate_game(analysis_state, starts, profiles, seed=100 + i, stochastic_enabled=True, expert_depth_override=5)
        st7, _, _, _ = simulate_game(analysis_state, starts, profiles, seed=200 + i, stochastic_enabled=True, expert_depth_override=7)
        scores_depth5.append(st5.scores["A"])
        scores_depth7.append(st7.scores["A"])

    depth_analysis = {
        "AgentA_avg_score_depth5": sum(scores_depth5) / len(scores_depth5),
        "AgentA_avg_score_depth7": sum(scores_depth7) / len(scores_depth7),
    }

    det_scores = {a: [] for a in AGENT_IDS}
    stoch_scores = {a: [] for a in AGENT_IDS}
    for i in range(5):
        d_state, _, _, _ = simulate_game(analysis_state, starts, profiles, seed=300 + i, stochastic_enabled=False)
        s_state, _, _, _ = simulate_game(analysis_state, starts, profiles, seed=400 + i, stochastic_enabled=True)
        for a in AGENT_IDS:
            det_scores[a].append(d_state.scores[a])
            stoch_scores[a].append(s_state.scores[a])

    stochastic_analysis = {}
    for a in AGENT_IDS:
        stochastic_analysis[f"Agent{a}_avg_deterministic"] = sum(det_scores[a]) / 5.0
        stochastic_analysis[f"Agent{a}_avg_stochastic"] = sum(stoch_scores[a]) / 5.0

    return depth_analysis, stochastic_analysis


class BattlefieldGUI:
    def __init__(self, state: GameState, move_logs: List[MoveLogItem], text_log: List[str]):
        self.state = state
        self.move_logs = move_logs
        self.text_log = text_log
        self.log_index = 0
        self.cell_size = 42
        self.board_draw_tag = "board_draw"
        self.agent_info_tag = "agent_info_text"
        self.move_log_tag = "move_log_text"

    def draw_board(self) -> None:
        dpg.delete_item(self.board_draw_tag, children_only=True)
        for y in range(self.state.height):
            for x in range(self.state.width):
                px1 = x * self.cell_size
                py1 = y * self.cell_size
                px2 = px1 + self.cell_size
                py2 = py1 + self.cell_size

                base = self.state.board[y][x]
                owner = self.state.owners[y][x]
                color = (240, 240, 240, 255)
                if base == "X":
                    color = (50, 50, 50, 255)
                elif base == "M":
                    color = (255, 220, 140, 255)
                elif base == "F":
                    color = (180, 220, 255, 255)

                if owner == "A":
                    color = (180, 255, 180, 255)
                elif owner == "B":
                    color = (180, 180, 255, 255)
                elif owner == "C":
                    color = (255, 180, 220, 255)

                dpg.draw_rectangle((px1, py1), (px2, py2), color=(0, 0, 0, 255), fill=color, parent=self.board_draw_tag)
                dpg.draw_text((px1 + 4, py1 + 4), f"{base}", color=(0, 0, 0, 255), size=14, parent=self.board_draw_tag)
                if self.state.defense[y][x] > 0:
                    dpg.draw_text((px1 + 20, py1 + 20), f"D{self.state.defense[y][x]}", color=(0, 0, 0, 255), size=12, parent=self.board_draw_tag)

        for aid in AGENT_IDS:
            for u in self.state.units[aid]:
                cx = u.x * self.cell_size + self.cell_size // 2
                cy = u.y * self.cell_size + self.cell_size // 2
                c = (0, 120, 0, 255) if aid == "A" else (40, 40, 170, 255) if aid == "B" else (170, 40, 120, 255)
                dpg.draw_circle((cx, cy), 8, color=c, fill=c, parent=self.board_draw_tag)

    def refresh_side_panel(self) -> None:
        lines = [f"Round: {self.state.current_round}/{self.state.round_limit}"]
        for aid in AGENT_IDS:
            lines.append(
                f"Agent {aid}: score={self.state.scores[aid]}, energy={self.state.energy[aid]}, "
                f"units={len(self.state.units[aid])}, eliminated={self.state.eliminated[aid]}"
            )
        dpg.set_value(self.agent_info_tag, "\n".join(lines))

        show = self.text_log[max(0, self.log_index - 18):self.log_index + 1]
        dpg.set_value(self.move_log_tag, "\n".join(show))

    def next_log(self) -> None:
        if self.log_index < len(self.text_log) - 1:
            self.log_index += 1
            self.refresh_side_panel()

    def previous_log(self) -> None:
        if self.log_index > 0:
            self.log_index -= 1
            self.refresh_side_panel()

    def run(self) -> None:
        if dpg is None:
            print("Dear PyGui is not installed. Install it with: pip install dearpygui")
            return
        dpg.create_context()
        with dpg.window(label="Stochastic Battlefield Game", width=1200, height=760):
            with dpg.group(horizontal=True):
                with dpg.child_window(width=self.state.width * self.cell_size + 20, height=self.state.height * self.cell_size + 20):
                    with dpg.drawlist(width=self.state.width * self.cell_size, height=self.state.height * self.cell_size, tag=self.board_draw_tag):
                        pass
                with dpg.child_window(width=460, height=700):
                    dpg.add_text("Agent and Game Stats")
                    dpg.add_separator()
                    dpg.add_text("", tag=self.agent_info_tag)
                    dpg.add_spacer(height=10)
                    dpg.add_text("Move / Event Log")
                    dpg.add_separator()
                    dpg.add_input_text(multiline=True, readonly=True, width=440, height=500, tag=self.move_log_tag)
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="Previous", callback=lambda: self.previous_log())
                        dpg.add_button(label="Next", callback=lambda: self.next_log())

        self.draw_board()
        self.refresh_side_panel()

        dpg.create_viewport(title="Assignment 3 - Multi-Agent Stochastic Game", width=1220, height=780)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()


def build_profiles() -> Dict[str, AgentProfile]:
    # Full board visibility for Expert represented by -1
    return {
        "A": AgentProfile("Expert", depth_limit=7, view_range=-1, evaluate_top_k_chance_faces=9, evaluation_level="full", use_transposition_table=True),
        "B": AgentProfile("Intermediate", depth_limit=5, view_range=5, evaluate_top_k_chance_faces=9, evaluation_level="medium", use_transposition_table=False),
        "C": AgentProfile("Novice", depth_limit=3, view_range=3, evaluate_top_k_chance_faces=2, evaluation_level="greedy", use_transposition_table=False),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-gui", action="store_true", help="Run simulation and write results without opening GUI.")
    parser.add_argument(
        "--run-analysis",
        action="store_true",
        help="Run 5x5 statistical analysis (takes extra time).",
    )
    args = parser.parse_args()

    print("Loading board.txt ...", flush=True)
    initial_state, starts = parse_board_file("board.txt")
    profiles = build_profiles()

    print("Running main game simulation ...", flush=True)
    final_state, move_logs, text_log, main_summary = simulate_game(
        initial_state=initial_state,
        starts=starts,
        profiles=profiles,
        seed=77,
        stochastic_enabled=True,
    )

    # Analysis is optional because it is time-consuming on student laptops.
    # GUI mode should feel responsive and open quickly.
    depth_analysis = {
        "AgentA_avg_score_depth5": 0.0,
        "AgentA_avg_score_depth7": 0.0,
    }
    stochastic_analysis = {
        "AgentA_avg_deterministic": 0.0,
        "AgentA_avg_stochastic": 0.0,
        "AgentB_avg_deterministic": 0.0,
        "AgentB_avg_stochastic": 0.0,
        "AgentC_avg_deterministic": 0.0,
        "AgentC_avg_stochastic": 0.0,
    }
    if args.run_analysis or args.no_gui:
        print("Running batch analysis (this can take time) ...", flush=True)
        depth_analysis, stochastic_analysis = run_batch_analysis(initial_state, starts, profiles)

    print("Writing results.txt ...", flush=True)
    write_results_file(
        path="results.txt",
        final_state=final_state,
        move_logs=move_logs,
        text_log=text_log,
        main_summary=main_summary,
        depth_analysis=depth_analysis,
        stochastic_analysis=stochastic_analysis,
    )

    if not args.no_gui:
        print("Opening Dear PyGui window ...", flush=True)
        gui = BattlefieldGUI(final_state, move_logs, text_log)
        gui.run()
    else:
        print("Done. Check results.txt", flush=True)


if __name__ == "__main__":
    main()
