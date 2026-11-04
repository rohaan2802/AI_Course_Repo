# Hill Climbing ALgo

## Hill Climbing: Key Terms

Here is a simple explanation of each term shown in the diagram:

#### 1) Objective Function

This is the thing we want to improve or maximize.  
- It could be profit, accuracy, score, or performance.  
- Higher value = better result.  
In the graph, the vertical axis represents the objective function.

#### 2) State Space

This is the set of all possible solutions.  
- Every point on the horizontal axis is one possible state (solution).  
- Some states are good, some are bad.  
In the graph, the horizontal axis represents the state space.

#### 3) Current State

This is the solution where we are right now.  
- The algorithm starts here.  
- Then it tries to move to better states.  
It is shown as the small circle on the curve.

#### 4) Global Maximum

This is the best possible solution in the entire space.  
- No other state has a higher value.  
- This is the final goal.  
In the graph, it is the highest peak.

#### 5) Local Maximum

This is a peak that is better than nearby states, but not the best overall.  
- It looks like the best solution if you only check nearby points.  
- But a better peak exists somewhere else.  
In the graph, it is a smaller peak than the global maximum.

#### 6) Flat Local Maximum

This is a flat area at the top instead of a sharp peak.  
- Many nearby states have the same value.  
- The algorithm may stop because it sees no improvement.  
In the graph, it is the flat plateau on the right.

#### 7) Shoulder

This is a flat or gentle slope that is not a maximum.  
- It is not the top, but progress seems slow.  
- The algorithm might think it is stuck.  
In the graph, it is the flat area on the left side before the big peak.

#### Simple Real-Life Example

Imagine climbing hills in the fog:  
- State space → the whole mountain range  
- Current state → where you are standing  
- Objective function → your height  
- Local maximum → a small hill top  
- Global maximum → the tallest mountain  
- Shoulder → flat area on the slope  
- Flat local maximum → wide, flat hilltop  
Your goal is to reach the tallest mountain, not just any hill. Annealing behave on this graph.

## Finding Each Term Mathematically

To find these things mathematically, we use derivatives and some simple rules from calculus.  
Assume we have a function:

```text
f(x)
```

This function represents the objective function.

#### Step 1: Find the first derivative

```text
f (x) ′
```

This tells us the slope of the curve.

#### Step 2: Set the derivative equal to zero

```text
f (x) = ′ 0
```

Solve this equation.  
The solutions are called critical points.  
These points may be:  
- Local maximum  
- Local minimum  
- Flat region (shoulder)

#### Step 3: Use the second derivative test

Find:

```text
f (x) ′′
```

Then check:

| Condition | Result |
|---|---|

f (x) < 0 Local maximum  
f (x) > 0 Local minimum  
f (x) = 0 Flat point / shoulder

### 2) How to Find Global Maximum

After finding all local maxima:  
1. Calculate function value at each local maximum.  
2. Compare all values.  
3. The highest value is the global maximum.

### 3) Flat Local Maximum (Plateau)

At these points:

```text
f (x) = ′ 0
```

But the curve is flat for a range of values.  
Example:

```text
f(x) = 5 for 2 ≤x ≤4
```

All points between 2 and 4 have the same value → flat maximum.

### 4) Shoulder (Flat but not maximum)

At a shoulder:

```text
f (x) = ′ 0
```

But the slope becomes positive or negative again.  
Example:

```text
f(x) = x3
f (x) = ′ 3x2
x = 0
```

At :

```text
f (0) = ′ 0
```

But this is not a maximum or minimum → it is a shoulder.

### Full Example

Let:

```text
f(x) = −x + 2 4x
```

#### Step 1: First derivative

```text
f (x) = ′ −2x + 4
```

#### Step 2: Set to zero

```text
−2x + 4 = 0
x = 2
```

#### Step 3: Second derivative

```text
f (x) = ′′ −2
```

Since:

```text
f (2) < ′′ 0
```

So this is a local maximum.  
Now check value:

```text
f(2) = −4 + 8 = 4
```

Since this is the highest value, it is also the global maximum.

### Quick Summary (Rule Sheet)

| Term | Mathematical Condition |
|---|---|

f (x) = 0

Critical point  
′ ′′  
f (x) = 0 f (x) < 0

| Local maximum | and |
|---|---|

′ ′′  
f (x) = 0 f (x) > 0

| Local minimum | and |
|---|---|
| Global maximum | Highest value among all maxima |

f (x) = 0

| Shoulder | but not max/min |
|---|---|
| Flat maximum | Same value over a range |

