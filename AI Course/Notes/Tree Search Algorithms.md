# Tree Search Algorithms

## Hirsova Eforie Neamt Oradea Zerind Arad Timisoara Lugoj Mehadia Dobreta
## 199 244 380 226 234 374 98 Giurgiu Urziceni Hirsova

## Rimnicu Vilcea Bucharest 71 75 118 111 70 75 120
## 646=280+366 413=220+193 415=239+176 671=291+380 Chapter 4, Sections 1–2 19 A∗

## L M D C R F P G B U

Here is a simple and exam-friendly explanation of all the concepts step by step.

### 1 Tree Search (Basic Idea)

Tree Search is a general search method used to solve problems like finding a path from a start state to a goal state.

#### How it works

1. Start from the initial state  
2. Put it in a list called fringe (queue)  
3. Repeat:  
  - Remove one node from fringe  
  - If it is the goal → return solution  
  - Otherwise expand it (generate its children)  
  - Add children to fringe  
The only thing that changes between algorithms is:  
The order in which nodes are removed from the fringe  
That order defines the search strategy.

### 2 Best-First Search

Instead of expanding nodes randomly, we use an evaluation function.  
Each node gets a score  
Expand the node that looks most promising  
The fringe is sorted based on this score.  
Two important types:  
- Greedy Search  
- A* Search

#### Idea

Expand the node that looks closest to the goal.  
It uses:  
h(n) = estimatedcostfromntogoal  
Example:  
In Romania map problem,  
h(n) = straight-line distance to Bucharest.  
So it always chooses the city that appears closest to Bucharest.

#### Properties of Greedy Search

| Property | Answer |
|---|---|
| Complete? | No (can get stuck in loops) |
| Time Complexity | O(b^m) |
| Property | Answer |
| Space Complexity | O(b^m) |
| Optimal? | No |

It may choose a path that looks good but is actually longer.

### 4 A* Search (Most Important for Exam )

A* improves greedy search.  
Instead of only looking at distance to goal, it also considers cost already traveled.  
It uses:

```text
f(n) = g(n) + h(n)
```

Where:  
- g(n) = cost from start to n  
- h(n) = estimated cost from n to goal  
- f(n) = total estimated cost  
A* expands node with smallest f(n)

### 5 Admissible Heuristic

A heuristic is admissible if:

```text
h(n) ≤h (n) ∗
```

Meaning:  
It never overestimates the real cost to goal.  
If heuristic is admissible:  
A* is optimal  
A* finds shortest path  
Example:  
Straight-line distance is admissible because real road distance is always equal or longer.

### 6 Why A* is Optimal

A* always expands nodes in order of increasing f(n).  
It will:  
- Expand all nodes with f(n) < C*  
- Expand some nodes with f(n) = C*  
- Never expand nodes with f(n) > C*  
Where C* = optimal solution cost.  
So it never misses the shortest path.

### 7 Properties of A*

| Property | Answer |
|---|---|
| Complete? | Yes |
| Optimal? | Yes (if heuristic admissible) |
| Time Complexity | Exponential (depends on heuristic quality) |
| Space | Very high (stores all nodes) |

A* uses a lot of memory.

### 8 Consistent Heuristic

A heuristic is consistent if:

```text
′ ′
```

h(n) ≤cost(n, n ) + h(n )  
Meaning:  
The estimated cost always decreases properly along a path.  
If heuristic is consistent:  
f(n) never decreases along a path  
A* becomes easier to analyze  
All consistent heuristics are admissible.

### 9 8-Puzzle Heuristics

Two common heuristics:

#### h1(n) = Number of misplaced tiles

Counts how many tiles are in wrong position.

#### h2(n) = Manhattan distance

Total distance each tile is from correct position.  
h2 is better because it gives more accurate estimate.  
If:  
h2(n) ≥ h1(n)  
Then h2 dominates h1  
Dominating heuristic = better performance.

### Dominance

If one heuristic always gives larger (but still admissible) value:  
Then it reduces search more.  
Better heuristic → fewer expanded nodes → faster search.

### 11 Relaxed Problems

To design good heuristics:  
1. Simplify the problem (remove restrictions)  
2. Solve simplified problem  
3. Use its cost as heuristic  
Because simplified problem cost ≤ real problem cost  
Example:  
- In 8-puzzle, if tiles can move anywhere → gives h1  
- If tiles can move freely to adjacent squares → gives h2

#### Greedy Search

- Uses h(n)  
- Fast sometimes  
- Not optimal  
- Not always complete

#### A* Search

- Uses g(n) + h(n)  
- Complete  
- Optimal (if heuristic admissible)  
- Uses lot of memory

#### Good Heuristic

- Never overestimates (Admissible)  
- Preferably consistent  
- Closer to real cost → better performance

### One-Line Exam Answer Summary

