# A_ and Negative Weights

## Can A* Handle Negative Weights? Checking the Estimated Distance

s — these come up a lot in AI search and graph algorithms.

#### No — A* cannot handle negative edge weights or negative cycles

Why?  
A* works using this formula:

```text
f(n) = g(n) + h(n)
```

- g(n) = cost from start → node n  
- h(n) = estimated cost from n → goal (heuristic)  
A* assumes all step costs are non-negative, just like Dijkstra.

#### Problem with negative cycles

If a negative cycle exists:  
- The path cost can keep decreasing infinitely  
- A* may loop forever or keep updating costs  
- “Shortest path” is not well-defined

#### Comparison

| Algorithm | Negative weights | Negative cycles |
|---|---|---|
| Dijkstra | No | No |
| A* | No | No |
| Bellman–Ford | Yes | Detects |
| Algorithm | Negative weights | Negative cycles |
| Floyd–Warshall | Yes | Detects |

If negative weights exist, use Bellman-Ford, not A*.

### 2 How do we know the estimated distance (heuristic) is true or reliable?

This is the most important concept in A*.

#### A heuristic is not required to be true

It must be safe.

#### Admissible Heuristic (MOST IMPORTANT)

A heuristic must never overestimate the real cost:  
h(n) ≤actual shortest cost from n to goal  
If this holds:  
- A* guarantees optimal shortest path  
Example  
- Straight-line distance in maps  
- Manhattan distance in grids  
They underestimate → safe

#### Consistent (Monotonic) Heuristic (Stronger condition)

```text
h(n) ≤c(n, n ) + ′ h(n ) ′
```

Meaning:  
- Estimated cost at n ≤ cost to neighbor + neighbor’s estimate  
If consistent:  
- A* never reopens nodes  
- Faster & simpler implementation

### 3 What if heuristic is wrong?

| Heuristic type | Result |
|---|---|
| Admissible & consistent | Optimal & efficient |
| Admissible only | Optimal (slower) |
| Overestimates | May give wrong path |
| h(n) = 0 | Becomes Dijkstra |
| Very large h(n) | Becomes Greedy Best-First |

### 4 Simple intuition (exam-friendly)

- A* is like Dijkstra + intelligent guessing  
- Negative cycles break the idea of “shortest path”  
- Heuristic must be optimistic, not exact

### 5 One-line exam answers

- Can A* handle negative cycles?  
- No, because shortest path becomes undefined.  
- How do we know heuristic is true?  
- We don’t — it must be admissible (never overestimate).  
- Explain with a diagram  
- Give a numerical example  
- Compare A* vs Dijkstra vs Greedy  
- Help you write exam-perfect answers

## Algorithms That Handle Negative Weight Cycles

Ah! Now we are in graph algorithms territory.

#### Bellman–Ford Algorithm

- Purpose: Finds shortest paths from a single source to all other vertices.  
- Can handle: Graphs with negative edge weights.  
- Limitation: If there’s a negative cycle, it can detect it but cannot give a finite shortest path (because the path cost can go to −∞).

### 2 How Bellman–Ford works

1. Initialize distances:  
dist[source] = 0, dist[others] = ∞  
2. Relax all edges V−1 times (V = number of vertices):  
for each edge u →v with weight w : dist[v] = min(dist[v], dist[u] + w)  
3. Check for negative cycles:  
  - If you can relax any edge again, there is a negative cycle.  
  - Why? Because the shortest path can still decrease → cycle exists.

#### 3 Example

Graph edges:

| Edge | Weight |
|---|---|
| A → B | 4 |
| Edge | Weight |
| B → C | -2 |
| C → A | -3 |

- Step 1: Relax edges V-1 = 3-1 = 2 times  
- Step 2: Distances keep decreasing because of negative cycle  
- Step 3: Detect negative cycle → stop

#### 4 Key points

| Feature | Bellman–Ford |
|---|---|
| Negative weights | Yes |
| Negative cycles | Detects (cannot compute path) |
| Time Complexity | O(V * E) |
| Single source shortest path |  |

#### 5 Other algorithms

- Floyd–Warshall (All-Pairs Shortest Path):  
  - Works with negative weights  
  - Detects negative cycles  
  - Can tell if a path exists from i → j that goes through a negative cycle  
- Dijkstra / A*  
  - Cannot handle negative weights  
  - Cannot detect negative cycles  
Intuition:  
- Negative cycles make the concept of "shortest path" meaningless.  
- Bellman-Ford doesn’t compute an infinite path but tells you, “Hey, a negative cycle exists here!” negative cycle, which makes it super easy to remember for exams.

## Computing With Negative Weight Cycles

