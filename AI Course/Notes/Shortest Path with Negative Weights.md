# Shortest Path with Negative Weights

## Shortest-Path Algorithms for Negative Weights

When edge weights can be negative, many standard shortest path algorithms (like Dijkstra) fail. So we use special algorithms designed to handle such cases.

#### Key Idea

Relax all edges repeatedly (V−1 times, where V = number of vertices).

#### Why it works

Even with negative weights, the shortest path can have at most (V−1) edges.

### Steps

1. Initialize distance:  
  - Source = 0  
  - Others = ∞  
2. Repeat (V−1) times:  
  - For each edge (u → v), do:

```text
d[v] = min(d[v], d[u] + w)
```

3. Extra iteration:  
  - If distance still updates → negative cycle exists

### Example

Graph:

A → B (4)  
A → C (5)  
B → C (-3)

#### Iteration process

- Start:  
- A=0, B=∞, C=∞  
- After 1st iteration:  
- B=4  
- C=1 (via B: 4 + (-3))  
- Final distances:  
- A=0, B=4, C=1

### Negative Cycle Detection

If after V−1 iterations, values still decrease → cycle like:

A → B → C → A (sum < 0)

### ⏱ Complexity

- Time: O(V × E)  
- Slower than Dijkstra, but more powerful

#### Key Idea

Find shortest paths between all pairs of vertices, even with negative weights.

### Formula (Dynamic Programming)

We update:

```text
d[i][j] = min(d[i][j], d[i][k] + d[k][j])
```

for all intermediate vertices .

```text
k
```

### Example

Matrix initially:

```text
A   B   C
A   0   4   5
B   ∞   0  -3
C   ∞   ∞   0
```

After applying algorithm:

```text
A   B   C
A   0   4   1
B   ∞   0  -3
C   ∞   ∞   0
```

### Negative Cycle Check

If any diagonal element becomes negative, i.e.:

```text
d[i][i] < 0
```

→ Negative cycle exists

### ⏱ Complexity

- Time: O(V³)  
- Good for small graphs or dense graphs

#### Key Idea

- Combines:  
  - Bellman-Ford (to remove negative weights)  
  - Dijkstra (for efficiency)

### Steps

1. Add new vertex and run Bellman-Ford  
2. Reweight edges (remove negatives)  
3. Run Dijkstra from each vertex

### Use Case

- Works for all-pairs shortest path  
- Efficient for sparse graphs

### ⏱ Complexity

- O(V² log V + V E)

### Why Dijkstra Fails

Dijkstra’s algorithm assumes once a node is finalized, its distance is minimum — but with negative edges, a shorter path may appear later.

### Summary Table

| Algorithm | Handles Negative Edges | Detects Negative Cycles | Type |
|---|---|---|---|
| Bellman-Ford | Yes | Yes | Single-source |
| Floyd-Warshall | Yes | Yes | All-pairs |
| Johnson’s | Yes | (indirectly) | All-pairs (efficient) |
| Dijkstra | No | No | Single-source |

### Quick Tip

- Use Bellman-Ford → when negative edges exist  
- Use Floyd-Warshall → small graph, all pairs  
- Use Johnson’s → large sparse graph without STL (based on your preferences).

## Can These Algorithms Fail With Negative Weights?

Short answer: Yes — some algorithms fail with negative weights, but not all.

#### Dijkstra’s algorithm

Fails if even one negative edge exists

#### Why?

It assumes once a node gets the shortest distance, it will never improve later — which is false when negative edges exist.

#### Example where it fails

Graph:

A → B (2)  
A → C (5)  
B → C (-4)  
- Dijkstra picks:  
  - A → C = 5 (initially shortest)  
- But actual shortest path:  
  - A → B → C = 2 + (-4) = -2  
So Dijkstra gives wrong answer.

#### Bellman–Ford algorithm

Works with negative edges  
Fails only if there is a negative cycle

#### Why it fails with negative cycle?

Example:

A → B (1)  
B → C (-2)  
C → A (-2)  
Cycle weight = 1 - 2 - 2 = -3  
You can keep looping and reduce distance infinitely  
So no shortest path exists

#### Floyd–Warshall algorithm

Works with negative edges  
Also fails in presence of negative cycles  
- It detects failure when:

```text
d[i][i] < 0
```

#### Johnson’s algorithm

Handles negative edges  
But:  
- If negative cycle exists → Bellman-Ford step will detect it → algorithm stops

### Final Conclusion

| Case | Result |
|---|---|
| Negative edges only | Safe (Bellman-Ford, Floyd, Johnson) |
| Negative cycle present | No algorithm can give correct shortest path |
| Using Dijkstra with negative edges | Incorrect result |

### Key Concept (Very Important for Exams)

Negative edges are okay  
Negative cycles are NOT okay  
Because:  
- Negative edge → finite shortest path exists  
- Negative cycle → shortest path = −∞ (undefined) cycle, which is a very common exam question.