- Tree search expands nodes from fringe.  
- Strategy depends on node removal order.  
- Greedy uses only h(n).  
- A* uses f(n)=g(n)+h(n).  
- A* is optimal if heuristic is admissible.  
- Better heuristics reduce search cost.  
- 5-mark answer version  
- 10-mark long answer version  
- Or short revision notes for last-minute study

## Checking Admissibility and Consistency by Example
### Example graph

Goal = G  
Edges (real costs):  
- S → A cost 2  
- S → B cost 1  
- A → G cost 2  
- B → G cost 5  
So the true cheapest cost to goal (h*) is:  
- h*(G)=0  
- h*(A)=2 (A→G)  
- h*(B)=5 (B→G)  
- h*(S)= min(S→A→G = 2+2=4, S→B→G = 1+5=6) = 4

#### Rule (Admissible)

```text
∗
```

h(n) ≤h (n) for every node n  
Means: heuristic never overestimates the real cheapest remaining cost.

#### Suppose heuristic values

- h(G)=0  
- h(A)=2  
- h(B)=4  
- h(S)=4  
Now compare with true costs h*:

| Node | h(n) | h*(n) | OK? |
|---|---|---|---|
| G | 0 | 0 |  |
| A | 2 | 2 | (equal allowed) |
| B | 4 | 5 | (less) |
| S | 4 | 4 |  |

So this heuristic is admissible because every h(n) is ≤ real remaining cost.

#### If we had h(B)=6

But h*(B)=5  
Then 6 > 5  overestimate → not admissible.

#### Rule (Consistent)

```text
n →n′
```

For every edge with cost :

```text
c
h(n) ≤c(n, n ) + ′ h(n ) ′
```

This is like a “triangle inequality”.  
Meaning: your estimate at n should not be more than “one step cost + estimate from neighbor”.  
Using the same heuristic:  
- h(S)=4, h(A)=2, h(B)=4, h(G)=0  
Check each edge:

#### Edge S→A (cost 2)

```text
h(S) ≤2 + h(A) ⇒4 ≤2 + 2 = 4
```

#### Edge S→B (cost 1)

```text
h(S) ≤1 + h(B) ⇒4 ≤1 + 4 = 5
```

#### Edge A→G (cost 2)

```text
h(A) ≤2 + h(G) ⇒2 ≤2 + 0 = 2
```

#### Edge B→G (cost 5)

```text
h(B) ≤5 + h(G) ⇒4 ≤5 + 0 = 5
```

All edges pass → heuristic is consistent.

### Key point to remember (exam line)

- Admissible: never overestimates the true cost to the goal.  
- Consistent: for every move, heuristic follows triangle inequality:  
- “current estimate ≤ step cost + next estimate”.

### Quick “Fail” example for consistency

Keep same graph, but set:  
- h(S)=6, h(A)=2  
Check S→A (cost 2):

```text
6 ≤2 + 2 = 4
```

So heuristic is not consistent.  
And also notice: if h(S)=6 but true h*(S)=4 → it also becomes not admissible. explain why that heuristic is admissible (and typically consistent) in maps.

## h(n) and h*(n)

Very simple explanation

### What is h(n) ?

h(n) is the heuristic value.  
It means:  
Estimated cost from node n to the goal  
It is a guess.  
It is not necessarily the real cost.  
It is what our heuristic function predicts.  
Example (Romania problem):  
If you are in Arad  
Straight-line distance to Bucharest = 366 km  
So:  
h(Arad) = 366  
That is just an estimate.

### What is h*(n) ?

h*(n) (read as “h star of n”) is:  
The true actual minimum cost from node n to the goal  
It is the real shortest path cost.  
In Romania:  
Real shortest road distance from Arad to Bucharest = 418 km  
So:

```text
∗
```

h (Arad) = 418

### Difference Between Them

| Symbol | Meaning | Real or Guess? |
|---|---|---|
| h(n) | Estimated cost to goal | Guess |
| h*(n) | True minimum cost to goal | Real |

### Why is this important?

For a heuristic to be admissible:

```text
h(n) ≤h (n) ∗
```

Meaning:  
Your guess should never be bigger than the real cost.  
Example:  
- h(Arad) = 366  
- h*(Arad) = 418  
Since 366 ≤ 418  
It is admissible.  
If we guessed 500  
That would not be admissible.

### One-Line Exam Answer

- h(n) = estimated cost from n to goal  
- h*(n) = actual shortest cost from n to goal

## When a Heuristic Is Admissible or Consistent

Good  let’s explain this clearly and in exam style.

#### Symbol

```text
h(n) ≤h (n) ∗
```

#### What it represents

- h(n) = estimated cost from node n to goal  
- h*(n) = true (actual shortest) cost from node n to goal

#### Meaning

A heuristic is admissible if it never overestimates the real cost to reach the goal.  
It can:  
- Be equal to real cost  
- Be smaller than real cost  
- But NEVER be bigger

#### Example

If real shortest cost from A to Goal = 10  
- h(A) = 8 → admissible  
- h(A) = 10 → admissible  
- h(A) = 12 → NOT admissible

#### Why important?

