# Qualitative Response Models

## Qualitative Response Models: Full Explanation

The notes are about Qualitative Response Regression Models, especially binary response models like Linear Probability Model, Logit Model, Probit Model, and Tobit Model.  
In simple words:  
- Normal regression predicts numbers like income, marks, price, weight.  
- Qualitative response models predict choices, usually Yes/No, 1/0, success/failure.  
Example:  
Will a person buy a house?  
= 1  
No = 0  
Will a student attend college?  
= 1  
No = 0  
Will a woman enter the labour market?  
= 1  
No = 0  
So here the dependent variable is not a normal number. It is a category.

### 1. What is a Qualitative Response Model? Goal

We want to predict the probability of an event.  
For example:  
- What is the probability that a family owns a house?  
We do not directly predict “house” or “no house”.  
We predict:

```text
P(Y = 1)
```

Meaning:  
P(family owns a house)

### 2. Binary Dependent Variable

A binary variable has only two values:  
{1, if the event happens

```text
Y =
```

0, if the event does not happen  
Example from the notes:  
{1, if individual drives to work

```text
Y =
```

0, if individual uses bus  
Simple meaning:  
1 means “Yes”.  
0 means “No”.  
Roman Urdu:  
- Binary variable ka matlab hai sirf 2 options: haan ya nahi.

### 3. Why Do We Use 1 and 0?

Because probability becomes easy.  
If:

```text
Y = 1
```

then event happened.  
If:

```text
Y = 0
```

then event did not happen.  
Example:  
Suppose 100 people are asked:  
“Do you drive to work?”  
70 say yes.  
30 say no.  
Then:

```text
70
P(Y = 1) = = 0.70
100
30
P(Y = 0) = = 0.30
100
```

So probability of driving to work is 0.70.

### 4. Bernoulli Distribution

In the notes, this formula is written:

```text
f(y; p) = p (1 − y p) 1−y , y = 0, 1
```

This is called the Bernoulli probability function.  
It is used when the outcome is only 0 or 1.  
Here:

```text
p = P(Y = 1)
```

and

```text
1 −p = P(Y = 0)
```

#### Case 1: When

```text
y = 1
```

Put in formula:

```text
f(1; p) = p (1 − 1 p)1−1
f(1; p) = p (1 − 1 p)0
```

Anything power 0 is 1:

```text
(1 −p) = 0 1
```

So:

```text
f(1; p) = p
```

Meaning:

```text
P(Y = 1) = p
```

#### Case 2: When

```text
y = 0
```

Put :

```text
f(0; p) = p (1 − 0 p)1−0
f(0; p) = p (1 − 0 p)1
```

Again:

```text
p = 0 1
```

So:

```text
f(0; p) = 1 −p
```

Meaning:

```text
P(Y = 0) = 1 −p
```

### 5. Mean and Variance of Binary Variable

For Bernoulli variable:

```text
E(Y ) = p
Var(Y ) = p(1 −p)
```

Simple meaning:  
The average value of a binary variable equals its probability of success.  
Example:  
If probability of driving to work is:

```text
p = 0.70
```

then:

```text
E(Y ) = 0.70
```

Variance:

```text
Var(Y ) = p(1 −p)
Var(Y ) = 0.70(1 −0.70)
Var(Y ) = 0.70(0.30)
Var(Y ) = 0.21
```

### 6. Explanatory Variables

We use independent variables to explain the choice.  
Example from the notes:  
A person may drive to work or use bus.  
Possible explanatory variables:  
= commuting time by bus −commuting time by car

```text
X 1
```

If bus takes more time than car, the person is more likely to drive.  
Other possible variables:  
= cost of car −cost of bus

```text
X 2
```

= income

```text
X 3
```

= distance

```text
X 4
```

So model may ask:  
- How do time, cost, income, and distance affect the probability of driving to work?

### 7. Types of Qualitative Response Models

The notes list these:  
1. Linear Probability Model  
2. Logit Model  
3. Probit Model  
4. Tobit Model  
Also, the notes mention polychotomous/multicategory models.

### 8. Linear Probability Model

The Linear Probability Model is:

```text
Y i = β 0 + β 1 X i + u i
```

But since is 0 or 1, we interpret this as:

```text
Y i
P(Y i = 1∣X ) = i β 0 + β 1 X i
```

Simple meaning:  
- Probability is assumed to be a straight-line function of X.  
Example:  
Suppose:

```text
P(Y = 1∣X) = −0.20 + 0.03X
```

where:  
X = income in thousand rupees  
Question:  
If income is 30, what is probability of owning a house?  
Step 1:

```text
P = −0.20 + 0.03(30)
```

Step 2:

```text
P = −0.20 + 0.90
```

Step 3:

```text
P = 0.70
```

Final answer:

```text
P(Y = 1) = 0.70
```

So probability of owning house is 70%.

### Problem with Linear Probability Model

Probability must always be between 0 and 1.

```text
0 ≤P ≤1
```

But LPM can give values less than 0 or greater than 1.  
Example:

```text
P = −0.20 + 0.03X
```

If:

```text
X = 50
```

then:

```text
P = −0.20 + 0.03(50)
P = −0.20 + 1.50
P = 1.30
```

This is impossible because probability cannot be 130%.  
So LPM is easy, but not always correct.

### 9. Logit Model

This is the main model in your images.  
The logit model solves the LPM problem because it always gives probability between 0 and 1.  
The logit model is:

```text
1
P i = 1 + e−Z
```

i  
where:

```text
Z i = β 0 + β 1 X i
```

So:

```text
1
P i = 1 + e−(β +β X )
```

0 1 i  
This is called the logistic function.

### Simple Meaning

The logit model does not directly make probability a straight line.  
Instead, it makes log odds a straight line.  
That is why it is better than LPM.

### 10. UnderstandingP i

```text
P i
```

means:

```text
P(Y i = 1∣X i )
```

Example:  
If:

```text
Y = 1
```

means family owns house, then:  
= P(family owns house)

```text
P i
```

If:

```text
Y = 0
```

means family does not own house, then:

```text
=
```

1 −P P(family does not own house)

```text
i
```

### 11. Odds Ratio

The notes mention:

```text
P i
1 −P i
```

This is called odds.  
It compares probability of success with probability of failure.  
Example:  
Suppose:

```text
P i = 0.80
```

Then:

```text
1 −P i = 0.20
```

Odds:

```text
P i = 0.80
1 −P i 0.20
= 4
```

Meaning:  
The event is 4 times more likely to happen than not happen.  
Roman Urdu:  
- Odds ka matlab hai success aur failure ka comparison.

### 12. Logit Formula

The logit is:

```text
L i = ln (1 −P P i )
i
```

And in logit regression:

```text
L i = β 0 + β 1 X i
```

So:

```text
ln (1 −P P i ) = β 0 + β 1 X i
i
```

This means:  
- The log of odds is linear in X.  
This is very important for exams.

### 13. Derivation of Logit Model

Start with logistic probability:

```text
eZ i
P i = 1 + eZ
```

i  
Now failure probability:

```text
eZ i
1 −P i = 1 − 1 + eZ
```

i  
Take common denominator:

```text
1 + eZ eZ
```

i i

```text
1 −P i = 1 + eZ − 1 + eZ
```

i i

```text
1 + e Z −e Z
```

i i

```text
1 −P i = 1 + eZ
```

i

```text
1
1 −P i = 1 + eZ
```

i  
Now odds:

```text
P i
1 −P i
```

Put both values:

```text
eZ i
P i = 1+eZ i
1 −P i 1+eZ 1
```

i  
Dividing by a fraction means multiplying by its reciprocal:

```text
eZ i 1 + eZ i
= ×
1 + eZ 1
```

i  
Cancel:

```text
1 + eZ i
```

So:

```text
P i = eZ i
1 −P i
```

Now take natural log on both sides:

```text
ln (1 −P P i ) = ln(e ) Z i
i
```

Since:

```text
ln(e ) = Z i Z i
```

Therefore:

```text
ln (1 −P P i ) = Z i
i
```

And:

```text
Z i = β 0 + β 1 X i
```

So:

```text
ln (1 −P P i ) = β 0 + β 1 X i
i
```

This is the logit model.

### 14. Properties of Logit Model Property 1

As probability goes from 0 to 1, logit goes from:

```text
−∞ to  + ∞
```

Meaning:  
If probability is close to 0, log odds are very negative.  
If probability is close to 1, log odds are very positive.

### Property 2

The logit is linear in , but probability is not linear in .

```text
L i X X
```

So:

```text
L i = β 0 + β 1 X i
```

is linear.  
But:

```text
1
P i = 1 + e−(β +β X )
```

0 1 i  
is S-shaped.

### Property 3

LPM says:

```text
P i = β 0 + β 1 X i
```

Logit says:

```text
ln (1 −P P i ) = β 0 + β 1 X i
i
```

So the difference is:

| Model | What is linear? |
|---|---|
| LPM | Probability itself |
| Logit | Log odds |

### Property 4

If:

```text
β 1 > 0
```

then as increases, probability also increases.

```text
X
```

If:

```text
β 1 < 0
```

then as increases, probability decreases.

```text
X
```

### Property 5

If:

```text
P i > 0.5
```

we usually classify as:

```text
Y = 1
```

If:

```text
P i < 0.5
```

we usually classify as:

```text
Y = 0
```

### 15. Solved Example: Logit Model

Suppose:

```text
Z i = −4 + 0.08X i
```

where:  
= family income

```text
X i
```

Find probability of owning a house when:

```text
X i = 60
```

### Step 1: Write formula

```text
1
P i = 1 + e−Z
```

i

### Step 2: FindZ

i

```text
Z i = −4 + 0.08(60)
Z i = −4 + 4.8
Z i = 0.8
```

### Step 3: Put in probability formula

```text
1
P i = 1 + e−0.8
```

We know:

```text
e −0.8 ≈ 0.449
```

So:

```text
1
P i = 1 + 0.449
1
P i = 1.449
P i ≈ 0.69
```

Final answer:

```text
P i = 0.69
```

So probability of owning a house is about 69%.

### 16. Solved Example: Odds and Log Odds

Suppose:

```text
P = 0.75
```

Find odds and logit.

### Step 1: Find failure probability

```text
1 −P = 1 −0.75
1 −P = 0.25
```

### Step 2: Find odds

```text
P 0.75
=
1 −P 0.25
= 3
```

Odds are 3.  
Meaning:  
The event is 3 times more likely to happen than not happen.

### Step 3: Find logit

```text
P
L = ln (1 −P )
L = ln(3)
L ≈1.099
```

Final answer:

```text
L = 1.099
```

### 17. Solved Example: From Logit to Probability

Suppose:

```text
L = 2
```

Find probability.  
We know:

```text
P
L = ln (1 −P )
```

So:

```text
P
= eL
1 −P
P
= e2
1 −P
e ≈ 2 7.389
```

So:

```text
P
= 7.389
1 −P
```

Now solve:

```text
P = 7.389(1 −P)
P = 7.389 −7.389P
```

Bring terms together:

```text
P
P + 7.389P = 7.389
8.389P = 7.389
7.389
P =
8.389
P ≈0.881
```

Final answer:

```text
P = 0.881
```

So probability is 88.1%.  
Shortcut formula:

```text
eL
P =
1 + eL
```

### 18. Interpretation of Logit Coefficients

Suppose:

```text
L = −4 + 0.08X
```

Here:

```text
β 0 = −4
β 1 = 0.08
```

Meaning of :

```text
β 1
```

If increases by 1 unit, log odds increase by 0.08.

```text
X
```

Odds multiplier:

```text
e 0.08 = 1.083
```

This means:  
Odds increase by about 8.3%.  
Exam line:  
- A one-unit increase in increases the log odds by , holding other variables

```text
X β 1
```

- constant.

### 19. Estimation of Logit Coefficients

The notes say logit coefficients are estimated using Maximum Likelihood Estimation, not usually OLS.

### Why MLE?

Because is 0 or 1.

```text
Y
```

OLS is for continuous dependent variables.  
Logit uses probability, so MLE chooses coefficients that make the observed data most likely.

### Likelihood for one observation

If:

```text
Y i = 1
```

likelihood contribution is:

```text
P i
```

If:

```text
Y i = 0
```

likelihood contribution is:

```text
1 −P i
```

Combined formula:

```text
L = P Y (1 − P ) 1−Y
```

i i

```text
i i i
```

This is the same idea as Bernoulli formula.

### Example of likelihood

Suppose predicted probabilities are:

|  | Actual | Predicted |
|---|---|---|

Y P

| Person |  |  |
|---|---|---|
| 1 | 1 | 0.80 |
| 2 | 0 | 0.30 |
| 3 | 1 | 0.70 |

For person 1:

```text
Y = 1
```

Actual , so likelihood = 0.80.  
For person 2:

```text
Y = 0 1 −0.30 = 0.70
```

Actual , so likelihood = .  
For person 3:

```text
Y = 1
```

Actual , so likelihood = 0.70.  
Total likelihood:

```text
L = 0.80 × 0.70 × 0.70
L = 0.392
, β
```

MLE tries to choose so this likelihood becomes as large as possible.

```text
β 0 1
```

### 20. Prediction Rule

After estimating the model, we predict:

```text
P^i
```

Usually:  
If:

```text
P^i > 0.5
```

predict:

```text
Y^ = 1
```

If:

```text
P^i < 0.5
```

predict:

```text
Y^ = 0
```

Example:

```text
P^ = 0.72
```

Since 0.72 > 0.5:

```text
Y^ = 1
```

Meaning: predict the person owns a house.

### 21. Probit Model

The probit model is similar to logit.  
But instead of logistic function, it uses the normal distribution function.  
Formula:

```text
P i = P(Y i = 1∣X i ) = Φ(β 0 + β 1 X i )
```

Here:

```text
Φ
```

means standard normal cumulative distribution function.  
Simple meaning:  
- Probit also gives probability between 0 and 1, but it uses normal curve.

### Difference Between Logit and Probit

| Point | Logit | Probit |
|---|---|---|
| Function used | Logistic function | Normal CDF |
| Probability range | 0 to 1 | 0 to 1 |
| Shape | S-shaped | S-shaped |
| Interpretation | Odds/log odds are easy | Odds interpretation is not direct |
| Common use | Very common | Also common |

For most exams:  
- Logit and probit give very similar results. Logit is easier to interpret because of odds ratio.

### 22. Solved Example: Probit

Suppose:

```text
Z = −1 + 0.5X
```

and:

```text
X = 3
```

Find:

```text
P(Y = 1)
```

### Step 1: FindZ

```text
Z = −1 + 0.5(3)
Z = −1 + 1.5
Z = 0.5
```

### Step 2: Use normal table

```text
P = Φ(0.5)
```

From standard normal table:

```text
Φ(0.5) = 0.6915
```

Final answer:

```text
P = 0.6915
```

So probability is about 69.15%.

### 23. Tobit Model

Tobit model is used when dependent variable is limited or censored.  
Example:  
Spending on luxury goods:  
Some people spend 0.  
Others spend positive amount.  
So dependent variable is:

```text
Y ≥0
```

It cannot go below 0.  
Another example:  
Hours worked by women:  
Some women work 0 hours.  
Some work positive hours.  
So Tobit handles cases where many observations are stuck at a limit, usually 0.  
Simple exam line:  
- Tobit model is used when the dependent variable is censored or limited, for example when many values are zero.

### 24. Polychotomous / Multicategory Response Models

The notes mention models where dependent variable has more than two categories.  
Binary model:

```text
Y = 0 or 1
```

Multicategory model:

```text
Y = 1, 2, 3, 4, …
```

Example from politics:  
A voter may vote for:

```text
⎧1,
```

PMLN

```text
Y = ⎨ 2, PPP
⎩
3, PTI
```

This is not binary.  
This is multicategory.  
For this, we use:  
- Multinomial logit model  
- Multinomial probit model

### 25. Most Important Exam Comparisons LPM vs Logit

| Feature | LPM | Logit |
|---|---|---|
| Dependent variable |  |  |

1  
P = β P =  
Main formula β X  
0 1 1+e−Z

| Probability range | Can be below 0 or above 1 | Always between 0 and 1 |
|---|---|---|
| Shape | Straight line | S-shaped |
| Estimation | OLS | MLE |
| Interpretation | Simple but weak | Better and more reliable |

### Logit vs Probit

| Feature | Logit | Probit |
|---|---|---|
| Distribution | Logistic | Normal |

1 Φ(Z)

Formula  
1+e−Z

| Odds interpretation | Easy | Not easy |
|---|---|---|
| Results | Usually similar to probit | Usually similar to logit |

### 26. Full Solved Practice Question Question

A researcher wants to study whether a family owns a house or not. The dependent variable is:  
{1, if family owns house

```text
Y =
```

0, otherwise  
The estimated logit model is:

```text
L = −3 + 0.06X
```

where is income.

```text
X
```

Find the probability that a family owns a house when:

```text
X = 50
```

### Step 1: Identify the model

This is logit because:

```text
L = β 0 + β 1 X
```

### Step 2: Calculate logit value

```text
L = −3 + 0.06(50)
L = −3 + 3
L = 0
```

### Step 3: Convert logit into probability

Formula:

```text
1
P =
1 + e−L
L = 0
```

Put :

```text
1
P =
1 + e0
```

We know:

```text
e = 0 1
```

So:

```text
1
P =
1 + 1
1
P =
2
P = 0.5
```

Final answer:

```text
P = 0.50
```

So probability of owning a house is 50%.

### 27. Another Practice Question Question

Suppose probability of success is:

```text
P = 0.60
```

Find:  
1. Probability of failure  
2. Odds  
3. Logit

### Step 1: Failure probability

```text
1 −P = 1 −0.60
= 0.40
```

### Step 2: Odds

```text
P 0.60
=
1 −P 0.40
= 1.5
```

### Step 3: Logit

```text
L = ln(1.5)
L = 0.405
```

Final answer:

```text
1 −P = 0.40
```

Odds = 1.5  
Logit = 0.405

### 28. How Questions Can Come in Exam

They may ask:

### Theory Questions

Explain qualitative response models.  
Define binary dependent variable.  
What is linear probability model?  
What are limitations of LPM?  
Explain logit model.  
Derive the logit transformation.  
Differentiate logit and probit.  
What is Tobit model?  
What are polychotomous response models?

### Numerical Questions

They may give:

```text
L = β 0 + β 1 X
```

and ask you to find probability.  
They may give probability and ask for odds.  
They may give odds and ask for probability.  
They may give and ask for logit.

```text
P
```

They may give income and coefficients and ask whether prediction is 0 or 1.

### 29. Exam Shortcut Sheet

Remember these formulas:

```text
P(Y = 1) = p
P(Y = 0) = 1 −p
E(Y ) = p
Var(Y ) = p(1 −p)
P
```

Odds =

```text
1 −P
P
(1 −P )
```

Logit = ln

```text
L = β 0 + β 1 X
1
P =
1 + e−L
```

or:

```text
eL
P =
1 + eL
```

Both probability formulas are same.

### 30. Baby Explanation

Imagine a question:  
“Will a person buy a house?”  
Answer is only:  
or No.  
We write:  
= 1  
No = 0  
Now we do not just guess.  
We use income, age, education, job, family size, etc.  
The model gives:

```text
P(Y = 1)
```

Meaning:  
“How much chance is there that the person will buy a house?”  
If probability is high, predict yes.  
If probability is low, predict no.  
LPM draws a straight line, but sometimes gives impossible probability.  
Logit and probit fix this by keeping probability between 0 and 1.

### 31. Common Mistakes

Do not write probability greater than 1.  
Wrong:

```text
P = 1.25
```

: Probability must be between 0 and 1.  
Do not confuse odds with probability.  
Probability:

```text
P = 0.80
```

Odds:

```text
0.80
= 4
0.20
```

Do not say directly increases probability by fixed amount in logit.

```text
β 1
```

In logit, increases log odds, not probability directly.

```text
β 1
```

Do not use OLS as the main estimation method for logit.  
Logit uses MLE.

### 32. One-Line Exam Definitions

Qualitative response model:  
A regression model where the dependent variable is categorical, such as yes/no or success/failure.  
Binary response model:  
A model where the dependent variable takes only two values, 0 and 1.  
Linear Probability Model:  
A model where probability is assumed to be a linear function of explanatory variables.  
Logit model:  
A binary response model where log odds are a linear function of explanatory variables.  
Probit model:  
A binary response model that uses the normal cumulative distribution function to model probability.  
Tobit model:  
A model used when the dependent variable is censored or limited.  
Odds:  
The ratio of probability of success to probability of failure.

```text
P
```

Odds =

```text
1 −P
```

Logit:  
The natural log of odds.

```text
P
(1 −P )
```

Logit = ln

## Formula List for the Exam

Here is the formula list you should remember for exam for Qualitative Response Models / Logit Model.

### 1. Binary Variable Formula

{1, if event happens

```text
Y =
```

0, if event does not happen  
Example:  
{1, owns house

```text
Y =
```

0, does not own house

### 2. Probability of Success and Failure

```text
P(Y = 1) = p
P(Y = 0) = 1 −p
```

Remember:

```text
P(Y = 1) + P(Y = 0) = 1
```

### 3. Bernoulli Probability Function

```text
f(y; p) = p (1 − y p)1−y
```

where:

```text
y = 0, 1
y = 1
```

If :

```text
f(1; p) = p
y = 0
```

If :

```text
f(0; p) = 1 −p
```

### 4. Mean and Variance of Binary Variable

```text
E(Y ) = p
Var(Y ) = p(1 −p)
```

### 5. Linear Probability Model

```text
Y i = β 0 + β 1 X i + u i
```

Probability form:

```text
P(Y i = 1∣X ) = i β 0 + β 1 X i
```

For multiple variables:

```text
P(Y i = 1∣X i ) = β 0 + β 1 X 1i + β 2 X 2i + ... + β k X ki
```

Important limitation:

```text
0 ≤P i ≤ 1
```

But LPM can sometimes give:

```text
P i < 0
```

or

```text
P i > 1
```

That is why logit/probit are used.

### 6. Logit Model Main Formula

```text
1
P i = 1 + e−Z
```

i  
where:

```text
Z i = β 0 + β 1 X i
```

So full formula:

```text
1
P i = 1 + e−(β +β X )
```

0 1 i  
Alternative same formula:

```text
eZ i
P i = 1 + eZ
```

i

### 7. Failure Probability in Logit

```text
1
1 −P i = 1 + eZ
```

i

### 8. Odds Formula

```text
P i
```

Odds =

```text
1 −P i
```

In logit model:

```text
P i = eZ i
1 −P i
```

Meaning:

```text
+β
```

Odds = eβ X  
0 1 i

### 9. Logit / Log-Odds Formula

```text
L i = ln (1 −P P i )
i
```

And:

```text
L i = Z i
```

So:

```text
ln (1 −P P i ) = β 0 + β 1 X i
i
```

This is the most important formula.

### 10. From Logit Back to Probability

If logit value is given:

```text
L
1
P =
1 + e−L
```

or:

```text
eL
P =
1 + eL
```

Both are same.

### 11. From Probability to Odds

```text
P
```

Odds =

```text
1 −P
```

Example:

```text
P = 0.80
0.80
=
```

Odds = 4

```text
0.20
```

### 12. From Odds to Probability

If odds are given:  
Odds

```text
P =
```

1 + Odds  
Example:  
Odds = 4

```text
4 4
P = = = 0.80
1 + 4 5
```

### 13. From Probability to Logit

```text
P
(1 −P )
```

Logit = ln  
Example:

```text
P = 0.75
(0.25 0.75)
```

Logit = ln  
Logit = ln(3)

### 14. Odds Ratio for Coefficient

For coefficient :

```text
β 1
```

Odds Ratio = eβ1  
Interpretation:  
If:

```text
e β 1 > 1
```

odds increase.  
If:

```text
e β 1 < 1
```

odds decrease.  
Percentage change in odds:

```text
(e β − 1) × 100
```

1

### 15. Prediction Rule

If:

```text
P^i > 0.5
```

then:

```text
Y^i = 1
```

If:

```text
P^i < 0.5
```

then:

```text
Y^i = 0
```

Usually:

```text
0.5
```

is used as cut-off value.

### 16. Probit Model Formula

```text
P i = P(Y i = 1∣X i ) = Φ(Z i )
```

where:

```text
Z i = β 0 + β 1 X i
```

So:

```text
P i = Φ(β 0 + β 1 X i )
```

Here:

```text
Φ
```

means standard normal cumulative distribution function.

### 17. Maximum Likelihood Formula

For one observation:

```text
L = P Y (1 − P ) 1−Y
```

i i

```text
i i i
```

For all observations:

```text
n
L = ∏ P Y (1 − P ) 1−Y
```

i i

```text
i i
i=1
```

Log-likelihood:

```text
n
ln L = ∑ Y [ i ln(P i ) + (1 −Y i ) ln(1 −P i ] )
i=1
```

This is used to estimate logit/probit coefficients.

### 18. Tobit Model Basic Form

Latent variable:

```text
Y i ∗ = β 0 + β 1 X i + u i
```

Observed variable:

```text
Y i = {Y 0, i ∗ , if Y if Y i i ∗ ∗ > 0 ≤0
```

Use Tobit when the dependent variable is censored, usually at 0.

### 19. Most Important Exam Formula Set

Memorize these first:

```text
P(Y = 1) = p
P(Y = 0) = 1 −p
E(Y ) = p
Var(Y ) = p(1 −p)
1
P i = 1 + e−Z
```

i

```text
Z i = β 0 + β 1 X i
P i
```

Odds =

```text
1 −P i
P i
(1 −P )
```

Logit = ln

```text
i
ln (1 −P P i ) = β 0 + β 1 X i
i
eL
P =
1 + eL
```

Odds Ratio = eβ1

```text
Y^ = 1 if P^ > 0.5
Y^ = 0 if P^ < 0.5
```

### 20. Super Short Memory Trick

Remember this chain:

```text
Z = β 0 + β 1 X
1
P =
1 + e−Z
P
```

Odds =

```text
1 −P
```

Logit = ln(Odds)  
So:

```text
P
(1 −P )
```

Logit = ln = Z  
This is the main heart of the topic.

## Step-by-Step Problem Solving

The topic is Logistic Regression.  
Logistic regression is used when the answer is only two classes:  
y = 1 ⇒Yes / Spam / Smoker  
y = 0 ⇒No / Not spam / Non-smoker  
It predicts a probability:

```text
P(y = 1)
```

### 1. Why Sigmoid Function is Used?

The sigmoid function is:

```text
1
σ(x) =
1 + e−x
```

It is used because it converts any value into a number between 0 and 1.  
In logistic regression, the model first gives a linear score:

```text
z = β 0 + β 1 x 1 + β 2 x 2
```

This  can be any number:

```text
z
−∞ to  + ∞
```

But probability must be between:

```text
0 ≤P ≤1
```

So we pass  through sigmoid:

```text
z
1
P =
1 + e−z
```

Simple meaning:  
- Sigmoid changes any big or small number into probability.  
Example:  
If:

```text
z = 5
```

then:

```text
1
P = = 0.993
1 + e−5
```

So probability is very high.  
If:

```text
z = −5
```

then:

```text
1
P = = 0.0067
1 + e5
```

So probability is very low.

### 2. Derivative of Sigmoid Function

We have to prove:

```text
dσ(x)
= σ(x)(1 −σ(x))
dx
```

Given:

```text
1
σ(x) =
1 + e−x
```

Rewrite it as power form:

```text
σ(x) = (1 + e −x −1 )
```

Now differentiate:

```text
dσ(x) = d (1 + e −x −1 )
dx dx
```

Use chain rule.  
If:

```text
u = 1 + e−x
```

then:

```text
σ(x) = u−1
u−1
```

Derivative of is:

```text
−u −2 du
dx
```

Now:

```text
du = d (1 + e −x )
dx dx
```

Derivative of 1 is 0.

```text
e−x
```

Derivative of is:

```text
−e−x
```

So:

```text
du
= −e−x
dx
```

Now put back:

```text
dσ(x) = −(1 + e −x −2 ) (−e −x )
dx
```

Negative times negative becomes positive:

```text
dσ(x) e−x
=
dx (1 + e −x 2 )
```

Now we need to show this equals:

```text
σ(x)(1 −σ(x))
```

We know:

```text
1
σ(x) =
1 + e−x
```

Now find:

```text
1 −σ(x)
1
1 −σ(x) = 1 −
1 + e−x
```

Take common denominator:

```text
1 + e−x 1
1 −σ(x) = −
1 + e−x 1 + e−x
1 + e −x −1
1 −σ(x) =
1 + e−x
e−x
1 −σ(x) =
1 + e−x
```

Now multiply:

```text
σ(x)(1 −σ(x))
1 e−x
= ×
1 + e−x 1 + e−x
e−x
=
(1 + e −x 2 )
```

This is same as derivative.  
Therefore:

```text
dσ(x)
= σ(x)(1 −σ(x))
dx
```

### 3. Inverse of Sigmoid is Logit Function

We have to prove:

```text
σ −1 (p) = log (1 −p p )
```

Start with:

```text
1
p =
1 + e−x
```

Now solve for .

```text
x
```

Step 1:

```text
p(1 + e −x ) = 1
```

Step 2:

```text
p + pe −x = 1
```

Step 3:

```text
pe −x = 1 −p
```

Step 4:

```text
e −x = 1 −p
p
```

Now take natural log:

```text
ln(e −x ) = ln ( 1 −p)
p
```

Since:

```text
ln(e −x ) = −x
```

So:

```text
−x = ln ( 1 −p)
p
−1
```

Multiply both sides by :

```text
x = −ln ( 1 −p)
p
```

Using log rule:

```text
p
−ln ( 1 −p) = ln (1 −p )
p
```

Therefore:

```text
p
x = ln (1 −p )
```

So:

```text
σ −1 (p) = ln (1 −p p )
```

This is called the logit function.

### 4. Main Logistic Regression Model

The model is:

```text
1
P(y = 1∣x) =
1 + e−z
```

where:

```text
z = β 0 + β 1 x 1 + β 2 x 2
```

In this example:

```text
β 0 = −2
β 1 = 0.5
β 2 = 0.1
```

So:

```text
z = −2 + 0.5x 1 + 0.1x 2
```

And:

```text
1
P(y = 1∣x) =
1 + e−(−2+0.5x +0.1x )
```

1 2  
Here:  
= keyword frequency score

```text
x 1
```

= sender reputation score

```text
x 2
```

y = 1 ⇒spam  
y = 0 ⇒not spam

### 5. Classification Rule

Usually:

```text
P > 0.5 ⇒y = 1
P < 0.5 ⇒y = 0
```

So for spam email:  
P > 0.5 ⇒Spam  
P < 0.5 ⇒Not spam

### 6. Example 1 Part i

Question:  
If probability is:

```text
P = 0.87
```

and threshold is:

```text
0.5
```

how will the email be classified?  
Since:

```text
0.87 > 0.5
```

Therefore:

```text
y^ = 1
```

Final answer:  
Email is classified as spam.

### 7. Example 1 Part ii

Question:  
Calculate probability for:

```text
x 1 = 6
x 2 = 40
```

Model:

```text
z = −2 + 0.5x 1 + 0.1x 2
```

Step 1: Put values.

```text
z = −2 + 0.5(6) + 0.1(40)
```

Step 2: Multiply.

```text
0.5(6) = 3
0.1(40) = 4
```

Step 3:

```text
z = −2 + 3 + 4
z = 5
```

Now use sigmoid:

```text
1
P =
1 + e−z
1
P =
1 + e−5
```

We know:

```text
e −5 ≈ 0.0067
```

So:

```text
1
P =
1 + 0.0067
1
P =
1.0067
P ≈0.9933
```

Final answer:

```text
P = 0.9933
```

Meaning:  
99.33% chance that email is spam  
Since:

```text
0.9933 > 0.5
```

the email is classified as spam.

### 8. Example 1 Part iii: Odds to Probability

Question:  
Odds of being spam are:

```text
7 : 3
```

This means:  
success : failure = 7 : 3  
Probability formula from odds:  
success

```text
P =
```

success + failure  
So:

```text
7
P =
7 + 3
7
P =
10
P = 0.7
```

Final answer:

```text
P = 0.7
```

Meaning:  
70% probability of being spam

### 9. Example 1 Part iv: Compute Probability for Each Email

Given data:

|  | Actual |
|---|---|

x1 x2 y

| Email |  |  |  |
|---|---|---|---|
| 1 | 1 | 17 | 0 |
| 2 | 2 | 25 | 0 |
| 3 | 3 | 40 | 1 |
| 4 | 4 | 35 | 1 |

Model:

```text
z = −2 + 0.5x 1 + 0.1x 2
1
P =
1 + e−z
```

### Email 1

```text
x 1 = 1, x 2 = 17
z = −2 + 0.5(1) + 0.1(17)
z = −2 + 0.5 + 1.7
z = 0.2
```

Now:

```text
1
P =
1 + e−0.2
P ≈0.5498
```

So Email 1 has:  
54.98% chance of spam

### Email 2

```text
x 1 = 2, x 2 = 25
z = −2 + 0.5(2) + 0.1(25)
z = −2 + 1 + 2.5
z = 1.5
```

Now:

```text
1
P =
1 + e−1.5
P ≈0.8176
```

So Email 2 has:  
81.76% chance of spam

### Email 3

```text
x 1 = 3, x 2 = 40
z = −2 + 0.5(3) + 0.1(40)
z = −2 + 1.5 + 4
z = 3.5
```

Now:

```text
1
P =
1 + e−3.5
P ≈0.9707
```

So Email 3 has:  
97.07% chance of spam

### Email 4

```text
x 1 = 4, x 2 = 35
z = −2 + 0.5(4) + 0.1(35)
z = −2 + 2 + 3.5
z = 3.5
```

Now:

```text
1
P =
1 + e−3.5
P ≈0.9707
```

So Email 4 has:  
97.07% chance of spam

### Final Table

z P

| Email | Prediction |  |  |
|---|---|---|---|
| 1 | 0.2 | 0.5498 | Spam |
| 2 | 1.5 | 0.8176 | Spam |
| 3 | 3.5 | 0.9707 | Spam |
| 4 | 3.5 | 0.9707 | Spam |

### 10. Most Uncertain Email

The model is most uncertain when probability is closest to:

```text
0.5
```

Because 0.5 means model is confused.  
Compare probabilities:

```text
0.5498, 0.8176, 0.9707, 0.9707
```

Closest to 0.5 is:

```text
0.5498
```

So the most uncertain email is:  
Email 1

### 11. Example 1 Part v: Change for Email 2 x 2

Question:  
For Email 2, changes from 25 to 40.

```text
x 2
```

Email 2 originally:

```text
x 1 = 2
```

New:

```text
x 2 = 40
```

Model:

```text
z = −2 + 0.5x 1 + 0.1x 2
```

Put values:

```text
z = −2 + 0.5(2) + 0.1(40)
z = −2 + 1 + 4
z = 3
```

Now probability:

```text
1
P =
1 + e−3
e −3 ≈ 0.0498
1
P =
1 + 0.0498
1
P =
1.0498
P ≈0.9526
```

Old probability was:

```text
0.8176
```

New probability is:

```text
0.9526
```

Difference:

```text
0.9526 −0.8176 = 0.135
```

So probability increased by:

```text
13.5%
```

Classification before:  
0.8176 > 0.5 ⇒Spam  
Classification after:  
0.9526 > 0.5 ⇒Spam  
Final answer:  
The probability increases, but the classification remains spam.

### 12. Example 1 Part vi: Log-Likelihood

This is slightly difficult, but important.  
Formula:

```text
n
ℓ(β) = ∑ y [ i ln(p i ) + (1 −y i ) ln(1 −p i ] )
i=1
```

Simple meaning:  
- Log-likelihood checks how well the model fits the actual data.

```text
y = 1
```

If actual , we use:

```text
ln(p i )
y = 0
```

If actual , we use:

```text
ln(1 −p i )
```

Given probabilities:  
Actualy pi

| Email |  |  |
|---|---|---|
| 1 | 0 | 0.5498 |
| 2 | 0 | 0.8176 |
| 3 | 1 | 0.9707 |
| 4 | 1 | 0.9707 |

### Email 1

Actual:

```text
y = 0
```

So use:

```text
ln(1 −p)
ln(1 −0.5498)
= ln(0.4502)
≈−0.7981
```

### Email 2

Actual:

```text
y = 0
```

So:

```text
ln(1 −0.8176)
= ln(0.1824)
≈−1.7017
```

### Email 3

Actual:

```text
y = 1
```

So use:

```text
ln(p)
ln(0.9707)
≈−0.0298
```

### Email 4

Actual:

```text
y = 1
```

So:

```text
ln(0.9707)
≈−0.0298
```

### Total Log-Likelihood

```text
ℓ= −0.7981 −1.7017 −0.0298 −0.0298
ℓ≈−2.5594
```

Final answer:

```text
ℓ≈−2.5594
```

Simple meaning:  
- Larger log-likelihood is better. In log-likelihood, values are often negative. Less negative means better.  
For example:  
−1.5 is better than  −2.5

### 13. Example 2: Smoking Data

Now the second example studies whether a person is a smoker or non-smoker.  
Dependent variable:  
{1, smoker  
Smoke =  
0, non-smoker  
Independent variables:  
Age = age in years  
Educ = years of education  
Income = family income  
Pcigs = price of cigarettes  
The model is:

```text
1
```

P(Smoke = 1) =

```text
1 + e−z
```

where:  
z = β + Age + Educ + Income +  
β β β β Pcigs

```text
0 1 2 3 4
```

### 14. How to Interpret Coefficients

In logistic regression, coefficients affect log odds, not direct probability.  
The logit model is:

```text
P
ln (1 −P ) = β 0 + β 1 X 1 + β 2 X 2 + ⋯
```

So if a coefficient is positive:

```text
β > 0
```

then probability usually increases.  
If a coefficient is negative:

```text
β < 0
```

then probability usually decreases.

### 15. Interpretation of Age

The notes say age has a negative coefficient.  
That means:  
- As age increases, probability of smoking decreases.  
Simple meaning:  
Older people are less likely to smoke, according to this model.  
In exam language:  
- Holding other variables constant, an increase in age decreases the log odds of being a smoker.

### 16. Interpretation of Education

Education also has a negative coefficient.  
That means:  
- More educated people are less likely to smoke.  
If education coefficient is about:

```text
−0.09
```

then odds ratio is:

```text
e−0.09
≈0.914
```

This means odds become about 0.914 times the previous odds.  
Percentage change:

```text
(0.914 −1) × 100
= −8.6%
```

So one extra year of education decreases the odds of smoking by about:

```text
8.6%
```

Simple exam line:  
- One additional year of education reduces the odds of smoking by approximately 8.6%, holding other variables constant.

### 17. Interpretation of Income

The notes say income is not very important statistically.  
If p-value is greater than 0.05:  
p-value > 0.05  
then variable is usually called insignificant.  
Simple meaning:  
- Income may not have a strong effect on smoking in this data.

### 18. Interpretation of Cigarette Price

The cigarette price coefficient is negative.  
That means:  
- If cigarette price increases, probability of smoking decreases.  
Simple meaning:  
If cigarettes become expensive, fewer people smoke.  
Exam line:  
- Holding other variables constant, an increase in cigarette price decreases the log odds of being a smoker.

### 19. What is p-value in the Table?

The table contains p-values.  
Rule:  
p-value < 0.05 ⇒significant  
p-value > 0.05 ⇒not significant  
Significant means:  
- The variable has a statistically meaningful effect.  
Not significant means:  
- The variable may not have a reliable effect.

### 20. Example 2: Probability Calculation

The notes calculate probability for a person with:

```text
Age = 28
```

Educ = 15  
Income = 12500  
Pcigs = 60.0  
After substituting these values into the model, the notes get:

```text
z = −0.4935
```

Now use logistic formula:

```text
1
P =
1 + e−z
```

Put:

```text
z = −0.4935
1
P =
1 + e−(−0.4935)
```

Since:

```text
−(−0.4935) = 0.4935
```

So:

```text
1
P =
1 + e0.4935
```

Now:

```text
e 0.4935 ≈ 1.638
```

So:

```text
1
P =
1 + 1.638
1
P =
2.638
P ≈0.3782
```

Final answer:

```text
P = 0.3782
```

Meaning:

```text
37.82%
```

The probability that this person is a smoker is about:

```text
38%
```

Since:

```text
0.3782 < 0.5
```

the person is classified as:  
Non-smoker

### 21. Second Probability Calculation

The notes also calculate for another person:

```text
Age = 63
```

Educ = 10  
Income = 20000  
Pcigs = 60.8  
After substituting into the model, the notes get approximately:

```text
z = −0.7362
```

Now use:

```text
1
P =
1 + e−z
```

Put:

```text
z = −0.7362
1
P =
1 + e−(−0.7362)
1
P =
1 + e0.7362
```

Now:

```text
e 0.7362 ≈ 2.088
```

So:

```text
1
P =
1 + 2.088
1
P =
3.088
P ≈0.3227
```

Final answer:

```text
P = 0.3227
```

Meaning:

```text
32.27%
```

Since:

```text
0.3227 < 0.5
```

the person is classified as:  
Non-smoker

### 22. Important Difference: Probability vs Odds vs Logit Probability

Probability is chance of event:

```text
P
```

Example:

```text
P = 0.80
```

means 80% chance.

### Odds

Odds compare success with failure:

```text
P
```

Odds =

```text
1 −P
```

Example:

```text
P = 0.80
0.80
```

Odds = = 4

```text
0.20
```

Meaning:  
Success is 4 times more likely than failure.

### Logit

Logit is log of odds:

```text
P
(1 −P )
```

Logit = ln  
In logistic regression:  
Logit = z  
So:

```text
P
ln (1 −P ) = β 0 + β 1 X 1 + β 2 X 2 + ⋯
```

### 23. Most Important Exam Formulas from These Pages

Memorize these:

```text
1
σ(x) =
1 + e−x
dσ(x)
= σ(x)(1 −σ(x))
dx
σ −1 (p) = ln (1 −p p )
z = β 0 + β 1 x 1 + β 2 x 2 + ⋯+ β k x k
1
P(y = 1∣x) =
1 + e−z
ez
P(y = 1∣x) =
1 + ez
P
```

Odds =

```text
1 −P
P
(1 −P )
```

Logit = ln  
Odds

```text
P =
```

1 + Odds  
Odds = ez  
Odds Ratio = eβ

```text
n
ℓ(β) = ∑ y [ i ln(p i ) + (1 −y i ) ln(1 −p i ] )
i=1
```

Classification rule:

```text
P > 0.5 ⇒y = 1
P < 0.5 ⇒y = 0
```

### 24. Common Exam Questions

They can ask:  
Why sigmoid is used?  
Because it converts any real number into probability between 0 and 1.  
Find derivative of sigmoid.  
Answer:

```text
σ (x) = ′ σ(x)(1 −σ(x))
```

Find inverse of sigmoid.  
Answer:

```text
σ −1 (p) = ln (1 −p p )
```

Calculate probability using logistic regression.  
First calculate:

```text
z = β 0 + β 1 x 1 + β 2 x 2
```

Then:

```text
1
P =
1 + e−z
```

Classify using threshold 0.5.  
If probability greater than 0.5, predict 1.  
If probability less than 0.5, predict 0.  
Interpret coefficient.  
Positive coefficient means probability increases.  
Negative coefficient means probability decreases.  
But proper logistic regression wording:  
- A coefficient changes the log odds, not probability directly.

### 25. Baby Explanation

Logistic regression works like this:  
First it calculates a score:

```text
z = β 0 + β 1 x 1 + β 2 x 2
```

This score can be big, small, positive, or negative.  
Then sigmoid converts it into probability:

```text
1
P =
1 + e−z
```

If probability is high, model says:

```text
y = 1
```

If probability is low, model says:

```text
y = 0
```

For spam:  
y = 1 ⇒spam  
For smoking:  
y = 1 ⇒smoker  
That is the whole idea.

## When z Becomes 0 in P

```text
z = 0
```

If , then in logistic regression:

```text
1
P =
1 + e−z
```

Put:

```text
z = 0
1
P =
1 + e−0
```

Now:

```text
e = 0 1
```

So:

```text
1
P =
1 + 1
1
P =
2
P = 0.5
```

So when:

```text
z = 0
```

then:

```text
P = 0.5
```

Meaning:  
- The model is exactly 50% sure.  
- It is confused between class 0 and class 1.  
For classification:

```text
P = 0.5
```

is the boundary point.  
Usually:

```text
P > 0.5 ⇒y = 1
P < 0.5 ⇒y = 0
```

If exactly:

```text
P = 0.5
```

then teacher/software may decide by rule. Some use:

```text
P ≥0.5 ⇒y = 1
```

Some use:

```text
P > 0.5 ⇒y = 1
```

So in exam, write:

```text
z = 0 P = 0.5
```

- When , , so the observation lies on the decision boundary. Classification depends on the chosen threshold rule.
