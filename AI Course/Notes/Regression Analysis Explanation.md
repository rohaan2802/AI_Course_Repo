# Regression Analysis Explanation

## Regression Analysis: Full Explanation

definitions, model setup, matrix form, assumptions, formulas, solved house-price example, parameter testing, and what to memorize.  
It covers Regression Analysis, especially Multiple Linear Regression Model using Matrix Approach, its assumptions, least- squares formulas, coefficient of determination, and testing parameters using t- test / p-value / confidence interval.

### 1. Big Idea: What is Regression?

Regression means:  
We use one or more variables to predict another variable.  
Example:  
House price depends on:  
- number of bedrooms  
- number of baths  
- location  
- size  
- etc.  
So regression helps us write an equation like:  
House Price = base price + effect of bedrooms + effect of baths  
In the notes, regression is defined as a statistical technique for studying and modeling the relationship between variables.  
Simple meaning:  
Regression tells how Y changes when X changes.  
Roman Urdu:  
Regression ka kaam hota hai predict karna: agar X change ho, to Y kitna change hoga.

### 2. Dependent and Independent Variables

In regression, there are two types of variables.

### Dependent Variable

This is the variable we want to predict.  
It is usually called:

```text
Y
```

Example:  
Y = house price

### Independent Variable

These are the variables used to predict .

```text
Y
```

They are called:

```text
X 1 , X 2 , X 3 , … , X k
```

Example:  
= number of bedrooms

```text
X 1
```

= number of baths

```text
X 2
```

Simple meaning:  
Y is the answer. X variables are the reasons.

### 3. Simple Regression vs Multiple Regression Simple Linear Regression

Only one independent variable.

```text
Y = β 0 + β 1 X + ϵ
```

Example:  
Price = β + (bedrooms) +

```text
0 β 1 ϵ
```

### Multiple Linear Regression

More than one independent variable.

```text
Y = β 0 + β 1 X 1 + β 2 X 2 + ⋯+ β k X k + ϵ
```

Example:  
Price = β + (bedrooms) + (baths) +

```text
0 β 1 β 2 ϵ
```

The notes say regression is simple if there is one independent variable and multiple if there is more than one independent variable.

### 4. Multiple Linear Regression Model

The general model is:

```text
Y i = β 0 + β 1 X i1 + β 2 X i2 + ⋯+ β k X ik + ϵ i
```

Meaning of each symbol:

| Symbol | Meaning |
|---|---|
|  | dependent variable value for observation |

Y i  
i

|  | value of first independent variable for observation |
|---|---|

X i  
i1

|  | value of second independent variable for observation |
|---|---|

X i  
i2

|  | intercept / constant |
|---|---|

β0

|  | effect of | on |
|---|---|---|

β X1 Y  
1

|  | effect of | on |
|---|---|---|

β X2 Y  
2

|  | error term |
|---|---|

ϵ  
i

|  | observation number |
|---|---|

i

|  | number of independent variables |
|---|---|

k

|  | number of observations |
|---|---|

n  
Baby meaning:  
For every row of data:  
Y = starting value + effect of X + effect of X + error

```text
1 2
```

### 5. What is Error Term ? ϵ

The error term means:  
The difference between actual value and the value predicted by the model.  
Because real life is never perfectly predicted.  
Example:  
Actual house price:

```text
307500
```

Predicted house price:

```text
308100
```

Error:

```text
e = y − y^
e = 307500 −308100 = −600
```

Meaning:  
The model predicted $600 more than the actual price.  
Roman Urdu:  
Error wo difference hai jo actual answer aur predicted answer ke darmiyan hota hai.

### 6. Matrix Form of Regression

Instead of writing many equations one by one, we write regression in matrix form:

### Y = XB + E

1.0

b  
Meaning:

| Symbol | Meaning |
|---|---|
|  | column vector of actual dependent variable values |

Y

|  | data matrix of independent variables |
|---|---|

X

|  | vector of regression coefficients |
|---|---|

B

|  | vector of error terms |
|---|---|

E  
For example:

```text
y 1
Y = y 2
y 3
1 x 11 x 12
X = 1 x 21 x 22
1 x 31 x 32
β 0
B = β 1
β 2
e 1
E = e 2
e 3
```

Important:  
The first column of is always 1 because of , the intercept.

```text
X β0
```

### 7. Why First Column of X is 1?

Regression equation:

```text
Y = β 0 + β 1 X 1 + β 2 X 2
```

In matrix form, we need to multiply coefficients with something.  
So we write:

```text
Y = 1(β 0 ) + X 1 (β 1 ) + X 2 (β 2 )
```

That is why the first column is 1.  
Example row:

```text
[1, 4, 2]
```

Means:

```text
1(β 0 ) + 4(β 1 ) + 2(β 2 )
```

### 8. Least Squares Method

Least squares means:  
Choose the regression line/equation that makes total squared errors minimum.  
Error:

```text
e = y − y^
```

Squared error:

```text
e2
```

Sum of squared errors:

```text
SSE = e e t
```

Why square the errors?  
Because positive and negative errors can cancel each other.  
Example:  
Error 1:

```text
+5
```

Error 2:

```text
−5
```

If we add directly:

```text
5 + (−5) = 0
```

But error is not actually zero. So we square:

```text
5 + 2 (−5) = 2 25 + 25 = 50
```

### 9. Formula for Estimating Parameters

The main formula from the notes is:

```text
B^ = (X X) t −1 X Y t
```

Meaning:

| Term | Meaning |
|---|---|

B^ estimated coefficients  
Xt transpose ofX

t matrix multiplication  
X X  
−1  
(X X)

t inverse matrix  
t matrix multiplication of transpose X with Y  
X Y  
Exam shortcut:  
Whenever question says matrix approach, write:

```text
B^ = (X X) t −1 X Y t
```

Then calculate:

```text
1. X
Xt
```

2.

```text
3. X X t
(X X) t −1
```

4.

```text
5. X Y t
B^
```

6.

### 10. Assumptions of Multiple Linear Regression

The notes give 10 assumptions. These are very important for theory questions.

### Assumption 1: Linearity

The model must be linear in parameters.  
Allowed:

```text
Y = β 0 + β 1 X + ϵ
```

Also allowed:

```text
Y = β 0 + β 1 X + 2 ϵ
```

Why? Because is still not squared.

```text
β 1
```

Not allowed:

```text
Y = β 0 + β 1 2 X + ϵ
```

Because parameter is squared.

```text
β 1
```

Simple meaning:  
Beta values must appear normally, not as powers or inside complex functions.

### Assumption 2: Number of Observations

Number of observations must be greater than number of parameters.

```text
n > p
```

Example:  
If model has:

```text
β 0 , β 1 , β 2
```

Then:

```text
p = 3
```

So we need:

```text
n > 3
```

In this example:

```text
n = 8
p = 3
```

So:

```text
8 > 3
```

Valid.

### Assumption 3: Independent Variables Have Variation

All values should not be the same.

```text
X
```

Bad example:

| House | Bedrooms |
|---|---|
| 1 | 3 |
| 2 | 3 |
| 3 | 3 |

Here bedrooms has no variation.  
If all values are same, regression cannot know how changes when changes.

```text
Y X
```

Simple meaning:  
X must change, otherwise we cannot study its effect.

### Assumption 4: Expected Error is Zero

```text
E(ϵ i ) = 0
```

Meaning:  
On average, errors should be zero.  
Sometimes model predicts high, sometimes low, but average error should balance out.

### Assumption 5: Homoscedasticity

```text
Var(ϵ i ) = σ2
```

Meaning:  
All error terms should have same variance.  
Simple meaning:  
The spread of errors should remain almost same for all values of X.  
If small houses have small errors but large houses have huge errors, then this assumption fails.

### Assumption 6: Independence of Error Terms

```text
Cov(ϵ i , ϵ j ) = 0
```

Meaning:  
One error should not depend on another error.  
Example:  
If error in house 1 affects error in house 2, that is bad.  
Simple meaning:  
Errors should be independent.

### Assumption 7: Independent Variables and Errors are Independent

```text
Cov(X i , ϵ i ) = 0
```

Meaning:  
The independent variable should not be related to the error term.  
Simple meaning:  
X should not secretly contain the missing error information.

### Assumption 8: No Exact Linear Relationship Between Regressors

This means no perfect multicollinearity.  
Bad example:

```text
X 2 = 2X 1
```

If baths are always exactly double bedrooms, then both variables are giving the same information.  
Simple meaning:  
Independent variables should not be perfect copies of each other.

### Assumption 9: Normality of Error Terms

```text
ϵ i ∼ N(0, σ ) 2
```

Meaning:

```text
σ2
```

Errors should follow normal distribution with mean 0 and variance .  
This is mainly important for:  
- t-test  
- confidence interval  
- p-value

### Assumption 10: No Specification Bias

The model should be correctly written.  
Bad model:  
House price depends on bedrooms and baths, but you forget baths.

```text
Y = β 0 + β 1 X 1 + ϵ
```

Better model:

```text
Y = β 0 + β 1 X 1 + β 2 X 2 + ϵ
```

Simple meaning:  
Important variables should not be missing, and wrong variables should not be added.

### 11. Solved Example from the Notes

The data is about house prices.

|  | Bedrooms | Baths | Price |
|---|---|---|---|

X X Y

| House 1 2 |  |  |  |
|---|---|---|---|
| 1 | 4 | 2 | 307500 |
| 2 | 5 | 3 | 333000 |
| 3 | 2 | 2 | 275500 |
| 4 | 3 | 2 | 302000 |
| 5 | 2 | 1 | 265500 |
| 6 | 4 | 3 | 317500 |
| 7 | 2 | 1 | 264600 |
| 8 | 3 | 2 | 292000 |

We want to fit:

```text
Y^ = β^0 + β^1 X 1 + β^2 X 2
```

Where:  
= bedrooms

```text
X 1
```

= baths

```text
X 2
```

Y = price

### 12. Step 1: Write the X Matrix

Because we have intercept, first column is 1.

```text
1 4 2
1 5 3
1 2 2
1 3 2
X =
1 2 1
1 4 3
1 2 1
1 3 2
```

And:

```text
307500
333000
275500
302000
Y =
265500
317500
264600
292000
```

### t 13. Step 2: CalculateX X

From the notes:

```text
8 25 16
X X = t 25 87 55
16 55 36
```

Why first value is 8?  
Because there are 8 observations, and first column has eight 1s:

```text
1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 8
```

Why 25?  
Sum of bedrooms:

```text
4 + 5 + 2 + 3 + 2 + 4 + 2 + 3 = 25
```

Why 16?  
Sum of baths:

```text
2 + 3 + 2 + 2 + 1 + 3 + 1 + 2 = 16
```

### t 14. Step 3: CalculateX Y