Ah, now I see exactly what you mean — you want an algorithm that can actually compute shortest paths even if there are negative weight cycles, or at least handle them in a meaningful way.

### 1 Important distinction

- Negative weights : edges can have negative values.  
- Negative cycles : a cycle whose total sum of edge weights is negative.  
- If there is a negative cycle in the path, the shortest path is undefined because you can go around the cycle infinitely and reduce the total cost endlessly.  
So technically: no algorithm can compute a finite shortest path if the path includes a negative cycle.

#### A. Bellman–Ford (Single Source Shortest Path)

- Handles negative edge weights.  
- Can detect negative cycles:  
  - After V-1 relaxations, try one more relaxation:  
    - If any distance decreases → negative cycle exists.  
- Cannot give finite shortest path if the negative cycle is in the path.  
How it works:  
1. Initialize dist[source] = 0 and dist[others] = ∞.  
2. Relax all edges V-1 times:  
- dist[v] = min(dist[v], dist[u] + w) for edge u→v with weight w .  
3. Check for negative cycles by trying one more relaxation.  
4. If detected → shortest path undefined for nodes reachable through cycle.

#### B. Floyd–Warshall (All-Pairs Shortest Path)

- Works for graphs with negative weights.  
- Can detect negative cycles by checking dist[i][i] < 0 after computation.  
- Like Bellman-Ford, cannot give a finite shortest path through a negative cycle, but can compute all other shortest paths.

### 3 Summary Table

| Algorithm | Handles Negative Weights | Handles Negative Cycles |
|---|---|---|
| Dijkstra | No | No |
| A* | No | No |
| Bellman–Ford | Yes | Detects (cannot compute path with cycle) |
| Floyd–Warshall | Yes | Detects (cannot compute path with cycle) |

#### Key Takeaway

- Negative edge weights: Bellman-Ford or Floyd-Warshall  
- Negative cycles: Can detect but cannot compute a finite shortest path through them  
- No algorithm can compute a finite path if the negative cycle is part of the path. negative cycle and handles negative weights, so it’s crystal clear.

## Negative Weights vs Negative Cycles
### 1 What is negative weight?

- A weight is just the cost, distance, or value of an edge in a graph.  
- Negative weight means the cost is less than zero.  
Example:

| Edge | Weight |
|---|---|
| A → B | 5 |
| B → C | -2 |

- Edge B → C has negative weight = -2  
- Interpretation: Going from B to C actually reduces total cost by 2.

### 2 What is a negative cycle?

- A cycle is a path that starts and ends at the same node.  
- A negative cycle is a cycle where the sum of all edge weights in the cycle is negative.

#### Example

Graph edges:

```text
css
```

A → B (4)  
B → C (-2)  
C → A (-3)  
- Sum of weights in cycle A → B → C → A = 4 + (-2) + (-3) = -1  
- This is a negative cycle  
Implication:  
- If you go around this cycle repeatedly, your total cost keeps decreasing infinitely.  
- So the “shortest path” that goes through a negative cycle is undefined.

#### A. Bellman–Ford (Single Source Shortest Path)

- Handles: Negative weights  
- Technique: “Relax edges repeatedly”  
- Steps:  
  1. Initialize distances: dist[source] = 0, others = ∞  
2. Repeat V-1 times (V = number of vertices):

```text
sql
```

|  | for each edge u→v with weight w: |
|---|---|

```text
if dist[v] > dist[u] + w:
dist[v] = dist[u] + w
```

3. Check for negative cycles by trying one more relaxation.  
    - If any distance decreases → negative cycle exists  
- Cannot compute shortest path through negative cycles (infinite loop problem)

#### B. Floyd–Warshall (All-Pairs Shortest Path)

- Works for negative weights  
- Computes shortest paths between all pairs of nodes  
- Detects negative cycles if dist[i][i] < 0 after algorithm finishes  
- Cannot compute finite shortest path through negative cycles

### 4 Technique used to handle negative weights

- Relaxation technique:  
  - Keep updating distances if a shorter path is found  
  - Works even if some edges reduce cost (negative weights)  
- Cycle detection:  
  - If after V-1 relaxations, distances still decrease → negative cycle exists

### 5 Summary Table

| Concept | Meaning |
|---|---|
| Negative weight | Edge with cost < 0 |
| Negative cycle | Cycle with total sum of weights < 0 |
| Algorithms handling negative weights | Bellman-Ford, Floyd-Warshall |
| Technique | Relaxation + check for negative cycles |

Key takeaway:  
- Negative weight = edge cost < 0  
- Negative cycle = loop with total cost < 0  
- Bellman-Ford / Floyd-Warshall can handle negative weights and detect negative cycles, but cannot compute finite shortest path through a negative cycle. cycles using relaxation, so it’s crystal clear visually.

