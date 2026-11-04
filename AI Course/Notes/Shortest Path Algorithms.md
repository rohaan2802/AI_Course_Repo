# Shortest Path Algorithms

## Shortest-Path Algorithms Summary and Negative Cycles

Below is a clear, exam-oriented explanation of shortest path algorithms, focusing on their core idea, how they work, negative weight cycle detection, reaction, and why.  
(I’m keeping it simple and structured—good for FAST / DS&A exams.)

### 1. What is a Shortest Path Algorithm?

A shortest path algorithm finds the minimum-cost path from:  
- a source node → all other nodes  
- or  
- a source → destination  
Cost = sum of edge weights (distance, time, cost, etc.).

### 2. Main Shortest Path Algorithms (Overview)

| Algorithm | Main Idea | Negative Weights | Detects Negative Cycle | Use Case |
|---|---|---|---|---|
| BFS | Level-by-level | Unweighted graph |  |  |
| Dijkstra | Greedy | Fast, positive weights |  |  |
| Bellman–Ford | Relax edges repeatedly | Negative edges |  |  |
| Floyd–Warshall | DP on all pairs | Small graphs |  |  |
| Johnson’s | Reweight + Dijkstra | Sparse graphs |  |  |

### A. BFS (Breadth First Search)

#### Idea

- All edges have equal weight (1)

#### How it works

- Visit nodes level by level  
- First time you reach a node → shortest path

#### Negative cycle?

Not applicable

#### Why?

Because there are no weights, only edge count.

#### Idea

- Greedy choice: always pick the node with smallest known distance

#### How it works

1. Set source distance = 0  
2. Pick unvisited node with smallest distance  
3. Relax its edges  
4. Mark node as final  
5. Repeat

#### Negative weights?

Not allowed

#### Why it fails with negative edges?

Because once a node is marked final, Dijkstra never rechecks it.  
Negative edge later could reduce the distance → algorithm becomes incorrect.

#### Negative cycle detection?

Cannot detect

#### Idea

- Repeatedly relax all edges

#### Key Principle

- In a graph with V vertices, the shortest path has at most V−1 edges

#### How it works

1. Initialize distances  
2. Repeat V−1 times:  
  - Relax every edge  
3. Do one extra iteration:  
  - If any distance still decreases → negative cycle exists

#### Negative Weight Cycle Detection

YES

#### How Bellman–Ford detects it

- If after V−1 relaxations, a distance can still be reduced  
- → implies infinite reduction → negative cycle

#### Reaction

- Algorithm stops  
- Reports: “Negative weight cycle detected”  
- Shortest path does NOT exist

#### Why shortest path doesn’t exist?

Because:

```text
pgsql
```

Loop around negative cycle → distance keeps decreasing forever

#### Idea

- Dynamic Programming on all pairs

#### DP Relation

