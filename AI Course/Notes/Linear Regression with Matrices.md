# Linear Regression with Matrices

### 1. Linear Regression (One Feature) using Matrices

Suppose we have data:

| x | y |
|---|---|
| 1 | 2 |
| 2 | 3 |
| 3 | 5 |

We want line:

```text
y = mx + b
```

Here:  
m= slope (weight)  
b= intercept (bias)  
In matrix form:

```text
Y = Xθ
```

Where:

```text
θ = [ b m]
```

#### Step 1: Build Matrix X

Add column of 1s for bias.

```text
1 1
X = 1 2
1 3
```

Output vector:

```text
2
Y = 3
5
```

#### Step 2: Use Normal Equation

Formula:

```text
θ = (X X) T −1 X Y T
```

T

### Step 3: FindX X

```text
X T = [1 1 1 3]
1 2
```

Multiply:

```text
X X = T [3 14] 6
6
```

#### Step 4: Find inverse

```text
(X X) T −1 = 1 [14 6 −6 −6 3 ]
```

T

### Step 5: FindX Y

```text
X Y = T [10 23]
```

#### Step 6: Final calculation

```text
θ = 1 [14 6 −6 −6 3 ] [10 23]
```

After multiplication:

```text
θ = [0.33 1.5 ]
```

So:

```text
b = 0.33
```

- bias

```text
m = 1.5
```

- slope  
Final model:

```text
y = 1.5x + 0.33
```

Check:

```text
x = 2
```

For

```text
y = 1.5(2) + 0.33
y = 3.33
```

Close to actual value 3.

### 2. Multiple Linear Regression (Multiple Features)

Now use 2 input features.  
Suppose:

| Size | Rooms | Price |
|---|---|---|
| 1 | 2 | 10 |
| 2 | 1 | 12 |
| 3 | 3 | 20 |

Model:

```text
y = b + w 1 x 1 + w 2 x 2
```

#### Step 1: Build Matrix

Add bias column.

```text
1 1 2
X = 1 2 1
1 3 3
```

Target:

```text
10
Y = 12
20
```

Unknown parameters:

```text
b
θ = w 1
w 2
```

#### Step 2: Use same formula

```text
θ = (X X) T −1 X Y T
```

#### Step 3: Compute transpose

```text
1 1 1
X T = 1 2 3
2 1 3
```

T

### Step 4: ComputeX X

```text
3 6 6
X X = T 6 14 13
6 13 14
```

T

### Step 5: ComputeX Y

```text
42
X Y = T 94
92
```

After inverse and multiplication (skipping lengthy arithmetic):

```text
2
θ = 4
2
```

Final equation:

```text
y = 2 + 4x 1 + 2x2
```

Meaning:  
- intercept = 2  
- feature1 weight = 4  
- feature2 weight = 2

#### Prediction Example

For:  
Size=2  
Rooms=4

```text
y = 2 + 4(2) + 2(4)
y = 2 + 8 + 8
y = 18
```

Predicted output = 18

### Big Picture (Simple Logic)

Linear algebra method treats regression as:

```text
Y = Xθ
```

Where:  
- X → input matrix  
- Y → outputs  
- θ → unknown weights  
Goal:  
Find best θ minimizing squared error.  
Linear algebra directly solves it using:

```text
θ = (X X) T −1 X Y T
```

instead of trial-and-error or gradient descent.  
Simple summary:

| Method | Features |
|---|---|
| Linear Regression | 1 input feature |
| Multiple Linear Regression | Many input features |
| Matrix Technique | Solve all weights together |

inverse calculation step by step.

## Linear Regression With Matrices (y = Xθ)

Given:

| X | Y |
|---|---|
| 1 | 12 |
| 2 | 18 |
| 3 | 25 |
| 4 | 31 |
| 5 | 38 |

Equation:

```text
y = mx + c
```

Matrix form:

```text
Y = Xθ
```

- Why don't we simply multiplyXand  ?

```text
θ
```

We actually DO multiply them — but first we must find θ.

### Step 1 — Build matrices

Add bias column (1s).  
Input matrix:

```text
1 1
1 2
X = 1 3
1 4
1 5
```

Output vector:

```text
12
18
Y = 25
31
38
```

Parameters:

```text
θ = [ c m]
```

### Step 2 — Why can't we directly doXθ?

Because θ is unknown.  
You know:

```text
Y = Xθ
```

But:

```text
θ =??
```

It is like:

```text
12 = 1m + c
```

You know result and x value.  
But m and c are missing.  
So first task is:  
find θ.

### Step 3 — Solve for θ using normal equation

Formula:

```text
θ = (X X) T −1 X Y T
```

#### Compute

