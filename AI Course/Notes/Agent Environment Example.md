# Agent Environment Example

## Run_vacuum_agent(vacuum_agent)
## Lab Tasks Using Only the Manual Functions

Below are 3 separate beginner-friendly Python programs written in the same simple style as your lab manual (Agent / Environment, percept → decide → action). I’m keeping the code basic, using only simple classes + loops + if/else, and no “extra smart” AI-looking code.

### Q1) Simple Reflex Agent (Warehouse Smart Robot) — no memory, only current percept

- 2D grid given by you (S start, G goal, 0 free, 1 obstacle)  
- Robot only checks immediate obstacles (up/down/left/right)  
- Uses condition–action rules  
- Prints moves, or says unreachable (if stuck or step limit ends)

```python
python
# Q1: SIMPLE REFLEX AGENT (Only current percept)
class Environment:
def __init__(self, grid):
self.grid = grid
self.rows = len(grid)
self.cols = len(grid[0])
def find_position(self, item):
for r in range(self.rows):
for c in range(self.cols):
if self.grid[r][c] == item:
return (r, c)
return None
def percept(self, agent):
r, c = agent.location
# check if each direction is blocked (obstacle or wall)
percept = {
"up_blocked": True,
"down_blocked": True,
"left_blocked": True,
"right_blocked": True,
"current": (r, c),
"goal": agent.goal
}
# UP
if r - 1 >= 0 and self.grid[r - 1][c] != 1:
percept["up_blocked"] = False
# DOWN
if r + 1 < self.rows and self.grid[r + 1][c] != 1:
percept["down_blocked"] = False
# LEFT
if c - 1 >= 0 and self.grid[r][c - 1] != 1:
percept["left_blocked"] = False
# RIGHT
if c + 1 < self.cols and self.grid[r][c + 1] != 1:
percept["right_blocked"] = False
return percept
def execute_action(self, agent, action):
r, c = agent.location
if action == "UP":
agent.location = (r - 1, c)
elif action == "DOWN":
agent.location = (r + 1, c)
elif action == "LEFT":
agent.location = (r, c - 1)
elif action == "RIGHT":
agent.location = (r, c + 1)
else:
# "STOP" or unknown
pass
class SimpleReflexRobot:
def __init__(self, start, goal):
self.location = start
self.goal = goal
self.moves = []
def select_action(self, percept):
# Simple rule: try to move closer to goal using only current percept
r, c = percept["current"]
gr, gc = percept["goal"]
# try vertical direction first if it helps
if gr < r and percept["up_blocked"] == False:
return "UP"
if gr > r and percept["down_blocked"] == False:
return "DOWN"
# then horizontal
if gc < c and percept["left_blocked"] == False:
return "LEFT"
if gc > c and percept["right_blocked"] == False:
return "RIGHT"
# if "best" direction blocked, try any available direction
if percept["up_blocked"] == False:
return "UP"
if percept["down_blocked"] == False:
return "DOWN"
if percept["left_blocked"] == False:
return "LEFT"
if percept["right_blocked"] == False:
return "RIGHT"
return "STOP"
# ---- Given Warehouse Grid ----
env_grid = [
['S', 0, 1, 0, 0],
[0,   0, 1, 0, 1],
[1,   0, 0, 0, 0],
[0,   1, 1, 0, 0],
[0,   0, 0, 1, 'G']
]
environment = Environment(env_grid)
start_pos = environment.find_position('S')
goal_pos = environment.find_position('G')
agent = SimpleReflexRobot(start_pos, goal_pos)
# Run robot
max_steps = 50  # step limit to avoid infinite loop
step = 0
while step < max_steps:
if agent.location == agent.goal:
print("Goal reached!")
break
p = environment.percept(agent)
action = agent.select_action(p)
if action == "STOP":
print("Robot is stuck. Destination unreachable.")
break
environment.execute_action(agent, action)
agent.moves.append(action)
step += 1
# Output
print("Moves:", agent.moves)
print("Total Moves:", len(agent.moves))
print("Final Position:", agent.location)
```

### Q2) Model-Based Agent (Warehouse Inspection Robot) — keeps internal model of inspected cells

- 5×5 grid  
- # = obstacle, X = damaged (treat like blocked), 0 = safe  
- Robot inspects current cell  
- Robot uses internal model to remember inspected cells  
- Avoids obstacles and tries not to revisit any cell  
- Note: This is written in a simple “beginner” way: it always moves to an uninspected neighbor if possible. If no move is possible, it stops.

```python
python
# Q2: MODEL-BASED INSPECTION AGENT
class Environment:
def __init__(self, grid):
self.grid = grid
self.rows = len(grid)
self.cols = len(grid[0])
def percept(self, agent):
r, c = agent.location
# percept includes: current cell value + whether already inspected (from
return {
"cell": self.grid[r][c],
"location": (r, c),
"already_inspected": agent.model["inspected"][r][c]
}
def is_safe(self, r, c):
if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
return False
if self.grid[r][c] == "#":
return False
if self.grid[r][c] == "X":
return False
return True
class ModelBasedInspectionRobot:
def __init__(self, start, rows, cols):
self.location = start
# internal model
self.model = {
"inspected": []
}
# make inspected grid (all False)
for r in range(rows):
row = []
for c in range(cols):
row.append(False)
self.model["inspected"].append(row)
self.actions = []
def update_model(self, percept):
r, c = percept["location"]
# mark inspected when we inspect
self.model["inspected"][r][c] = True
def decide(self, environment, percept):
r, c = percept["location"]
# Rule 1: If not inspected, inspect it
if percept["already_inspected"] == False:
return "INSPECT"
# Try order: UP, RIGHT, DOWN, LEFT (any order is fine)
if environment.is_safe(r - 1, c) and self.model["inspected"][r - 1][c] ==
return "UP"
if environment.is_safe(r, c + 1) and self.model["inspected"][r][c + 1] ==
return "RIGHT"
if environment.is_safe(r + 1, c) and self.model["inspected"][r + 1][c] ==
return "DOWN"
if environment.is_safe(r, c - 1) and self.model["inspected"][r][c - 1] ==
return "LEFT"
return "STOP"
# 0 = safe
# X = damaged
warehouse = [
[0,  0,  "#", 0,  0],
[0,  "X", "#", 0,  0],
[0,  0,  0,  0,  "#"],
["#", 0,  "#", 0,  0],
[0,  0,  0,  "X", 0]
]
env = Environment(warehouse)
start = (0, 0)  # starting point
robot = ModelBasedInspectionRobot(start, env.rows, env.cols)
max_steps = 100
step = 0
while step < max_steps:
p = env.percept(robot)
action = robot.decide(env, p)
if action == "INSPECT":
robot.update_model(p)
robot.actions.append("INSPECT " + str(robot.location))
elif action == "UP":
robot.location = (robot.location[0] - 1, robot.location[1])
robot.actions.append("MOVE UP")
elif action == "DOWN":
robot.location = (robot.location[0] + 1, robot.location[1])
robot.actions.append("MOVE DOWN")
elif action == "LEFT":
robot.location = (robot.location[0], robot.location[1] - 1)
robot.actions.append("MOVE LEFT")
elif action == "RIGHT":
robot.location = (robot.location[0], robot.location[1] + 1)
robot.actions.append("MOVE RIGHT")
else:
# STOP
break
step += 1
print("Robot Actions:")
for a in robot.actions:
print(a)
print("Stopped at:", robot.location)
```

### Q3) Goal-Based Agent (Food Delivery Robot) — completes all pickups

- 6×6 grid  
- Food points = F  
- Percepts = current position + pending pickups  
- Actions = Move + Pick  
- Goal = pick all food points  
Beginner logic:  
- Always target the first pending pickup  
- Move step-by-step toward it  
- When reached → pick and remove from pending list

```python
python
# Q3: GOAL-BASED AGENT (Food Pickup Robot)
class Environment:
def __init__(self, grid):
self.grid = grid
self.rows = len(grid)
self.cols = len(grid[0])
def find_all_food(self):
foods = []
for r in range(self.rows):
for c in range(self.cols):
if self.grid[r][c] == "F":
foods.append((r, c))
return foods
def percept(self, agent):
return {
"position": agent.location,
"pending": agent.pending_pickups
}
def execute_action(self, agent, action):
r, c = agent.location
if action == "UP":
agent.location = (r - 1, c)
elif action == "DOWN":
agent.location = (r + 1, c)
elif action == "LEFT":
agent.location = (r, c - 1)
elif action == "RIGHT":
agent.location = (r, c + 1)
elif action == "PICK":
# remove food from pending if robot is on it
if agent.location in agent.pending_pickups:
agent.pending_pickups.remove(agent.location)
else:
pass
class GoalBasedFoodRobot:
def __init__(self, start, pickups):
self.location = start
self.pending_pickups = pickups
self.actions = []
def decide(self, percept):
# if no pending pickups, goal done
if len(percept["pending"]) == 0:
return "STOP"
current = percept["position"]
target = percept["pending"][0]  # simple: pick the first one
r, c = current
tr, tc = target
# if on target, pick
if current == target:
return "PICK"
# move toward target (simple)
if tr < r:
return "UP"
if tr > r:
return "DOWN"
if tc < c:
return "LEFT"
if tc > c:
return "RIGHT"
return "STOP"
# ---- 6x6 Grid with Food Points ----
grid6 = [
[0, 0, 0, 0, "F", 0],
[0, 0, 0, 0, 0,  0],
[0, "F", 0, 0, 0, 0],
[0, 0, 0, 0, 0, "F"],
[0, 0, 0, 0, 0,  0],
["F", 0, 0, 0, 0, 0]
]
env = Environment(grid6)
all_food = env.find_all_food()
start = (0, 0)
robot = GoalBasedFoodRobot(start, all_food)
max_steps = 200
step = 0
while step < max_steps:
p = env.percept(robot)
action = robot.decide(p)
if action == "STOP":
break
env.execute_action(robot, action)
robot.actions.append(action + " -> " + str(robot.location))
step += 1
print("Actions Taken:")
for a in robot.actions:
print(a)
if len(robot.pending_pickups) == 0:
print("All food pickups completed!")
else:
print("Some pickups are still pending:", robot.pending_pickups)
```