```text
lua
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

#### How it works

- Tries every node as an intermediate  
- Complexity: O(V³)

#### Negative weights?

Allowed

#### Negative cycle detection?

YES

#### How it detects

- After completion:

```text
css
```

If dist[i][i] < 0 → negative cycle

#### Why?

Distance from a node to itself should be 0.  
Negative value means a cycle with negative total weight.

#### Idea

- Handle negative weights using reweighting

#### Steps

1. Run Bellman–Ford to detect negative cycles  
2. Reweight edges to make all weights positive  
3. Run Dijkstra from every node

#### Negative cycle detection?

YES (via Bellman–Ford)

#### Why use it?

- Faster than Floyd–Warshall for large sparse graphs

#### What is it?

A cycle where:

```text
mathematica
Total weight < 0
```

#### Why is it a problem?

- You can keep looping  
- Distance keeps decreasing  
- No shortest path exists

### 5. Who Detects Negative Cycles?

| Algorithm | Detects? | How |
|---|---|---|
| BFS | No weights |  |
| Dijkstra | Greedy finalization |  |
| Bellman–Ford | Extra relaxation |  |
| Floyd–Warshall | dist[i][i] < 0 |  |
| Johnson | Uses Bellman–Ford |  |

### 6. One-Line Exam Summary

- BFS → Unweighted graphs  
- Dijkstra → Fast, positive weights only  
- Bellman–Ford → Handles negatives, detects cycles  
- Floyd–Warshall → All pairs, DP, small graphs  
- Negative cycle → No shortest path exists  
Explain with diagrams  
Provide exam-ready short answers  
Give C++ / pseudo-code  
Compare time complexities in detail

## Edge Relaxation and Floyd–Warshall

— these two ideas are core concepts in shortest-path algorithms.

#### Short definition (exam-ready)

- Relaxing an edge means checking whether going through that edge gives a shorter path, and updating the distance if it does.

### Simple idea

Suppose you know:  
- Current shortest distance to u  
- There is an edge u → v with weight w  
You ask:  
- “If I go from source → u → v, is this cheaper than what I already know for v?”

### Mathematical form

If:

```text
css
dist[u] + w < dist[v]
```

then:

```text
dist[v] = dist[u] + w
```

This update is called edge relaxation.

```text
py d
```

### Why is it called “relaxation”?

Initially, distances are very tight/strict (∞).  
By checking edges, we relax (loosen) these values until they reach the true minimum.

### Small example

Graph:

```text
css
A --5--> B
```

Initial:

```text
dist[A] = 0
dist[B] = ∞
```

Relax edge A→B:

0 + 5 < ∞

```text
dist[B] = 5
```

Edge relaxed successfully

### Where is edge relaxation used?

| Algorithm | Uses Relaxation |
|---|---|
| Dijkstra | Yes (greedy order) |
| Bellman–Ford | Yes (all edges repeatedly) |
| Floyd–Warshall | Yes (via DP) |

### 2. How Floyd–Warshall Algorithm Works What problem does it solve?

- Finds shortest paths between ALL pairs of vertices

### Core Idea (Very Important)

- Try every vertex as an intermediate point between every pair.  
Meaning:  
- “Is going from i → k → j shorter than going directly i → j?”

### Dynamic Programming Relation

This is the heart of the algorithm:

```text
lua
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

#### Interpretation

- Current best path: dist[i][j]  
- New possible path via k : dist[i][k] + dist[k][j]  
- Pick the smaller one  
This is relaxation in DP form

#### Step 1: Initialization

Create a distance matrix:

| From\To | A | B | C |
|---|---|---|---|
| A | 0 | 3 | ∞ |
| From\To | A | B | C |
| B | ∞ | 0 | 2 |
| C | 1 | ∞ | 0 |

- 0 for same node  
- Edge weight if edge exists  
- ∞ if no direct edge

#### Step 2: Choose intermediate vertex k

We loop:

```text
java
for k = 1 to V
for i = 1 to V
for j = 1 to V
```

#### Step 3: Relax paths using k

Check:

```text
css
Is dist[i][k] + dist[k][j] < dist[i][j]?
```

If yes → update.

### Example (easy)

Suppose:

```text
mathematica
```

A → C = 10  
A → B = 3  
B → C = 2  
When k = B:

```text
lua
dist[A][C] = min(10, 3 + 2) = 5
```

Shorter path found via B

#### Key rule

- After algorithm ends:

```text
css
```

If dist[i][i] < 0 → Negative cycle exists

#### Why?

- Distance from a node to itself should be 0  
- Negative value means:

```text
css
```

i → ... → i  (total weight < 0)  
→ Negative cycle

#### Reaction

- Shortest paths are invalid  
- Algorithm reports negative cycle

### 4. Relaxation vs Floyd–Warshall (Connection)

| Concept | Edge Relaxation |
|---|---|
| Dijkstra | Relax one edge at a time |
| Bellman–Ford | Relax all edges repeatedly |
| Floyd–Warshall | Relax all pairs using DP |