```text
X T = [1 1 1 1 1 5]
1 2 3 4
```

T

### ComputeX X

```text
X X = T [ 5 15 55]
15
```

T

### ComputeX Y

```text
X Y = T [124 433]
```

#### Find inverse

```text
(X X) T −1 = 50 1 [ 55 −15 −15 5 ]
```

#### Compute θ

```text
θ = 50 1 [ 55 −15 −15 5 ] [124 433]
```

Result:

```text
θ = [5.7 6.3]
```

So:

```text
c = 5.7
m = 6.3
```

Final regression line:

```text
y = 6.3x + 5.7
```

### Step 4 — NOW we multiplyXθ

Now θ is known.  
So:

```text
1 1
1 2
Xθ = 1 3 [5.7 6.3]
1 4
1 5
```

Multiply row by column:  
First row:

```text
1(5.7) + 1(6.3) = 12
```

Second row:

```text
1(5.7) + 2(6.3) = 18.3
```

Third row:

```text
1(5.7) + 3(6.3) = 24.6
```

Fourth row:

```text
1(5.7) + 4(6.3) = 30.9
```

Fifth row:

```text
1(5.7) + 5(6.3) = 37.2
```

Predicted values:

```text
12
18.3
Y^ = 24.6
30.9
37.2
```

Actual:

```text
12
18
Y = 25
31
38
```

Very close.

### Main intuition

We have:

```text
Y = Xθ
```

But initially:  
- X = known  
- Y = known  
- θ = unknown  
So you cannot directly multiply because one matrix is missing.  
Instead:  
1. Use data to calculate θ.  
2. Then multiply:

```text
Y^ = Xθ
```

to get predictions.  
Think of it like:  
Known:

```text
12 = 1m + c
```

Unknown:  
m,c  
First solve m,c.  
Then plug them back.  
That is exactly what linear regression does.

## Using X Horizontally

Excellent question.  
You mean:  
Instead of writingXvertically like this:

```text
1 1
1 2
X = 1 3
1 4
1 5
```

what if we write it horizontally?  
Like:

```text
X = [1 2 3 4 5]
```

Right?  
The answer is: possible, but dimensions must match.

### Standard ML convention (vertical samples)

Usually in machine learning:  
Rows = observations/samples  
Columns = features  
Your data:  
5 samples, 1 feature.  
So:

```text
1
2
X = 3
4
5
```

After adding bias:

```text
1 1
1 2
X = 1 3
1 4
1 5
```

Dimension:

```text
5 × 2
```

(5 rows = 5 data points)  
Then:

```text
θ = [ c m]
```

Dimension:

```text
2 × 1
```

Multiplication works:

```text
(5 × 2)(2 × 1)
```

Result:

```text
5 × 1
```

gives one prediction per sample.

### If X is horizontal

Suppose:

```text
X = [1 2 3 4 5]
```

Dimension:

```text
1 × 5
```

Now try:

```text
Y = Xθ
```

But θ is:

```text
2 × 1
```

Multiplication:

```text
(1 × 5)(2 × 1)
```

Impossible.  
Because inner dimensions must match.  
5 ≠ 2.

### Can horizontal form still work?

You can use the transpose version.  
Write:

```text
X = [1 2 3 4 5]
```

and

```text
Y = [12 18 25 31 38]
```

as row vectors.  
Then use a different equation setup:

```text
Y = θ X T
```

instead of

```text
Y = Xθ
```

Example:

```text
θ T = [c m]
```

Bias-added X:

```text
1 1 1 1
X = [1 5]
1 2 3 4
```

Dimensions:

```text
(1 × 2)(2 × 5)
```

Result:

```text
1 × 5
```

Works.

### Simple intuition

Two equivalent styles exist.

#### Style 1 (common ML style)

Each row = one sample

```text
Y = Xθ
```

#### Style 2 (horizontal style)

Each column = one sample

```text
Y = θ X T
```

Both give same mathematics.  
People usually prefer vertical rows because datasets naturally look like:

| sample | feature1 | feature2 |
|---|---|---|
| 1 | 2 | 5 |
| 2 | 3 | 7 |
| 3 | 4 | 9 |

Rows = data points.  
So ML books mostly use vertical form.

## Layout Convention in Conventional ML

Not exactly.  
In conventional ML, usually:  
- X → vertical matrix  
- Y → vertical vector  
Both are typically stored vertically.  
Example with your data:

| x | y |
|---|---|
| 1 | 12 |
| 2 | 18 |
| 3 | 25 |
| 4 | 31 |
| 5 | 38 |

#### X matrix (vertical)

Add bias column:

```text
1 1
1 2
X = 1 3
1 4
1 5
```