## How Floyd–Warshall Handles Negative Weights
### 1 What Floyd–Warshall does

- Goal: Find the shortest path between all pairs of nodes in a graph.  
- Works even if some edges have negative weights.  
- Cannot handle negative cycles for computing finite shortest paths, but can detect them.  
Key idea:  
- It uses dynamic programming: gradually improves estimates of shortest paths using intermediate nodes.

#### Step 0: Initialize distance matrix dist[i][j]

- If there is a direct edge i → j with weight w , set dist[i][j] = w  
- If no direct edge, set dist[i][j] = ∞  
- Distance from a node to itself: dist[i][i] = 0  
Example graph:

| Edge | Weight |
|---|---|
| A → B | 4 |
| B → C | -2 |
| A → C | 5 |

Distance matrix initially:

|  | A | B | C |
|---|---|---|---|
| A | 0 | 4 | 5 |
| B | ∞ | 0 | -2 |
| C | ∞ | ∞ | 0 |

#### Step 1: Consider each node as an intermediate node

Floyd–Warshall formula:  
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])  
- k is an intermediate node  
- i → j may be shorter if it passes through k

#### Step 2: Update distances

Using B as intermediate:  
- Check A → C via B  
dist[A][C] = min(dist[A][C], dist[A][B] + dist[B][C])dist[A][C] = min(5, 4 + (−2))  
- Distance from A → C is updated to 2 because going through B reduces cost.  
Notice: Negative weight edge ( B → C = -2 ) is correctly handled — it reduces the path cost.

#### Step 3: Repeat for all nodes as intermediate

- Eventually, all shortest paths between all pairs are computed  
- Negative edges are handled naturally because the min() formula automatically reduces distances

#### Step 4: Detect negative cycles

- After all updates, if any dist[i][i] < 0 , it means negative cycle exists  
  - Why? Distance from a node to itself < 0 → total cycle cost < 0

### 3 Key intuition

- Floyd–Warshall doesn’t mind negative edges, it just keeps improving dist[i][j] using

```text
dist[i][k] + dist[k][j]
```

- Only problem: if a negative cycle exists, distances can go to -∞ if you try to traverse the cycle multiple times  
- You can detect this by checking the diagonal ( dist[i][i] )

#### Quick Example Result

Original graph:

```text
less
```

A → B: 4  
B → C: -2  
A → C: 5  
After Floyd–Warshall:

|  | A | B | C |
|---|---|---|---|
| A | 0 | 4 | 2 |
| B | ∞ | 0 | -2 |
| C | ∞ | ∞ | 0 |

- Notice A → C became 2 (shorter than direct edge 5) because negative edge B→C helped  
So the technique is:  
1. Initialize distance matrix  
2. Use intermediate nodes to improve paths  
3. Use min() to naturally handle negative edges  
4. Check diagonal to detect negative cycles super easy to understand how negative weights are handled.

## Manhattan Distance

Ah, Manhattan distance — a classic in AI, pathfinding, and heuristics! Let me explain it clearly.

### 1 Definition

Manhattan distance is the distance between two points measured along the grid lines, like how a taxi drives in a city with square blocks (hence the name “Manhattan”).  
- Only horizontal and vertical moves are counted.  
- Diagonal moves are not allowed.  
Mathematically, for two points in 2D:

```text
− −
```

Manhattan distance = ∣x ∣+ ∣y ∣

```text
1 x 2 1 y 2
```

Where:

```text
(x , y ) (x , y )
```

    - and are the coordinates of the two points.

```text
1 1 2 2
```

- | | means absolute value.

### 2 Example

Suppose point A = (1, 2) and B = (4, 5):  
Manhattan distance = ∣1 −4∣+ ∣2 −5∣= 3 + 3 = 6  
- You can imagine moving 3 units right and 3 units up along the grid to reach B from A.

### 3 In 3D

```text
(x , y , z ) (x , y , z )
```

For pointsP andP :

```text
1 1 1 1 2 2 2 2
− − −
```

Manhattan distance = ∣x ∣+ ∣y y ∣+ ∣z ∣

```text
1 x 2 1 2 1 z 2
```

### 4 Why it’s useful in AI

- Used as a heuristic in A* when movement is restricted to horizontal/vertical directions.  
- Always admissible (never overestimates the true cost if only grid moves are allowed).  
- Simpler than Euclidean distance if diagonal movement isn’t allowed.

#### Quick comparison

| Distance type | Formula | Diagonal moves allowed? |
|---|---|---|
| Manhattan | ( | x_1-x_2 |

−x −y  
2 2 2 2  
(x ) + (y )

| Euclidean | Yes |
|---|---|

1 1 intuitive for AI heuristics.