From the notes:

```text
2357600
X Y = t 7558200
4835600
```

Meaning:  
First value:

```text
∑ Y = 2357600
```

Second value:

```text
∑ X 1 Y = 7558200
```

Third value:

```text
∑ X 2 Y = 4835600
```

### B^ 15. Step 4: Calculate

Formula:

```text
B^ = (X X) t −1 X Y t
```

From the notes:

```text
224928.57
B^ = 15314.28
10957.14
```

So:

```text
β^0 = 224928.57
β^1 = 15314.28
β^2 = 10957.14
```

Rounded:

```text
β^0 = 224929
β^1 = 15314
β^2 = 10957
```

### 16. Final Regression Equation

```text
Y^ = 224929 + 15314X 1 + 10957X 2
```

Meaning:  
Predicted Price = 224929 + 15314(bedrooms) + 10957(baths)

### 17. Interpretation of Coefficients β^0 = 224929 Intercept

Meaning:  
If bedrooms and baths are 0, predicted price is:

```text
224929
```

But practically, a house cannot have 0 bedrooms and 0 baths.  
So in real life, intercept is often just a mathematical starting point.  
Exam answer:  
When all independent variables are zero, expected house price is $224929.

### β^1= Bedroom coefficient 15314

Meaning:  
If number of bedrooms increases by 1, house price increases by about:

```text
15314
```

while keeping baths constant.  
Exam answer:  
For each additional bedroom, average house price increases by $15314, holding number of baths constant.

### β^2= 10957 Bath coefficient

Meaning:  
If number of baths increases by 1, house price increases by about:

```text
10957
```

while keeping bedrooms constant.  
Exam answer:  
For each additional bath, average house price increases by $10957, holding number of bedrooms constant.

### 18. Prediction Example

Question:  
Predict price of a house with:

```text
X 1 = 3
X 2 = 2
```

Use:

```text
Y^ = 224929 + 15314X 1 + 10957X 2
```

Put values:

```text
Y^ = 224929 + 15314(3) + 10957(2)
```

First calculate bedroom part:

```text
15314(3) = 45942
```

Calculate bath part:

```text
10957(2) = 21914
```

Now add:

```text
Y^ = 224929 + 45942 + 21914
Y^ = 292785
```

Final answer:

```text
Y^ = 292785
```

So predicted house price is:

```text
$292785
```

### 19. Fitted Values

Fitted value means predicted value:

```text
y^ = XB^
```

Using the model, the predicted prices are:  
e = Y −Y^  
Y^

|  | Actual | Error |
|---|---|---|
|  | Predicted |  |

Y

| House |  |  |  |
|---|---|---|---|
| 1 | 307500 | 308100.00 | -600.00 |
| 2 | 333000 | 334371.43 | -1371.43 |
| 3 | 275500 | 277471.43 | -1971.43 |
| 4 | 302000 | 292785.71 | 9214.29 |
| 5 | 265500 | 266514.29 | -1014.29 |
| 6 | 317500 | 319057.14 | -1557.14 |
| 7 | 264600 | 266514.29 | -1914.29 |
| 8 | 292000 | 292785.71 | -785.71 |

Important:

```text
e = Y −Y^
```

Example for house 1:

```text
e = 307500 −308100 = −600
```

### 20. SSE: Sum of Squares Error

Formula:

```text
SSE = e e t
```

Meaning:  
Square all errors and add them.

```text
SSE = (−600) + 2 (−1371.43) + 2 ⋯+ (−785.71)2
```

From the notes:

```text
SSE = 98765714
```

Simple meaning:  
SSE tells total unexplained error left in the model.  
Lower SSE means better model.

### 21. SST: Sum of Squares Total

Formula:

```text
SST = Y Y − t nYˉ 2
```

Meaning:  
SST tells total variation in .

```text
Y
```

First:

```text
∑ Y
Yˉ =
n
```

From the notes:

```text
∑ Y = 2357600
n = 8
2357600
Yˉ = = 294700
8
```

Also:

```text
Y Y = t 699123160000
```

So:

```text
SST = 699123160000 −8(294700)2
SST = 4338440000
```

Simple meaning:  
SST tells total variation in house prices before using regression.

### 22. SSR: Sum of Squares Regression

Formula:

```text
SSR = B^t X Y − t nYˉ 2
```

From the notes:

```text
SSR = 4239674286
```

Simple meaning:  
SSR tells how much variation is explained by the regression model.

### R2 23. Coefficient of Determination

Formula:

```text
R = 2 SSR
SST
```

Put values:

```text
R = 2 4239674286
4338440000
R = 2 0.9772
```

Rounded:

```text
R = 2 0.98
```

Meaning:

```text
98%
```

So:  
98% of variation in house price is explained by bedrooms and baths.  
Remaining:

```text
100% −98% = 2%
```

So:  
2% variation is due to other factors.  
Exam answer:

```text
R = 0.98 2
```

Interpretation:  
\boxed{\text{98% of the variation in house price is explained by bedrooms and baths.}}

### 24. Testing Parameters of MLRM

Now we test whether each coefficient is significant or not.  
Meaning:  
Does really affect ?

```text
X 1 Y
```

Does really affect ?

```text
X 2 Y
```

Or are their effects just random?

### 25. Hypotheses for Testing Parameters

For any parameter :

```text
β j
H 0 : β j = 0
H 1 : β j 0 =
```

Meaning:

### Null hypothesis

```text
H 0 : β j = 0
```

The variable has no significant effect.

### Alternative hypothesis

```text
H 1 : β j 0 =
```

The variable has significant effect.  
Roman Urdu:  
Agar beta zero hai, to X ka Y par koi effect nahi. Agar beta zero nahi, to X ka effect hai.

### 26. Test Statistic Formula

```text
t = β^j −β j
se( β^j )
```

Usually under :

```text
H 0
β j = 0
```

So:

```text
β^j
t =
se( β^j )
```

Degrees of freedom:

```text
df = n −p
```

In this example:

```text
n = 8
```

There are 3 parameters:

```text
β 0 , β 1 , β 2
```

So:

```text
p = 3
df = 8 −3 = 5
```

At:

```text
α = 0.05
```

two-tailed test:

```text
t 0.025,5 = 2.571
```

Decision rule:  
Reject if:

```text
H 0
∣t∣> 2.571
```

### 27. Variance-Covariance Matrix

Before testing, we need standard errors.  
Formula:

```text
C = σ e 2 (X X) t −1
```

Where:

```text
σ = 2 e n −p SSE
```

From notes:

```text
SSE = 98765714
n −p = 5
```

So:

```text
σ e 2 = 98765714 5
σ e 2 = 19753143
```

Then:

```text
C = 19753143(X X) t −1
```

From the notes, diagonal variances are:

```text
Var( β^0 ) = 25161741
Var( β^1 ) = 7525007
Var( β^2 ) = 16696109
```

Standard error is square root of variance:

```text
se( β^0 ) = 25161741 = 5016.15
se( β^1 ) = 7525007 = 2743.17
se( β^2 ) = 16696109 = 4086.09
```

### 28. Test ofβ 0 Step 1: Hypotheses

```text
H 0 : β 0 = 0
H 1 : β 0 0 =
```

### Step 2: Level of significance

```text
α = 0.05
```

### Step 3: Test statistic

```text
β^0 −0
t =
se( β^0 )
224928.57
t =
5016.15
t = 44.84
```

### Step 4: Critical value

```text
t 0.025,5 = 2.571
```

### Step 5: Decision

```text
44.84 > 2.571
```

So reject .

```text
H 0
```

### Final conclusion

is significant

```text
β 0
```

Meaning:  
The intercept is statistically significant.

### 29. Test of : Bedrooms β 1 Step 1: Hypotheses

```text
H 0 : β 1 = 0
H 1 : β 1 0 =
```

### Step 2: Level of significance

```text
α = 0.05
```

### Step 3: Test statistic

```text
β^1 −0
t =
se( β^1 )
15314
t =
2743.18
t = 5.58
```

### Step 4: Critical value

```text
t 0.025,5 = 2.571
```

### Step 5: Decision

```text
5.58 > 2.571
```

So reject .

```text
H 0
```

### Final conclusion

is significant

```text
β 1
```

Meaning:  
Number of bedrooms has a significant effect on house price.

### 30. Test of : Baths β 2 Step 1: Hypotheses

```text
H 0 : β 2 = 0
H 1 : β 2 0 =
```

### Step 2: Level of significance

```text
α = 0.05
```

### Step 3: Test statistic

```text
β^2 −0
t =
se( β^2 )
10957
t =
4086.09
t = 2.68
```

### Step 4: Critical value

```text
t 0.025,5 = 2.571
```

### Step 5: Decision

```text
2.68 > 2.571
```

So reject .

```text
H 0
```

### Final conclusion

is significant

```text
β 2
```

Meaning:  
Number of baths has a significant effect on house price.

### 31. P-Value Approach

P-value rule:  
If:  
p-value < α  
Reject .

```text
H 0
```

If:  
p-value > α  
Do not reject .

```text
H 0
```

In this example:

| Parameter | t-value | p-value | Decision |
|---|---|---|---|
|  | 44.84 | 0.006 | reject |

β H  
0 0

|  | 5.58 | 0.005 | reject |
|---|---|---|---|

β H  
1 0

|  | 2.68 | 0.021 | reject |
|---|---|---|---|

β H  
2 0  
Since all p-values are less than:

```text
0.05
```

All parameters are significant.  
Important note:  
In the notes, the p-value line for seems to contain a small typo because it writes

```text
β 2
2[44.84] t = 2.68
```

  - , but it should correspond to . The final p-value and conclusion are still about .

```text
β 2
```

### 32. Confidence Interval Approach

General formula:

```text
β^j − t α/2,n−p se( β^j ) ≤ β j ≤ β^j + t α/2,n−p se( β^j )
```

For 95% confidence interval:

```text
α = 0.05
t 0.025,5 = 2.571
```

Decision rule:  
If 0 is inside the confidence interval:  
Do not reject .

```text
H 0
```

If 0 is not inside the confidence interval:  
Reject .

```text
H 0
```

### CI forβ

0

```text
224928.57 ± 2.571(5016.15)
224928.57 −12898.07 = 212030.50
224928.57 + 12898.07 = 237826.64
```

So:

```text
212030.50 ≤β 0 ≤ 237826.63
```

0 is not inside the interval.  
So reject .

```text
H 0
```

is significant

```text
β 0
```

### CI forβ

1

```text
15314 ± 2.571(2743.18)
15314 −7052.72 = 8261.28
15314 + 7052.72 = 22366.72
```

So:

```text
8261.28 ≤β 1 ≤ 22366.72
```

0 is not inside the interval.  
So reject .

```text
H 0
```