- Solve some practice questions step-by-step  
- Give exam-style problems  
- Explain this without calculus (for algorithms).

## Shoulder vs Flat Local Maximum

Totally fair — shoulder and flat local maximum look similar because both can be “flat”. The difference is:  
- Flat local maximum (plateau top): flat and it’s the best nearby (if you move a little left or right, value goes down).  
- Shoulder: flat but not a peak (after the flat part, the function can continue going up on at least one side).  
Think like hiking:  
- Plateau top: you’re on a flat summit.  
- Shoulder: you’re on a flat ledge but the mountain continues upward later.

#### Step 0: You need a function

#### Step 1: Find places where slope is zero (flatness)

Compute:

```text
f (x) ′
```

Find where:

```text
f (x) = ′ 0
```

These points (or intervals) are “flat candidates”.

#### Step 2A: Check values around it (the simplest test)

```text
0.1
```

Pick a tiny number  like .

```text
h
x = a
```

If at some point :

```text
f(a −h) < f(a) and f(a + h) < f(a)
```

then  is a local maximum.

```text
a
```

If this happens for many points in a range (like from  to ), then it’s a flat local

```text
a b
```

maximum (plateau).  
Key idea: both sides go down.

#### Step 2B: Check around it again

```text
x = a
```

At , if:  
- one side goes down and the other side goes up, OR  
- both sides go up/down but it’s not a “top”  
Then it’s not a maximum → likely a shoulder (or inflection-type flat point).  
Key idea: it’s flat, but not the top.

### Super-clear examples Example 1: Shoulder

```text
f(x) = x3
f (x) = ′ 3x2
f (x) = ′ 0
```

Set :

```text
3x = 2 0 ⇒x = 0
```

Now test values around 0:

```text
f(−0.1) = (−0.1) = 3 −0.001
f(0) = 0
f(0.1) = (0.1) = 3 0.001
```

Here:

```text
f(−0.1) < f(0) < f(0.1)
```

So it keeps increasing through 0 (not a top).  
That flat point is a shoulder.

### Example 2: Flat local maximum (plateau top)

Here’s a simple “plateau” style function idea:

```text
2 ≤x ≤4 f(x) = 5
```

- For , (flat)

```text
f(x) < 5
```

- Outside that range,

```text
x = 3
```

To test any point like :

```text
h = 0.1
```

Pick

```text
f(2.9) = 5
f(3) = 5
f(3.1) = 5
```

It’s flat inside.  
Now check near the edges:

```text
f(1.9) < 5
f(4.1) < 5
```

So near that flat region, moving away makes it go down.  
That flat region is a flat local maximum.

#### Flat local maximum

Flat AND both sides eventually go down.

#### Shoulder

Flat BUT at least one side eventually goes up (it’s on the way to a higher place).

```text
f (a) = ′ 0
```

After finding :

### Do the sign test on arounda

Pick just left and just right:

```text
f (x) ′
```

- If changes + to - → local maximum

```text
f (x) ′
```

- If changes - to + → local minimum  
- If it stays same sign (like + to +) → shoulder/flat inflection

```text
x3
```

For shoulder example :

```text
f (x) = ′ 3x2
```

- left of 0: is positive  
- right of 0: still positive  
- So no sign change → not max/min → shoulder.  
For a flat local max, you’d still see “up then down” behavior (eventually), but sometimes the derivative can be zero across an interval (plateau).

```text
h
```

sign test.

## One Side vs Both Sides

When we say “both sides” or “one side”, we are talking about the function’s behavior just to the left and just to the right of a point.  
Imagine a number line:

```text
css
---- left side ---- a ---- right side ----
```

Here:  
- a is the point we are testing.  
- Left side means a value slightly smaller than a.  
- Right side means a value slightly larger than a.  
For example, if:

```text
a = 3
```

Then:

```text
2.9
```

- Left side: (just before 3)

```text
3.1
```

- Right side: (just after 3)  
We check what the function does at those nearby points.

### Why we check both sides

We want to know if the point is:  
- A peak (maximum)  
- A valley (minimum)  
- Or just a flat place on the way up or down  
So we compare:

```text
f(a −h), f(a), f(a + h)
```

Where  is a small number like 0.1.

```text
h
```

### What “both sides” means Case 1: Both sides go down → Local maximum

If:

```text
f(a −h) < f(a) and f(a + h) < f(a)
```

That means:  
- Left side is lower  
- Right side is lower  
- So the point is a peak  
Example:

| x | f(x) |
|---|---|
| 2.9 | 4 |
| 3 | 5 |
| 3.1 | 4 |