If heuristic is admissible →  
A* will always find optimal (shortest) solution.

#### Symbol (Triangle Inequality)

```text
h(n) ≤c(n, n ) + ′ h(n ) ′
```

Where:  
h(n)= estimate at current node

```text
′
```

c(n, n )= actual step cost from n to neighbor n'

```text
′
```

h(n )= estimate at next node

#### What it represents

It means:  
Estimated cost from n  
should be less than or equal to  
(step cost to neighbor + estimate from neighbor)  
It follows the triangle inequality rule.

#### Simple Meaning

Your heuristic should decrease smoothly as you move toward the goal.  
It should NOT jump down suddenly.

### 3 Relationship Between Them

Important exam point:  
Every consistent heuristic is admissible  
But every admissible heuristic is NOT necessarily consistent

### 4 Difference in One Table

| Property | Admissible | Consistent |
|---|---|---|
| Main Condition | h(n) ≤ h*(n) | h(n) ≤ c(n,n') + h(n') |
| Checks Against | True goal cost | Neighbor step cost |
| Property | Admissible | Consistent |
| Ensures A* Optimal? | Yes | Yes |
| Stronger Condition? | No | Yes |

### 5 What They Represent Conceptually

- Admissible → Safe guess (never overestimate)  
- Consistent → Smooth & logical guess (f(n) never decreases along path)

### 6 Very Short Exam Answer

- A heuristic is admissible if

```text
h(n) ≤h (n) ∗
```

- (never overestimates true cost)  
- A heuristic is consistent if

```text
h(n) ≤c(n, n ) + ′ h(n ) ′
```

- (satisfies triangle inequality)  
- 5-mark answer format  
- OR numerical example to check both step-by-step.

## Hill Climbing Algorithm

Here is a simple and clear explanation of Hill Climbing Algorithm for the exam.

### Hill Climbing Algorithm

Hill Climbing is a local search algorithm.  
It tries to improve the current solution step by step.  
At each step, it moves to the better neighboring state.  
It stops when no better neighbor exists.  
It is called “hill climbing” because it is like climbing a mountain:  
- You always move upward  
- You stop when you reach the top

### Basic Idea

1. Start from an initial state.  
2. Look at all neighboring states.  
3. Move to the neighbor with the best value.  
4. Repeat until no improvement is possible.

### Simple Pseudocode

```text
Current = Initial State
Loop:
Find best neighbor of Current
If neighbor is better than Current:
Current = neighbor
Else:
Stop (local maximum reached)
```

|  | Code |
|---|---|

### Example

Suppose we want to maximize function:  
f(x) = -x² + 6x  
Start at x = 1  
Check neighbors:  
- x = 2 → better value  
- x = 3 → better  
- x = 4 → worse  
Algorithm stops at x = 3  
That is the peak (maximum).

### Types of Hill Climbing

1 Simple Hill Climbing  
- Chooses first better neighbor.  
2 Steepest-Ascent Hill Climbing  
- Checks all neighbors.  
- Chooses the best one.  
3 Stochastic Hill Climbing  
- Chooses randomly among better neighbors.

### Problems in Hill Climbing

Local Maximum  
Stops at small peak, not global best.  
Plateau  
Flat area — no direction to improve.  
Ridge  
Needs diagonal move but algorithm can't.

### Example of Local Maximum Problem

Imagine small hill before big mountain.  
Algorithm climbs small hill and stops,  
even though a bigger hill exists elsewhere.

### Properties

| Property | Value |
|---|---|
| Complete? | No |
| Optimal? | No |
| Time Complexity | Depends on neighbors |
| Space Complexity | Very low (stores only current state) |

### Advantages

Very simple  
Fast  
Uses very little memory

### Disadvantages

Can get stuck  
No backtracking  
May miss best solution

### One-Line Exam Definition

Hill Climbing is a local search algorithm that continuously moves to the best neighboring state until no better state is available.  
- Hill Climbing vs A*  
- Or give diagram-based explanation for exam clarity.

## State Space
#### State Space (in Easy Words)

State space means:  
All possible situations (states) of a problem from start to goal.  
It includes:  
- Initial state  
- All possible intermediate states  
- Goal state

#### Simple Definition (Exam Line)

State space is the set of all possible states that can be reached while solving a problem.

#### Example 1: Chess

In chess:  
- Every possible board arrangement is a state  
- All possible board positions together form the state space  
There are millions of possible states.

#### Example 2: 8-Puzzle

In 8-puzzle:  
- Every different tile arrangement is a state  
- All arrangements together = state space

#### Example 3: Map Problem (Romania)

- Each city = a state  
- All cities together = state space

#### Why It Is Important?

Search algorithms (like BFS, DFS, A*) explore the state space to find the goal.

#### Simple Analogy

Think of state space like:  
A big map of all possible moves you can make in a problem.

#### Very Short Exam Answer

State space is the collection of all possible states in a problem, from the initial state to the goal state.  
- State space vs Search space  
- Or draw a small example tree explanation.