is significant

```text
β 1
```

### CI forβ

2

```text
10957 ± 2.571(4086.09)
2.571(4086.09) = 10503.54
```

Lower limit:

```text
10957 −10503.54 = 453.46
```

Upper limit:

```text
10957 + 10503.54 = 21460.54
```

So approximately:

```text
453.46 ≤β 2 ≤ 21460.54
```

0 is not inside the interval.  
So reject .

```text
H 0
```

is significant

```text
β 2
```

### 33. Full Exam-Style Summary of Example

Model:

```text
Y^ = 224929 + 15314X 1 + 10957X 2
```

Where:  
= bedrooms

```text
X 1
```

= baths

```text
X 2
```

Prediction for 3-bedroom, 2-bath house:

```text
Y^ = 224929 + 15314(3) + 10957(2)
Y^ = 292785
```

Coefficient of determination:

```text
R = 2 0.98
```

Interpretation:  
98% variation in house price is explained by bedrooms and baths.  
Parameter testing:

| Parameter | Meaning | t-value | Decision |
|---|---|---|---|
|  | intercept | 44.84 | significant |

β0

|  | bedrooms | 5.58 | significant |
|---|---|---|---|

β1

|  | baths | 2.68 | significant |
|---|---|---|---|

β2  
Final conclusion:  
Both bedrooms and baths significantly affect house price at 5% level of significance.

### 34. Formula List to Memorize for Exam Regression Model

```text
Y i = β 0 + β 1 X i1 + β 2 X i2 + ⋯+ β k X ik + ϵ i
```

### Matrix Model

```text
Y = XB + E
```

### Estimated Coefficients

```text
B^ = (X X) t −1 X Y t
```

### Fitted Values

```text
Y^ = XB^
```

### Error

```text
e = Y −Y^
```

### Sum of Squares Error

```text
SSE = e e t
```

### Sum of Squares Total

```text
SST = Y Y − t nYˉ 2
```

### Sum of Squares Regression

```text
SSR = B^t X Y − t nYˉ 2
```

### Coefficient of Determination

```text
R = 2 SSR
SST
```

or:

```text
R = 2 1 − SSE
SST
```

### Error Variance

```text
σ = 2 e n −p SSE
```

### Variance-Covariance Matrix

```text
C = σ e 2 (X X) t −1
```

### Standard Error

```text
β^j
```

se( ) = diagonal value of C

### t-Test

```text
t = β^j −β j
se( β^j )
```

Usually:

```text
β^j
t =
se( β^j )
```

### Degrees of Freedom

```text
df = n −p
```

### Confidence Interval

```text
β^j ± t α/2,n−p se( β^j )
```

### 35. What is Most Important for Exam?

Memorize these strongly:  
1. Definition of regression.  
2. Difference between simple and multiple regression.  
3. MLRM equation.  
4. Matrix form:

```text
Y = XB + E
```

5. Parameter estimation formula:

```text
B^ = (X X) t −1 X Y t
, β , β
```

6. Meaning of .

```text
β 0 1 2
```

7. Assumptions of MLRM.

```text
R2
```

8. formula and interpretation.  
9. t-test steps.  
10. Confidence interval decision rule.

### 36. Baby Explanation

Regression is like guessing house price using reasons.  
Reasons:  
- bedrooms  
- baths  
The model says:  
price = starting price + bedroom effect + bath effect  
For this example:  
price = 224929 + 15314(bedrooms) + 10957(baths)  
So every extra bedroom adds about:

```text
15314
```

Every extra bath adds about:

```text
10957
```

The model explains:

```text
98%
```

of house price variation.  
So it is a very strong model for this data.

### 37. Common Mistakes Mistake 1: Forgetting first column of 1s in X

Always write:

```text
[1, X 1 , X 2 ]
```

not just:

```text
[X 1 , X 2 ]
```

### Y^ Mistake 2: Confusing and Y

Y = actual value  
Y^ predicted value

```text
=
```

### Mistake 3: Wrong error formula

:

```text
e = Y −Y^
```

Not:

```text
e = Y^ − Y
```

### df = n −p Mistake 4: Forgetting

Here:

```text
n = 8
p = 3
df = 5
```

### R2 Mistake 5: Wrong interpretation of

Do not say:  
“Model is 98% accurate.”  
Say:  
98% variation in Y is explained by X variables.

### Mistake 6: Wrong conclusion in t-test

If:

```text
∣t∣> t critical
```

Reject .

```text
H 0
```

If:

```text
p < α
```

Reject .

```text
H 0
```

If 0 is not inside CI:  
Reject .

```text
H 0
```

### 38. Exam Shortcut

For matrix regression question, follow this fixed order:  
1. Write model:

```text
Y = β 0 + β 1 X 1 + β 2 X 2 + ϵ
```

2. Write matrix with first column 1.

```text
X
```

3. Write .

```text
Y
```

4. Calculate:

```text
X X t
```

5. Calculate:

```text
X Y t
```

6. Use:

```text
B^ = (X X) t −1 X Y t
```

7. Write final regression equation.  
8. Interpret coefficients.  
9. Predict if asked.

```text
R2
```

10. Find if asked.  
11. Test parameters if asked.  
Final key line to remember:

```text
Y^ = 224929 + 15314X 1 + 10957X 2
```

This is the main result of your given example.

## 26. Test Statistic Formula
## 31. p-Value Approach

|  | Show more |
|---|---|

means total number of rows/observations in the dataset.

```text
n
```

In your house-price example, there are 8 houses, so:

```text
n = 8
```

The notes test regression parameters using the t-test, p-value approach, and confidence interval approach.

### 1. What are we testing?

Your regression equation is:

```text
Y^ = 224929 + 15314X 1 + 10957X 2
```

Where:  
= bedrooms

```text
X 1
```

= baths

```text
X 2
```

So:  
= intercept

```text
β 0
```

= effect of bedrooms

```text
β 1
```

= effect of baths

```text
β 2
```

Now the question is:  
Are these beta values really important, or did they come by chance?  
That is why we do testing of parameters.

### : = 0 2. What does mean? H β 0 j

For any beta:

```text
H 0 : β j = 0
```

This means:  
That variable has no effect.  
Example for baths:

```text
H 0 : β 2 = 0
```

Meaning:  
Number of baths has no effect on house price.  
Alternative hypothesis:

```text
H 1 : β 2 0 =
```

Meaning:  
Number of baths has some effect on house price.  
Roman Urdu:  
Agar beta zero hai, to us variable ka price par effect nahi. Agar beta zero nahi, to effect hai.

### 3. What is t-test?

A t-test checks whether a beta value is big enough compared to its error.  
Simple idea:  
estimated effect

```text
t =
```

standard error  
Big t-value means:  
effect is large compared to error, so variable is important.  
Small t-value means:  
effect is small compared to error, so maybe variable is not important.  
Main formula:

```text
t = β^j −β j
se( β^j )
```

Usually in exam:

```text
H 0 : β j = 0
```

So formula becomes:

```text
β^j −0
t =
se( β^j )
β^j
t =
se( β^j )
```

### 4. What is Standard Error?

Standard error means:  
How much uncertainty/error exists in our estimated beta.  
Example:

```text
β^2 = 10957
```

This says:  
One extra bath increases price by about $10957.  
But this is only an estimate from sample data. It may not be exact.  
So we also calculate:

```text
se( β^2 ) = 4086.09
```

Meaning:  
There is some uncertainty around the bath effect.  
Simple meaning:  
Beta is the estimated effect. Standard error tells how reliable that estimate is.

### 5. What is ? p

In regression testing:  
p = number of parameters  
Not p-value.  
In your model:

```text
Y^ = β 0 + β 1 X 1 + β 2 X 2
```

There are 3 parameters:

```text
β 0 , β 1 , β 2
```

So:

```text
p = 3
```

And:

```text
n = 8
```

So degrees of freedom:

```text
df = n −p
df = 8 −3 = 5
```

### 6. What are Degrees of Freedom?

Degrees of freedom means:  
How much free information is left after estimating parameters.  
You had 8 rows.  
But you used data to estimate 3 beta values.  
So remaining freedom:

```text
8 −3 = 5
```

That is why:

```text
df = 5
```

Exam shortcut:

```text
df = n −p
```

where:  
n = number of rows  
p = number of beta parameters including intercept

### 7. What is Two-Tailed Test?

Two-tailed test means we check both sides:  
1. Beta may be positive  
2. Beta may be negative  
Because alternative hypothesis is:

```text
H 1 : β j 0 =
```

This means beta can be:

```text
β j > 0
```

or:

```text
β j < 0
```

So we check both tails of the t-distribution.  
Simple meaning:  
Two-tailed test checks whether beta is different from zero in any direction.  
Roman Urdu:  
Two-tailed ka matlab: beta zero se zyada bhi ho sakta hai, ya zero se kam bhi. Dono sides check karni hoti hain.

### 8. Critical Value

For this example:

```text
α = 0.05
df = 5
```

Two-tailed test means:

```text
α/2 = 0.025
```

From t-table:

```text
t 0.025,5 = 2.571
```

Decision rule:

```text
∣t∣> 2.571
```

then reject .

```text
H 0
```

Meaning:  
If calculated t-value is bigger than 2.571, the beta is significant.

### 9. Test of : Intercept β 0

From the notes:

```text
β^0 = 224928.57
se( β^0 ) = 5016.15
```

### Step 1: Hypotheses

```text
H 0 : β 0 = 0
H 1 : β 0 0 =
```

Meaning:  
Null says intercept is not important.  
Alternative says intercept is important.

### Step 2: Formula

```text
β^0 −0
t =
se( β^0 )
```

### Step 3: Put values

```text
224928.57
t =
5016.15
```

### Step 4: Divide

```text
t = 44.84
```

### Step 5: Compare with critical value

Critical value:

```text
2.571
```

Calculated value:

```text
44.84
```

Since:

```text
44.84 > 2.571
```

Reject .

```text
H 0
```

### Final conclusion

is significant

```text
β 0
```

Simple meaning:  
The intercept is statistically different from zero.

### 10. Test of : Baths β 2

Now baths coefficient.  
From your model:

```text
β^2 = 10957
```

This means:  
One extra bath increases price by about:

```text
10957
```

But we test if this effect is really significant.  
Given:

```text
se( β^2 ) = 4086.09
```

### Step 1: Hypotheses

```text
H 0 : β 2 = 0
```

Meaning:  
Baths have no effect on price.

```text
H 1 : β 2 0 =
```

Meaning:  
Baths have an effect on price.

### Step 2: Formula

```text
β^2 −0
t =
se( β^2 )
```

### Step 3: Put values

```text
10957
t =
4086.09
```

### Step 4: Divide

```text
t = 2.68
```

### Step 5: Compare

