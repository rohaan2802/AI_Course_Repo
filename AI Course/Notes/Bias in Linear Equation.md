# Bias in Linear Equation

## Is c in y = mx + c the Bias?

In linear models, the c in:

```text
y = mx + c
```

can be called the bias term or intercept.  
Machine learning usually writes it as:

```text
y = wx + b
```

Here:

```text
m = w
c = b
```

So:

```text
y = mx + c
```

is the same idea as:

```text
y = wx + b
```

Meaning:  
- m / w = weight or slope  
- It controls how strongly  affects .

```text
x y
```

- c / b = bias or intercept  
- It shifts the line up or down.  
Example:

```text
y = 2x + 3
```

Here 3 is the bias/intercept.

```text
x = 0
```

When :

```text
y = 2(0) + 3 = 3
```

So the line starts from 3 on the y-axis.  
In multiple features:

```text
y = w 1 x 1 + w 2 x 2 + w 3 x 3 + b
```

Here b is the bias term.  
Important: This “bias” means mathematical bias/intercept, not unfairness or discrimination bias.

|  | Show more |
|---|---|

In the Linear Probability Model:

```text
Y i = β 0 + β 1 X i + u i
```

the term is the error term or disturbance term.

```text
u i
```

It means:  
= actual value −predicted value

```text
u i
```

So:

```text
u i = Y i − (β 0 + β 1 X i )
```

#### Simple meaning

The model predicts using , but prediction is not always perfect.

```text
Y i X i
```

So contains everything that affects but is not included in the model.

```text
u i Y i
```

For example, suppose:  
= whether a person buys a product

```text
Y i
```

= income

```text
X i
```

Then the model is:

```text
= + +
```

Y β β Income u

```text
i 0 1 i i
```

But buying a product does not depend only on income. It may also depend on: taste  
- age  
- advertisement  
- need  
- mood  
- family influence  
All these missing factors go into .

```text
u i
```

#### In Linear Probability Model

Usually is binary:

```text
Y i
Y i = 1
```

or

```text
Y i = 0
```

Example:  
= 1 if person buys

```text
Y i
```

= 0 if person does not buy

```text
Y i
```

The predicted value is:

```text
Y^i = β 0 + β 1 X i
```

In LPM, this predicted value is treated as a probability.  
So:

```text
Y^i = P(Y i = 1∣X i )
```

#### Example

Suppose model predicts:

```text
Y^i = 0.70
```

This means the model says:

```text
=
```

70% chance that Y 1

```text
i
```

Now if actual value is:

```text
Y i = 1
```

Then:

```text
u i = Y i − Y^i
u i = 1 −0.70
u i = 0.30
```

If actual value is:

```text
Y i = 0
```

Then:

```text
u i = 0 −0.70
u i = −0.70
```

#### Final simple answer

```text
u i
```

is the error term. It shows the difference between the actual outcome and the predicted probability.

```text
u i = Y i − (β 0 + β 1 X i )
```

- is the part of that the model cannot explain using .

```text
u i Y i X i
```

## The Error Term u and the Intercept β0

No, is not biasness.

```text
u i
```

In this equation:

```text
Y i = β 0 + β 1 X i + u i
```

### β

0

```text
β 0
```

is the intercept or bias term.  
It is like  in:

```text
c
y = mx + c
```

So:

```text
β 0 = c = b
X = 0
```

It tells the starting value of when .

```text
Y
```

### u

i

```text
u i
```

is the error or unexplained part.  
It shows how much the actual value differs from the predicted value.

```text
u i = Y i − Y^i
```

where:

```text
Y^i = β 0 + β 1 X i
```

#### Simple comparison

| Term | Meaning |
|---|---|
|  | bias/intercept |

β0

| Term | Meaning |
|---|---|
|  | slope/weight |

β1

|  | input/independent variable |
|---|---|

X  
i

|  | error/unexplained part |
|---|---|

u  
i

#### Easy example

```text
Y i = 2 + 0.5X i + u i
```

Here:

```text
β 0 = 2
```

This is the bias/intercept.

```text
β 1 = 0.5
```

This is the slope/weight.

```text
u i
```

is the mistake/error left after prediction.  
So final answer:  
is bias/intercept, and u is error term.

```text
β 0 i
```