### 5. One-Line Exam Answers

- Edge Relaxation: Updating distance if a shorter path is found  
- Floyd–Warshall: DP algorithm that checks all pairs using all vertices as intermediates Time Complexity: O(V³)  
- Negative Cycle Detection: dist[i][i] < 0  
Dry run with table  
Pseudocode  
Comparison with Bellman-Ford  
Visual explanation

## All Shortest-Path Algorithms

Below is a comprehensive, structured list of shortest-path algorithms (practically all major ones you’ll ever encounter), grouped by idea, graph type, and use case. This is the closest realistic answer to “all shortest path algorithms that exist.”

### 1. By Problem Type A. Single-Source Shortest Path (SSSP)

(from one source → all nodes)  
- BFS – unweighted graphs  
- 0–1 BFS – weights ∈ {0,1}  
- Dijkstra  
- Bellman–Ford  
- SPFA (Shortest Path Faster Algorithm)  
- Dial’s Algorithm  
- Δ-Stepping  
- Goldberg–Radzik  
- Thorup’s Algorithm (integer weights, theoretical)  
- A* (goal-directed SSSP)  
- Lagrangian Relaxation based methods

### B. Single-Pair Shortest Path

(from source → specific destination)  
- A*  
- Bidirectional Dijkstra  
- Bidirectional BFS  
- ALT (A* + Landmarks + Triangle inequality)  
- Reach-based routing  
- Contraction Hierarchies (used in Google Maps)

### C. All-Pairs Shortest Path (APSP)

(every node → every node)  
- Floyd–Warshall  
- Johnson’s Algorithm  
- Repeated Dijkstra  
- Repeated Bellman–Ford  
- Seidel’s Algorithm (unweighted, randomized)  
- Tropical Matrix Multiplication based methods

### 2. By Graph Weights A. Unweighted Graphs

- BFS  
- Bidirectional BFS  
- Seidel’s Algorithm

### B. Non-negative Weights

- Dijkstra  
- Dial’s Algorithm  
- Δ-Stepping  
- Bidirectional Dijkstra  
- Contraction Hierarchies

### C. Negative Weights (No negative cycle)

- Bellman–Ford  
- Floyd–Warshall  
- Johnson’s Algorithm  
- Goldberg–Radzik

### D. Negative Weight Cycle Detection

(very important conceptually)  
- Bellman–Ford → extra relaxation  
- Floyd–Warshall → dist[i][i] < 0  
- Johnson’s → uses Bellman–Ford  
- Karp’s Algorithm (minimum mean cycle)

### 3. By Core IDEA (This is exam gold) 1 Greedy

- Dijkstra  
- Bidirectional Dijkstra  
Idea:  
- Finalize the nearest node first  
Fails with negative edges

### 2 Relaxation-Based

- Bellman–Ford  
- SPFA  
- Goldberg–Radzik  
Idea:  
- Keep improving distances until no improvement is possible  
Detects negative cycles

### 3 Dynamic Programming

- Floyd–Warshall  
- Seidel’s Algorithm  
Idea:  
- Build solution using smaller subproblems

### 4 Heuristic / Informed Search

- A*  
- ALT  
Idea:  
- Guide search using estimated distance (heuristic)

### 5 Reweighting

- Johnson’s Algorithm  
Idea:  
- Remove negative weights, then apply Dijkstra

### 6 Hierarchical / Preprocessing (Industry)

- Contraction Hierarchies  
- Hub Labeling  
- Transit Node Routing  
Idea:  
- Preprocess graph for ultra-fast queries

### 4. Which Algorithms Detect Negative Weight Cycles?

| Algorithm | Detects? | How |
|---|---|---|
| BFS | No weights |  |
| Dijkstra | Greedy final |  |
| Bellman–Ford | Extra relaxation |  |
| Floyd–Warshall dist[i][i] < 0 |  |  |
| Johnson’s | Uses Bellman–Ford |  |
| Karp’s | Mean cycle |  |