Critical value:

```text
2.571
```

Calculated t-value:

```text
2.68
```

Since:

```text
2.68 > 2.571
```

Reject .

```text
H 0
```

### Final conclusion

is significant

```text
β 2
```

Simple meaning:  
Number of baths significantly affects house price.  
Roman Urdu:  
Baths ka house price par real effect hai, sirf random chance nahi.

### 11. What is P-Value?

P-value means:  
If null hypothesis is true, what is the chance of getting this result or more extreme result?  
Very simple:  
Small p-value means:  
Our result is unlikely to happen by chance. So reject .

```text
H 0
```

Large p-value means:  
Our result may have happened by chance. So do not reject .

```text
H 0
```

Decision rule:  
p-value < α ⇒reject H

```text
0
```

p-value > α ⇒do not reject H

```text
0
```

In this example:

```text
α = 0.05
```

So if p-value is less than 0.05, reject .

```text
H 0
```

### 12. P-Value Approach forβ 2

From notes for baths:

```text
t = 2.68
```

p-value:

```text
0.021
```

Now compare:

```text
0.021 < 0.05
```

So reject .

```text
H 0
```

Conclusion:  
is significant

```text
β 2
```

Meaning:  
Baths have significant effect on house price.  
Important note: In the notes, the p-value section for seems to have a typing mistake

```text
β 2
44.84 2.68
```

where it writes , but for , the correct t-value is .

```text
β 2
```

### 13. Critical Value Approach vs P-Value Approach

Both give the same conclusion.

### Critical Value Approach

Compare:  
t value with critical value  
If:

```text
∣t∣> t critical
```

Reject .

```text
H 0
```

### P-Value Approach

Compare:  
p-value with α  
If:  
p-value < α  
Reject .

```text
H 0
```

For :

```text
β 2
```

Critical value approach:

```text
2.68 > 2.571
```

Reject .

```text
H 0
```

P-value approach:

```text
0.021 < 0.05
```

Reject .

```text
H 0
```

Same answer.

### 14. Confidence Interval Approach

Confidence interval gives a range of possible values for beta.  
Formula:

```text
β^j ± t α/2,n−p se( β^j )
```

Meaning:  
estimate ± margin of error  
Or:

```text
β^j − t × se
```

to

```text
β^j + t × se
```

### 15. Confidence Interval Decision Rule

For testing:

```text
H 0 : β j = 0
```

Check whether 0 lies inside the confidence interval.

### If 0 is inside CI

Do not reject .

```text
H 0
```

Meaning:  
Beta could be zero.  
Variable may not be significant.

### If 0 is not inside CI

Reject .

```text
H 0
```

Meaning:  
Beta is probably not zero.  
Variable is significant.

### 16. Confidence Interval for : Baths β 2

Given:

```text
β^2 = 10957
se( β^2 ) = 4086.09
t 0.025,5 = 2.571
```

Formula:

```text
β^2 ± t × se( β^2 )
```

Put values:

```text
10957 ± 2.571(4086.09)
```

First multiply:

```text
2.571 × 4086.09 = 10503.54
```

Now lower limit:

```text
10957 −10503.54 = 453.46
```

Upper limit:

```text
10957 + 10503.54 = 21460.54
```

So confidence interval is:

```text
453.46 ≤β 2 ≤ 21460.54
```

Now check:  
Is 0 inside this interval?  
Interval starts at:

```text
453.46
```

and ends at:

```text
21460.54
```

0 is not inside.  
So reject .

```text
H 0
```

Final conclusion:  
is significant

```text
β 2
```

Simple meaning:  
We are 95% confident that the true bath effect is between:

```text
453.46
```

and:

```text
21460.54
```

Since the whole interval is positive, baths increase house price.

### 17. Confidence Interval forβ 0

Given:

```text
β^0 = 224928.57
se( β^0 ) = 5016.15
t = 2.571
```

Formula:

```text
224928.57 ± 2.571(5016.15)
```

Multiply:

```text
2.571(5016.15) = 12898.07
```

Lower limit:

```text
224928.57 −12898.07 = 212030.50
```

Upper limit:

```text
224928.57 + 12898.07 = 237826.64
```

So:

```text
212030.50 ≤β 0 ≤ 237826.64
```

0 is not inside.  
So reject .

```text
H 0
```

Conclusion:  
is significant

```text
β 0
```

### 18. One Simple Example to Understand Everything

Suppose you say:

```text
β^2 = 10957
```

This means:  
Baths increase price by $10957.  
But we ask:  
Is 10957 large enough, or could it be random?  
So we divide by its standard error:

```text
10957
t =
4086.09
t = 2.68
```

This means:  
Bath effect is 2.68 times bigger than its standard error.  
Now t-table says:  
Required value is:

```text
2.571
```

Since:

```text
2.68 > 2.571
```

Bath effect is large enough.  
So:  
Baths are significant

### 19. Full Comparison Table