Both sides are lower than the middle → local maximum.

### Case 2: Both sides go up → Local minimum

If:

```text
f(a −h) > f(a) and f(a + h) > f(a)
```

Example:

| x | f(x) |
|---|---|
| 2.9 | 5 |
| 3 | 4 |
| 3.1 | 5 |

Both sides higher → local minimum.

### Case 3: One side up, one side down → Shoulder

If:

```text
f(a −h) < f(a) < f(a + h)
```

or

```text
f(a −h) > f(a) > f(a + h)
```

Example:

| x | f(x) |
|---|---|
| 2.9 | 2 |
| 3 | 3 |
| 3.1 | 4 |

Left side lower, right side higher.  
So the function is still going up.  
This is a shoulder, not a peak.

### Simple real-life picture

Imagine standing on a path:

#### Both sides down

You’re on a hilltop.

```text
/\
/  \
```

#### One side up, one side down

You’re on a slope, not the top.

```text
/
/
```

That flat moment is a shoulder.

### One-line memory trick

- Both sides down → maximum  
- Both sides up → minimum  
- One up, one down → shoulder  
- 5 quick practice questions  
- Or one function and we solve it step by step together.

## Neighbours at a Shoulder and a Flat Maximum
### Shoulder vs Flat Local Maximum (Final Clear Rule)

Assume we are checking a point a.  
We look at values just left and right of it:

```text
f(a −h), f(a), f(a + h)
```

### Shoulder

At a shoulder, the point is flat, but it is not the top.  
That means:  
- On one side, the function goes up.  
- So the point is just part of a slope, not a peak.  
Example pattern:

| Left | Middle | Right |
|---|---|---|
| 2 | 3 | 4 |

Here:

```text
2 < 3 < 4
```

So the function keeps going up → shoulder.

#### Key idea

At least one side goes up.

### Flat Local Maximum

At a flat local maximum, the top is flat, but it is still the highest nearby point.  
That means:  
- On both sides, the value is same or lower.  
- If you move away from that flat region, it eventually goes down.  
Example:

| Left | Middle | Right |
|---|---|---|
| 4 | 5 | 4 |

Here:

```text
4 < 5 > 4
```

Both sides go down → maximum.  
If many points have value 5, that becomes a flat local maximum (plateau).

### Your sentence corrected

- at shoulder one side will go up  
- at flat local maxima both sides go down

#### Correct version

- Shoulder: at least one side goes up (not a peak).  
- Flat local maximum: both sides go down (it is a peak, but flat).

### Super short memory trick

- Shoulder = still climbing  
- Flat local max = reached the top (but flat)  
- A quick visual graph example, or  
- 3 short practice questions to test your understanding.

## A Shoulder Where Both Sides Rise

The confusion comes from how the shoulder looks in the picture versus what it means mathematically.

### What a shoulder really means

A shoulder is a point where:  
- The slope becomes zero (flat for a moment).  
- But it is not a peak.  
- The function continues rising later.  
So it is just a temporary flat spot while going upward.

### Can both sides go up at a shoulder?

but not at the same time in the immediate small neighborhood.

#### True shoulder behavior (correct case)

At a shoulder:  
- Just before the point → function is increasing  
- Just after the point → function is still increasing  
So both sides are lower than the next points, but the function does not go down.  
Example:

| x | f(x) |
|---|---|
| 2.9 | 2 |
| 3 | 3 |
| 3.1 | 3.01 |

Here:  
- Left is lower than middle  
- Right is slightly higher than middle  
So the function keeps going up → shoulder.

#### What about the picture’s first shoulder?

In the diagram, the first shoulder:  
- Looks flat  
- Then the curve continues upward to a higher peak  
So overall:  
- It is not the top  
- The function eventually rises higher  
That is why it is called a shoulder.

### Important clarification

When we say “check both sides,” we mean:  
Very close to the point, not far away.  
So:

#### Shoulder (mathematically)

Near the point:

```text
f(a −h) < f(a) ≤f(a + h)
```

or

```text
f(a −h) ≤f(a) < f(a + h)
```

The function does not go down on both sides.

#### Flat local maximum

Near the point:

```text
f(a −h) < f(a) and f(a + h) < f(a)
```

Both sides go down → true peak.

#### Shoulder

- Flat point  
- Not the highest  
- Function continues rising somewhere

#### Flat local maximum

- Flat point  
- Highest in the neighborhood  
- Both sides go down  
in a shoulder, the function can be rising before and after it overall, but very close to the point, at least one side does not go down. That’s why it is not a maximum. cases step by step.

