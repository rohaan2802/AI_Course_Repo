# AI Agents and Rationality

## Agents and Rationality: Exam Explanation

Absolutely, Hamiz!

### 1. What is an Agent?

- An agent is anything that perceives its environment and acts to achieve goals. Examples: humans, robots, software bots, thermostats.  
- How it works:  
  - Sensors → perceive the environment (e.g., camera, microphone, temperature sensor)  
  - Actuators → take actions (e.g., wheels, arms, display screen, heating)  
- Think of it as: Eyes + Brain + Hands  
Key terms:  
- Percept = what the agent senses at a moment (e.g., [A, Dirty] for vacuum)  
- Action = what the agent does (e.g., Suck, Move Left, Move Right)

### 2. Agent Function vs Agent Program

- Agent function: theoretical mapping from percept histories → actions  
  - f: P* → A  
- Agent program: actual code that runs on physical architecture to produce the agent function.  
- Example: Reflex Vacuum Agent code is the program, the idea “if dirty → suck, else move” is the function.

### 3. Vacuum Cleaner Example

- Environment: 2 locations A and B, each can be clean or dirty  
- Percepts: [location, status]  
- Actions: Left, Right, Suck, NoOp  
Simple Reflex Agent Code (in plain English):

```text
If the square is dirty → Suck
Else if at A → Move Right
```

|  | Plain text |
|---|---|

```text
Else if at B → Move Left
```

- Works in fully observable environments  
- Problem: fails if sensors fail or environment is partially observable

### 4. Rationality

- A rational agent chooses actions that maximize expected performance based on percept history.  
- Performance measures evaluate success:  
  - Example: 1 point per clean square, -1 point per move  
- Rationality is not omniscience – agent may not know everything or outcomes may be uncertain.  
- Rational agents can explore, learn, and act autonomously.

### 5. PEAS Framework

To design any agent, define PEAS:

| Component | Example: Automated Taxi |
|---|---|
| Performance measure | Safety, comfort, legality, speed |
| Environment | Streets, traffic, weather |
| Actuators | Steering, brakes, horn, display |
| Sensors | Camera, GPS, speedometer, accelerometer |

- Same idea for internet shopping agents:  
  - Performance: price, quality, efficiency  
  - Environment: web pages, vendors, shippers  
  - Actuators: follow URL, fill forms, display info  
  - Sensors: HTML pages, images, scripts

### 6. Environment Types

Environments are categorized along dimensions:

| Feature | Example: Vacuum | Taxi | Internet Shopping |
|---|---|---|---|
| Observable | Yes | No | No |
| Deterministic | Yes | No | Partly |
| Episodic | No | No | No |
| Static | Yes | No | Semi |
| Discrete | Yes | No | Yes |
| Single-agent | Yes | No | Yes (except auctions) |

- Real world = partially observable, stochastic, sequential, dynamic, continuous, multi-agent

### 7. Types of Agents

1. Simple reflex agents:  
  - Respond to current percept only (condition-action rules)  
  - Works only in fully observable environments  
  - Example: simple vacuum agent  
2. Reflex agents with state:  
  - Remember some past information to handle partially observable environments Example: vacuum keeps track of last clean location  
3. Goal-based agents:  
  - Have goals, choose actions to achieve them  
  - Example: "Clean both rooms" → plans moves  
4. Utility-based agents:  
  - Have utility function → choose actions that maximize happiness/value  
  - Example: prefers faster cleaning over energy saving  
- All agent types can be turned into learning agents for adapting to new situations.

### 8. Summary

- Agents sense and act through sensors and actuators.  
- Rational agents maximize expected performance.  
- PEAS describes tasks.  
- Environment type affects agent design.  
- Agents can be reflex, reflex with state, goal-based, utility-based.

#### Memory Tip for Exam

- Agents → PEAS → Types → Environment  
- Simple story: Vacuum agent sees dirt → Sucks (reflex) → remembers last clean room (state) → plans to clean both rooms (goal) → chooses best efficiency vs speed (utility) you recall everything in 5 minutes before exam. It’ll have agents, types, PEAS, and environment table.