| Concept | Simple Meaning | Rule |
|---|---|---|
| t-test | checks if beta is important | large t means significant |
| critical value | boundary value from t-table | reject if ( |

p-value | chance result happened | reject if p-value <α

|  | randomly |  |
|---|---|---|
| confidence interval | possible range of beta | reject if 0 not inside CI |

n = 8

|  | total rows/observations | here |
|---|---|---|

n  
p = 3

|  | total parameters including | here |
|---|---|---|

p

|  | intercept |
|---|---|

df = n −p = 5

| df | degrees of freedom |
|---|---|

### 20. Most Important Exam Steps

For every beta test, write this:

### Step 1

```text
H 0 : β j = 0
H 1 : β j 0 =
```

### Step 2

```text
α = 0.05
```

### Step 3

```text
β^j
t =
se( β^j )
```

### Step 4

```text
df = n −p
```

### Step 5

Compare with critical value.

### Step 6

If:

```text
∣t∣> t c
```

Reject .

```text
H 0
```

### Step 7

Conclusion:  
The parameter is significant.

### 21. Baby Summary

You have beta values:

```text
β 0 , β 1 , β 2
```

But we do not blindly trust them.  
We test them.  
The test asks:  
Is this beta far enough from zero?  
If yes, it is significant.  
For baths:

```text
β^2 = 10957
```

Standard error:

```text
4086.09
```

t-value:

```text
2.68
```

Critical value:

```text
2.571
```

Since:

```text
2.68 > 2.571
```

Baths are significant.  
P-value also confirms:

```text
0.021 < 0.05
```

Confidence interval also confirms:

```text
453.46 ≤β 2 ≤ 21460.54
```

0 is not inside.  
So final answer:  
Number of baths significantly affects house price.

|  | \=2.68 |
|---|---|

## Estimating β and Setting Up the Hypothesis Test

```text
β^
```

The key confusion is this: is the real unknown effect in the population, while  is only

```text
β
```

our sample estimate. We test whether the unknown real effect could reasonably be zero.  
this is the main point:

```text
β = β^
```

They are different.

### β

```text
β
```

is the true real effect in the whole population.  
Example:  
The real effect of baths on house price in the whole housing market.  
But we do not know the true .

```text
β
```

### β^

```text
β^
```

is the estimated effect calculated from our sample data.  
In this example:

```text
β^2 = 10957
```

This means:  
From our sample of 8 houses, we estimated that one extra bath increases price by about $10957.  
But this is only an estimate. It may be correct, or it may have sampling error.  
So:  
β = true unknown value  
β^= estimated value from sample

```text
B^ (X X) t −1 t
```

The notes use = to estimate the regression coefficients from the

```text
X Y
```

sample data.

### 2. Then how do we know whether  is 0 or not? β

We do not know directly.  
That is why we do hypothesis testing.  
We ask:

```text
β^
```

“Based on our sample estimate , is the real  probably zero or probably not zero?”

```text
β
```

For baths:

```text
β^2 = 10957
```

Question:  
Is the true bath effect really different from zero?  
Or did this value come just because of random sample variation?

### : β = 0 3. Why do we take ? H 0

Because zero means no effect.  
For baths:

```text
H 0 : β 2 = 0
```

Meaning:  
Baths have no effect on house price.  
Alternative:

```text
H 1 : β 2 0 =
```

Meaning:  
Baths have some effect on house price.  
We start with because in statistics we usually begin with the “no effect” assumption.

```text
H 0
```

Simple example:  
In court:  
- Start: person is assumed not guilty.  
- Evidence decides whether to reject that assumption.  
In statistics:  
- Start: variable has no effect.  
- Data decides whether to reject that assumption.  
So is not something we “know.”

```text
H 0
```

It is something we assume temporarily for testing.

### 4. What does the t-value do?

The t-value checks:

```text
β^
```

How far is from 0 compared to its error?  
Formula:

```text
β^j −0
t =
se( β^j )
```

or simply:

```text
β^j
t =
se( β^j )
```

For baths:

```text
β^2 = 10957
se( β^2 ) = 4086.09
```

So:

```text
10957
t =
4086.09
t = 2.68
```

Meaning:  
The estimated bath effect is 2.68 standard errors away from zero.  
That is why the notes say:

```text
t = 2.68
```

### 5. What is standard error?

Standard error tells:

```text
β^
```

How much uncertainty exists in .  
If standard error is small, estimate is reliable.  
If standard error is large, estimate is not very reliable.  
Example:

```text
β^2 = 10957
se( β^2 ) = 4086.09
```

This means:  
The bath effect is estimated as 10957, but there is uncertainty of about 4086 around it.

### 6. How to calculate standard error step by step?

For regression, standard error comes from the variance-covariance matrix.

### Step 1: Calculate predicted values

```text
Y^ = XB^
```

### Step 2: Calculate errors

```text
e = Y −Y^
```

Example:  
Actual price:

```text
Y = 307500
```

Predicted price:

```text
Y^ = 308100
```

Error:

```text
e = 307500 −308100 = −600
```

Do this for all 8 rows.

### Step 3: Calculate SSE

```text
SSE = e e t
```

Meaning:  
Square all errors and add them.  
From the notes:

```text
SSE = 98765714
```

### Step 4: Calculate degrees of freedom

```text
df = n −p
```

Here:

```text
n = 8
```

is the total number of rows/houses/observations.

```text
n
```

There are 3 beta parameters:

```text
β 0 , β 1 , β 2
```

So:

```text
p = 3
```

Therefore:

```text
df = 8 −3 = 5
```

### Step 5: Calculate error variance

```text
σ = 2 e n −p SSE
```

Put values:

```text
σ e 2 = 98765714 5
σ e 2 = 19753142.8
```

Approximately:

```text
σ e 2 = 19753143
```

### Step 6: Calculate variance-covariance matrix

Formula:

```text
C = σ e 2 (X X) t −1
```

This gives the variance-covariance matrix.  
From this matrix, we use the diagonal values.  
The notes give these variances:

```text
Var( β^0 ) = 25161741
Var( β^1 ) = 7525007
Var( β^2 ) = 16696109
```

### Step 7: Take square root to get standard errors

For :

```text
β 0
se( β^0 ) = 25161741
se( β^0 ) = 5016.15
```

For :

```text
β 1
se( β^1 ) = 7525007
se( β^1 ) = 2743.17
```

For :

```text
β 2
se( β^2 ) = 16696109
se( β^2 ) = 4086.09
```

So:

```text
se( β^2 ) = 4086.09
```

### t < 2.571 7. If , what happens?

In this example:

```text
= 2.571
```

tcritical  
Decision rule:  
∣t∣> 2.571 ⇒Reject H0  
∣t∣< 2.571 ⇒Do not reject H

```text
0
```

So if:

```text
t < 2.571
```

then we do not reject .

```text
H 0
```

That means:  
The variable is not statistically significant.  
Important:  
We usually do not say “accept .”

```text
H 0
```

Better exam wording:  
Do not reject H

```text
0
```

Simple meaning:  
There is not enough evidence to say beta is different from zero.

### 8. For baths, why do we reject ? H 0

For baths:

```text
t = 2.68
```

Critical value:

```text
2.571
```

Since:

```text
2.68 > 2.571
```

We reject:

```text
H 0 : β 2 = 0
```

Conclusion:  
is significant

```text
β 2
```

Meaning:  
Baths have a statistically significant effect on house price.

### 9. What is p-value in very easy words?

P-value means:  
If is true, how surprising is our result?

```text
H 0
```

For baths:

```text
H 0 : β 2 = 0
```

This means we assume baths have no effect.  
But sample gives:

```text
t = 2.68
```

Now p-value asks:  
“If baths really have no effect, what is the chance of getting a t-value as large as 2.68 or even larger?”  
If this chance is very small, we reject .

```text
H 0
```

### 10. Very simple p-value meaning

Small p-value:  
Result is very unlikely under H

```text
0
```

So reject .

```text
H 0
```

Large p-value:  
Result is possible under H

```text
0
```

So do not reject .

```text
H 0
```

Rule:  
p-value < α ⇒Reject H

```text
0
```

p-value > α ⇒Do not reject H

```text
0
```

In this example:

```text
α = 0.05
```

For baths:

```text
p = 0.021
```

Since:

```text
0.021 < 0.05
```

Reject .

```text
H 0
```

### 11. How do we calculate p-value?

For exam level, usually you do not calculate p-value fully by hand.  
You get it from:  
- t-table  
- calculator  
- software  
- statistical table  
But conceptually:  
For two-tailed test:  
p-value = 2P(T > ∣t∣)  
For baths:

```text
t = 2.68
df = 5
```

So:  
p-value = 2P(T > 2.68)  
Using t-table/software:

```text
p ≈0.021
```

Meaning:  
There is about 2.1% chance of getting such a strong result if baths truly have no effect.  
Since 2.1% is less than 5%, we reject .

```text
H 0
```

### 12. What if p-value is equal to alpha?

Suppose:  
p-value = α  
Example:

```text
p = 0.05
α = 0.05
```

Most textbooks use:  
p ≤α ⇒Reject H

```text
0
```

So if p-value equals alpha exactly, usually:  
Reject H

```text
0
```

But practically, it is called a borderline case.  
Exam-safe answer:

```text
p ≤α p > α
```

If , reject . If , do not reject .

```text
H 0 H 0
```

### 13. What if t-value is equal to critical value?

Suppose:

```text
∣t∣= 2.571
```

Most rules use:  
∣t∣≥t ⇒ Reject H  
critical 0  
So if equal:  
Reject H

```text
0
```

But again, it is a boundary case.  
Exam-safe rule:  
∣t∣≥t ⇒ Reject H

```text
c 0
```

∣t∣< t ⇒ Do not reject H

```text
c 0
```

### 14. Main confusion: how do we know true beta?

We do not know true beta.  
We only know:

```text
β^
```

That is why we use:  
1. t-test  
2. p-value  
3. confidence interval  
These methods help us guess whether the true beta is probably zero or not.  
For baths:

```text
β^2 = 10957
```

Standard error:

```text
4086.09
```

t-value:

```text
2.68
```

p-value:

```text
0.021
```

Confidence interval:

```text
453.46 ≤β 2 ≤ 21460.54
```

Since this interval does not contain 0, we say:  
is probably not zero

```text
β 2
```

So baths are significant.

### 15. Confidence interval also answers the question

How do we know beta?  
We do not know exact beta, but confidence interval gives a possible range.  
For baths:

```text
453.46 ≤β 2 ≤ 21460.54
```

This means:  
The true bath effect is likely between 453.46 and 21460.54.  
Since zero is not in this range, beta is probably not zero.  
That is why we reject .

```text
H 0
```

### 16. Final decision rules t-test rule

∣t∣≥t ⇒ Reject H

```text
c 0
```

∣t∣< t ⇒ Do not reject H

```text
c 0
```

### p-value rule

p ≤α ⇒Reject H

```text
0
```

p > α ⇒Do not reject H

```text
0
```

### confidence interval rule

If 0 is inside CI:  
Do not reject H

```text
0
```

If 0 is not inside CI:  
Reject H

```text
0
```

### 17. Baby summary

We do not know real .

```text
β
```

We only know sample estimate:

```text
β^
```

So we test:

```text
H 0 : β = 0
```

because zero means no effect.  
For baths:

```text
β^2 = 10957
se = 4086.09
10957
t = = 2.68
4086.09
```

Critical value:

```text
2.571
```

Since:

```text
2.68 > 2.571
```

Reject .

```text
H 0
```

P-value also says:

```text
0.021 < 0.05
```

Reject .

```text
H 0
```

Final meaning:  
Baths have a significant effect on house price.

## Choosing Alpha and Reading p-Values
### 1. What is ? α

```text
α
```

is called the level of significance.  
Simple meaning:  
α = maximum risk of rejecting H when H is actually true

```text
0 0
```

In very easy words:  
Alpha is the allowed mistake level.  
Usually:

```text
α = 0.05
```

means:

```text
5%
```

So we are saying:  
“I am willing to take a 5% risk of making a wrong rejection of .”

```text
H 0
α = 0.05
```

In the notes, the test uses .

### 2. How do we decide the value of ? α

Usually, the question gives it.  
Example:  
“Test at 5% level of significance.”  
That means:

```text
α = 0.05
```

If question says:  
“Test at 1% level of significance.”  
Then:

```text
α = 0.01
```

If question says:  
“Test at 10% level of significance.”  
Then:

```text
α = 0.10
```

If exam question does not mention , most of the time we use:

```text
α
α = 0.05
```

because 5% is the most common value.

### α = 0.05 3. Why is common?

Because it is a balanced choice.

```text
α = 0.10
```

means 10% risk. This is more relaxed.

```text
α = 0.05
```

means 5% risk. This is standard.

```text
α = 0.01
```

means 1% risk. This is very strict.  
Simple meaning:

| Alpha | Meaning | Strictness |
|---|---|---|
| 0.10 | 10% mistake risk | less strict |
| 0.05 | 5% mistake risk | common/standard |
| 0.01 | 1% mistake risk | very strict |

### 4. What is p-value again?

P-value means:  
If is true, what is the chance of getting this result or an even more extreme

```text
H 0
```

result?  
For example, for baths:

```text
H 0 : β 2 = 0
```

This means:  
Baths have no real effect.  
But sample gave:

```text
t = 2.68
```

So p-value asks:

```text
t = 2.68
```

“If baths really have no effect, what is the chance of getting or more extreme?”  
If this chance is small, we reject .

```text
H 0
```

### 5. Why you did not find p-value in t-table?

Because many t-tables do not directly give p-value.  
Most t-tables give critical values, like:

```text
t 0.025,5 = 2.571
```

This tells the boundary value.  
But p-value is the area/probability beyond your calculated t-value.  
Some detailed t-tables give p-value ranges, but many basic tables do not.  
So in exams, if you only have a t-table, use the critical value approach.  
That means compare:  
tcalculated  
with:  
tcritical

### 6. How to get p-value by calculator?

For regression beta tests, use:

```text
df = n −p
```

In this example:

```text
n = 8
p = 3
df = 8 −3 = 5
```

For two-tailed p-value:  
p-value = 2P(T > ∣t∣)  
For baths:

```text
t = 2.68
df = 5
```

So:  
p-value = 2P(T > 2.68)  
Using calculator/software:

```text
p ≈0.0438
```

So:

```text
p ≈0.044
```

Important correction:

```text
0.021 t = 2.68
```

The notes show about for . That is approximately the one-tailed p-value. But because the hypothesis is:

```text
H 1 : β 2 0 =
```

this is a two-tailed test, so the two-tailed p-value is approximately:

```text
2(0.0219) = 0.0438
```

Still:

```text
0.0438 < 0.05
```

So the final decision is still the same:  
Reject H

```text
0
```

### 7. Calculator method using Excel

If you have Excel, write:  
=T.DIST.2T(ABS(t), df)  
For baths:

```text
=T.DIST.2T(ABS(2.68),5)
```

Answer:

```text
0.0438
```

For one-tailed p-value:

```text
=T.DIST.RT(2.68,5)
```

Answer:

```text
0.0219
```

But for your regression test:

```text
H 1 : β =0
```

Use the two-tailed one.

### 8. Calculator method using t CDF

If your calculator has t CDF, use this idea:  
For positive :

```text
t
```

p-value = 2 × P(T > t)  
So for baths:

```text
p = 2 × P(T > 2.68)
```

Calculator input idea:

```text
tcdf(2.68, very large number, 5)
```

Then multiply answer by 2.  
For example:

```text
P(T > 2.68) ≈0.0219
```

So:

```text
p = 2(0.0219) = 0.0438
```

### 9. If calculator does not have t-distribution?

Then do not worry.  
Use critical value approach.  
For baths:

```text
t = 2.68
```

Critical value:

```text
2.571
```

Since:

```text
2.68 > 2.571
```

Reject .

```text
H 0
```

This is enough for exam if p-value is not required.

### 10. What if t-value is equal to critical value?

Suppose:

```text
∣t∣= t critical
```

Example:

```text
∣t∣= 2.571
```

and:

```text
= 2.571
```

tcritical  
Then use this rule:

```text
⇒
```

∣t∣≥t Reject H  
critical 0  
So if equal:  
Reject H

```text
0
```

But write carefully:  
The result is exactly on the rejection boundary, so we reject using the usual

```text
H 0
```

rule.

### 11. What if p-value is equal to alpha?

Suppose:

```text
p = α
```

Example:

```text
p = 0.05
α = 0.05
```

Use this rule:  
p ≤α ⇒Reject H

```text
0
```

So if equal:  
Reject H

```text
0
```

But again, it is a boundary case.  
Exam wording:  
Since p-value is equal to , it lies on the rejection boundary; therefore, reject .

```text
α H 0
```

### 12. Why both equality cases reject ? H 0

Because rejection region includes the boundary.  
Critical value rule:

```text
∣t∣≥t c
```

P-value rule:

```text
p ≤α
```

So equality is included in rejection.

### 13. Very simple decision rules Critical value method

```text
∣t∣≥t c
```

Reject .

```text
H 0
∣t∣< t c
```

Do not reject .

```text
H 0
```

### P-value method

```text
p ≤α
```

Reject .

```text
H 0
p > α
```

Do not reject .

```text
H 0
```

### 14. Apply to baths example

For baths:

```text
t = 2.68
t c = 2.571
```

Since:

```text
2.68 > 2.571
```

Reject .

```text
H 0
```

Using p-value:

```text
p ≈0.0438
α = 0.05
```

Since:

```text
0.0438 < 0.05
```

Reject .

```text
H 0
```

Conclusion:  
is significant

```text
β 2
```

Meaning:  
Baths have a significant effect on house price.

### 15. Baby explanation

Alpha is your allowed mistake risk.  
Usually:

```text
α = 0.05
```

means:  
“I allow 5% risk.”  
P-value is the actual chance of getting your result if is true.

```text
H 0
```

If p-value is smaller than alpha:  
result is too unlikely  
So reject .

```text
H 0
```

For baths:

```text
p = 0.0438
α = 0.05
```

Because:

```text
0.0438 < 0.05
```

we reject .

```text
H 0
```

Final meaning:  
The bath variable is statistically significant.

## p-Value on a Casio fx-991ES Plus

Your calculator issue is very normal: many basic t-tables do not list exact p-values, and the fx-991ES Plus usually cannot directly calculate t-distribution p-values like software does.  
Casio fx-991ES Plus usually cannot directly calculate exact t-test p-values. So for the exam, use the critical value approach from the t-table. That is enough.  
Casio’s ES Plus distribution mode lists normal, binomial, and Poisson distribution calculations, but not Student’s t-distribution p-value calculation.  
CASIO Official W…

### 1. Why you did not find exact p-value in t-table?

Most t-tables do not give exact p-values.  
They give critical values.

```text
df = 5
α = 0.05
```

two-tailed test:

```text
t 0.025,5 = 2.571
```

So your table tells:

```text
2.571
```

It does not directly tell:

```text
p = 0.0438
```

That exact p-value usually comes from software, Excel, advanced calculator, or online calculator.

### 2. What should you do in exam with fx-991ES Plus?

Use critical value method, not p-value method.  
For baths:

```text
t = 2.68
```

Critical value:

```text
t c = 2.571
```

Compare:

```text
2.68 > 2.571
```

So:  
Reject H

```text
0
```

Conclusion:  
is significant

```text
β 2
```

Meaning:  
Baths have significant effect on house price.

### 3. Then why notes mention p-value?

The notes show p-value approach as another method for parameter testing. But if the calculator/table does not give exact p-value, you do not need to use that method. The notes also use critical value approach, p-value approach, and confidence interval approach for testing regression parameters.  
In exam, you can write:  
Since exact p-value is not available from the t-table, we use the critical value approach.  
That is acceptable.

### 4. Can we still estimate p-value from t-table?

approximately.

```text
df = 5
```

For :  
Two-tailedα Critical t-value

|  | 0.10 | 2.015 |
|---|---|---|
|  | 0.05 | 2.571 |
|  | 0.02 | 3.365 |
|  | 0.01 | 4.032 |

Your calculated value:

```text
t = 2.68
```

Now compare:

```text
2.571 < 2.68 < 3.365
```

So:

```text
0.02 < p < 0.05
```

Meaning:  
p-value is between 0.02 and 0.05.  
That is enough to reject at:

```text
H 0
α = 0.05
```

Because p-value is less than 0.05.

### 5. Exact p-value for baths

For baths:

```text
t = 2.68
df = 5
```

Two-tailed p-value is approximately:

```text
p ≈0.0438
```

So:

```text
0.0438 < 0.05
```

Reject .

```text
H 0
```

But again, you do not need this exact p-value if your calculator cannot calculate it.

### 6. What about fx-991ES Plus?

Your calculator can help with arithmetic, like:

```text
10957
t =
4086.09
```

On calculator:

```text
10957 ÷ 4086.09 =
```

Answer:

```text
2.68
t = 2.68
```

But it cannot easily convert that into exact p-value for Student’s t-distribution.  
So use t-table:

```text
t = 2.68
```

Compare with:

```text
t c = 2.571
```

Decision:

```text
2.68 > 2.571
```

Reject .

```text
H 0
```

### 7. What if t-value is equal to critical value?

If:

```text
∣t∣= t c
```

Example:

```text
∣t∣= 2.571
```

Then use:

```text
⇒
```

∣t∣≥t Reject H

```text
c 0
```

So if equal:  
Reject H

```text
0
```

But write:  
The value lies exactly on the rejection boundary, so is rejected using the

```text
H 0
```

usual rule.

### 8. What if p-value is equal to alpha?

If:

```text
p = α
```

Example:

```text
p = 0.05
α = 0.05
```

Use:  
p ≤α ⇒Reject H

```text
0
```

So if equal:  
Reject H

```text
0
```

Again, it is a boundary case.

### 9. Final exam rule for you

Use this simple method:

### If question asks critical value approach

∣t∣≥t ⇒ Reject H

```text
c 0
⇒
```

∣t∣< t Do not reject H

```text
c 0
```

### If question asks p-value approach but exact p-value is not available

Use table range.  
Example:

```text
2.571 < 2.68 < 3.365
```

So:

```text
0.02 < p < 0.05
```

Since:

```text
p < 0.05
```

Reject .

```text
H 0
```

### 10. Baby summary

Your calculator is not the problem.  
The fx-991ES Plus is not good for exact t-test p-values.  
So do this:  
1. Calculate  using calculator.

```text
t
```

2. Find critical value from t-table.  
3. Compare.  
4. Decide.  
For baths:

```text
t = 2.68
t c = 2.571
2.68 > 2.571
```

Final answer:  
Reject H

```text
0
```

Baths are significant.

## Calculating the p-Value Manually

You can calculate an approximate p-value manually, but exact p-value needs t-distribution software/calculator because it comes from area under a curve. For exams, table range or interpolation is normally enough.  
we can calculate p-value manually approximately, but exact p-value is difficult manually because it is the area under the t-distribution curve.  
For the exam, you usually use:  
1. t-table range method — easy and accepted.  
2. Interpolation method — gives approximate p-value.  
3. Exact calculation — needs software/advanced calculator.  
The notes use p-value approach for regression parameter testing, but with an fx-991ES Plus, table-based approximation is the practical method.

### 1. Example: Baths test

For baths:

```text
t = 2.68
df = 5
```

Because:

```text
df = n −p = 8 −3 = 5
```

Hypotheses:

```text
H 0 : β 2 = 0
H 1 : β 2 0 =
```

Since has:

```text
H 1
=
```

this is a two-tailed test.

### 2. Method 1: Simple t-table range method

```text
df = 5
```

For , t-table values are usually like this:

|  | Two-tailed p-value | t-value |
|---|---|---|
|  | 0.10 | 2.015 |
|  | 0.05 | 2.571 |
|  | 0.02 | 3.365 |
|  | 0.01 | 4.032 |

Our calculated value is:

```text
t = 2.68
```

Now compare:

```text
2.571 < 2.68 < 3.365
```

This means:

```text
0.02 < p < 0.05
```

So p-value is between 0.02 and 0.05.  
Since:

```text
p < 0.05
```

we reject .

```text
H 0
```

Final conclusion:  
is significant

```text
β 2
```

Meaning:  
Baths significantly affect house price.

### 3. Method 2: Manual approximate p-value using interpolation

We know:

```text
t = 2.571 ⇒p = 0.05
t = 3.365 ⇒p = 0.02
```

Our value:

```text
t = 2.68
2.68 2.571 3.365
```

So lies between and .

### 2.68 2.571 Step 1: Find how far is from

```text
2.68 −2.571 = 0.109
```

### Step 2: Find total distance between table values

```text
3.365 −2.571 = 0.794
```

### Step 3: Find fraction

```text
0.109
= 0.137
0.794
2.68 2.571 3.365
```

This means is about 13.7% of the way from to .

### Step 4: Difference between p-values

```text
0.05 −0.02 = 0.03
```

### Step 5: Multiply

```text
0.137 × 0.03 = 0.00411
```

### Step 6: Subtract from 0.05

Because as t-value increases, p-value decreases:

```text
p ≈0.05 −0.00411
p ≈0.04589
```

So approximate p-value:

```text
p ≈0.046
```

Exact software value is close, around:

```text
p ≈0.044
```

Your manual table estimate is good enough.

### 4. Decision using this p-value

```text
p ≈0.046
α = 0.05
```

Compare:

```text
0.046 < 0.05
```

So:  
Reject H

```text
0
```

Conclusion:  
is significant

```text
β 2
```

### p = 0.021 5. Why notes may show ?

```text
0.021
```

Because is approximately the one-tailed p-value.  
But your hypothesis is:

```text
H 1 : β 2 0 =
```

That means two-tailed test.  
So:  
= 2 × pone-tailed  
ptwo-tailed

```text
≈ 2(0.021)
```

ptwo-tailed

```text
≈ 0.042
```

ptwo-tailed  
Still less than:

```text
0.05
```

So final decision remains the same:  
Reject H

```text
0
```

### 6. Can we calculate exact p-value by hand?

Technically yes, but practically no for exams.  
Exact p-value comes from this idea:

```text
p = 2P(T > ∣t∣)
```

For baths:

```text
p = 2P(T > 2.68)
```

This means:

```text
2.68
```

Find the area under the t-distribution curve after , then multiply by 2.  
But calculating that area manually requires integration. That is not expected in a normal statistics exam.  
So use table or interpolation.

### 7. Exam-safe answer

If they ask p-value and you only have t-table, write:

```text
t = 2.68, df = 5
```

From t-table:

```text
t 0.025,5 = 2.571
t 0.01,5 = 3.365
```

Since:

```text
2.571 < 2.68 < 3.365
```

Therefore:

```text
0.02 < p < 0.05
```

Since:

```text
p < 0.05
```

Reject .

```text
H 0
```

Conclusion:  
\boxed{\text{Baths are significant at 5% level of significance.}}

### 8. Baby summary

Exact p-value manually is hard.  
But approximate p-value manually is easy:  
Use t-table.  
For baths:

```text
t = 2.68
```

In table:

```text
2.571 ⇒p = 0.05
3.365 ⇒p = 0.02
```

Since:

```text
2.68
```

is between them:

```text
0.02 < p < 0.05
```

So:

```text
p < 0.05
```

Reject .

```text
H 0
```

Final:  
Baths significantly affect house price.

## Without Any p-Value Table

then do not use p-value approach.  
If you do not know p-value against t-value, use the critical value approach instead.

```text
, β , β
```

This is why the notes also show the critical value method for testing .

```text
β 0 1 2
```

### Main idea

There are 3 ways to test:  
1. Critical value approach  
2. P-value approach  
3. Confidence interval approach  
You do not need all three. Any one method is enough.

### If p-value is not available, do this

For example, baths:

```text
t = 2.68
df = 5
α = 0.05
```

Two-tailed test:

```text
t c = 2.571
```

Now compare:

```text
∣t∣≥t c
2.68 ≥2.571
```

So:  
Reject H

```text
0
```

Conclusion:  
is significant

```text
β 2
```

Meaning:  
Baths have significant effect on house price.

### What if you do not know p-value at all?

Then write in exam:  
Since exact p-value is not available, we use critical value approach.  
Then continue:

```text
⇒
```

∣t∣≥t Reject H

```text
c 0
```

∣t∣< t ⇒ Do not reject H

```text
c 0
```

### What if you do not even have critical value?

Then you cannot make a proper statistical decision.  
You need at least:

```text
t
df
α
```

and either:  
- t-table critical value, or  
- p-value from calculator/software.  
Without table/software, you can only say:

```text
t = 2.68
```

but you cannot formally decide reject/not reject.

### Important exam shortcut

If the table gives:

```text
t 0.025,5 = 2.571
```

That already means:

```text
α = 0.05
```

For two-tailed , critical value is:

```text
2.571
```

So you do not need p-value.

### Baby explanation

P-value is one method.  
Critical value is another method.  
If p-value is not available, no problem.  
Use this:  
Compare calculated t with critical t  
For baths:

```text
2.68 > 2.571
```

So:  
Reject H

```text
0
```

Final meaning:  
Baths are significant.

## Is There a Formula for the p-Value?

p-value formula exists, but it is not a simple formula like mean, variance, or t- value.  
For a t-test, p-value comes from the t-distribution area.  
Your test statistic in the notes is based on:

```text
t = β^j −β j
se( β^j )
```

Usually under :

```text
H 0
β j = 0
```

so:

```text
β^j
t =
se( β^j )
```

This is the same testing idea used in your regression notes for .  
, β , β

```text
β 0 1 2
```

### 1. General p-value formula for t-test

For a two-tailed test:

```text
H 0 : β j = 0
H 1 : β j 0 =
```

The p-value formula is:

```text
p = 2P(T > ∣t∣)
```

or:

```text
p = 2[1 −F t (∣t∣)]
```

Where:

| Symbol | Meaning |
|---|---|
|  | p-value |

p

|  | t-distribution random variable |
|---|---|

T

|  | calculated t-value |
|---|---|

t

|  | cumulative t-distribution function |
|---|---|

Ft

|  | degrees of freedom |
|---|---|

df

### 2. For your baths example

For baths:

```text
t = 2.68
df = 5
```

Because:

```text
df = n −p = 8 −3 = 5
```

Since it is two-tailed:

```text
p = 2P(T > 2.68)
```

or:

```text
p = 2[1 −F t (2.68)]
```

This is the formula.  
But the hard part is this:

```text
F t (2.68)
```

cannot be calculated easily by normal arithmetic.

### 3. Why is it hard manually?

```text
(t)
```

Because means area under the t-distribution curve.

```text
F t
```

The t-distribution formula is:  
v+1

```text
f(t) = Γ ( v+1) 2 ( 1 + t2 ) − 2
vπ Γ ( 2 v) v
```

Where:

```text
v = df
```

To get p-value, we need area:

```text
∞
P(T > t) = ∫ f(x) dx
t
```

So for baths:

```text
∞
P(T > 2.68) = ∫ f(x) dx
2.68
```

This is why exact p-value is usually found using:  
- t-table  
- software  
- Excel  
- scientific calculator with t-distribution  
- online calculator  
Not by normal hand calculation.

### 4. Easy exam answer

If someone asks:  
Can we calculate p-value by formula?  
Write:

```text
p = 2P(T > ∣t∣)
```

or:

```text
p = 2[1 −F t (∣t∣)]
```

Then say:  
The value is obtained from t-distribution table or statistical software.  
That is the correct academic answer.

### 5. Manual approximate method using t-table

```text
df = 5
```

For , suppose your t-table gives:

|  | Two-tailed p-value | t-value |
|---|---|---|
|  | 0.05 | 2.571 |
|  | 0.02 | 3.365 |

Your calculated value:

```text
t = 2.68
```

Now:

```text
2.571 < 2.68 < 3.365
```

So:

```text
0.02 < p < 0.05
```

That means p-value is less than:

```text
0.05
```

So:  
Reject H

```text
0
```

### 6. Approximate p-value by interpolation

You can estimate it.  
Known table points:

```text
t = 2.571 ⇒p = 0.05
t = 3.365 ⇒p = 0.02
```

Your value:

```text
t = 2.68
```

Distance from lower t-value:

```text
2.68 −2.571 = 0.109
```

Total distance:

```text
3.365 −2.571 = 0.794
```

Fraction:

```text
0.109
= 0.137
0.794
```

Difference in p-values:

```text
0.05 −0.02 = 0.03
```

Decrease in p-value:

```text
0.137(0.03) = 0.00411
```

Estimated p-value:

```text
p ≈0.05 −0.00411
p ≈0.0459
```

So:

```text
p ≈0.046
```

Actual software value is about:

```text
p ≈0.044
```

So manual approximation is close.

### 7. Important point

There is no simple direct formula like:

```text
t
p =
df
```

or:

```text
1
p =
t
```

No.  
The formula exists, but it uses area under t-distribution.  
So for exams, use:

```text
p = 2P(T > ∣t∣)
```

and then get the probability from table/software.

### 8. Baby explanation

p-value is an area.  
t-value is a point.  
Example:

```text
t = 2.68
```

This is one point on the t-axis.  
p-value asks:  
How much area is after this point on both sides?  
That area is the p-value.  
So we need t-distribution table/software to find the area.  
Final simple answer:  
p-value has a formula, but exact calculation needs t-distribution area.  
For exam:

```text
p = 2P(T > ∣t∣)
```

For your baths example:

```text
p = 2P(T > 2.68)
```

Approximately:

```text
p ≈0.044
```

So:  
p < 0.05 ⇒Reject H

```text
0
```

|  | vπΓ(2v) |
|---|---|

## Evaluating the Gamma Function

This gamma part looks scary, but it is only needed if someone tries to derive the exact t- distribution curve. For the exam, you normally do not solve gamma to get p-value manually.  
You are asking about this part of the t-distribution formula:

```text
Γ ( v + 1)
2
```

and also this denominator part:

```text
vπ Γ (2 v )
```

Here:

```text
v = df
```

For this example:

```text
v = 5
```

because:

```text
df = n −p = 8 −3 = 5
```

### Γ 1. What is Gamma ?

Gamma is like an extended factorial.  
For whole numbers:

```text
Γ(n) = (n −1)!
```

So:

```text
Γ(1) = 0! = 1
Γ(2) = 1! = 1
Γ(3) = 2! = 2
Γ(4) = 3! = 6
```

Simple meaning:

```text
Γ(n)
```

is almost factorial, but one number less.

### 2. Important rule

```text
Γ(n + 1) = nΓ(n)
```

This is the main rule.  
Example:

```text
Γ(3) = 2Γ(2)
Γ(2) = 1
```

So:

```text
Γ(3) = 2(1) = 2
```

### 3. Special value

You must remember this special value:

```text
Γ (2 1) = π
```

This is used when the input is a half value like:

```text
3 5 7
, ,
2 2 2
```

### v+1) Γ 4. How to solve ( 2

In this example:

```text
v = 5
```

So:

```text
Γ ( v + 1) = Γ ( 5 + 1)
2 2
= Γ (2 6)
= Γ(3)
```

Now use:

```text
Γ(n) = (n −1)!
```

So:

```text
Γ(3) = 2!
Γ(3) = 2
```

So:

```text
Γ ( v + 1) = 2
2
```

when:

```text
v = 5
```

### v) Γ 5. How to solve ( 2

Again:

```text
v = 5
```

So:

```text
Γ (2 v ) = Γ (2 5)
```

Now:

```text
5
= 2.5
2
```

This is a half-integer, so use:

```text
Γ(n + 1) = nΓ(n)
```

Write:

```text
3
Γ (2 5) = Γ (2 3)
2
```

Now:

```text
1
Γ (2 3) = Γ (2 1)
2
```

And:

```text
Γ (2 1) = π
```

So:

```text
1
Γ (2 3) = π
2
```

Now put this back:

```text
3 1
Γ (2 5) = ⋅ π
2 2
3
= π
4
```

So:

```text
3
Γ (2 5) = π
4
```

### 6. Now solve denominator part

The denominator is:

```text
vπ Γ (2 v )
```

For:

```text
v = 5
vπ = 5π
```

and:

```text
Γ (2 v ) = Γ (2 5) = 3 π
4
```

So denominator becomes:

```text
3
5π ⋅ π
4
```

That is:

```text
3
5π π
4
```

Since:

```text
5π π = 5π2
= π 5
```

So denominator is:

```text
3
π 5
4
```

### v = 5 7. Full constant part for

The t-distribution formula has this constant:

```text
Γ ( v+1) 2
vπ Γ ( 2 v)
```

For:

```text
v = 5
```

Numerator:

```text
Γ ( 5 + 1) = Γ(3) = 2
2
```

Denominator:

```text
3
5π Γ (2 5) = π 5
4
```

So:

```text
2
3 4 π 5
```

Dividing by a fraction means multiply by reciprocal:

```text
4
2 ×
3π 5
8
=
3π 5
```

So the constant part is:

```text
8
3π 5
```

### 8. But important: this still does not give p-value easily

Even after solving gamma, you only get the t-distribution curve formula.  
To get p-value, you still need area:

```text
p = 2P(T > ∣t∣)
```

For baths:

```text
p = 2P(T > 2.68)
```

That means:

```text
∞
p = 2 ∫ f(t) dt
2.68
```

This integration is difficult manually.  
So in exams, you do not calculate p-value through gamma formula.  
You use:  
- t-table,  
- critical value approach,  
- or p-value given by software/calculator.

### 9. Easy rule for Gamma values If input is whole number

```text
Γ(n) = (n −1)!
```

Examples:

```text
Γ(5) = 4! = 24
Γ(4) = 3! = 6
```

### If input is half number

Use:

```text
Γ (2 1) = π
```

Then move upward.  
Examples:

```text
1
Γ (2 3) = π
2
3 1 3
Γ (2 5) = ⋅ π = π
2 2 4
5 3 1 15
Γ (2 7) = ⋅ ⋅ π = π
2 2 2 8
```

### 10. Baby explanation

Gamma is like factorial.  
But:

```text
Γ(3)
```

means:

```text
2!
```

not:

```text
3!
```

So:

```text
Γ(3) = 2
```

For half numbers:

```text
Γ (2 1) = π
```

Then keep multiplying backward/forward.  
For your case:

```text
v = 5
Γ ( v + 1) = Γ(3) = 2
2
Γ (2 v ) = Γ (2 5) = 3 π
4
```

But for exam decision, avoid this difficult method.  
Use this instead:  
∣t∣≥t ⇒ Reject H

```text
c 0
```

For baths:

```text
2.68 > 2.571
```

So:  
Reject H

```text
0
```

Final:  
Baths are significant.

## Main Solving Techniques by Question Type

good idea. These 5 questions are mostly the same type. You do not need to solve all separately. Learn the main techniques, then apply them to any question.  
In these questions, the repeated topic is:  
Multiple Linear Regression  
General model:

```text
y^ = a + b 1 x 1 + b 2 x 2 + ⋯+ b k x k
```

### 1. First identify repeated parts

Almost every question asks these same parts:

| Part | What it asks | Method |
|---|---|---|
| (a) | Fit multiple regression model | Normal equations / matrix method |
| (b) | Predict value of | Put given -values in equation |

y x  
R2 SSR, SSE, SST

| (c) | Find | / correlation | Use | formulas |
|---|---|---|---|---|
| (d) | Test parameters | t-test for each beta |  |  |

So you only need to learn 4 techniques.

### Technique 1: Fit Multiple Linear Regression Model

Use this when question says:  
Fit a multiple linear regression model.  
For two independent variables:

```text
y^ = a + b 1 x 1 + b 2 x 2
```

For four independent variables:

```text
y^ = a + b 1 x 1 + b 2 x 2 + b 3 x 3 + b 4 x 4
```

### Matrix formula

```text
B^ = (X X) T −1 X Y T
```

Where:

```text
a
B^ = b 1
b 2
```

or for more variables:

```text
a
b 1
B^ = b 2
b 3
b 4
```

### Important

In matrix, first column is always 1.

```text
X
```

Example for two variables:

```text
1 x 11 x 12
X = 1 x 21 x 22
1 x 31 x 32
```

Why first column is 1?  
Because of intercept .

```text
a
```

### Technique 2: Prediction

Use this when question says:

```text
, x , x
```

Estimate / predict  when are given.

```text
y x 1 2 3
```

After finding regression equation:

```text
y^ = a + b 1 x 1 + b 2 x 2
```

Just put values.  
Example form:

```text
y^ = a + b 1 (2400) + b 2 (1200)
```

Do not do a new regression calculation for prediction.  
Prediction means:  
Put given x-values into the fitted equation

### R2 Technique 3: Coefficient of Determination

Use this when question says:  
Find coefficient of determination and interpret it.  
Formula:

```text
R = 2 SSR
SST
```

or:

```text
R = 2 1 − SSE
SST
```

Where:

```text
SST = ∑ (y − yˉ 2 )
SSE = ∑ (y − y^ 2 )
SSR = ∑y^ ( − yˉ 2 )
```

Also:

```text
SST = SSR + SSE
```

### Interpretation

If:

```text
R = 2 0.92
```

then say:  
92% variation in  is explained by the independent variables. Remaining 8% is

```text
y
```

due to other factors/error.  
Do not say:  
“The model is 92% accurate.”  
That is wrong wording.

### Technique 4: Multiple Correlation CoefficientR

```text
R2
```

Some answer keys give  or , not .

```text
r R
```

Formula:

```text
R = R2
```

If question asks coefficient of determination, use:

```text
R2
```

If question asks coefficient of multiple correlation, use:

```text
R
```

Example:

```text
R = 2 0.846
```

Then:

```text
R = 0.846
```

Interpretation:  
There is a strong positive relationship between actual  and predicted .

```text
y y
```

### Technique 5: Testing Parameters of Multiple Regression

Use this when question says:  
Test the parameters of the multiple linear regression model.  
You test every coefficient:

```text
β 0 , β 1 , β , … 2
```

### Step 1: Hypotheses

For each coefficient:

```text
H 0 : β j = 0
H 1 : β j 0 =
```

Meaning:  
: variable has no effect

```text
H 0
```

: variable has effect

```text
H 1
```

### Step 2: Test statistic

```text
β^j −0
t =
se( β^j )
```

Usually:

```text
β^j
t =
se( β^j )
```

### Step 3: Degrees of freedom

```text
df = n −p
```

Where:  
n = number of rows  
p = number of parameters including intercept  
Example:  
If model is:

```text
y^ = a + b 1 x 1 + b 2 x 2
```

then:

```text
p = 3
```

because parameters are:

```text
a, b 1 , b 2
```

If there are 12 rows:

```text
df = 12 −3 = 9
```

### Step 4: Critical value

For two-tailed test:

```text
t c = t α/2,df
```

If:

```text
α = 0.05
```

then:

```text
α/2 = 0.025
```

Use t-table.

### Step 5: Decision

```text
⇒
```

∣t∣≥t Reject H

```text
c 0
```

∣t∣< t ⇒ Do not reject H

```text
c 0
```

If reject , say:

```text
H 0
```

The parameter is significant  
If do not reject , say:

```text
H 0
```

The parameter is not significant

### Distinct Question Types in Your Sheet

You only need to practice these distinct types:

### Type A: 2-variable regression

Example structure:

```text
y^ = a + b 1 x 1 + b 2 x 2
```

Questions 1, 2, and 3 are like this.  
Use same method.

### Type B: 3-variable regression

Example structure:

```text
y^ = a + b 1 x 1 + b 2 x 2 + b 3 x 3
```

Question 4 is like this.  
Same method, only one extra .

```text
x
```

### Type C: 4-variable regression

Example structure:

```text
y^ = a + b 1 x 1 + b 2 x 2 + b 3 x 3 + b 4 x 4
```

Question 5 is like this.  
Same method, but matrix is bigger.

### Main formula list for exam Regression model

```text
y^ = a + b 1 x 1 + b 2 x 2 + ⋯+ b k x k
```

### Matrix formula

```text
B^ = (X X) T −1 X Y T
```

### Prediction

```text
y^ = a + b 1 x 1 + b 2 x 2 + ⋯+ b k x k
```

### Error

```text
e = y − y^
```

### SSE

```text
SSE = ∑ e 2
```

### SST

```text
SST = ∑ (y − yˉ 2 )
```

### SSR

```text
SSR = SST −SSE
```

or:

```text
SSR = ∑y^ ( − yˉ 2 )
```

### Coefficient of determination

```text
R = 2 SSR
SST
```

or:

```text
R = 2 1 − SSE
SST
```

### Multiple correlation coefficient

```text
R = R2
```

### Error variance

```text
s = 2 SSE
n −p
```

### Variance-covariance matrix

```text
C = s (X X) 2 T −1
```

### Standard error

β^j diagonal element of C

```text
se( ) =
```

### t-test

```text
β^j
t =
se( β^j )
```

### Degrees of freedom

```text
df = n −p
```

### Exam solving order

For any question, follow this order:  
1. Write the regression model.  
2. Make matrix with first column 1.

```text
X
```

3. Make column.

```text
Y
```

4. Calculate:

```text
X X T
```

5. Calculate:

```text
X Y T
```

6. Use:

```text
B^ = (X X) T −1 X Y T
```

7. Write final regression equation.  
8. For prediction, put given -values.

```text
x
R2 SSE, SST, SSR
```

9. For , calculate .  
10. For testing, use t-test.

### Most important shortcut

All 5 questions are not different.  
The only difference is number of independent variables.

|  | Number of independent |  |
|---|---|---|
| Question | variables | Model form |

a + b  
Q1 | 2 x b x  
1 1 2 2  
a + b  
Q2 | 2 x b x  
1 1 2 2  
a + b  
Q3 | 2 x b x  
1 1 2 2  
a + b  
Q4 | 3 x b x b x  
1 1 2 2 3 3  
+ + +  
a + b  
Q5 | 4 x b x b x b x  
1 1 2 2 3 3 4 4  
So for practice:  
Do one 2-variable question, then one 3-variable question, then one 4-variable question.  
That will cover all methods.

## Why Use the Coefficient of Determination

We use coefficient of determination because it tells:  
How much of the change/variation in Y  is explained by the regression model.  
It is written as:

```text
R2
R2
```

Your regression notes also use to interpret how much variation in house price is explained by bedrooms and baths.

### R2 1. Simple meaning of

Suppose:  
Y = house price  
and independent variables are:  
= bedrooms

```text
X 1
```

= baths

```text
X 2
```

Now house prices are different for different houses.  
Some houses are expensive.  
Some houses are cheap.  
So there is variation in house prices.  
R2tells:  
How much of that variation is explained by bedrooms and baths.

### 2. Example

If:

```text
R = 2 0.98
```

Then:

```text
0.98 × 100 = 98%
```

Meaning:

```text
98%
```

of the variation in house price is explained by bedrooms and baths.  
Remaining:

```text
100% −98% = 2%
```

So:

```text
2%
```

is due to other factors, like:  
- location  
- house size  
- condition  
- market demand  
- error/randomness

### R2 3. Why do we need ?

Because only finding the regression equation is not enough.  
Example:

```text
Y^ = 224929 + 15314X 1 + 10957X 2
```

This gives prediction, but we also need to know:  
Is this model explaining the data well or badly?  
That is why we use:

```text
R2
```

### 4. Formula

```text
R = 2 SSR
SST
```

or:

```text
R = 2 1 − SSE
SST
```

Where:  
SST = total variation in Y  
SSR = variation explained by regression  
SSE = variation not explained by regression

### 5. Baby explanation

Think like this:  
Total variation in house prices = 100%.  
Regression tries to explain this variation.  
If:

```text
R = 2 0.80
```

then model explains:

```text
80%
```

and cannot explain:

```text
20%
```

So:

```text
2
```

R  tells model explanation power.

### 6. Important exam wording

Do not write:  
“Model is 98% accurate.”  
Better write:  
98% of the variation in Y  is explained by the independent variables.  
That is the correct interpretation.

### 7. Short final answer

We use coefficient of determination because it tells how good the regression model is at explaining variation in the dependent variable.

```text
R2
```

High :  
model explains data well

```text
R2
```

Low :  
model does not explain data well