## Flat Local Minimum

flat local minimum does exist.  
It is just the opposite of a flat local maximum.

### What is a Flat Local Minimum?

A flat local minimum is:  
- A lowest point in a small region.  
- But the bottom is flat, not sharp.  
- Several nearby points may have the same lowest value.

### Simple definition (easy rule)

At a point :

```text
a
f(a −h) > f(a) and f(a + h) > f(a)
```

This means:  
- Left side is higher  
- Right side is higher  
- So the point is a minimum

#### For flat local minimum

Not just one point — a range of points has the same lowest value.  
So:

```text
f(x) = c for a ≤x ≤b
```

And outside that range:

```text
f(x) > c
```

### Visual idea Flat local minimum

```text
markdown
\      /
\____/
```

The bottom is flat, not a sharp V.

### How to compute it mathematically (step by step)

```text
f(x)
```

Assume we have a function .

### Step 1: Find first derivative

```text
f (x) ′
```

### Step 2: Set it equal to zero

```text
f (x) = ′ 0
```

Solve for .

```text
x
```

These are the critical points.

### Step 3: Check second derivative

```text
f (x) ′′
```

Now:

| Condition | Meaning |
|---|---|

f (x) > 0 Local minimum  
f (x) < 0 Local maximum  
f (x) = 0 Could be flat minimum, flat max, or shoulder

### Step 4: Check both sides (final test)

Pick small .

```text
h
```

If:

```text
f(a −h) > f(a) and f(a + h) > f(a)
```

Then it is a local minimum.  
If this happens over a range of values, it becomes a flat local minimum.

### Example of flat local minimum

Consider:

```text
⎧(x −2)2 x < 2
f(x) = ⎨ 0 2 ≤x ≤4
⎩ (x −4)2 x > 4
```

Between 2 and 4:

```text
f(x) = 0
```

That whole region is flat and lowest.

```text
x = 3
```

Check around :

```text
f(2.9) = 0
f(3) = 0
f(3.1) = 0
```

Now check outside:

```text
f(1.9) > 0
f(4.1) > 0
```

So both sides go up → flat local minimum.

### Final comparison table

| Type | Both sides behavior |
|---|---|
| Local maximum | Both sides go down |
| Flat local maximum | Flat top, then both sides go down |
| Local minimum | Both sides go up |
| Flat local minimum | Flat bottom, then both sides go up |
| Shoulder | One side up, one side down |

### One-line memory trick

- Maximum: top of hill  
- Minimum: bottom of valley  
- Flat minimum: flat valley floor  
- A single function where we find shoulder, flat max, and flat min all together step by step.

## Flat Extrema and Relative Extrema
### 1) Flat Local Minimum

#### Meaning

in a flat local minimum:  
- Both sides go upward.  
- But the bottom is flat across a range, not just one point.  
So your idea is correct.

### 2) Flat Local Maximum vs Flat Local Minimum (simple rule)

| Type | Behavior near the point/range |
|---|---|
| Flat local maximum | Both sides go down |
| Flat local minimum | Both sides go up |

### 3) Are they found like relative extrema?

The method is basically the same, but there is one extra condition.

### Normal relative extrema (single point)

We check:

```text
f (x) = ′ 0
```

1.  
2. Second derivative or sign test  
And we get:  
- Local max at a point  
- Local min at a point

### Flat extrema (range of points)

Same idea, but:  
Instead of one point, there is a whole interval where:  
f(x) = constant  
So the function is flat across that region.

### 4) Key difference (most important idea)

| Normal extrema | Flat extrema |
|---|---|
| Happens at one point | Happens over a range |
| Sharp peak or valley | Flat top or flat bottom |

f (x) = 0 f (x) = 0

|  | at one point | across an interval |
|---|---|---|

### 5) Step-by-step method to detect flat extrema Step 1: Find derivative

```text
f (x) ′
```

### Step 2: Solve

```text
f (x) = ′ 0
```

#### Two possibilities

- You get single value → normal extremum  
- You get range of values → flat extremum  
Example:  
If:

```text
f (x) = ′ 0 for 2 ≤x ≤4
```

Then the function is flat in that region.

### Step 3: Check both sides of the range

For a flat maximum:  
- Outside the range → values go down  
For a flat minimum:  
- Outside the range → values go up

### Final simple conclusion (your sentence corrected)

:  
- Flat maximum: both sides go down.  
- Flat minimum: both sides go up.  
- And yes, they are found like relative extrema, but over a range instead of a single point.  
- One exam-style question where we find all types (max, min, shoulder, flat max, flat min) in one function.