### 5. Real-World Usage

- Google Maps / GPS → A*, Contraction Hierarchies  
- Networking (Routing) → Bellman–Ford (RIP), Dijkstra (OSPF)  
- AI / Games → A*  
- Databases / Theory → Floyd–Warshall  
- Competitive Programming → Dijkstra, Bellman–Ford, 0–1 BFS

### 6. Ultra-Short Exam Summary

- BFS → unweighted  
- Dijkstra → positive weights, greedy  
- Bellman–Ford → negatives + cycle detection  
- Floyd–Warshall → all pairs, DP  
- Johnson’s → APSP with negatives  
- A* → heuristic-based shortest path  
Timeline (historical evolution)  
Which one to use WHEN  
Dry-run examples  
C++ pseudocode for all major ones  
A* (A-star) is one of the most important shortest-path algorithms, especially in AI, games, and maps.

#### Simple definition

- A* finds the shortest path by combining  
- distance already traveled  
- estimated distance to the goal  
So it is Dijkstra + intelligence (heuristic).

### 2. Core Idea (MOST IMPORTANT)

A* chooses the next node based on:

```text
f(n) = g(n) + h(n)
```

Where:  
- g(n) = actual cost from start → n  
- h(n) = estimated cost from n → goal (heuristic)  
- f(n) = estimated total cost of path through n  
Always expand the node with smallest f(n).

#### Heuristic = smart guess

It estimates how far the goal is.  
Examples:  
- Grid map → Manhattan distance  
- 2D map → Euclidean distance

#### Important condition

- h(n) must never overestimate the true distance  
- (then it is called admissible)  
This guarantees optimal shortest path.

#### Data structures

- OPEN list → nodes to be explored (priority queue)  
- CLOSED list → nodes already explored

#### Algorithm Steps

1. Put start node in OPEN  
2. Set g(start) = 0  
3. Compute f(start) = g + h  
4. While OPEN is not empty:  
  - Pick node with lowest f  
  - If it is the goal → STOP  
  - Move node to CLOSED  
  - For each neighbor:  
    - Compute new g  
    - If better path found:  
    - Update g, f  
    - Set parent  
    - Add to OPEN if not present

#### Graph

```text
sql
Start(S) ----2---- A ----2---- Goal(G)
\               |
\----5---------|
```

Heuristic values:

```text
powershell
h(S)=4, h(A)=2, h(G)=0
```

#### Step 1

From S:  
- A: g=2, h=2 → f=4  
- G: g=5, h=0 → f=5  
Choose A (smaller f).

#### Step 2

From A:  
- G: g=4, h=0 → f=4  
Goal reached with cost 4

#### Because

- It explores promising paths first  
- If h(n) ≤ true cost, A* never misses the shortest path

### 7. Relationship with Dijkstra

| Algorithm | Priority |
|---|---|
| Dijkstra g(n) |  |
| A* g(n) + h(n) |  |

#### Special case

If:

```text
powershell
h(n) = 0
```

Then A* becomes Dijkstra.

### 8. Negative Weights?

Not allowed

#### Why?

Heuristic + negative weights breaks correctness.

### 9. Where A* is Used

- Game AI (pathfinding)  
- GPS / Maps  
- Robotics  
- Maze solving  
- Motion planning

### 10. One-Line Exam Answers

- A* → heuristic-based shortest path algorithm  
- f(n) → estimated total cost  
- h(n) → admissible heuristic  
- Optimal when → heuristic never overestimates  
- Special case → h(n)=0 → Dijkstra

### 11. Key Diagram Idea (remember this)

```text
pgsql
Actual cost so far (g)
+
Estimated cost to goal (h)
=
Total estimated cost (f)
```

Dry-run on grid  
Pseudocode  
Heuristic examples  
Compare A* vs Dijkstra vs BFS  
Exam MCQs