- Your exact Q2 grid (where X and # are), and  
- Your exact Q3 food locations + start point

## Shorter, Beginner-Friendly Versions

below are shorter + simpler versions for Q1, Q2, Q3, written in the same beginner style as your manual (simple classes, percept() , execute_action() , and agent decide/select_action() with only if/elif ). No extra fancy functions.

### Q1 (Simple Reflex Agent) — short & beginner

```python
python
# Q1: Simple Reflex Robot (no memory)
class Environment:
def __init__(self, grid):
self.grid = grid
def percept(self, pos):
r, c = pos
return (r, c)
def is_free(self, r, c):
if r < 0 or r > 4 or c < 0 or c > 4:
return False
if self.grid[r][c] == 1:
return False
return True
class SimpleReflexRobot:
def __init__(self, start, goal):
self.pos = start
self.goal = goal
self.moves = []
def select_action(self, env):
r, c = env.percept(self.pos)
gr, gc = self.goal
# try to go closer to goal (only current view)
if gr > r and env.is_free(r + 1, c):
return "DOWN"
if gr < r and env.is_free(r - 1, c):
return "UP"
if gc > c and env.is_free(r, c + 1):
return "RIGHT"
if gc < c and env.is_free(r, c - 1):
return "LEFT"
# else try any open direction
if env.is_free(r, c + 1):
return "RIGHT"
if env.is_free(r + 1, c):
return "DOWN"
if env.is_free(r, c - 1):
return "LEFT"
if env.is_free(r - 1, c):
return "UP"
return "STOP"
def move(self, action):
r, c = self.pos
if action == "UP":
self.pos = (r - 1, c)
elif action == "DOWN":
self.pos = (r + 1, c)
elif action == "LEFT":
self.pos = (r, c - 1)
elif action == "RIGHT":
self.pos = (r, c + 1)
grid = [
['S', 0, 1, 0, 0],
[0,   0, 1, 0, 1],
[1,   0, 0, 0, 0],
[0,   1, 1, 0, 0],
[0,   0, 0, 1, 'G']
]
# find S and G manually (beginner way)
start = (0, 0)
goal = (4, 4)
env = Environment(grid)
robot = SimpleReflexRobot(start, goal)
for i in range(50):
if robot.pos == robot.goal:
print("Goal reached!")
break
action = robot.select_action(env)
if action == "STOP":
print("Unreachable (stuck).")
break
robot.move(action)
robot.moves.append(action)
print("Moves:", robot.moves)
print("Final:", robot.pos)
```

### Q2 (Model-Based Agent) — short & beginner

```python
python
# Q2: Model-Based Inspection Robot (remembers inspected)
class Environment:
def __init__(self, grid):
self.grid = grid
def is_safe(self, r, c):
if r < 0 or r > 4 or c < 0 or c > 4:
return False
if self.grid[r][c] == "#" or self.grid[r][c] == "X":
return False
return True
class ModelRobot:
def __init__(self, start):
self.pos = start
self.inspected = [[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False]]
self.actions = []
def percept(self):
r, c = self.pos
return (r, c, self.inspected[r][c])
def decide(self, env):
r, c, done = self.percept()
if done == False:
return "INSPECT"
# move to any uninspected safe neighbor
if env.is_safe(r - 1, c) and self.inspected[r - 1][c] == False:
return "UP"
if env.is_safe(r, c + 1) and self.inspected[r][c + 1] == False:
return "RIGHT"
if env.is_safe(r + 1, c) and self.inspected[r + 1][c] == False:
return "DOWN"
if env.is_safe(r, c - 1) and self.inspected[r][c - 1] == False:
return "LEFT"
return "STOP"
def do_action(self, action):
r, c = self.pos
if action == "INSPECT":
self.inspected[r][c] = True
self.actions.append("INSPECT " + str(self.pos))
elif action == "UP":
self.pos = (r - 1, c)
self.actions.append("MOVE UP")
elif action == "DOWN":
self.pos = (r + 1, c)
self.actions.append("MOVE DOWN")
elif action == "LEFT":
self.pos = (r, c - 1)
self.actions.append("MOVE LEFT")
elif action == "RIGHT":
self.pos = (r, c + 1)
self.actions.append("MOVE RIGHT")
grid = [
[0,  0,  "#", 0,  0],
[0,  "X", "#", 0,  0],
[0,  0,  0,  0,  "#"],
["#", 0,  "#", 0,  0],
[0,  0,  0,  "X", 0]
]
env = Environment(grid)
robot = ModelRobot((0, 0))
for i in range(100):
action = robot.decide(env)
if action == "STOP":
break
robot.do_action(action)
for a in robot.actions:
print(a)
print("Stopped at:", robot.pos)
```

### Q3 (Goal-Based Agent) — short & beginner

```python
python
# Q3: Goal-Based Food Pickup Robot
class Environment:
def __init__(self, grid):
self.grid = grid
def find_food(self):
foods = []
for r in range(6):
for c in range(6):
if self.grid[r][c] == "F":
foods.append((r, c))
return foods
class GoalRobot:
def __init__(self, start, foods):
self.pos = start
self.foods = foods
self.actions = []
def percept(self):
return (self.pos, self.foods)
def decide(self):
pos, foods = self.percept()
if len(foods) == 0:
return "STOP"
target = foods[0]
r, c = pos
tr, tc = target
if pos == target:
return "PICK"
if tr > r:
return "DOWN"
if tr < r:
return "UP"
if tc > c:
return "RIGHT"
if tc < c:
return "LEFT"
return "STOP"
def do_action(self, action):
r, c = self.pos
if action == "UP":
self.pos = (r - 1, c)
elif action == "DOWN":
self.pos = (r + 1, c)
elif action == "LEFT":
self.pos = (r, c - 1)
elif action == "RIGHT":
self.pos = (r, c + 1)
elif action == "PICK":
if self.pos in self.foods:
self.foods.remove(self.pos)
self.actions.append(action + " -> " + str(self.pos))
grid6 = [
[0, 0, 0, 0, "F", 0],
[0, 0, 0, 0, 0,  0],
[0, "F", 0, 0, 0, 0],
[0, 0, 0, 0, 0, "F"],
[0, 0, 0, 0, 0,  0],
["F", 0, 0, 0, 0, 0]
]
env = Environment(grid6)
foods = env.find_food()
robot = GoalRobot((0, 0), foods)
for i in range(200):
action = robot.decide()
if action == "STOP":
break
robot.do_action(action)
for a in robot.actions:
print(a)
print("Pending Foods:", robot.foods)
```

keep only the main logic, but these are already short + beginner-friendly and match your lab style.  
here are even more tiny / manual-style versions for Q1, Q2, Q3. Same basic pattern: Environment + Agent, simple percept / decide / execute_action , only if/elif , beginner-looking.

### Q1) Extra Short Simple Reflex Robot

```python
python
# Q1: Simple Reflex Agent (very short)
class Environment:
def __init__(self, grid):
self.grid = grid
def is_free(self, r, c):
if r < 0 or r > 4 or c < 0 or c > 4:
return False
return self.grid[r][c] != 1
def percept(self, pos):
return pos
class Robot:
def __init__(self, start, goal):
self.pos = start
self.goal = goal
self.moves = []
def select_action(self, env):
r, c = env.percept(self.pos)
gr, gc = self.goal
if gr > r and env.is_free(r+1, c): return "DOWN"
if gr < r and env.is_free(r-1, c): return "UP"
if gc > c and env.is_free(r, c+1): return "RIGHT"
if gc < c and env.is_free(r, c-1): return "LEFT"
if env.is_free(r, c+1): return "RIGHT"
if env.is_free(r+1, c): return "DOWN"
if env.is_free(r, c-1): return "LEFT"
if env.is_free(r-1, c): return "UP"
return "STOP"
def move(self, action):
r, c = self.pos
if action == "UP": self.pos = (r-1, c)
elif action == "DOWN": self.pos = (r+1, c)
elif action == "LEFT": self.pos = (r, c-1)
elif action == "RIGHT": self.pos = (r, c+1)
grid = [
['S', 0, 1, 0, 0],
[0,   0, 1, 0, 1],
[1,   0, 0, 0, 0],
[0,   1, 1, 0, 0],
[0,   0, 0, 1, 'G']
]
env = Environment(grid)
robot = Robot((0, 0), (4, 4))
for i in range(50):
if robot.pos == robot.goal:
print("Reached Goal")
break
a = robot.select_action(env)
if a == "STOP":
print("Unreachable")
break
robot.move(a)
robot.moves.append(a)
print(robot.moves)
```

### Q2) Extra Short Model-Based Inspection Robot

```python
python
# Q2: Model-Based Agent (very short)
class Environment:
def __init__(self, grid):
self.grid = grid
def safe(self, r, c):
if r < 0 or r > 4 or c < 0 or c > 4: return False
if self.grid[r][c] == "#" or self.grid[r][c] == "X": return False
return True
class Robot:
def __init__(self, start):
self.pos = start
self.ins = [[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False]]
self.actions = []
def percept(self):
r, c = self.pos
return (r, c, self.ins[r][c])
def decide(self, env):
r, c, done = self.percept()
if done == False: return "INSPECT"
if env.safe(r-1, c) and self.ins[r-1][c] == False: return "UP"
if env.safe(r, c+1) and self.ins[r][c+1] == False: return "RIGHT"
if env.safe(r+1, c) and self.ins[r+1][c] == False: return "DOWN"
if env.safe(r, c-1) and self.ins[r][c-1] == False: return "LEFT"
return "STOP"
def do(self, action):
r, c = self.pos
if action == "INSPECT":
self.ins[r][c] = True
self.actions.append("INSPECT")
elif action == "UP":
self.pos = (r-1, c); self.actions.append("UP")
elif action == "DOWN":
self.pos = (r+1, c); self.actions.append("DOWN")
elif action == "LEFT":
self.pos = (r, c-1); self.actions.append("LEFT")
elif action == "RIGHT":
self.pos = (r, c+1); self.actions.append("RIGHT")
grid = [
[0,  0,  "#", 0,  0],
[0,  "X", "#", 0,  0],
[0,  0,  0,  0,  "#"],
["#", 0,  "#", 0,  0],
[0,  0,  0,  "X", 0]
]
env = Environment(grid)
robot = Robot((0, 0))
for i in range(100):
a = robot.decide(env)
if a == "STOP":
break
robot.do(a)
print(robot.actions)
```

### Q3) Extra Short Goal-Based Food Pickup Robot

```python
python
# Q3: Goal-Based Agent (very short)
class Environment:
def __init__(self, grid):
self.grid = grid
def foods(self):
f = []
for r in range(6):
for c in range(6):
if self.grid[r][c] == "F":
f.append((r, c))
return f
class Robot:
def __init__(self, start, foods):
self.pos = start
self.foods = foods
self.actions = []
def decide(self):
if len(self.foods) == 0:
return "STOP"
r, c = self.pos
tr, tc = self.foods[0]
if self.pos == (tr, tc):
return "PICK"
if tr > r: return "DOWN"
if tr < r: return "UP"
if tc > c: return "RIGHT"
if tc < c: return "LEFT"
return "STOP"
def do(self, action):
r, c = self.pos
if action == "UP": self.pos = (r-1, c)
elif action == "DOWN": self.pos = (r+1, c)
elif action == "LEFT": self.pos = (r, c-1)
elif action == "RIGHT": self.pos = (r, c+1)
elif action == "PICK":
if self.pos in self.foods:
self.foods.remove(self.pos)
self.actions.append(action)
grid6 = [
[0, 0, 0, 0, "F", 0],
[0, 0, 0, 0, 0,  0],
[0, "F", 0, 0, 0, 0],
[0, 0, 0, 0, 0, "F"],
[0, 0, 0, 0, 0,  0],
["F", 0, 0, 0, 0, 0]
]
env = Environment(grid6)
robot = Robot((0, 0), env.foods())
for i in range(200):
a = robot.decide()
if a == "STOP":
break
robot.do(a)
print(robot.actions)
print("Pending:", robot.foods)
```

- print the path positions (like (row,col) after each move),  
- or make output exactly like: Move: RIGHT , Move: DOWN etc.

## Task 3 Line by Line

Below is a simple, line-by-line explanation of Task 3 (Goal-Based Food Pickup Robot).

### Task 3 Code (for reference)

```python
python
class Environment:
def __init__(self, grid):
self.grid = grid
def foods(self):
f = []
for r in range(6):
for c in range(6):
if self.grid[r][c] == "F":
f.append((r, c))
return f
class Robot:
def __init__(self, start, foods):
self.pos = start
self.foods = foods
self.actions = []
def decide(self):
if len(self.foods) == 0:
return "STOP"
r, c = self.pos
tr, tc = self.foods[0]
if self.pos == (tr, tc):
return "PICK"
if tr > r: return "DOWN"
if tr < r: return "UP"
if tc > c: return "RIGHT"
if tc < c: return "LEFT"
return "STOP"
def do(self, action):
r, c = self.pos
if action == "UP": self.pos = (r-1, c)
elif action == "DOWN": self.pos = (r+1, c)
elif action == "LEFT": self.pos = (r, c-1)
elif action == "RIGHT": self.pos = (r, c+1)
elif action == "PICK":
if self.pos in self.foods:
self.foods.remove(self.pos)
self.actions.append(action)
grid6 = [
[0, 0, 0, 0, "F", 0],
[0, 0, 0, 0, 0,  0],
[0, "F", 0, 0, 0, 0],
[0, 0, 0, 0, 0, "F"],
[0, 0, 0, 0, 0,  0],
["F", 0, 0, 0, 0, 0]
]
env = Environment(grid6)
robot = Robot((0, 0), env.foods())
for i in range(200):
a = robot.decide()
if a == "STOP":
break
robot.do(a)
print(robot.actions)
print("Pending:", robot.foods)
```

### Environment Class

#### Line

```text
python
class Environment:
```

Creates a class called Environment.  
This represents the warehouse grid.

#### Line

```python
python
def __init__(self, grid):
```

This is the constructor.  
It runs automatically when we create the environment.

#### Line

```text
python
self.grid = grid
```

Stores the grid inside the environment.  
Variable:  
- self.grid → the 6×6 warehouse map  
- Contains:  
  - 0 → empty space  
  - "F" → food pickup point

#### Line

```python
python
def foods(self):
```

Function to find all food points in the grid.

#### Line

```text
python
f = []
```

Creates an empty list called f .  
Variable:  
- f → list of all food locations

#### Lines

```python
python
for r in range(6):
for c in range(6):
```

Loops through every cell of the 6×6 grid.  
Variables:  
- r → row number (0–5)  
- c → column number (0–5)

#### Line

```text
python
if self.grid[r][c] == "F":
```

Checks if the cell contains food.

#### Line

```text
python
f.append((r, c))
```

If food found, store its position.  
Example:

```text
scss
(0,4)
(2,1)
(3,5)
(5,0)
```

#### Line

```text
python
return f
```

Returns the list of food positions.

#### Line

```text
python
class Robot:
```

Creates a robot class.

#### Line

```python
python
def __init__(self, start, foods):
```

Robot constructor.  
Parameters:  
- start → starting position  
- foods → list of all food locations

#### Line

```text
python
self.pos = start
```

Stores robot’s current position.  
Variable:  
- self.pos → robot’s location  
- Example:

```text
scss
(0,0)
```

#### Line

```text
python
self.foods = foods
```

Stores list of remaining food pickups.  
Example:

```text
css
[(0,4), (2,1), (3,5), (5,0)]
```

#### Line

```text
python
self.actions = []
```

Stores all actions robot performs.  
Example:

```text
css
["RIGHT", "RIGHT", "DOWN", "PICK"]
```

#### Line

```python
python
def decide(self):
```

Robot decides what to do next.

#### Line

```text
python
if len(self.foods) == 0:
return "STOP"
```

If no food left:  
- Stop the robot

#### Line

```text
python
r, c = self.pos
```

Splits robot’s position into row and column.  
Example:

```text
ini
self.pos = (2,3)
r = 2
c = 3
```

#### Line

```text
python
tr, tc = self.foods[0]
```

Selects the first food location as target.  
Variables:  
- tr → target row  
- tc → target column  
Example:

```text
ini
target = (0,4)
tr = 0
tc = 4
```

#### Line

```text
python
if self.pos == (tr, tc):
return "PICK"
```

If robot is already on food:  
- Pick it up

#### Movement logic

```text
python
if tr > r: return "DOWN"
```

If food is below robot:  
- Move down

```text
python
if tr < r: return "UP"
```

If food is above robot:  
- Move up

```text
python
if tc > c: return "RIGHT"
```

If food is to the right:  
- Move right

```text
python
if tc < c: return "LEFT"
```

If food is to the left:  
- Move left

#### Line

```text
python
return "STOP"
```

If nothing matches, stop.

#### Line

```python
python
def do(self, action):
```

Executes the action.

#### Line

```text
python
r, c = self.pos
```

Get current position.

#### Movement actions

```text
python
if action == "UP": self.pos = (r-1, c)
```

Move up.

```text
python
elif action == "DOWN": self.pos = (r+1, c)
```

Move down.

```text
python
elif action == "LEFT": self.pos = (r, c-1)
```

Move left.

```text
python
elif action == "RIGHT": self.pos = (r, c+1)
```

Move right.

#### Picking food

```text
python
elif action == "PICK":
if self.pos in self.foods:
self.foods.remove(self.pos)
```

If robot is on a food location:  
- Remove that food from list

#### Store action

```text
python
self.actions.append(action)
```

Save action in history.

### Grid Definition

```text
python
grid6 = [
[0, 0, 0, 0, "F", 0],
...
]
```

Defines the 6×6 warehouse.

### Create environment and robot

```text
python
env = Environment(grid6)
```

Creates environment.

```text
python
robot = Robot((0, 0), env.foods())
```

Creates robot:  
- Start at (0,0)  
- With list of food positions

### Main loop

```python
python
for i in range(200):
```

Runs robot for up to 200 steps.

```text
python
a = robot.decide()
```

Robot decides next action.

```text
python
if a == "STOP":
break
```

Stop if no more actions.

```text
python
robot.do(a)
```

Execute action.

### Output

```python
python
print(robot.actions)
```

Shows all actions taken.

```python
python
print("Pending:", robot.foods)
```

Shows remaining food (if any).

### Summary of Main Variables

| Variable | Meaning |
|---|---|
|  | 6×6 warehouse map |

```text
grid6
```

|  | Robot’s current position |
|---|---|

```text
self.pos
```

|  | List of remaining food locations |
|---|---|

```text
self.foods
```

| Variable | Meaning |
|---|---|
|  | List of actions taken |

```text
self.actions
```

|  | Robot row and column |
|---|---|

```text
r, c
```

|  | Target food position |
|---|---|

```text
tr, tc
```

|  | Current action (UP, DOWN, etc.) |
|---|---|

```text
action
```

- explain Q1 and Q2 line by line  
- draw a step-by-step movement diagram  
- or convert this into exam-ready written explanation.

## Room.action() print("Updated State:", room.state) # Agent acts again room.action() print("Updated
## Class ModelBasedReflexAgent: def __init__(self, environment): self.environment = environment self.model =

## Def choose_action(self)
## Rewriting the Tasks From the Sample Code

- very small classes  
- simple percept() and action() / choose_action()  
- simple lists + if/elif  
- no extra libraries (only random if really needed — but here we don’t need it)

### Q1) Simple Reflex Warehouse Robot (Only Current Percept, No Memory)

Idea: Robot just checks immediate neighbors and follows simple rules to move toward goal.

```python
python
class WarehouseEnv:
def __init__(self, grid):
self.grid = grid
def percept(self, pos):
r, c = pos
return (r, c)
def free(self, r, c):
if r < 0 or r > 4 or c < 0 or c > 4:
return False
if self.grid[r][c] == 1:
return False
return True
class SimpleReflexRobot:
def __init__(self, start, goal):
self.pos = start
self.goal = goal
self.moves = []
def choose_action(self, env):
r, c = env.percept(self.pos)
gr, gc = self.goal
# go closer to goal
if gr > r and env.free(r+1, c): return "DOWN"
if gr < r and env.free(r-1, c): return "UP"
if gc > c and env.free(r, c+1): return "RIGHT"
if gc < c and env.free(r, c-1): return "LEFT"
# else try any open direction
if env.free(r, c+1): return "RIGHT"
if env.free(r+1, c): return "DOWN"
if env.free(r, c-1): return "LEFT"
if env.free(r-1, c): return "UP"
return "STOP"
def action(self, act):
r, c = self.pos
if act == "UP": self.pos = (r-1, c)
elif act == "DOWN": self.pos = (r+1, c)
elif act == "LEFT": self.pos = (r, c-1)
elif act == "RIGHT": self.pos = (r, c+1)
self.moves.append(act)
grid = [
['S', 0, 1, 0, 0],
[0,   0, 1, 0, 1],
[1,   0, 0, 0, 0],
[0,   1, 1, 0, 0],
[0,   0, 0, 1, 'G']
]
env = WarehouseEnv(grid)
robot = SimpleReflexRobot((0,0), (4,4))
for i in range(50):
if robot.pos == robot.goal:
print("Goal reached!")
break
act = robot.choose_action(env)
if act == "STOP":
print("Destination unreachable!")
break
robot.action(act)
print("Moves:", robot.moves)
print("Final Position:", robot.pos)
```

### Q2) Model-Based Inspection Robot (Remembers Inspected Cells)

Idea: Robot keeps an internal memory grid inspected (True/False).  
It inspects current cell if not inspected, else moves to a safe uninspected neighbor.

```python
python
class InspectionEnv:
def __init__(self, grid):
self.grid = grid
def safe(self, r, c):
if r < 0 or r > 4 or c < 0 or c > 4:
return False
if self.grid[r][c] == "#" or self.grid[r][c] == "X":
return False
return True
def percept(self, pos):
return pos
class ModelRobot:
def __init__(self, start):
self.pos = start
self.inspected = [
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False]
]
self.actions = []
def choose_action(self, env):
r, c = env.percept(self.pos)
if self.inspected[r][c] == False:
return "INSPECT"
if env.safe(r-1, c) and self.inspected[r-1][c] == False: return "UP"
if env.safe(r, c+1) and self.inspected[r][c+1] == False: return "RIGHT"
if env.safe(r+1, c) and self.inspected[r+1][c] == False: return "DOWN"
if env.safe(r, c-1) and self.inspected[r][c-1] == False: return "LEFT"
return "STOP"
def action(self, act):
r, c = self.pos
if act == "INSPECT":
self.inspected[r][c] = True
self.actions.append("INSPECT " + str(self.pos))
elif act == "UP":
self.pos = (r-1, c); self.actions.append("UP")
elif act == "DOWN":
self.pos = (r+1, c); self.actions.append("DOWN")
elif act == "LEFT":
self.pos = (r, c-1); self.actions.append("LEFT")
elif act == "RIGHT":
self.pos = (r, c+1); self.actions.append("RIGHT")
grid = [
[0,  0,  "#", 0,  0],
[0,  "X", "#", 0,  0],
[0,  0,  0,  0,  "#"],
["#", 0,  "#", 0,  0],
[0,  0,  0,  "X", 0]
]
env = InspectionEnv(grid)
robot = ModelRobot((0,0))
for i in range(100):
act = robot.choose_action(env)
if act == "STOP":
break
robot.action(act)
print("Actions:", robot.actions)
print("Stopped:", robot.pos)
```

### Q3) Goal-Based Food Pickup Robot (Finish All Pickups)

Idea: Robot always targets the first pending food and moves step-by-step until it reaches it, then PICK.

```python
python
class FoodEnv:
def __init__(self, grid):
self.grid = grid
def find_food(self):
foods = []
for r in range(6):
for c in range(6):
if self.grid[r][c] == "F":
foods.append((r, c))
return foods
def percept(self, pos, foods):
return (pos, foods)
class GoalRobot:
def __init__(self, start, foods):
self.pos = start
self.foods = foods
self.actions = []
def choose_action(self, env):
pos, foods = env.percept(self.pos, self.foods)
if len(foods) == 0:
return "STOP"
target = foods[0]
r, c = pos
tr, tc = target
if pos == target:
return "PICK"
if tr > r: return "DOWN"
if tr < r: return "UP"
if tc > c: return "RIGHT"
if tc < c: return "LEFT"
return "STOP"
def action(self, act):
r, c = self.pos
if act == "UP": self.pos = (r-1, c)
elif act == "DOWN": self.pos = (r+1, c)
elif act == "LEFT": self.pos = (r, c-1)
elif act == "RIGHT": self.pos = (r, c+1)
elif act == "PICK":
if self.pos in self.foods:
self.foods.remove(self.pos)
self.actions.append(act)
grid6 = [
[0, 0, 0, 0, "F", 0],
[0, 0, 0, 0, 0,  0],
[0, "F", 0, 0, 0, 0],
[0, 0, 0, 0, 0, "F"],
[0, 0, 0, 0, 0,  0],
["F", 0, 0, 0, 0, 0]
]
env = FoodEnv(grid6)
foods = env.find_food()
robot = GoalRobot((0,0), foods)
for i in range(200):
act = robot.choose_action(env)
if act == "STOP":
break
robot.action(act)
print("Actions:", robot.actions)
print("Pending Food:", robot.foods)
print("Final Position:", robot.pos)
```

but these already match your sample patterns closely.

## The self Keyword and Task 3 Step by Step
#### What does self mean in Python?

self simply means “this object itself”.  
When you create an object (like robot = GoalRobot(...) ), that object has its own data (variables) and functions (methods).  
Inside the class, Python needs a way to refer to that same object — so we use self .  
Example:

```text
python
self.pos
```

means: the position stored inside THIS robot object.  
If you remove self , Python will not know which object’s data you are talking about.  
Important point:  
self is not a special keyword in Python (like if , for ).  
It’s just a name, but everyone uses self by convention.

### Task 3 (Goal-Based Food Pickup Robot) — Full Step-by-Step Explanation

- each class  
- each function  
- each line  
- each argument (parameters)  
- why we use it  
- what syntax means

### Task 3 Code (same one)

```python
python
class FoodEnv:
def __init__(self, grid):
self.grid = grid
def find_food(self):
foods = []
for r in range(6):
for c in range(6):
if self.grid[r][c] == "F":
foods.append((r, c))
return foods
def percept(self, pos, foods):
return (pos, foods)
class GoalRobot:
def __init__(self, start, foods):
self.pos = start
self.foods = foods
self.actions = []
def choose_action(self, env):
pos, foods = env.percept(self.pos, self.foods)
if len(foods) == 0:
return "STOP"
target = foods[0]
r, c = pos
tr, tc = target
if pos == target:
return "PICK"
if tr > r: return "DOWN"
if tr < r: return "UP"
if tc > c: return "RIGHT"
if tc < c: return "LEFT"
return "STOP"
def action(self, act):
r, c = self.pos
if act == "UP": self.pos = (r-1, c)
elif act == "DOWN": self.pos = (r+1, c)
elif act == "LEFT": self.pos = (r, c-1)
elif act == "RIGHT": self.pos = (r, c+1)
elif act == "PICK":
if self.pos in self.foods:
self.foods.remove(self.pos)
self.actions.append(act)
grid6 = [
[0, 0, 0, 0, "F", 0],
[0, 0, 0, 0, 0,  0],
[0, "F", 0, 0, 0, 0],
[0, 0, 0, 0, 0, "F"],
[0, 0, 0, 0, 0,  0],
["F", 0, 0, 0, 0, 0]
]
env = FoodEnv(grid6)
foods = env.find_food()
robot = GoalRobot((0,0), foods)
for i in range(200):
act = robot.choose_action(env)
if act == "STOP":
break
robot.action(act)
print("Actions:", robot.actions)
print("Pending Food:", robot.foods)
print("Final Position:", robot.pos)
```

### 1) class FoodEnv

- class keyword is used to create a blueprint.  
- FoodEnv is the name of environment class.  
Environment means: the warehouse grid.

### 2) def __init__(self, grid)

- def means we are defining a function.  
- __init__ is a special function (constructor).  
- It runs automatically when we make an object like:

```text
python
env = FoodEnv(grid6)
```

#### Arguments

- self = current object (env object)  
- grid = the grid we pass (grid6)

### 3) self.grid = grid

Stores the grid inside the environment object.  
So later we can use:

```text
python
self.grid[r][c]
```

### 4) def find_food(self)

This function finds all food points "F" .

### 5) foods = []

Creates an empty list.  
- foods will store all food positions.  
Example:

```text
python
foods = [(0,4), (2,1), (3,5), (5,0)]
```

### 6) for r in range(6)

Loop rows from 0 to 5.  
- for = loop keyword  
- range(6) = gives numbers 0,1,2,3,4,5  
- r = row index

### 7) for c in range(6)

Loop columns from 0 to 5.  
- c = column index

### 8) if self.grid[r][c] == "F"

Checks if current cell contains food.

### 9) foods.append((r, c))

If it is food, save location.  
- append() adds item at end of list  
- (r, c) is a tuple showing position (row, col)

### 10) return foods

Returns list back to where function is called.

### 11) def percept(self, pos, foods)

This is percept function (like your manual).  
Robot sensors detect:  
- current position  
- pending pickups list  
So we pass:  
- pos = robot location  
- foods = remaining food list

### 12) return (pos, foods)

Returns both things as percept.

### 13) class GoalRobot

Goal-based robot class.  
Goal: pick all food.

### 14) def __init__(self, start, foods)

Constructor of robot.  
Arguments:  
- start = starting location, like (0,0)  
- foods = list of food locations

### 15) self.pos = start

Robot position stored.

### 16) self.foods = foods

Stores list of pending pickups.

### 17) self.actions = []

Stores actions history.

### Decision Making 18) def choose_action(self, env)

Robot chooses next action.  
Argument:  
- env = environment object  
- We need it because environment provides percept.

### 19) pos, foods = env.percept(self.pos, self.foods)

- Calls percept method of environment.  
- Gets:  
  - pos (robot location)  
  - foods (pending foods)  
Why do we use it?  
Because in AI agent concept:  
agent chooses action based on percept.

### 20) if len(foods) == 0: return "STOP"

- len() gives list size.  
- if no food left => goal achieved => stop.

### 21) target = foods[0]

Takes the first food as target.  
- foods[0] means first element of list.

### 22) r, c = pos

Split robot position into row and column.

### 23) tr, tc = target

Split target position.

### 24) if pos == target: return "PICK"

If robot is already on food location, pick it.

### 25) Movement rules

```text
python
if tr > r: return "DOWN"
```

If target row is below robot => go down.

```text
python
if tr < r: return "UP"
python
if tc > c: return "RIGHT"
python
if tc < c: return "LEFT"
```

This is the simplest beginner movement.

### 26) return "STOP"

If nothing possible, stop (rare case).

### Executing Actions 27) def action(self, act)

Perform action that was decided.  
Argument:  
- act = action string ("UP", "DOWN", "PICK"...)

### 28) r, c = self.pos

Get current position.

### 29) Move updates

```text
python
if act == "UP": self.pos = (r-1, c)
```

Because moving up means row decreases.  
Similarly for other directions.

### 30) Pick

```text
python
elif act == "PICK":
if self.pos in self.foods:
self.foods.remove(self.pos)
```

- in checks if position exists in list  
- remove() removes that food from pending list

### 31) self.actions.append(act)

Store that action into history list.

### Main Program 32) grid6 = [...]

This is your 6x6 environment.

### 33) env = FoodEnv(grid6)

Creates environment object.

### 34) foods = env.find_food()

Gets all food locations.

### 35) robot = GoalRobot((0,0), foods)

Creates robot starting at (0,0) with pending foods.

### 36) Loop

```python
python
for i in range(200):
```

Runs max 200 steps (just safety).

### 37)

```text
python
act = robot.choose_action(env)
```

Robot decides what to do.

### 38)

```text
python
if act == "STOP":
break
```

Stop loop if finished.

### 39)

```text
python
robot.action(act)
```

Robot performs action and updates its position or picks food.

### 40) Print results

Shows actions list, pending foods, final position.

### Why we use these keywords (Very Simple)

| Keyword | Why used |
|---|---|
|  | create a blueprint |

```text
class
```

|  | define a function |
|---|---|

```text
def
```

|  | send result back |
|---|---|

```text
return
```

|  | decision making |
|---|---|

```text
if/elif
```

|  | looping through grid |
|---|---|

```text
for
```

|  | checking membership in list |
|---|---|

```text
in
```

|  | exit loop |
|---|---|

```text
break
```

|  | generate numbers for loop |
|---|---|

```text
range()
```

|  | check list size |
|---|---|

```text
len()
```

|  | store data inside object |
|---|---|

```text
self
```

- Step 1: robot at (0,0) target (0,4) move RIGHT  
- Step 2: robot at (0,1) ...  
- until it picks all food.

## Working Without self (Compared With this in C++)
### What happens if we don’t use self in Python?

Inside a class, if you don’t use self , Python cannot access the object’s variables or functions.  
It will cause an error.

#### Example WITHOUT self (wrong code)

```python
python
class Robot:
def __init__(start):
pos = start   # no self
```

This will cause an error because:  
- Python expects the first parameter of class methods to refer to the object. Without it, Python does not know where to store pos .

#### Correct version WITH self

```python
python
class Robot:
def __init__(self, start):
self.pos = start
```

Here:  
- self = the current robot object  
- self.pos = the position stored inside that robot

### Why is self necessary?

Because Python needs a way to say:  
- “This variable belongs to this specific object.”  
Example:

```text
python
robot1 = Robot((0,0))
robot2 = Robot((5,5))
```

Now:

```text
ini
robot1.pos = (0,0)
robot2.pos = (5,5)
```

Without self , both robots would not have their own separate data.

### What happens if you remove self from a method?

Example:

```python
python
class Robot:
def move():
print("Moving")
```

Now if you run:

```text
python
r = Robot()
r.move()
```

You will get an error like:

```text
javascript
TypeError: move() takes 0 positional arguments but 1 was given
```

Because Python automatically sends the object as the first argument.

### Can we use something other than self ?

self is not a keyword. It is just a naming convention.  
You can technically write:

```python
python
class Robot:
def __init__(me, start):
me.pos = start
```

This will work.  
But it is not recommended, because:  
- All Python programmers use self  
- It is the standard style  
- Your teacher or examiner may expect it  
So always use:

```text
python
self
```

### Is self like this in C++?

conceptually they are the same.

| Concept | Python | C++ |
|---|---|---|
| Reference to current object self this |  |  |
| Used inside class methods | Yes | Yes |
| Automatically passed | Yes | Yes |
| Keyword or convention | Convention | Keyword |

#### Example comparison

Python

```python
python
class Robot:
def __init__(self, x):
self.x = x
```

C++

```text
cpp
class Robot {
int x;
public:
Robot(int x) {
this->x = x;
}
};
```

Both mean:  
- “Store the value x inside this object.”

### Key Differences between self and this

|  | Python self | C++ this |
|---|---|---|
| Feature |  |  |
| Is it a keyword? | No | Yes |
| Must you write it? | Yes (in method parameters) | No (automatic pointer) |
| Used to access variables self.x this->x |  |  |

### Simple Summary

- self = the current object  
- It lets the object access its own variables  
- Without self , class methods will not work  
- You can rename it, but you should not  
- It works like this in C++  
- a visual diagram of how self works in memory  
- or a step-by-step example with two robots showing how self keeps their data separate.

## self vs this, and Operator Overloading

self in Python is conceptually similar to the this keyword in C++, but it is not related to operator overloading.  
They are two completely different concepts.

### 1) self in Python vs this in C++ Main idea

Both refer to the current object.

#### Python example

```python
python
class Robot:
def __init__(self, x):
self.x = x
```

#### C++ equivalent

```text
cpp
class Robot {
int x;
public:
Robot(int x) {
this->x = x;
}
};
```

#### Meaning

Both lines mean:  
- “Store this value inside this object.”

### Key difference

|  | Python self | C++ this |
|---|---|---|
| Feature |  |  |
| Type | Convention (name) | Real keyword |
| Must be written? | Yes, in parameters | No, automatic pointer |
| How used self.x this->x |  |  |

So yes:  
self ≈ this  
But only in object reference meaning.

### 2) What is Operator Overloading?

Operator overloading is a completely different concept.  
It means:  
- Changing how operators like + , - , * , == behave for your own objects.

### Example in C++

```text
cpp
class Point {
public:
int x, y;
Point(int a, int b) {
x = a;
y = b;
}
Point operator+(Point p) {
return Point(x + p.x, y + p.y);
}
};
```

Now you can write:

```text
cpp
Point a(1,2);
Point b(3,4);
Point c = a + b;   // uses overloaded +
```

### Same concept in Python

Python uses special methods for operator overloading.  
Example:

```python
python
class Point:
def __init__(self, x, y):
self.x = x
self.y = y
def __add__(self, other):
return Point(self.x + other.x,
self.y + other.y)
```

Now:

```text
python
a = Point(1,2)
b = Point(3,4)
c = a + b
```

Python internally calls:

```text
css
a.__add__(b)
```

### 3) Relationship between self and operator overloading

They are not the same thing.

| Concept | What it does |
|---|---|
|  | Refers to the current object |

```text
self
```

| Operator overloading | Changes behavior of operators |
|---|---|

But self is used inside operator overloading functions.  
Example:

```python
python
def __add__(self, other):
```

Here:  
- self = left object ( a )  
- other = right object ( b )

### Simple Comparison

| Concept | Meaning |
|---|---|
|  | Current object reference |

```text
self
```

| this (C++) | Current object pointer |
|---|---|
| Operator overloading | Redefining operators for objects |

### Very Simple Analogy

Imagine a robot:  
- self / this = the robot saying “me”  
- operator overloading = changing how the robot interprets commands  
Example:

```text
nginx
robot1 + robot2
```

Normally + means addition,  
but with operator overloading, it could mean:

```text
nginx
combine robots
```

### Final Short Answer

- self in Python works like this in C++.  
- But self is not operator overloading.  
- Operator overloading is about changing operators like + or == .  
- self is just a reference to the current object.  
- give 3–4 exam-style short definitions  
- or create a quick comparison cheat sheet for AI lab exams.

## Why the percept() Function Returns Its Input

In this simple code it looks like the percept() function is just returning the same values. But the reason it exists is because of the agent–environment model in AI.

### The line in question

```text
python
pos, foods = env.percept(self.pos, self.foods)
```

And the percept function:

```python
python
def percept(self, pos, foods):
return (pos, foods)
```

currently it returns the same data.  
But this is done on purpose, to follow the agent concept from the lab manual.

### Why do we use percept() at all?

In AI, an agent should:  
1. Sense the environment → percept  
2. Decide an action → based on percept  
3. Act on the environment  
So the correct structure is:

```text
mathematica
Environment → percept → Agent → action → Environment
```

Even if the percept is simple, we still keep the structure.

### What the percept represents here

In Task 3, the robot’s sensors detect:  
- Its current position  
- Remaining food pickups  
So percept should contain:

```text
python
(pos, foods)
```

That’s exactly what the function returns.

### Why not just use self.pos and self.foods directly?

You technically could:

```text
python
pos = self.pos
foods = self.foods
```

And remove percept() completely.  
But that would:  
Break the agent model from the lab manual  
Not follow the structure your instructor expects  
Not match the sample code style  
Your manual clearly defines:

```text
python
percept(self, agent)
```

So we must keep a percept function.

### What percept would do in a real system

In a real robot, percept() would:  
- Read sensors  
- Detect obstacles  
- Detect food  
- Update environment data  
Example:

```python
python
def percept(self, pos, foods):
# check sensors
if obstacle_detected():
return ("blocked", foods)
return (pos, foods)
```

So percept is not supposed to be trivial.  
It is just simple here because the lab task is simple.

#### Code

```text
python
pos, foods = env.percept(self.pos, self.foods)
```

#### Step-by-step

1. Robot calls environment:

```text
lua
env.percept(self.pos, self.foods)
```

2. Environment receives:

```text
ini
pos = (0,0)
foods = [(0,4), (2,1), ...]
```

3. Environment returns:

```text
scss
((0,0), [(0,4), (2,1), ...])
```

4. Python unpacks the tuple:

```text
ini
pos = (0,0)
foods = [(0,4), (2,1), ...]
```

### Simple summary

Why we use percept():

| Reason | Explanation |
|---|---|
| AI structure | Agent must act based on percept |
| Manual requirement | Lab manual defines percept function |
| Future flexibility | Real sensors would be used here |
| Code consistency | Matches sample codes given |

### Very short exam-style answer

Q: Why do we use percept() even if it returns the same values?  
Answer:  
Because in the agent model, the agent must make decisions based on percepts received from the environment. The percept function represents the agent’s sensors and maintains the standard agent–environment interaction structure, even if the percept is simple.  
- give a short viva-style answer  
- or rewrite Task 3 without percept (for comparison only).

## Task 1 Step by Step

Below is a full step-by-step explanation of Task 1 (Simple Reflex Warehouse Robot), with:  
- what each keyword means ( class , def , if , return , for , etc.)  
- what each line does  
- what each argument/parameter does  
- why we use each syntax

### Task 1 Code (Reference)

```python
python
class WarehouseEnv:
def __init__(self, grid):
self.grid = grid
def percept(self, pos):
r, c = pos
return (r, c)
def is_free(self, r, c):
if r < 0 or r > 4 or c < 0 or c > 4:
return False
if self.grid[r][c] == 1:
return False
return True
class SimpleReflexRobot:
def __init__(self, start, goal):
self.pos = start
self.goal = goal
self.moves = []
def choose_action(self, env):
r, c = env.percept(self.pos)
gr, gc = self.goal
if gr > r and env.is_free(r+1, c): return "DOWN"
if gr < r and env.is_free(r-1, c): return "UP"
if gc > c and env.is_free(r, c+1): return "RIGHT"
if gc < c and env.is_free(r, c-1): return "LEFT"
if env.is_free(r, c+1): return "RIGHT"
if env.is_free(r+1, c): return "DOWN"
if env.is_free(r, c-1): return "LEFT"
if env.is_free(r-1, c): return "UP"
return "STOP"
def move(self, action):
r, c = self.pos
if action == "UP": self.pos = (r-1, c)
elif action == "DOWN": self.pos = (r+1, c)
elif action == "LEFT": self.pos = (r, c-1)
elif action == "RIGHT": self.pos = (r, c+1)
grid = [
['S', 0, 1, 0, 0],
[0,   0, 1, 0, 1],
[1,   0, 0, 0, 0],
[0,   1, 1, 0, 0],
[0,   0, 0, 1, 'G']
]
env = WarehouseEnv(grid)
robot = SimpleReflexRobot((0,0), (4,4))
for i in range(50):
if robot.pos == robot.goal:
print("Goal reached!")
break
act = robot.choose_action(env)
if act == "STOP":
print("Destination unreachable!")
break
robot.move(act)
robot.moves.append(act)
print("Moves:", robot.moves)
print("Final:", robot.pos)
```

### Big Picture: What Task 1 is doing

- The warehouse is a grid  
- Robot starts at S  
- Robot wants to reach G  
- Robot can move: UP, DOWN, LEFT, RIGHT  
- Robot only uses current percept (its current location + immediate obstacle checks) Robot has no memory (it doesn’t remember old paths)

### Explanation of Each Keyword (Before lines)

```text
class
```

Used to make a blueprint (like a template) for objects.

```text
def
```

Defines a function (method) inside a class.

```text
__init__
```

Constructor. Runs automatically when we create an object.

```text
self
```

Refers to the current object (like this in C++).

```text
if / elif
```

Decision-making (condition–action rules).

```text
return
```

Sends back a value from a function.

```text
for
```

Loop repeats code multiple times.

```text
break
```

Stops the loop immediately.

```text
and
```

Combines two conditions; both must be true.

### Part A: Environment Class

#### Line

```text
python
class WarehouseEnv:
```

Creates an environment class named WarehouseEnv .  
Why?  
Because AI agent approach uses:  
- Environment (world)  
- Agent (robot)

#### Line

```python
python
def __init__(self, grid):
```

Constructor of environment.  
Arguments:  
- self → the current environment object  
- grid → the warehouse grid passed when creating env

#### Line

```text
python
self.grid = grid
```

Stores the grid inside the environment object so it can be used later.

#### Line

```python
python
def percept(self, pos):
```

Percept function: what the robot “sees”.  
Arguments:  
- pos = robot’s current position (r, c)  
Why do we use percept?  
Because manual says agent uses percept from environment.

#### Line

```text
python
r, c = pos
```

Tuple unpacking.  
If pos = (2,3) then:

```text
r = 2
c = 3
```

#### Line

```text
python
return (r, c)
```

Returns current location as percept.

#### Line

```python
python
def is_free(self, r, c):
```

A helper method to check if a cell is free.  
Arguments:  
- r row  
- c column

#### Line

```text
python
if r < 0 or r > 4 or c < 0 or c > 4:
return False
```

Checks boundary (grid is 5×5 so indexes are 0 to 4).  
- If outside the grid → not allowed → return False  
Keywords:  
- or means if ANY part is true, condition becomes true.

#### Line

```text
python
if self.grid[r][c] == 1:
return False
```

If the cell contains obstacle 1 → blocked.

#### Line

```text
python
return True
```

If not outside and not obstacle → cell is free.

#### Line

```text
python
class SimpleReflexRobot:
```

Creates robot class.  
Simple reflex means:  
decisions based only on current percept.

#### Line

```python
python
def __init__(self, start, goal):
```

Robot constructor.  
Arguments:  
- start → starting position  
- goal → destination position

#### Line

```text
python
self.pos = start
```

Stores robot position.

#### Line

```text
python
self.goal = goal
```

Stores goal position.

#### Line

```text
python
self.moves = []
```

Stores list of actions taken.  
Example:

```text
["RIGHT", "RIGHT", "DOWN"]
```

#### Line

```python
python
def choose_action(self, env):
```

Robot decides next action.  
Argument:  
- env → environment object (to use percept and obstacle check)

#### Line

```text
python
r, c = env.percept(self.pos)
```

Robot gets its current position from environment.  
- env.percept(...) returns location  
- we unpack into r,c

#### Line

```text
python
gr, gc = self.goal
```

Goal row and goal column.  
If goal is (4,4) :

```text
gr = 4
gc = 4
```

#### Movement rules toward goal

```text
python
if gr > r and env.is_free(r+1, c): return "DOWN"
```

Meaning:  
- if goal is below ( gr > r )  
- AND cell down is free  
- move DOWN  
Keyword:  
- and means both conditions must be true.  
Similar lines:

```text
python
if gr < r and env.is_free(r-1, c): return "UP"
if gc > c and env.is_free(r, c+1): return "RIGHT"
if gc < c and env.is_free(r, c-1): return "LEFT"
```

These are condition–action rules:  
- condition = where goal is  
- action = which direction to move

#### Backup (if direct goal path blocked)

```text
python
if env.is_free(r, c+1): return "RIGHT"
if env.is_free(r+1, c): return "DOWN"
if env.is_free(r, c-1): return "LEFT"
if env.is_free(r-1, c): return "UP"
```

If the preferred direction is blocked, robot tries any open direction.

#### Line

```text
python
return "STOP"
```

If no direction is possible → robot stuck.

#### Line

```python
python
def move(self, action):
```

Moves the robot based on action string.  
Argument:  
- action is "UP", "DOWN", etc.

#### Line

```text
python
r, c = self.pos
```

Get current location.

#### Update position based on action

Example:

```text
python
if action == "UP": self.pos = (r-1, c)
```

Why r-1 ?  
Because moving up decreases row number.  
Same for others.

#### Grid definition

```text
python
grid = [...]
```

Creates 2D grid map.

#### Create environment

```text
python
env = WarehouseEnv(grid)
```

#### Create robot

```text
python
robot = SimpleReflexRobot((0,0), (4,4))
```

Start and goal (we used fixed positions).

#### Loop

```python
python
for i in range(50):
```

Try up to 50 steps.  
Why?  
To avoid infinite loop if robot keeps moving.

#### Goal check

```python
python
if robot.pos == robot.goal:
print("Goal reached!")
break
```

#### Decide action

```text
python
act = robot.choose_action(env)
```

#### If stuck

```python
python
if act == "STOP":
print("Destination unreachable!")
break
```

#### Move robot and save move

```text
python
robot.move(act)
robot.moves.append(act)
```

#### Print output

```python
python
print("Moves:", robot.moves)
print("Final:", robot.pos)
```

### Why this is a Simple Reflex Agent?

Because robot is using:  
- current percept (current position)  
- immediate obstacle check  
- condition–action rules  
And it does not store path history or do planning.  
- show a real step-by-step movement simulation on this grid (like Step 1, Step 2, Step 3…)  
- or modify the code so it automatically finds S and G in the grid (still beginner style).

## Task 2 Step by Step

Below is Task 2 explained in full detail (Model-Based Inspection Robot).  
- each keyword ( class , def , if , for , return , elif , break , and )  
- each line  
- each argument/parameter  
- why we use each syntax  
- how the robot “remembers” inspected cells (internal model)

### Task 2 Code (Reference)

```python
python
class InspectionEnv:
def __init__(self, grid):
self.grid = grid
def safe(self, r, c):
if r < 0 or r > 4 or c < 0 or c > 4:
return False
if self.grid[r][c] == "#" or self.grid[r][c] == "X":
return False
return True
def percept(self, pos):
return pos
class ModelRobot:
def __init__(self, start):
self.pos = start
self.inspected = [
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False]
]
self.actions = []
def choose_action(self, env):
r, c = env.percept(self.pos)
if self.inspected[r][c] == False:
return "INSPECT"
if env.safe(r-1, c) and self.inspected[r-1][c] == False: return "UP"
if env.safe(r, c+1) and self.inspected[r][c+1] == False: return "RIGHT"
if env.safe(r+1, c) and self.inspected[r+1][c] == False: return "DOWN"
if env.safe(r, c-1) and self.inspected[r][c-1] == False: return "LEFT"
return "STOP"
def action(self, act):
r, c = self.pos
if act == "INSPECT":
self.inspected[r][c] = True
self.actions.append("INSPECT " + str(self.pos))
elif act == "UP":
self.pos = (r-1, c); self.actions.append("UP")
elif act == "DOWN":
self.pos = (r+1, c); self.actions.append("DOWN")
elif act == "LEFT":
self.pos = (r, c-1); self.actions.append("LEFT")
elif act == "RIGHT":
self.pos = (r, c+1); self.actions.append("RIGHT")
grid = [
[0,  0,  "#", 0,  0],
[0,  "X", "#", 0,  0],
[0,  0,  0,  0,  "#"],
["#", 0,  "#", 0,  0],
[0,  0,  0,  "X", 0]
]
env = InspectionEnv(grid)
robot = ModelRobot((0,0))
for i in range(100):
act = robot.choose_action(env)
if act == "STOP":
break
robot.action(act)
print("Actions:", robot.actions)
print("Stopped:", robot.pos)
```

#### Environment (warehouse grid)

- 0 = safe cell  
- # = obstacle (blocked)  
- X = damaged (blocked)  
- Robot must avoid # and X .

#### Robot goal

Inspect all reachable safe cells without revisiting any cell.

#### Model-based means

Robot keeps an internal memory:  
- which cells are already inspected ( True/False )  
This is called the robot’s internal model.

### Keywords Used and Why

| Keyword | Meaning | Why used |
|---|---|---|
|  | blueprint | to create Environment and Robot objects |

```text
class
```

|  | define function | to make methods like safe() , |
|---|---|---|

```text
def
choose_action()
```

|  | constructor | runs when object is created |
|---|---|---|

```text
__init__
```

|  | current object | store data inside the object |
|---|---|---|

```text
self
```

|  | condition | decision making |
|---|---|---|

```text
if
```

|  | else-if | multiple choices |
|---|---|---|

```text
elif
```

|  | send value back | function output like "UP" or True/False |
|---|---|---|

```text
return
```

|  | loop | run steps repeatedly |
|---|---|---|

```text
for
```

|  | stop loop | when robot can’t move |
|---|---|---|

```text
break
```

|  | both conditions must be true | safe cell AND not inspected |
|---|---|---|

```text
and
```

|  | any one condition true | obstacle # OR damaged X |
|---|---|---|

```text
or
```

### PART A: Environment Class

#### 1)

```text
python
class InspectionEnv:
```

Creates a class named InspectionEnv (warehouse environment).  
Why?  
Because agent model uses:  
- environment gives percept  
- agent decides action

#### 2)

```python
python
def __init__(self, grid):
self.grid = grid
```

- __init__ runs automatically when we do:

```text
python
env = InspectionEnv(grid)
```

- self.grid = grid stores the grid inside environment.  
So environment remembers the map.

#### 3)

```python
python
def safe(self, r, c):
```

This function checks: “Can robot go to cell (r,c)?”  
Arguments:  
- r = row  
- c = column

#### 4) Boundary check

```text
python
if r < 0 or r > 4 or c < 0 or c > 4:
return False
```

Why?  
Grid size is 5×5. Valid index is 0 to 4.  
If outside, robot cannot move there.  
- or used because if ANY condition is true → outside.

#### 5) Obstacle / damaged check

```text
python
if self.grid[r][c] == "#" or self.grid[r][c] == "X":
return False
```

If cell is obstacle # OR damaged X , it is blocked.

#### 6)

```text
python
return True
```

If it is inside grid and not blocked, then safe.

#### 7) Percept function

```python
python
def percept(self, pos):
return pos
```

Percept means what robot senses.  
Here robot senses only its current position.  
We keep this because lab manual expects a percept() function.

#### 8)

```text
python
class ModelRobot:
```

This is robot agent.

#### 9) Constructor

```python
python
def __init__(self, start):
```

Argument:  
- start = starting position (row,col)  
Example: (0,0)

#### 10)

```text
python
self.pos = start
```

Robot current position stored.

#### 11) Internal Model (inspection memory)

```text
python
self.inspected = [
[False, False, False, False, False],
...
]
```

This is robot’s internal model.  
- False means “not inspected yet”  
- True means “already inspected”  
Why do we need it?  
Because task says:  
do not revisit any inspected cell  
So robot must remember.

#### 12)

```text
python
self.actions = []
```

Stores robot actions list (history), for output.

#### 13)

```python
python
def choose_action(self, env):
```

Robot chooses next action.  
Argument:  
- env = environment object  
- Robot needs environment to check safe moves.

#### 14)

```text
python
r, c = env.percept(self.pos)
```

Robot gets percept from environment.  
- self.pos is current robot position  
- percept returns it back  
- unpack into r and c

#### 15) Inspect rule

```text
python
if self.inspected[r][c] == False:
return "INSPECT"
```

If current cell is not inspected:  
inspect it first  
This is correct because robot’s job is to inspect.

#### 16) Move rules to uninspected neighbor

Example:

```text
python
if env.safe(r-1, c) and self.inspected[r-1][c] == False: return "UP"
```

This means:  
- if the cell UP is safe  
- AND it is not inspected  
- then move UP.  
This is model-based because it uses memory:

```text
self.inspected[...]
```

Same for RIGHT, DOWN, LEFT.  
Order matters:  
Robot tries UP first, then RIGHT, then DOWN, then LEFT.

#### 17)

```text
python
return "STOP"
```

If all neighbors are either:  
- blocked OR  
- already inspected OR  
- outside grid  
Then no move possible → stop.

#### 18)

```python
python
def action(self, act):
```

Robot performs action.  
Argument:  
- act is string: "UP" , "DOWN" , "INSPECT" ...

#### 19)

```text
python
r, c = self.pos
```

Get current robot position.

#### 20) If INSPECT

```text
python
if act == "INSPECT":
self.inspected[r][c] = True
self.actions.append("INSPECT " + str(self.pos))
```

- Mark the cell inspected: now memory becomes True.  
- Save action in list.  
Why str(self.pos) ?  
Because self.pos is a tuple, we convert it to string for printing.

#### 21) Moving actions

Example:

```text
python
elif act == "UP":
self.pos = (r-1, c); self.actions.append("UP")
```

Move UP by decreasing row.  
Other moves update the tuple similarly.

#### 22) Grid creation

```text
python
grid = [...]
```

Defines warehouse with obstacles and damaged cells.

#### 23) Create objects

```text
python
env = InspectionEnv(grid)
robot = ModelRobot((0,0))
```

#### 24) Loop for steps

```python
python
for i in range(100):
```

Run up to 100 steps to prevent infinite loop.

#### 25)

```text
python
act = robot.choose_action(env)
```

Robot decides next action.

#### 26)

```text
python
if act == "STOP":
break
```

If robot cannot move, stop loop.

#### 27)

```text
python
robot.action(act)
```

Robot performs the action (inspect or move).

#### 28) Output

```python
python
print("Actions:", robot.actions)
print("Stopped:", robot.pos)
```

Show full action history and final position.

### Why Task 2 is Model-Based?

Because robot uses internal model:

```text
python
self.inspected
```

It stores memory of inspected cells and uses that memory while deciding next move.  
That’s exactly what “model-based reflex agent” means.  
- show a dry-run: step 1, step 2, step 3 on your grid  
- or modify it to print: Current cell: (r,c), Action: INSPECT each step (still beginner).

## Class robot_model: def __init__(self, start): self.pos = start self.inspect_var =
## Why the Actions Print Twice

Because you’re adding actions twice.

#### Where the duplication happens

1. Inside robot_model.action() you already append when act == "INSPECT" :

```text
python
if act == "INSPECT":
self.inspect_var[i][j] = True
self.actions_list.append("INSPECT " + str(self.pos))
```

2. Then again in the main loop you append for every action:

```text
python
if act == "INSPECT":
robot.actions_list.append("INSPECT " + str(robot.pos))
else:
robot.actions_list.append(act)
```

So INSPECT becomes double (and for moves you may also be logging twice depending on where you append).

### Option A (best): Keep logging ONLY in the loop

Remove all append() from action() .

#### Change your action() like this

```python
python
def action(self, act):
i, j = self.pos
if act == "INSPECT":
self.inspect_var[i][j] = True
elif act == "UP":
self.pos = (i-1, j)
elif act == "DOWN":
self.pos = (i+1, j)
elif act == "LEFT":
self.pos = (i, j-1)
elif act == "RIGHT":
self.pos = (i, j+1)
```

And keep your loop logging:

```python
python
for k in range(100):
act = robot.choose_action(env)
if act == "STOP":
break
robot.action(act)
if act == "INSPECT":
robot.actions_list.append("INSPECT " + str(robot.pos))
else:
robot.actions_list.append(act)
```

Now it will not duplicate.

### Option B: Keep logging ONLY inside action()

If you prefer logging inside the robot, then delete the extra append part from the loop:

```python
python
for k in range(100):
act = robot.choose_action(env)
if act == "STOP":
break
robot.action(act)
print(robot.actions_list)
```

But for this option you must also add logging for moves inside action() (otherwise only INSPECT will appear).

### Extra small note (your current code has another tiny issue)

Right now you log INSPECT twice inside loop and inside action() .  
That’s exactly why duplicates happen.  
duplication and simple output like:

```text
MOVE RIGHT
INSPECT (2,3)
```

## Fixed Version Using the Same Variables

here’s your same code, same variable names, but fixed so actions don’t print duplicate.  
What I changed (only 2 things):  
1. I removed the append() from inside robot_model.action()  
2. I kept only one logging place (the main loop)

```python
python
class inspection_environment:
def __init__(self, grid):
self.grid = grid
def is_cell_free(self, r, c):
if r < 0 or r > 4 or c < 0 or c > 4:
return False
if self.grid[r][c] == "#" or self.grid[r][c] == "X":
return False
return True
def percept(self, pos):
return pos
class robot_model:
def __init__(self, start):
self.pos = start
self.inspect_var = [
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False],
[False, False, False, False, False]
]
self.actions_list = []
def choose_action(self, env):
i, j = env.percept(self.pos)
if self.inspect_var[i][j] == False:
return "INSPECT"
if env.is_cell_free(i-1, j) and self.inspect_var[i-1][j] == False:
return "UP"
if env.is_cell_free(i, j+1) and self.inspect_var[i][j+1] == False:
return "RIGHT"
if env.is_cell_free(i+1, j) and self.inspect_var[i+1][j] == False:
return "DOWN"
if env.is_cell_free(i, j-1) and self.inspect_var[i][j-1] == False:
return "LEFT"
return "STOP"
def action(self, act):
i, j = self.pos
if act == "INSPECT":
self.inspect_var[i][j] = True
elif act == "UP":
self.pos = (i-1, j)
elif act == "DOWN":
self.pos = (i+1, j)
elif act == "LEFT":
self.pos = (i, j-1)
elif act == "RIGHT":
self.pos = (i, j+1)
grid = [
[0,  0,  "#", 0,  0],
[0,  "X", "#", 0,  0],
[0,  0,  0,  0,  "#"],
["#", 0,  "#", 0,  0],
[0,  0,  0,  "X", 0]
]
env = inspection_environment(grid)
robot = robot_model((0,0))
for i in range(100):
act = robot.choose_action(env)
if act == "STOP":
break
robot.action(act)
# logging only here (so no duplicates)
if act == "INSPECT":
robot.actions_list.append("INSPECT " + str(robot.pos))
else:
robot.actions_list.append(act)
print("All Actions:", robot.actions_list)
print("Stopped At:", robot.pos)
```

```text
MOVE RIGHT to (0,1)
INSPECT at (0,1)
```

- (using your same variables, still beginner style).
