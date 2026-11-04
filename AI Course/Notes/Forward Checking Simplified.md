# Forward Checking Simplified

## Forward Checking: Short Solution
### Part 1: Forward Checking

Given:  
M1 = P2  
Domains initially: {P1, P2, P3}  
Order: P1 < P2 < P3

#### Apply constraints

- M1 before M2 → M2 > P2 → {P3}  
- M1 ≠ M3 → remove P2 → {P1, P3}  
- M4 not directly affected → {P1, P2, P3}

#### Final Domains

- M2 = {P3}  
- M3 = {P1, P3}  
- M4 = {P1, P2, P3}

#### Step 1: MRV

Smallest domain → M2 = {P3}  
Assign: M2 = P3

#### Step 2: Forward Checking

- M2 ≠ M3 → remove P3 from M3 → {P1}  
- M3 before M4 → M4 > P1 → {P2, P3}

#### Final

- Selected Milestone: M2  
- Phase Assigned: P3

| Milestone | New Domain |
|---|---|
| M3 | {P1} |
| M4 | {P2, P3} |

Failure? → NO

### Part 3: FC vs Arc Consistency

Given: X = P1

#### Forward Checking

- X before Y → Y = {P2, P3}  
- Z unchanged → {P1, P2, P3}

#### Arc Consistency (Y before Z)

- If Y = P3, no value in Z > P3 →  remove P3  
Y = {P2}

#### Answers

- D(Y) = {P2}  
- D(Z) = {P1, P2, P3} (FC stage)  
- Additional removal? → YES (P3 removed from Y)  
- Smaller domain method → Arc Consistency

#### Bottom-up

Level 3 (MIN):  
- (2, -5) → -5  
- (4, 5) → 4  
- (-30, 10) → -30  
- (3, 4) → 3  
- (-4, 4) → -4  
- (5, 4) → 4  
- (-5, -15) → -15  
- (5, 7) → 5  
Level 2 (MAX):  
- (-5, 4) → 4  
- (-30, 3) → 3  
- (-4, 4) → 4  
- (-15, 5) → 5  
Level 1 (MIN):  
- (4, 3) → 3  
- (4, 5) → 4

#### Root (MAX)

max(3, 4) = 4

### Final Answers Summary

- Forward Checking Domains:  
- M2={P3}, M3={P1,P3}, M4={P1,P2,P3}  
- MRV Selection:  
- M2 = P3 → No failure  
- Arc Consistency better? → YES  
- Minimax Result:  
- Final Value = 4

## Alpha–Beta Pruning on the Corrected Tree

we’ll redo Part 4 using Alpha-Beta Pruning and fix that value (-5, 45).

### Corrected Leaf Values (left → right)

```text
(2, -5), (4, 5), (-30, 10), (3, 4),
(-4, 4), (5, 4), (-5, 45), (5, 7)
```

### Tree (Redrawn Simply)

```text
MAX
/           \
MIN           MIN
/     \       /     \
MAX     MAX   MAX     MAX
/  \    /  \   /  \    /  \
MIN MIN MIN MIN MIN MIN MIN MIN
```

#### Start at root

- α = -∞, β = +∞

#### MIN node

- α = -∞, β = +∞

#### First MAX

- MIN(2, -5) → -5  
- MIN(4, 5) → 4  
- MAX(-5, 4) = 4  
Update β = 4

#### Second MAX

- MIN(-30, 10) → -30  
MAX node gets -30  
Now:  
- α = -30, β = 4  
Check next:  
- MIN(3, 4) → 3  
MAX(-30, 3) = 3

#### Back to MIN

- MIN(4, 3) = 3  
Root α = max(-∞, 3) = 3

#### MIN node

- α = 3, β = +∞

#### First MAX

- MIN(-4, 4) → -4  
- MIN(5, 4) → 4  
- MAX(-4, 4) = 4  
β = 4

#### Second MAX

- MIN(-5, 45) → -5  
MAX node = -5  
Now:  
- α = -5, β = 4

#### Pruning happens here

Next:  
- MIN(5, 7) → would be 5  
- But check:  
At MIN parent:  
- current β = min(4, -5) = -5  
Now:  
- β = -5 ≤ α = 3 → PRUNE remaining branch  
So (5, 7) is NOT evaluated

### Final Computation

Right MIN:  
- min(4, -5) = -5

### Final Root Value

```text
MAX(3, -5) = 3
```

### Pruned Nodes

- Entire branch: (5, 7)

### Final Answer

- Alpha-Beta Result = 3  
- Pruned: last pair (5, 7)

## Python: (stack, [stack])

In Python, the expression:

```text
(stack, [stack])
```

means you are creating a tuple with two elements:

### Breakdown

- stack → first element (whatever value stack has)  
- [stack] → second element (a list containing stack)

### Example

```python
stack = 5
result = (stack, [stack])
print(result)
```

Output:

```text
(5, [5])
```

### Key Idea

| Part | Type | Meaning |
|---|---|---|
|  | variable | normal value |

```text
stack
```

|  | list | list with one element |
|---|---|---|

```text
[stack]
```

|  | tuple | fixed collection |
|---|---|---|

```text
( , )
```

### Important Difference

```python
stack = [1, 2]
print((stack, [stack]))
```

Output:

```text
([1, 2], [[1, 2]])
```

- First → original list  
- Second → list inside another list

### Simple Meaning

"(stack, [stack])" = value + list version of value packed together

## Tuples in Python

A tuple in Python is a collection of items (like a list) but it is immutable (cannot be changed after creation).

### Simple Definition

A tuple = ordered + unchangeable collection

### How to create a tuple

```text
t = (1, 2, 3)
```

You can also do:

```text
t = 1, 2, 3
```

### Example

```python
t = (10, 20, 30)
print(t[0])   # 10
```

### Key Features

| Feature | Tuple |
|---|---|
| Ordered | Yes |
| Changeable | No |
| Allows duplicates | Yes |
| Uses () |  |

### Immutable (Important)

```text
t = (1, 2, 3)
```

t[0] = 5   #  Error  
You cannot modify tuple values

### Tuple vs List

| Feature | Tuple | List |
|---|---|---|
| Syntax ( ) [ ] |  |  |
| Changeable | No | Yes |
| Feature | Tuple | List |
| Speed | Faster | Slower |

### Why use tuple?

- When data should not change  
- Faster than lists  
- Safe (no accidental modification)

### Easy Way to Remember

List = editable  
Tuple = fixed (locked)

## What Tuples Can Store

No  — a tuple is NOT only for numbers.  
A tuple can store any type of data.

#### 1. Numbers

```text
t = (1, 2, 3)
```

#### 2. Strings

```text
t = ("apple", "banana", "cherry")
```

#### 3. Mixed data types

```text
t = (1, "hello", 3.5, True)
```

#### 4. Other collections (even nested)

```text
t = (1, [2, 3], ("a", "b"))
```

### Important Point

Even though tuple is immutable, if it contains a list, that list can still change:

```python
t = (1, [2, 3])
t[1][0] = 100
print(t)   # (1, [100, 3])
```

### Simple Answer

Tuple can store:  
- Numbers  
- Strings  
- Booleans  
- Lists / Tuples  
- Mixed data

### Easy Trick

Think of tuple as a box that can hold anything,  
but once packed, you cannot replace items in the box.
