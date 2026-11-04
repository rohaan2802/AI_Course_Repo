# K-Means Clustering Steps

## Steps of K-Means Clustering
#### What is K-Means Clustering?

K-Means is an unsupervised machine learning algorithm that groups similar data points into K clusters.  
Think of it like:  
"Put similar things together in different groups."  
For example, if you have students' marks, K-Means can automatically make groups such as:  
- High performers  
- Average performers  
- Low performers

### Steps of K-Means Clustering

Suppose we have these students' marks:

| Student | Marks |
|---|---|
| A | 10 |
| B | 12 |
| C | 15 |
| D | 70 |
| E | 75 |
| F | 80 |

We want K = 2 clusters.

### Step 1: Choose K

Decide how many groups (clusters) you want.  
Here:  
K = 2  
So we want:  
- Cluster 1  
- Cluster 2

### Step 2: Select Initial Centroids

A centroid is the center of a cluster.  
Randomly choose two points as centroids.  
- Centroid 1 = 10  
- Centroid 2 = 70

```text
Cluster 1 Center = 10
Cluster 2 Center = 70
```

### Step 3: Calculate Distance

Find distance from every point to each centroid.  
Distance formula:  
Distance = ∣x −c∣  
where:  
- x = data point  
- c = centroid

#### For Student B (12)

Distance from Centroid 1:
| 12 − 10 | = 2 |
|---|---|

Distance from Centroid 2:
| 12 − 70 | = 58 |
|---|---|

Since 2 is smaller:  
Put 12 in Cluster 1

#### For Student D (70)

Distance from Centroid 1:
| 70 − 10 | = 60 |
|---|---|

Distance from Centroid 2:
| 70 − 70 | = 0 |
|---|---|

Since 0 is smaller:  
Put 70 in Cluster 2  
Doing this for all points:

#### Cluster 1

```text
10, 12, 15
```

#### Cluster 2

```text
70, 75, 80
```

### Step 4: Recalculate Centroids

Find the average of each cluster.

#### New Centroid 1

```text
10 + 12 + 15 = 12.33
3
```

#### New Centroid 2

```text
70 + 75 + 80
= 75
3
```

New centers:

```text
Centroid 1 = 12.33
Centroid 2 = 75
```

### Step 5: Assign Points Again

Now calculate distances using the new centroids.  
Check whether any point should move to another cluster.

#### Example: 15

Distance to 12.33  
= 2.67  
Distance to 75  
= 60  
Still belongs to Cluster 1.  
After checking all points:

```text
Cluster 1 = 10,12,15
Cluster 2 = 70,75,80
```

No point changes cluster.

### Step 6: Stop

When:  
- No points change clusters, OR  
- Centroids stop changing  
The algorithm stops.  
These are the final clusters.

#### Cluster 1 (Low Marks)

```text
10
12
15
```

Centroid = 12.33

#### Cluster 2 (High Marks)

```text
70
75
80
```

Centroid = 75

### Easy Real-Life Example

Imagine a teacher has students' marks:

```text
20, 25, 30, 85, 90, 95
```

K-Means automatically creates:

#### Group 1

```text
20,25,30
```

(Weak students)

#### Group 2

```text
85,90,95
```

(Strong students)  
The teacher did not manually label them. K-Means discovered the groups itself.

### Exam Answer (Short)

Steps of K-Means Clustering:  
1. Choose the number of clusters (K).  
2. Randomly select K centroids.  
3. Calculate the distance of each data point from every centroid.  
4. Assign each point to the nearest centroid.  
5. Recalculate the centroid of each cluster.  
6. Repeat steps 3–5 until centroids no longer change.  
7. Output the final clusters.

#### Simple Formula

```text
∑ x
```

Centroid =

```text
n
```

(Mean of all points in the cluster)  
Why called K-Means?  
- K = number of clusters  
- Means = cluster centers are calculated using the mean (average).

## Reassigning Points After Step 5

Ah, I see exactly where it gets confusing!

### Step 5: Assign Points Again → What it really means

After Step 4, you recalculate the centroids of each cluster.  
Now the centroids may have moved a little, because the new center is the average of points in the cluster.  
Because the centroids moved, some points might be closer to a different centroid now.  
So we check every point again:  
1. Calculate the distance from the point to each centroid.  
2. Assign the point to the closest centroid.

#### Example from our marks

Clusters after Step 4:  
- Centroid 1 = 12.33  
- Centroid 2 = 75  
Points:

```text
10, 12, 15, 70, 75, 80
```

#### Check each point

1. 10  
- Distance to 12.33 → 2.33  
- Distance to 75 → 65  
- Closest to 12.33 → stays in Cluster 1  
2. 12  
- Distance to 12.33 → 0.33  
- Distance to 75 → 63  
- Closest to 12.33 → stays in Cluster 1  
3. 15  
- Distance to 12.33 → 2.67  
- Distance to 75 → 60  
- Closest to 12.33 → stays in Cluster 1  
4. 70  
- Distance to 12.33 → 57.67  
- Distance to 75 → 5  
- Closest to 75 → stays in Cluster 2  
5. 75  
- Distance to 12.33 → 62.67  
- Distance to 75 → 0  
- Closest to 75 → stays in Cluster 2  
6. 80  
- Distance to 12.33 → 67.67  
- Distance to 75 → 5  
- Closest to 75 → stays in Cluster 2  
Observation:  
After checking all points, no point changed cluster.  
That’s why the algorithm stops in Step 6.

#### Key Idea

- “Assign points again” means: check all points against new centroids. If any point is closer to a different centroid, move it to that cluster.  
- If no points move, you are done.  
Think of it like: the center of the group moved slightly, so everyone double-checks if they are still closest to the same center. see visually why points might switch clusters — it becomes super clear.

|  | Show more |
|---|---|

#### What is Naive Bayes?

Naive Bayes is a supervised machine learning algorithm used for classification. Classification means:  
Put something into a category.  
Examples:  
- Is this email Spam or Not Spam?  
- Is this fruit Apple or Orange?  
- Is this message Positive or Negative?

### Why is it called "Naive"?

Because it makes a very simple assumption:  
All features are independent of each other.  
Independent means:  
One feature does not affect another feature.

#### Fruit Example

Suppose we want to identify a fruit using:  
- Color  
- Shape  
- Taste  
A fruit is:  
- Red  
- Round  
- Sweet  
Naive Bayes looks at each feature separately:

| Feature | Value |
|---|---|
| Color | Red |
| Shape | Round |
| Taste | Sweet |

It assumes:  
- Red does not depend on Round  
- Round does not depend on Sweet  
- Sweet does not depend on Red  
Then it combines all these probabilities and decides:  
Most likely this is an Apple.

### Why is it called "Bayes"?

Because it uses Bayes' Theorem.  
Bayes' theorem helps answer:  
Given some evidence, what is the probability that something belongs to a certain class? For example:  
If a fruit is:  
- Red  
- Round  
- Sweet  
What is the probability that it is:  
- Apple?  
- Orange?  
- Mango?  
Naive Bayes calculates these probabilities and chooses the highest one.

### Real-Life Example: Spam Email

Suppose an email contains words:

```text
Free
Win
Prize
Money
```

Naive Bayes checks:

#### Probability of Spam

If these words often appear in spam emails:

```text
P(Spam) = High
```

#### Probability of Not Spam

If these words rarely appear in normal emails:

```text
P(Not Spam) = Low
```

Since Spam probability is higher:  
Classify email as Spam

### Easy Exam Definition

Naive Bayes is a supervised classification algorithm based on Bayes' Theorem. It is called Naive because it assumes that all features are independent of each other. It is commonly used for classification tasks such as spam detection, sentiment analysis, and text classification.

### One-Line Memory Trick

Naive Bayes = Bayes Theorem + Assume all features are independent + Choose the class with highest probability.

|  | Show more |
|---|---|

### Bayes Theorem in Simple Words

Bayes Theorem helps us find:  
Probability of A happening, when we already know B has happened.  
Formula:

```text
P(B∣A) × P(A)
P(A∣B) =
P(B)
```

#### 1.

This means:  
Probability of A, given B happened.  
Example:  
Probability that an email is spam, given it contains the word “free”.

#### 2.

This means:  
Probability of B, given A happened.  
Example:  
Probability that the word “free” appears, given the email is spam.

#### 3. — Prior Probability

This means:  
Probability of A before seeing any new evidence.  
Example:  
Before checking email words, maybe:  
P(Spam) = 0.30  
So 30% emails are spam.

#### 4. — Marginal Probability

This means:  
Probability of evidence B happening in general.  
Example:  
P(Free) = 0.20  
Meaning 20% emails contain the word “free”.

### Easy Example

Suppose:  
P(Spam) = 0.30  
P(Free∣Spam) = 0.80  
P(Free) = 0.20  
Find:  
P(Spam∣Free)  
Use formula:  
P(Free∣Spam) × P(Spam)  
P(Spam∣Free) =  
P(Free)

```text
0.80 × 0.30
```

P(Spam∣Free) =

```text
0.20
```

P(Spam∣Free) = 1.2  
This example gives an invalid probability because the values are not realistic together, but the method is correct.

### Better Simple Understanding

Bayes Theorem means:  
Old belief + new evidence = updated belief.  
Example:  
Before seeing word “free”, spam chance may be low.  
After seeing word “free”, spam chance may increase.  
That updated chance is Bayes Theorem.

### Very Simple Memory Trick

| Term | Simple Meaning |
|---|---|

P(A) Probability of A before evidence  
P(B) Probability of evidence

| (P(B | A)) |
|---|---|
| (P(A | B)) |

Bayes Theorem tells us how new evidence changes probability.

|  | Show more |
|---|---|

### Conditional Probability

Conditional probability means:  
Probability of one event when another event has already happened.  
Formula style:

```text
P(A∣B)
```

Read it as:  
Probability of A given B.

### P(A∣B) Meaning of

```text
P(A∣B)
```

means:  
What is the chance of A happening, when B has already happened?  
Example:  
A = getting heads on third flip  
B = first two flips were tails  
So:

```text
P(A∣B)
```

means:  
Probability of getting heads on the third flip, given first two flips were tails. For a fair coin:

```text
P(A∣B) = 0.5
```

Because every coin flip is independent.

### P(B∣A) Meaning of

```text
P(B∣A)
```

means:  
What is the chance of B happening, when A has already happened?  
Example:  
B = getting tails on third flip  
A = first two flips were heads  
So:

```text
P(B∣A)
```

means:  
Probability of getting tails on third flip, given first two flips were heads.  
Again, for a fair coin:

```text
P(B∣A) = 0.5
```

### Important Point

For coin flips:  
Previous flips do not affect the next flip.  
So even if first two flips are tails, the third flip can still be:  
- Heads = 0.5  
- Tails = 0.5

### Naive Bayes Simple Explanation

Naive Bayes is based on conditional probability.  
It asks questions like:  
What is the probability this email is spam, given these words appear?  
Example:  
Email has words:

```text
free, prize, win
```

Naive Bayes checks:  
Probability of Spam, given the words free, prize, win.  
Then it compares:  
- Probability of Spam  
- Probability of Not Spam  
Whichever is higher becomes the final class.

### Why Naive Bayes is Useful

Naive Bayes is:  
- Easy to build  
- Fast  
- Good for large datasets  
- Very useful for text classification  
Example uses:  
- Spam detection  
- Sentiment analysis  
- News classification  
- Disease prediction

### One-Line Exam Answer

Naive Bayes is a supervised classification algorithm based on conditional probability and Bayes Theorem. It predicts the class of data by calculating the probability of each class and selecting the class with the highest probability.

## Naive Bayes Step by Step
### Problem

We have a school with 100 people:

|  | Female | Male | Total |
|---|---|---|---|
| Teacher | 8 | 12 | 20 |
| Student | 32 | 48 | 80 |
| Total | 40 | 60 | 100 |

We are asked:  
What is the probability that a person is a Teacher, given that the person is Male?

### Step 1: Write the conditional probability formula

Conditional probability formula:

```text
P(A ∩B)
P(A∣B) =
P(B)
```

Where:  
- = person is Teacher

```text
A
```

- = person is Male

```text
B
```

So we want:  
P(Teacher AND Male)  
P(Teacher | Male) =  
P(Male)

### Step 2: Find — Teacher AND Male

Look at the table:  
- Teachers who are Male = 12  
Total population = 100

```text
12 =
```

P(Teacher AND Male) = 0.12

```text
100
```

### Step 3: Find — Male

Total Males = 60

```text
60 =
```

P(Male) = 0.6

```text
100
```

### Step 4: Apply the formula

P(Teacher AND Male) 0.12

```text
= =
```

P(Teacher | Male) = 0.2  
P(Male) 0.6

### Step 5: Answer

P(Teacher | Male) = 0.2  
Meaning:  
If you pick a Male at random from the school, there is a 20% chance that he is a Teacher.

#### Step 6: Easy way to remember

- Conditional probability = "Look only at the group B (Males), then see how many belong to A (Teachers)."

| Male group only | Teacher | Student | Total |
|---|---|---|---|
| Count | 12 | 48 | 60 |

So:

```text
12 =
```

P(Teacher | Male) = 0.2

```text
60
```

group so it’s visually super easy to understand.

|  | Show more |
|---|---|

### Step 1: The Dataset

We have 14 observations with 4 features:  
- Outlook → Sunny, Overcast, Rainy  
- Temperature → Hot, Mild, Cool  
- Humidity → High, Normal  
- Wind → Weak, Strong  
Target label: Rain? → Yes / No  
Example row:

| Outlook | Temp | Humidity | Wind | Rain? |
|---|---|---|---|---|
| Sunny | Hot | High | Weak | No |

We want to predict Rain for new conditions.

### Step 2: Naive Bayes Formula

Naive Bayes uses Bayes’ Theorem:  
P(Conditions∣Rain) ⋅P(Rain)  
P(Rain∣Conditions) =  
P(Conditions)  
- P(Rain|Conditions) → Probability it will rain given the weather features  
- P(Rain) → Prior probability of Rain (from dataset)  
- P(Conditions|Rain) → Probability of observing the weather features if it rains  
P(Conditions)  
We usually ignore the denominator because it’s the same for Rain and No Rain.  
Simplified for calculation:  
P(Rain∣Conditions) ∝P(Rain) ⋅P(Outlook∣Rain) ⋅P(Temp∣Rain) ⋅P(Humidity∣Rain) ⋅P(Wind∣Rain)

### Step 3: Compute Priors

Count how many times Rain = Yes and Rain = No:  
- Rain = Yes → 9 times  
- Rain = No → 5 times  
So:  
P(Rain = Y es) = 9/14 ≈0.643  
P(Rain = No) = 5/14 ≈0.357

### Step 4: Compute Conditional Probabilities

Check likelihood of each feature given Rain:

#### Example: Outlook

| Outlook | P(Outlook | Rain=Yes) | P(Outlook | Rain=No) |
|---|---|---|---|---|
| --------- | ------------------- | ------------------ |  |  |
| Sunny | 2/9 ≈ 0.222 | 3/5 = 0.6 |  |  |
| Overcast | 4/9 ≈ 0.444 | 0/5 = 0 |  |  |
| Rainy | 3/9 ≈ 0.333 | 2/5 = 0.4 |  |  |

Do the same for Temperature, Humidity, Wind.

### Step 5: Compute Posterior Probability for a New Example

New example:  
- Outlook = Rainy  
- Temperature = Cool  
- Humidity = Normal  
- Wind = Strong  
Use Naive Bayes formula:  
P(Rain = Y es∣Conditions) ∝P(Rain = Y es) ⋅P(Outlook = Rainy∣Rain = Y es) ⋅P(Temp = Cool∣Rain = Y es) ⋅P(Humidity  
Plug in numbers from Step 4:  
P(Rain = Y es∣Conditions) ≈0.643 ⋅0.333 ⋅0.333 ⋅0.667 ⋅0.333 ≈0.0159  
P(Rain = No∣Conditions) ≈P(Rain = No) ⋅P(Outlook = Rainy∣No) ⋅P(Temp = Cool∣No) ⋅P(Humidity = Normal∣No) ⋅P(

```text
≈0.357 ⋅0.4 ⋅0.2 ⋅0.2 ⋅0.6 ≈0.0068
```

### Step 6: Make Prediction

Compare:  
P(Rain = Y es∣Conditions) = 0.0159  
P(Rain = No∣Conditions) = 0.0068  
- Since 0.0159 > 0.0068, the classifier predicts: Rain = Yes

#### Advantages

- Easy to implement  
- Works well with large datasets  
- Works well even with limited training data  
- Handles categorical features efficiently

#### Disadvantages

- Assumes features are independent (may not be true in real life)  
- Can be influenced by irrelevant attributes  
- Can assign zero probability to unseen events → poor prediction

#### Summary in 1 line

Naive Bayes predicts a class by multiplying prior probability with likelihoods of each feature, assuming all features are independent. Rain probability — this makes Naive Bayes super easy to “see” and remember.

## Naive Bayes Calculations in Detail
### Step 0: Dataset Summary

| Outlook | Temp | Humidity | Wind | Rain? |
|---|---|---|---|---|
| Sunny | Hot | High | Weak | No |
| Sunny | Hot | High | Strong | No |
| Overcast | Hot | High | Weak | Yes |
| Rainy | Mild | High | Weak | Yes |
| Rainy | Cool | Normal | Weak | Yes |
| Rainy | Cool | Normal | Strong | No |
| Overcast | Cool | Normal | Strong | Yes |
| Sunny | Mild | High | Weak | No |
| Sunny | Cool | Normal | Weak | Yes |
| Rainy | Mild | Normal | Weak | Yes |
| Sunny | Mild | Normal | Strong | Yes |
| Overcast | Mild | High | Strong | Yes |
| Overcast | Hot | Normal | Weak | Yes |
| Rainy | Mild | High | Strong | No |

Target: Predict Rain = Yes or No for new conditions.

### Step 1: Compute Prior Probabilities

Count Rain = Yes and Rain = No:  
- Rain = Yes → 9 occurrences  
- Rain = No → 5 occurrences

```text
9
≈
```

P(Rain = Y es) = 0.643

```text
14
5
```

P(Rain = No) = ≈ 0.357

```text
14
```

### Step 2: Compute Conditional Probabilities

Conditional probabilities are like:  
P(Feature = Value∣Rain = Y es)  
We calculate for each feature.

#### 2.1 Outlook

Rain = Yes (9 rows)

```text
2/9 = 0.222
```

- Sunny → 2 rows →

```text
4/9 = 0.444
```

- Overcast → 4 rows →

```text
3/9 = 0.333
```

- Rainy → 3 rows →  
Rain = No (5 rows)

```text
3/5 = 0.6
```

- Sunny → 3 rows →

```text
0/5 = 0.0
```

- Overcast → 0 rows →

```text
2/5 = 0.4
```

- Rainy → 2 rows →

#### 2.2 Temperature

Rain = Yes (9 rows)  
- Hot → 2/9 ≈ 0.222  
- Mild → 4/9 ≈ 0.444  
- Cool → 3/9 ≈ 0.333  
Rain = No (5 rows)  
- Hot → 2/5 = 0.4  
- Mild → 2/5 = 0.4  
- Cool → 1/5 = 0.2

#### 2.3 Humidity

Rain = Yes (9 rows)  
- High → 3/9 ≈ 0.333  
- Normal → 6/9 ≈ 0.667  
Rain = No (5 rows)  
- High → 4/5 = 0.8  
- Normal → 1/5 = 0.2

#### 2.4 Wind

Rain = Yes (9 rows)  
- Weak → 6/9 ≈ 0.667  
- Strong → 3/9 ≈ 0.333  
Rain = No (5 rows)  
- Weak → 2/5 = 0.4  
- Strong → 3/5 = 0.6

### Step 3: New Example

Predict Rain for:  
- Outlook = Rainy  
- Temperature = Cool  
- Humidity = Normal  
- Wind = Strong  
We calculate posterior probabilities for Yes and No.

### Step 4: Compute Posterior Probability for Rain = Yes

P(Rain = Y es∣Conditions) ∝P(Rain = Y es) ⋅P(Outlook = Rainy∣Y es) ⋅P(Temp = Cool∣Y es) ⋅P(Humidity = Normal∣Y es)  
Plug values:  
P(Rain = Y es) = 0.643  
P(Outlook = Rainy∣Y es) = 0.333  
P(Temp = Cool∣Y es) = 0.333  
P(Humidity = Normal∣Y es) = 0.667  
P(Wind = Strong∣Y es) = 0.333  
Multiply:

```text
0.643 ⋅0.333 ⋅0.333 ⋅0.667 ⋅0.333
```

Step by step:  
1. 0.643 × 0.333 ≈ 0.2138  
2. 0.2138 × 0.333 ≈ 0.0711  
3. 0.0711 × 0.667 ≈ 0.0474  
4. 0.0474 × 0.333 ≈ 0.0158  
So:  
P(Rain = Y es∣Conditions) ≈0.0158

### Step 5: Compute Posterior Probability for Rain = No

P(Rain = No∣Conditions) ∝P(Rain = No) ⋅P(Outlook = Rainy∣No) ⋅P(Temp = Cool∣No) ⋅P(Humidity = Normal∣No) ⋅P(  
Plug values:  
P(Rain = No) = 0.357  
P(Outlook = Rainy∣No) = 0.4  
P(Temp = Cool∣No) = 0.2  
P(Humidity = Normal∣No) = 0.2  
P(Wind = Strong∣No) = 0.6  
Multiply:

```text
0.357 ⋅0.4 ⋅0.2 ⋅0.2 ⋅0.6
```

Step by step:  
1. 0.357 × 0.4 ≈ 0.1428  
2. 0.1428 × 0.2 ≈ 0.02856  
3. 0.02856 × 0.2 ≈ 0.005712  
4. 0.005712 × 0.6 ≈ 0.003427  
So:  
P(Rain = No∣Conditions) ≈0.00343

### Step 6: Compare and Predict

P(Rain = Y es∣Conditions) = 0.0158  
P(Rain = No∣Conditions) = 0.00343  
- Since 0.0158 > 0.00343, we predict Rain = Yes for this new example.

### Step 7: Summary of Calculations

| Feature | P(Feature | Yes) | P(Feature | No) |
|---|---|---|---|---|
| ----------- | ---------------- | --------------- |  |  |
| Outlook=Rainy | 0.333 | 0.4 |  |  |
| Temp=Cool | 0.333 | 0.2 |  |  |
| Humidity=Normal | 0.667 | 0.2 |  |  |
| Wind=Strong | 0.333 | 0.6 |  |  |

Multiply with prior to get posterior:  
- : 0.643 × 0.333 × 0.333 × 0.667 × 0.333 ≈ 0.0158  
- No: 0.357 × 0.4 × 0.2 × 0.2 × 0.6 ≈ 0.00343  
Prediction: Rain = Yes you can see exactly how each feature contributes to the final probability.

## Worked Naive Bayes Calculation
### Given Information

Machine 1 makes:  
30 wrenches/hour  
Machine 2 makes:  
20 wrenches/hour  
Total:

```text
30 + 20 = 50
```

So:

```text
30 =
```

P(Mach1) = 0.6

```text
50
20 =
```

P(Mach2) = 0.4

```text
50
```

Meaning: out of all parts, 40% are made by Machine 2.

### Defective Information

Total defective parts:  
P(Defect) = 1% = 0.01  
Out of all defective parts:  
P(Mach2∣Defect) = 50% = 0.5  
Meaning: if a part is defective, there is a 50% chance it came from Machine 2.

### Question

Find:  
P(Defect∣Mach2)  
Meaning:  
If a part came from Machine 2, what is the chance that it is defective?

### Bayes Formula

P(Mach2∣Defect) × P(Defect)  
P(Defect∣Mach2) =  
P(Mach2)  
Now put values:

```text
0.5 × 0.01
```

P(Defect∣Mach2) =

```text
0.4
```

### Step-by-Step Calculation

First multiply numerator:

```text
0.5 × 0.01 = 0.005
```

Now divide by 0.4:

```text
0.005
= 0.0125
0.4
```

So:  
P(Defect∣Mach2) = 0.0125  
Convert into percentage:

```text
0.0125 × 100 = 1.25%
```

### Final Answer

P(Defect∣Mach2) = 1.25%  
Meaning:  
If a part was produced by Machine 2, there is a 1.25% chance that it is defective.

### Simple Intuition with 1000 Parts

Assume total parts = 1000  
Machine 2 makes 40%:

```text
1000 × 0.4 = 400
```

So Machine 2 made 400 parts.  
Total defective parts are 1%:

```text
1000 × 0.01 = 10
```

So total defective parts = 10.  
50% defective parts came from Machine 2:

```text
10 × 0.5 = 5
```

So Machine 2 made 5 defective parts.  
Now:

```text
5 = 0.0125 = 1.25%
400
```

Same answer.

### Quick Exercise

Find:  
P(Defect∣Mach1)  
Formula:  
P(Mach1∣Defect) × P(Defect)  
P(Defect∣Mach1) =  
P(Mach1)  
Values:  
P(Mach1∣Defect) = 0.5  
P(Defect) = 0.01  
P(Mach1) = 0.6  
So:

```text
0.5 × 0.01
```

P(Defect∣Mach1) =

```text
0.6
0.005
=
0.6
= 0.00833
```

Convert to percentage:

```text
0.00833 × 100 = 0.833%
```

Final:  
P(Defect∣Mach1) = 0.833%  
So Machine 1 has lower defective chance than Machine 2.

## Quick Exercise: Reading Conditional Probabilities

Excellent question. This is exactly where most students get confused.

### Part 1: How did we know

P(Mach1∣Defect) = 0.5  
Look at the statement:  
"Out of all defective parts, 50% came from Machine 1 and 50% came from Machine 2." This directly means:  
P(Mach1∣Defect) = 0.5  
and  
P(Mach2∣Defect) = 0.5

### What does this notation mean?

P(Mach1∣Defect)  
reads:  
Probability that the part came from Machine 1 GIVEN that it is defective.  
The question already tells us:  
Among defective parts, 50% came from Machine 1.  
So directly:  
P(Mach1∣Defect) = 50% = 0.5  
No calculation needed.  
It is GIVEN in the question.

### Visual Example

Suppose there are 10 defective parts.  
Question says:  
50% came from Machine 1  
So:

| Defective Parts | Count |
|---|---|
| From Machine 1 | 5 |
| From Machine 2 | 5 |
| Total | 10 |

Therefore:

```text
5 =
```

P(Mach1∣Defect) = 0.5

```text
10
```

### Part 2: When do we use Bayes Theorem?

Look carefully.

### Situation 1

You know:  
P(Mach2∣Defect)  
But you want:  
P(Defect∣Mach2)  
Notice:  
The order is reversed.  
Known:

```text
P(B∣A)
```

Need:

```text
P(A∣B)
```

This is exactly when Bayes Theorem is used.

#### Memory Trick

If question gives:  
Given Defect, probability of Machine 2  
But asks:  
Given Machine 2, probability of Defect  
Then use Bayes.  
Because the condition switched.

### Example

Known:  
P(Mach2∣Defect) = 0.5  
Want:  
P(Defect∣Mach2)  
Condition changed from:

```text
Given Defect
```

to

```text
Given Machine 2
```

Therefore:  
Use Bayes Theorem

### Part 3: When do we use Intersection Formula?

Intersection means:

```text
P(A ∩B)
```

Read:  
A AND B  
Formula:

```text
P(A ∩B) = P(A) × P(B∣A)
```

or

```text
P(A ∩B) = P(B) × P(A∣B)
```

### Example

Suppose:  
P(Defect) = 0.01  
P(Mach2∣Defect) = 0.5  
Find:  
P(Mach2 ∩Defect)  
Use intersection formula:  
P(Mach2 ∩Defect) = P(Mach2∣Defect) × P(Defect)

```text
= 0.5 × 0.01
= 0.005
```

Answer:  
P(Mach2 ∩Defect) = 0.005

### Why Bayes Uses Intersection

Bayes actually comes from the intersection formula.  
Start with:

```text
P(A ∩B) = P(B∣A)P(A)
```

Also:

```text
P(A ∩B) = P(A∣B)P(B)
```

Since both equal same intersection:

```text
P(B∣A)P(A) = P(A∣B)P(B)
```

Rearrange:

```text
P(B∣A)P(A)
P(A∣B) =
P(B)
```

This becomes Bayes Theorem.

### Part 4: When do we use Naive Bayes?

Naive Bayes is different.  
Bayes theorem usually has ONE condition.  
Example:  
P(Defect∣Mach2)  
Only one condition.  
Naive Bayes has MANY conditions/features.  
Example:  
Predict Rain using:  
- Outlook = Rainy  
- Temperature = Cool  
- Humidity = Normal  
- Wind = Strong  
We want:  
P(Rain∣Outlook, Temp, Humidity, Wind)  
Many conditions.  
Now Bayes becomes:  
P(Rain) × P(Outlook∣Rain) × P(Temp∣Rain) × P(Humidity∣Rain) × P(Wind∣Rain)  
This is Naive Bayes.

#### If question says

Find probability of A and B together  
Use:

```text
P(A ∩B)
```

(Intersection Formula)

#### If question says

Given B, find probability of A  
and condition is reversed from given data  
Use:

```text
P(B∣A)P(A)
P(A∣B) =
P(B)
```

(Bayes Theorem)

#### If question has many features

Example:  
- Sunny  
- Hot  
- High Humidity  
- Weak Wind  
Predict:  
- Rain?  
- Spam?  
- Disease?  
Use:  
Naive Bayes  
because there are multiple features contributing to one class prediction.

#### Quick Rule

| Question Type | Use |
|---|---|
| A AND B | Intersection Formula |
| Given B, find A (reversed condition) | Bayes Theorem |
| Predict class using many features | Naive Bayes |

This table alone solves about 90% of exam confusion.

## P(A∩B)/P(B) vs P(A∩B)/P(A)
### 1. Conditional Probability Formula

```text
P(A ∩B)
P(A∣B) =
P(B)
```

- Read as: Probability of A given B happened  
- You divide by B because your “universe” is now restricted to only the cases where B happens.  
Example:  
You have 100 people, 60 males (B), 12 male teachers (A ∩ B).

```text
12 =
```

P(Teacher∣Male) = 0.2

```text
60
```

- You divide by P(B) (total males) because you only care about males now.

### 2. Reverse Conditional

```text
P(A ∩B)
P(B∣A) =
P(A)
```

- Read as: Probability of B given A happened  
- Now the “universe” is all A’s.  
Example:  
Of 20 teachers (A), 12 are male (A ∩ B)

```text
12 =
```

P(Male∣Teacher) = 0.6

```text
20
```

- You divide by P(A) (total teachers) because you are now focusing only on teachers.

#### Quick Rule

| Formula | Read as | Divide by | Use when |
|---|---|---|---|
| (P(A | B) = P(A\cap B)/P(B)) | Probability of A given B | Universe = B |
| (P(B | A) = P(A\cap B)/P(A)) | Probability of B given A | Universe = A |

#### Visual Example

Population = 100

|  | Male | Female | Total |
|---|---|---|---|
| Teacher | 12 | 8 | 20 |
| Student | 48 | 32 | 80 |
| Total | 60 | 40 | 100 |

1. P(Teacher | Male) → Universe = Males = 60

```text
P = 12/60 = 0.2
```

2. P(Male | Teacher) → Universe = Teachers = 20

```text
P = 12/20 = 0.6
```

See? Which probability you want determines the denominator. and label exactly when you divide by P(A) or P(B) — this makes it super intuitive.

## Dependent and Independent Probability
### Independent Probability

Two events are independent when one event does not affect the other event.

#### Example: Coin Toss

Event A = first toss is Head  
Event B = second toss is Head  
First toss does not affect second toss.  
So:

```text
P(A ∩B) = P(A) × P(B)
1 1 1
```

P(Head and Head) = × =

```text
2 2 4
```

Answer:

```text
0.25 = 25%
```

### Dependent Probability

Two events are dependent when one event does affect the other event.

#### Example: Cards Without Replacement

A deck has 52 cards.  
Event A = first card is King  
Event B = second card is King  
If first card is King, then only 3 kings are left.  
So:

```text
P(A ∩B) = P(A) × P(B∣A)
4 3
```

P(King and King) = ×

```text
52 51
```

Why ?  
Because after taking one king:  
- Kings left = 3  
- Cards left = 51  
So events are dependent.

### Main Difference

| Type | Meaning | Formula |
|---|---|---|

Independent | First event does not affect P(A ∩B) = P(A)P(B)

|  | second |  |
|---|---|---|
| Dependent | First event affects second | (P(A \cap B)=P(A)P(B |

### Easy Trick

If probability stays same → Independent  
If probability changes → Dependent  
Example:  
Coin toss:

```text
1 1
,
2 2
```

same → independent.  
Cards without replacement:

```text
4 3
52 , 51
```

changed → dependent.

|  | Show more |
|---|---|

### Step 1: Understand the problem

We have a dataset with two independent features:  
- Age  
- Salary  
And a target variable:  
- Category 1 → Walks to work  
- Category 2 → Drives to work  
We want to predict for a new person:  
- Age = 25  
- Salary = $30,000  
Whether this person Walks or Drives.

### Step 2: Bayes Theorem Formula

The posterior probability is:  
P(X∣Class) ⋅P(Class)  
P(Class∣X) =

```text
P(X)
```

Where:  
- P(Class|X) → Posterior probability (what we want)  
- P(Class) → Prior probability (how many people walk/drives in total)  
- P(X|Class) → Likelihood (how likely features X are in this class)  
- P(X) → Marginal likelihood (how likely features X are in total)

### Step 3: Step 1 — Prior Probability

Count number of Walkers and Drivers:  
Number of Walkers 10

```text
= =
```

P(Walks) = 0.333  
Total Observations 30  
Number of Drivers 20

```text
= =
```

P(Drives) = 0.667  
Total Observations 30  
These are the priors.

### Step 4: Step 2 — Marginal Likelihood

Take a radius around new data point:  
- Age between 20–30  
- Salary between $25k–$35k  
Count how many existing Walkers and Drivers fall in this range:  
Number of Similar Observations 4

```text
P(X) = = = 0.133
```

Total Observations 30

### Step 5: Step 3 — Likelihood

Compute P(X|Class):  
Number of Walkers in radius 3  
P(X∣Walks) = = = 0.3  
Total Walkers 10  
Number of Drivers in radius 1

```text
= =
```

P(X∣Drives) = 0.05  
Total Drivers 20

### Step 6: Step 4 — Posterior Probability

For Walks:  
P(X∣Walks) ⋅P(Walks)  
P(Walks∣X) =

```text
P(X)
= 0.3 ⋅0.333 ≈ 0.75
0.133
```

For Drives:  
P(X∣Drives) ⋅P(Drives)  
P(Drives∣X) =

```text
P(X)
0.05 ⋅0.667
= ≈ 0.25
0.133
```

### Step 7: Step 5 — Compare Posteriors

P(Walks∣X) = 0.75  
P(Drives∣X) = 0.25  
- Prediction: The person is most likely to Walk to work.

### Step 8: Types of Naive Bayes Classifiers

1. Gaussian Naive Bayes → Continuous features assumed normally distributed  
2. Multinomial Naive Bayes → Count/frequency data, e.g., word counts in text  
3. Bernoulli Naive Bayes → Binary features, e.g., presence/absence of words in text

### Step 9: When to use Union in Probability

Union is used when you want A OR B:

```text
P(A ∪B) = P(A) + P(B) −P(A ∩B)
```

- Use union when counting probability of either one event or another event happening  
- Intersection is for A AND B, used in conditional probability and Bayes theorem Example:  
- P(A) = probability it rains  
- P(B) = probability it is windy  
- P(A ∪ B) = probability it rains OR it is windy

```text
P(A ∪B) = P(A) + P(B) −P(A ∩B)
```

Union is not used in Naive Bayes because we are always looking at AND combination of features, not OR.  
Summary: Quick Steps for Naive Bayes  
1. Compute P(Class) → Prior probability  
2. Compute P(X|Class) → Likelihood for each feature  
3. Compute P(X) → Marginal likelihood  
4. Compute Posterior → P(Class|X) = (Likelihood × Prior) / Marginal  
5. Compare posteriors → Choose class with highest probability circles showing all likelihoods, priors, and posteriors, so you can “see” exactly how Naive Bayes works for the Walks/Drives example.

## Union Probability and Independence in Naive Bayes

independence assumption.

### Part 1: Union Probability Example

Problem:  
A deck of 52 cards.  
- Event A = drawing a heart  
- Event B = drawing a face card (J, Q, K of any suit)  
We want:  
P(A ∪B) = Probability of drawing a Heart OR a Face card

#### Step 1: Find P(A)

- There are 13 hearts in the deck.

```text
13
P(A) = 52 = 0.25
```

#### Step 2: Find P(B)

- Face cards: J, Q, K of each suit → 12 cards

```text
P(B) = 12 ≈ 0.2308
52
```

#### Step 3: Find P(A ∩ B)

- Cards that are both hearts AND face cards → J, Q, K of hearts → 3 cards

```text
P(A ∩B) = 3 ≈ 0.0577
52
```

#### Step 4: Apply Union Formula

```text
P(A ∪B) = P(A) + P(B) −P(A ∩B)
P(A ∪B) = 0.25 + 0.2308 −0.0577
P(A ∪B) ≈0.4231
```

Answer: 42.31% chance of drawing a heart OR a face card.

### Part 2: When do we use Naive Bayes?

Naive Bayes Assumption:  
- All features are independent given the class.  
- That’s why it’s called “Naive”.  
Example:  
- Features: Outlook, Temperature, Humidity, Wind  
- Target: Rain = Yes / No  
Naive Bayes assumes:  
P(Outlook, Temp, Humidity, Wind∣Rain) = P(Outlook∣Rain) ⋅P(Temp∣Rain) ⋅P(Humidity∣Rain) ⋅P(Wind∣Rain)  
- Each feature contributes independently to the probability.  
If features are not independent, Naive Bayes still works surprisingly well, but technically the assumption is violated.  
Summary Rule:

| Question Type | Use |
|---|---|

Probability of A OR B | Use union formula:P(A ∪B) = P(A) +

| Predict class using multiple independent | Use Naive Bayes |
|---|---|
| features |  |

visualize it clearly.

|  | Show more |
|---|---|

### Step 1: Choose K

- K = number of nearest neighbors you want to check.  
- Example: K = 3 → look at 3 closest points to decide the class.

### Step 2: Calculate Distance

- Usually we use Euclidean distance for numerical features.  
Formula:

```text
d = (x 2 −x 1 2 ) + (y 2 −y 1 2 )
```

- Measure distance between new data point and all points in dataset.

### Step 3: Find K Nearest Neighbors

- Pick K points with smallest distance.

### Step 4: Count the Classes

- See how many neighbors belong to each category.  
- Example: Among 3 neighbors: 2 are Red, 1 is Blue.

### Step 5: Assign Class

- Assign the new point to the class that appears most among neighbors. Example: 2 Red, 1 Blue → new point = Red.

### Step 6: Model is Ready

- You can now predict class for any new data using KNN.

### Example Problem

Suppose we have points with 2 features (x, y) and 2 classes:

| x | y | Class |
|---|---|---|
| 1 | 1 | Red |
| 2 | 2 | Red |
| 3 | 3 | Blue |
| 6 | 6 | Blue |
| 7 | 7 | Blue |

New point: (3,2)  
K = 3

#### Step 2: Calculate Euclidean Distance

```text
d = (x new −x i 2 ) + (y new −y i 2 )
```

| Point | Distance |
|---|---|
| (1,1) Red | √((3-1)²+(2-1)²) = √(4+1) = √5 ≈ 2.24 |
| (2,2) Red | √((3-2)²+(2-2)²) = √(1+0) = 1 |
| (3,3) Blue | √((3-3)²+(2-3)²) = √(0+1) = 1 |
| (6,6) Blue | √((3-6)²+(2-6)²) = √(9+16) = √25 = 5 |
| (7,7) Blue | √((3-7)²+(2-7)²) = √(16+25) = √41 ≈ 6.40 |

#### Step 3: Take K = 3 Nearest Neighbors

- Closest 3 distances: 1, 1, 2.24  
- Points: (2,2) Red, (3,3) Blue, (1,1) Red

#### Step 4: Count Classes

- Red → 2 points  
- Blue → 1 point

#### Step 5: Assign Class

- Most neighbors = Red  
- So new point (3,2) → Red

#### Step 6: Done

- Model can now predict any new point using the same steps.

### Notes

- K choice matters:  
- Small K → sensitive to noise  
- Large K → smoother prediction  
- Always scale features if they are different units (height vs weight). and assigned class. This makes KNN very visual and easy to remember.

## Steps of K-Means and KNN
### 1 K-Means Clustering (Unsupervised Learning)

K-Means is used to group data into clusters without knowing the labels beforehand.

#### Steps

1. Select K → Number of clusters you want.  
- Example: K = 2 clusters  
2. Initialize Centroids → Pick K random points as initial centers.  
3. Calculate Distance → Compute Euclidean distance from each data point to each centroid.  
4. Assign Points to Nearest Centroid → Each point goes to the cluster of the nearest centroid.  
5. Recalculate Centroids → Find the new center (mean) of each cluster.  
6. Repeat Steps 3–5 until centroids don’t change or points stay in same clusters.

#### Example

Data: [10, 12, 15, 70, 75, 80]  
K = 2  
1. Initial centroids: 10, 70  
2. Assign points:  
- Cluster 1: 10, 12, 15  
- Cluster 2: 70, 75, 80  
3. Recalculate centroids:  
- Cluster 1 centroid = (10+12+15)/3 = 12.33  
- Cluster 2 centroid = (70+75+80)/3 = 75  
4. Reassign points → No change → Stop  
Final clusters:  
- Cluster 1: 10, 12, 15  
- Cluster 2: 70, 75, 80

### 2 K-Nearest Neighbors (KNN) (Supervised Learning)

KNN is used to classify a new point based on labeled data.

#### Steps

1. Choose K → Number of neighbors to check.  
- Example: K = 3  
2. Calculate Distance → Find distance between new point and all existing points (Euclidean distance).  
3. Find K Nearest Neighbors → Pick the K points with the smallest distance.  
4. Count Classes → Count how many neighbors belong to each class.  
5. Assign Class → New point gets the class with the most neighbors.  
6. Model is Ready → Repeat for any new point.

#### Example

Data:

| x | y | Class |
|---|---|---|
| 1 | 1 | Red |
| 2 | 2 | Red |
| 3 | 3 | Blue |
| 6 | 6 | Blue |
| 7 | 7 | Blue |

New point: (3,2)  
K = 3  
1. Calculate distances:

| Point | Distance |
|---|---|
| (1,1) Red | 2.24 |
| (2,2) Red | 1 |
| (3,3) Blue | 1 |
| (6,6) Blue | 5 |
| (7,7) Blue | 6.4 |

2. Pick 3 nearest neighbors: (2,2) Red, (3,3) Blue, (1,1) Red  
3. Count classes: Red → 2, Blue → 1  
4. Assign class: Red  
Prediction: New point is Red

#### Quick Comparison

| Feature | K-Means | KNN |
|---|---|---|
| Type | Unsupervised | Supervised |
| Goal | Group data into clusters | Classify new point |
| Input | Only features | Features + Labels |
| Output | Cluster labels | Predicted class |
| Steps | Initialize → Assign → Recompute | Compute distances → Pick K → Count → |
|  | centroids → Repeat | Assign class |

so you can see clusters vs classification in one view.

## KNN on Large Datasets

you are correct. One limitation of KNN is computational cost for large datasets or many new points. Let me explain this in detail and give ways to handle it.

### Why KNN is Slow on Large Data

1. Distance calculation:  
- For each new point, KNN computes distance to every single training point. If dataset has N points, each prediction requires O(N) computations.  
2. Multiple new points:  
- If you have M new points, total computation is O(M×N).  
3. High dimensions:  
- Each distance calculation is over all features (D dimensions) → slows further.

#### Example

- Dataset: 1,000,000 points  
- New points to classify: 100,000  
- Each point has 10 features  
Total distance calculations = 100,000 × 1,000,000 = 100 billion distances!  
Clearly, this is very slow.

### Ways to Speed Up KNN

1. KD-Trees / Ball Trees  
- These are data structures that allow fast nearest neighbor search in low to medium dimensions.  
- Avoid computing distance to all points.  
2. Approximate Nearest Neighbors  
- Instead of exact neighbors, use algorithms like Annoy, FAISS, or HNSW. Very fast for very large datasets.  
3. Reduce Dimensions  
- Use PCA or t-SNE to reduce features before KNN.  
- Fewer dimensions → faster distance calculations.  
4. Precompute Distances (for static datasets)  
- If training data is fixed, compute distance matrix once.  
- Then just lookup nearest neighbors instead of recomputing.  
5. Mini-batching / Subsampling  
- For huge datasets, only compare with a subset of points.  
- Sacrifices some accuracy but much faster.

#### Practical Tip

- KNN works well for small to medium datasets.  
- For large datasets with many predictions:  
- Use approximate nearest neighbors or other classifiers (Random Forest, Logistic Regression, Naive Bayes, etc.). why KD-Trees or Approximate Neighbors reduce computation, so it’s very visual and intuitive.

## Multiple Linear Regression in High Dimensions

Multiple Linear Regression is often used when you have multiple input features (dimensions).

### Simple Linear Regression

Only 1 input feature  
Example:  
Predict House Price using only:

```text
House Size
```

Formula:

```text
y = b 0 + b 1 x
```

Example:  
Price = b + (Size)

```text
0 b 1
```

Only one dimension (one feature).

### Multiple Linear Regression

Uses 2 or more input features.  
Example:  
Predict House Price using:  
- House Size  
- Number of Bedrooms  
- Location Score  
- Age of House  
Formula:

```text
y = b 0 + b 1 x 1 + b 2 x 2 + b 3 x 3 + ... + b n x n
```

Example:  
Price = b + (Size) + (Bedrooms) + (Age)

```text
0 b 1 b 2 b 3
```

Now we have multiple dimensions.

#### Yes and No

Multiple Linear Regression can handle many features.  
Example:  
- Age  
- Salary  
- Experience  
- Education  
- CGPA  
- Skills  
all together.

#### But Extremely High Dimensions?

Suppose:  
- 10,000 features  
- 100,000 features  
Then ordinary Multiple Linear Regression may:  
- Become slow  
- Overfit  
- Have multicollinearity problems  
For such cases people often use:  
- Ridge Regression  
- Lasso Regression  
- Elastic Net  
- PCA + Regression

### Difference from KNN

KNN also works with multiple dimensions.  
Example:  
Features:  
- Age  
- Salary  
- Height  
- Weight  
- Experience  
KNN calculates distance using all dimensions:

```text
d = (x 1 −y 1 2 ) + (x 2 −y 2 2 ) + ⋯
```

The problem is:  
As dimensions increase:  
- Distance calculations become expensive  
- Neighbors become less meaningful  
This is called:  
Curse of Dimensionality

### Exam Answer

Multiple Linear Regression is an extension of simple linear regression that uses two or more independent variables (features) to predict a dependent variable. It is suitable for multidimensional data where several factors influence the output.  
Example:  
Price = b + (Size) + (Bedrooms) + (Age)

```text
0 b 1 b 2 b 3
```

where Size, Bedrooms, and Age are multiple input dimensions.

## Elastic Net

Elastic Net is a type of regression that combines Ridge Regression (L2 regularization) and Lasso Regression (L1 regularization).  
- Purpose: Prevent overfitting and handle many correlated features.  
- Short version: It shrinks coefficients like Ridge and can set some coefficients to zero like Lasso, giving a balance.  
Formula (simplified):

```text
1 ∑ 2 ∑ 2
```

Minimize Loss + λ ∣b ∣+λ b

```text
j j
```

- → L1 penalty (Lasso)

```text
λ 1
```

- → L2 penalty (Ridge)

```text
λ 2
```

Use Elastic Net when you have many features, especially if some are highly correlated.  
Example in words:  
- Predict house prices using 100 features, many similar (size, square footage, rooms) → Elastic Net works better than Lasso or Ridge alone.

## The t-Test

T-test in a simple, short way:  
Definition:  
A t-test is a statistical test used to compare the means of two groups to see if they are significantly different from each other.  
Key Points:  
1. Purpose: Check if differences between groups are real or just by chance.  
2. Types:  
- Independent t-test → Compare two different groups (e.g., male vs female scores).  
- Paired t-test → Compare the same group before and after treatment.  
3. Output: Gives a t-value and a p-value:  
- p < 0.05 → Difference is significant  
- p ≥ 0.05 → Difference is not significant  
Example (Short):  
- Group A test scores: [80, 85, 90]  
- Group B test scores: [70, 75, 80]  
T-test checks:  
Are the average scores of Group A and Group B significantly different?  
Formula (simplified):  
−Mean  
Mean1 2

```text
t =
```

Standard Error of Difference  
In short: T-test tells you “Are these two averages really different?” calculate t-value and p-value so it’s super easy to understand.

## t-Test Worked Example
#### Problem Example

Two classes of students took the same test:  
- Class A scores: 85, 90, 88, 92, 87  
- Class B scores: 80, 82, 79, 85, 83  
We want to know: Are the class averages significantly different?  
We'll do an independent t-test because these are two different groups.

### Step 1: Find the Mean

```text
85 + 90 + 88 + 92 + 87 442
= = =
```

Mean 88.4

```text
A 5 5
80 + 82 + 79 + 85 + 83 409
```

Mean = = = 81.8

```text
B 5 5
```

### Step 2: Find Standard Deviation (SD)

Formula for SD:

```text
2
```

(x −mean)

```text
SD = ∑ i
n −1
```

#### Class A

- Deviations: 85-88.4=-3.4, 90-88.4=1.6, 88-88.4=-0.4, 92-88.4=3.6, 87-88.4=-1.4 Squared deviations: 11.56, 2.56, 0.16, 12.96, 1.96  
- Sum = 29.2  
- Divide by n-1 = 5-1=4 → 29.2/4 = 7.3  
- SD_A = √7.3 ≈ 2.70

#### Class B

- Deviations: 80-81.8=-1.8, 82-81.8=0.2, 79-81.8=-2.8, 85-81.8=3.2, 83-81.8=1.2 Squared deviations: 3.24, 0.04, 7.84, 10.24, 1.44  
- Sum = 22.8  
- Divide by 4 → 22.8/4=5.7  
- SD_B = √5.7 ≈ 2.39

### Step 3: Find Standard Error (SE)

```text
SE = SD A 2 + SD 2 B
n A n B
```

- SD_A² = 2.70² = 7.29  
- SD_B² = 2.39² = 5.71

```text
SE = 7.29 + 5.71 = 1.458 + 1.142 = 2.6 ≈ 1.61
5 5
```

### Step 4: Compute t-value

Mean −Mean 88.4 −81.8 6.6

```text
t = A B = = ≈ 4.10
SE 1.61 1.61
```

### Step 5: Degrees of Freedom (df)

For independent t-test:

```text
df = n A + n B − 2 = 5 + 5 −2 = 8
```

### Step 6: Compare with t-table

- df=8, significance level α=0.05 (two-tailed)  
- Critical t ≈ 2.306  
Our t-value = 4.10 > 2.306 → Reject null hypothesis  
Conclusion: Class A and Class B have significantly different averages.

#### Summary Table

| Class | Mean | SD | n |
|---|---|---|---|
| A | 88.4 | 2.70 | 5 |
| B | 81.8 | 2.39 | 5 |

- SE = 1.61  
- t = 4.10  
- df = 8 → p < 0.05 → Significant difference it very intuitive to remember.

## The p-Value With a Worked Example
### P-value simple meaning

P-value tells us:  
If there is actually no real difference, what is the chance that we got this result by luck?

### Easy rule

Usually we compare p-value with 0.05.

| P-value | Meaning |
|---|---|
| p < 0.05 | Result is significant, probably real difference |
| p ≥ 0.05 | Result is not significant, maybe due to chance |

### Example

Suppose two classes gave a test.  
Class A average:

```text
88.4
```

Class B average:

```text
81.8
```

We do a t-test and get:

```text
p = 0.003
```

#### Step 1: Null hypothesis

Null hypothesis means:  
There is no real difference between Class A and Class B.

#### Step 2: P-value says

```text
p = 0.003
```

This means:  
If there is no real difference, then chance of getting such a big difference by luck is only 0.3%.  
Because:

```text
0.003 × 100 = 0.3%
```

#### Step 3: Compare with 0.05

```text
0.003 < 0.05
```

So result is significant.

### Final conclusion

Because p-value is very small:

```text
p = 0.003
```

we reject the null hypothesis.  
Meaning:  
Class A and Class B averages are significantly different.

### Very simple example

Imagine tossing a coin 100 times.  
If you get:

```text
50 heads, 50 tails
```

This looks normal.  
But if you get:

```text
95 heads, 5 tails
```

That looks strange.  
P-value asks:  
If coin is fair, what is the chance of getting 95 heads?  
That chance is very small, so p-value is small.  
Small p-value means:  
Something unusual is happening. Probably not just luck.

## t-Value vs p-Value and Hypotheses

No issue — this confusion is very common.

### 1. Null Hypothesis means what?

Null hypothesis means:

```text
H 0
```

There is no real difference.  
Example:  
Two classes have test scores.

```text
H 0
```

Class A and Class B average marks are same.  
Alternative hypothesis :

```text
H 1
```

Class A and Class B average marks are different.

### 2. T-value vs P-value T-value

T-value tells how big the difference is between two averages.  
Bigger t-value = bigger difference compared to normal variation.  
Formula idea:  
Difference between means

```text
t =
```

Standard error  
So t-value answers:  
How far apart are the two groups?

### P-value

P-value tells whether that difference is significant or just by chance.  
It answers:  
If there is no real difference, what is the chance we got this result by luck?

### Main Difference

| T-value | P-value |
|---|---|
| Measures size of difference | Measures chance/luck |
| Bigger t-value usually means stronger result | Smaller p-value means stronger result |
| Used to calculate significance | Used to make final decision |

### 3. What means Significant Difference?

Significant difference means:  
The difference is probably real, not just random luck.  
Usually:

```text
p < 0.05
```

means significant difference.

```text
p ≥0.05
```

means not significant.

### 4. Full Problem Solving Steps

Example:  
Class A average = 88.4  
Class B average = 81.8  
After calculation:

```text
t = 4.10
p = 0.003
```

### Step 1: Write hypothesis

: No difference between Class A and Class B.

```text
H 0
```

: There is a difference between Class A and Class B.

```text
H 1
```

### Step 2: Calculate t-value

Suppose:

```text
t = 4.10
```

Meaning:  
The averages are quite far apart.

### Step 3: Find p-value

From t-table/software:

```text
p = 0.003
```

Meaning:  
Only 0.3% chance this difference happened by luck.

### Step 4: Compare p-value with 0.05

```text
0.003 < 0.05
```

So result is significant.

### Step 5: Final decision

Reject .

```text
H 0
```

Final answer:  
There is a significant difference between Class A and Class B marks.

### Super Easy Memory

T-value: How big is the difference?  
P-value: Is the difference real or just luck?  
Null hypothesis: There is no difference.  
Significant difference: Difference is probably real.

## From t-Value to p-Value
### Step 1: Know your t-value and degrees of freedom

- Suppose from your t-test you have:

```text
t = 2.5
```

- Degrees of freedom (df) = n₁ + n₂ - 2  
- If two groups of size 5 → df = 5 + 5 - 2 = 8

### Step 2: Decide if it’s one-tailed or two-tailed test

- One-tailed → testing if one mean > other  
- Two-tailed → testing if means are different (most common)

### Step 3: Use a t-distribution table or software

- T-table method:  
1. Look for df = 8  
2. Find t-value closest to 2.5  
3. Check the corresponding p-value (probability in table)  
- Software method:  
- Use Excel, Python, or online calculators:  
Python example:

Python

```python
from scipy import stats
t = 2.5
df = 8
p = 2 * (1 - stats.t.cdf(abs(t), df))
print(p)
```

- Multiply by 2 for two-tailed test.

### Step 4: Interpret

- Suppose p ≈ 0.036  
- Compare with α = 0.05:  
0.036 < 0.05 ⇒Significant difference

#### Quick Summary

1. Get t-value from your t-test.  
2. Find degrees of freedom (df).  
3. Decide one-tailed or two-tailed.  
4. Use t-distribution table or software to find p-value.  
5. Compare p-value with significance level (α = 0.05) → decide if difference is significant. and calculate the exact p-value from t = 4.10 step by step, so it’s crystal clear.

## Degrees of Freedom and Alpha
### 1. What is df?

df = degrees of freedom  
In simple words:  
df tells which row of the t-table to use.  
For independent t-test:

```text
df = n 1 + n 2 − 2
```

Example:  
Class A has 5 students.  
Class B has 5 students.

```text
df = 5 + 5 −2 = 8
```

So in t-table, use df = 8 row.

### 2. After calculating t-value, what do we do?

Suppose:

```text
t = 4.10
```

and:

```text
df = 8
```

Now we check the t-table.  
For df = 8 and alpha = 0.05, critical t-value is about:

```text
2.306
```

Now compare:

```text
4.10 > 2.306
```

So result is significant.  
Meaning:  
The difference between groups is real, not just by chance.

### 3. What is p-value?

P-value tells:  
Chance that this difference happened by luck.  
If:

```text
p < 0.05
```

then result is significant.  
If:

```text
p ≥0.05
```

then result is not significant.

### 4. Where do we get p-value?

After getting:

```text
t = 4.10
```

and:

```text
df = 8
```

we get p-value from:  
- t-table  
- calculator  
- Excel  
- SPSS  
- Python  
- online t-test calculator  
In exams, usually you compare t-value with critical t-value from table.

### 5. What is alpha?

Alpha  is the significance level.

```text
α
```

Usually:

```text
α = 0.05
```

It means:  
We allow 5% chance of error.  
So if:

```text
p < 0.05
```

we say result is significant.

### Full Simple Flow

1. Write hypotheses  
- : no difference

```text
H 0
```

- : difference exists

```text
H 1
```

2. Calculate means.  
3. Calculate standard deviation.  
4. Calculate SE.  
5. Calculate t-value.  
6. Calculate df:

```text
df = n 1 + n 2 − 2
```

7. Check t-table using df and alpha.  
8. Compare:

```text
t calculated > t critical
```

Reject .

```text
H 0
```

9. Final line:  
There is a significant difference between the two groups.

## Comparing With the Critical t-Value

No, alpha is not always 0.05, but in most exams and research examples, we use:

```text
α = 0.05
```

It means 5% chance of error is allowed.  
Sometimes alpha can be:

```text
0.01
```

for stricter testing, or:

```text
0.10
```

for less strict testing.

### If table t-value > calculated t-value

Example:

```text
= 2.306
```

ttable

```text
= 1.80
```

tcalculated  
Here:

```text
1.80 < 2.306
```

So we fail to reject .

```text
H 0
```

Meaning:  
There is no significant difference.

### If calculated t-value > table t-value

Example:

```text
= 4.10
```

tcalculated

```text
= 2.306
```

ttable  
Here:

```text
4.10 > 2.306
```

So we reject .

```text
H 0
```

Meaning:  
There is a significant difference.

#### : Null hypothesis

### H0

Means:  
No difference exists.

### H1

Means:  
Difference exists.

### Final decision rule

| Condition | Decision | Meaning |
|---|---|---|

- > Reject Significant difference  
t t H

```text
0
calculated table
```

- < Fail to reject No significant difference  
t t H

```text
0
calculated table
```

Never say “accept ” in a proper exam answer. Say:

```text
H 0
```

Fail to reject .

```text
H 0
```

|  | Show more |
|---|---|

### 1 What is SVM?

SVM is a supervised machine learning algorithm used for classification (deciding which category a data point belongs to).  
- It separates data points into classes using a line, plane, or hyperplane depending on dimensions.  
- Goal: find the best boundary between classes.

#### Hyperplane

- A decision boundary that separates classes.  
- 2D → line, 3D → plane, higher dimensions → hyperplane.

#### Support Vectors

- The closest points to the hyperplane.  
- They are the “critical” points that define the boundary.  
- SVM uses these to maximize the margin.

#### Margin

- The distance between the hyperplane and the support vectors.

#### Maximum Margin

- SVM chooses the hyperplane with the largest margin to make the classification as confident as possible.

### 3 Types of SVM

1. Linear SVM  
- Data can be separated with a straight line (2D) or plane (3D).  
- Example: Green vs Blue points with a line separating them.  
2. Non-Linear SVM  
- Data cannot be separated with a straight line.  
- SVM uses kernels to transform data to a higher dimension where it becomes linearly separable.

### 4 How Linear SVM Works (Step by Step)

Suppose we have two classes: Green and Blue.  
Step 1: Multiple possible hyperplanes  
- There are many lines that could separate the classes.  
Step 2: Choose the best hyperplane  
- The “best” line is the one with the maximum margin — farthest from the closest points of each class.  
Step 3: Identify support vectors  
- These are the points closest to the hyperplane.  
- They define the margin.

### 5 How SVM classifies a new point

Suppose we have a new point :

```text
X
```

1. Represent the point as a vector .

```text
X
```

2. Represent the hyperplane as a vector perpendicular to it.

```text
w
```

3. Distance from origin to hyperplane = .

```text
c
X ⋅w
```

4. Compute dot product:  
Decision rule:

```text
X ⋅w > c
```

- If → Point is on the right side → Class 1

```text
X ⋅w < c
```

- If → Point is on the left side → Class 2

```text
X ⋅w = c
```

- If → Point is exactly on the hyperplane

### 6 Simple Visual Example

2D points:

| X | Y | Class |
|---|---|---|
| 1 | 2 | Green |
| 2 | 3 | Green |
| 5 | 5 | Blue |
| 6 | 6 | Blue |

- Hyperplane: line separating Green and Blue  
- Support vectors: closest Green = (2,3), closest Blue = (5,5)  
- Margin = distance between hyperplane and support vectors  
- New point (3,4): calculate dot product → check which side → classify as Green or Blue.  
In short:  
- SVM draws a line/plane (hyperplane) that best separates classes.  
- Support vectors are critical points nearest the hyperplane.  
- SVM maximizes margin for confident classification.  
- For new points, SVM checks which side of the hyperplane they fall on. margin, which makes SVM extremely easy to visualize and remember.

## Closest Points and Maximum Margin

Let me explain these two concepts in a very simple way with easy examples:

### 1 Closest Point (Support Vectors)

- In SVM, the closest points are the points from each class that are nearest to the decision boundary (hyperplane).  
- These points are called support vectors.  
- They are crucial because the position of the hyperplane depends only on them, not the other points.  
Visualize:  
Imagine two groups of points:  
- Green points on the left  
- Blue points on the right  
You draw a line between them.  
- The points that are nearest to this line on each side are the support vectors. Other points far away do not affect the boundary.

### 2 Maximum Margin

- The margin is the distance between the hyperplane and the nearest points from each class.  
- Maximum margin means the hyperplane is placed so that this distance is as large as possible.  
- Why? Because a bigger margin usually makes the classifier more confident and robust.  
Visualize:  
- If the line is too close to Green points → risk misclassifying new points  
- If the line is in the middle, far from both classes → safer, more confident → maximum margin

#### Summary in simple words

| Term | Simple Meaning |
|---|---|
| Closest Points | Points nearest to the boundary → support vectors |
| Margin | Distance from boundary to support vectors |
| Maximum Margin | Place the boundary so it’s as far as possible from both |
|  | classes → better separation |

support vectors, and maximum margin, which makes it super easy to understand.

## SVM Worked Example and Points on the Hyperplane
### SVM Problem Solving Example

Suppose the hyperplane is:

```text
x 1 + x 2 − 5 = 0
```

This means:

```text
w ⋅x + b = 0
```

where:

```text
w = (1, 1)
```

and:

```text
b = −5
```

### Rule

Calculate:

```text
f(x) = x 1 + x 2 − 5
```

Then:

| Result | Meaning |
|---|---|

f(x) > 0 Class +1  
f(x) < 0 Class -1  
f(x) = 0 Point is exactly on hyperplane

### Example 1

Point:

```text
A = (4, 3)
```

Calculate:

```text
f(A) = 4 + 3 −5
= 2
```

Since:

```text
2 > 0
```

So:  
A = Class + 1

### Example 2

Point:

```text
B = (1, 2)
```

Calculate:

```text
f(B) = 1 + 2 −5
= −2
```

Since:

```text
−2 < 0
```

So:  
B = Class −1

### Example 3: Point exactly on hyperplane

Point:

```text
C = (2, 3)
```

Calculate:

```text
f(C) = 2 + 3 −5
= 0
```

Since:

```text
f(C) = 0
```

So the point lies exactly on the hyperplane.

### What if point is exactly on hyperplane?

It means:  
The model is not confident.  
Because the point is exactly on the decision boundary.  
In simple words:  
It is exactly between both classes.  
So:  
- It is not clearly Class +1  
- It is not clearly Class -1  
- It is an uncertain/borderline point  
In practical ML, the algorithm may assign it to one class by default, but conceptually it is exactly on the boundary.

### Final easy memory

```text
f(x) = w ⋅x + b
```

If:

```text
f(x) > 0
```

Right side/class +1.  
If:

```text
f(x) < 0
```

Left side/class -1.  
If:

```text
f(x) = 0
```

on hyperplane.

## w, x and b in the Hyperplane

Let me explain what w, x, and b are in SVM and how this defines a hyperplane, even in 3D or higher dimensions.

### 1 What is a Hyperplane?

- A hyperplane is a decision boundary that separates different classes.  
- In 2D, it’s a line.  
- In 3D, it’s a plane.  
- In higher dimensions, it’s a hyperplane.  
Equation of a hyperplane:

```text
w ⋅x + b = 0
```

### 2 What is w, x, and b?

1. x = input vector  
- Coordinates of the point you want to classify.  
- Example:

```text
x = (x , x )
```

  - In 2D:

```text
1 2
x = (x , x , x )
```

  - In 3D:

```text
1 2 3
```

2. w = weight vector (perpendicular to hyperplane)  
- Shows the direction of the hyperplane.  
- The hyperplane is always perpendicular to w.

```text
w = (1, 1)
```

- Example: In 2D, if , the line is perpendicular to the vector (1,1).  
3. b = bias / offset  
- Moves the hyperplane away from the origin.  
- Changes the position of the line/plane without changing its orientation.

### 3 How it becomes a hyperplane?

Equation:

```text
w ⋅x + b = 0
```

- In 2D:

```text
w 1 x 1 + w 2 x 2 + b = 0
```

This is a line — the decision boundary.  
- In 3D:

```text
w 1 x 1 + w 2 x 2 + w 3 x 3 + b = 0
```

This is a plane — the decision boundary in 3D.  
- In n-D:

```text
w 1 x 1 + w 2 x 2 + ... + w n x n + b = 0
```

This is called a hyperplane.

### 4 How the distance works

- Support vectors are points closest to the hyperplane.  
- Margin = distance from hyperplane to support vectors.  
- SVM chooses w and b to maximize this margin.  
- For any point x:

```text
f(x) = w ⋅x + b
f(x) > 0
```

- If → one side

```text
f(x) < 0
```

- If → other side

```text
f(x) = 0
```

- If → exactly on the hyperplane

#### Example in 2D

Equation:

```text
x 1 + x 2 − 5 = 0
```

- w = (1,1) → perpendicular to line  
- b = -5 → moves line away from origin  
- x = (3,2) → new point

```text
f(x) = x + − 5 = 0
```

- Check → on hyperplane

```text
1 x 2
```

#### Quick Memory

| Symbol | Meaning |
|---|---|
| w | Vector perpendicular to hyperplane (direction) |
| x | Point to classify |
| b | Bias, moves hyperplane away from origin |
| f(x) | Dot product + b → decides side of hyperplane |

and support vectors, which makes SVM very easy to visualize.

## Finding the Weights and Which Side a Point Is On
### 1. How do we get weight ? w

In SVM, we do not choose manually.

```text
w
```

The SVM algorithm learns from training data.

```text
w
```

It tries to find the best line/plane:

```text
w ⋅x + b = 0
```

such that:  
The margin between two classes is maximum.  
So:  
- = learned by model

```text
w
```

- = learned by model

```text
b
```

- = new point/input

```text
x
```

### 2. Simple example

Suppose SVM learned this boundary:

```text
x 1 + x 2 − 5 = 0
```

This means:

```text
w = (1, 1)
b = −5
```

Why?  
Because general formula is:

```text
w 1 x 1 + w 2 x 2 + b = 0
```

Compare:

```text
1x 1 + 1x 2 − 5 = 0
```

So:

```text
w 1 = 1, w 2 = 1, b = −5
```

### 3. How to know left or right side?

Take the new point , put it in:

```text
x
f(x) = w ⋅x + b
```

If:

```text
f(x) > 0
+1
```

one side, usually class .  
If:

```text
f(x) < 0
−1
```

other side, usually class .  
If:

```text
f(x) = 0
```

point is exactly on the hyperplane.

### 4. Example points

Boundary:

```text
x 1 + x 2 − 5 = 0
```

#### Point A =

```text
f(x) = 4 + 3 −5 = 2
2 > 0
```

So A is on positive side / right side / class +1.

#### Point B =

```text
f(x) = 1 + 2 −5 = −2
−2 < 0
```

So B is on negative side / left side / class -1.

#### Point C =

```text
f(x) = 2 + 3 −5 = 0
```

So C is exactly on the hyperplane.

### Very simple memory

```text
f(x) = w ⋅x + b
```

Positive = one side  
Negative = other side  
Zero = on boundary  
SVM learns and  automatically from data.

```text
w b
```

## Random Initial Weights

kind of, but with one correction:  
In SVM, can be started randomly or initialized automatically, but SVM does not

```text
w
```

just randomly keep trying lines.  
It uses an optimization process to find the best and .

```text
w b
```

### Simple idea

At first:

```text
w and b
```

may not give a good boundary.  
Then the algorithm adjusts them again and again until it finds the boundary with:  
maximum margin + minimum classification error

### Meaning

So yes:  
Weight is changed during training until the best hyperplane is found.

```text
w
```

But better exam wording:  
SVM learns the optimal weight vector and bias  from training data by solving

```text
w b
```

an optimization problem that maximizes the margin between classes.

### Easy memory

- controls the direction/angle of the line.

```text
w
```

- controls the position/shift of the line.

```text
b
```

- SVM changes and  until the best separating boundary is found.

```text
w b
```

## How the Best Hyperplane Is Checked
### 1 The goal of SVM

SVM wants to maximize the margin between the two classes while classifying all points correctly (or as best as possible if soft margin).

### 2 Equation of hyperplane

```text
w ⋅x + b = 0
```

- = weight vector (perpendicular to hyperplane)

```text
w
```

- = bias (shift of hyperplane)

```text
b
```

- = input point

```text
x
```

### 3 Margin formula

Margin = distance between hyperplane and closest points (support vectors):

```text
2
```

Margin =

```text
∥w∥
∥w∥
```

- Bigger margin = smaller

```text
∥w∥
```

- SVM wants to minimize to maximize margin.

### 4 Constraints

```text
(x , y ) = +1 −1
```

For all points , where or (class labels):

```text
i i y i
y i (w ⋅ x i + b) ≥1
```

- This ensures all points are on the correct side of the margin.

### 5 Optimization problem

SVM solves:

```text
1 2
```

Minimize ∥w∥

```text
2
```

Subject to:

```text
y i (w ⋅ x i + b) ≥1 for all i
1 ∥w∥ 2
```

- Minimize → maximize margin

```text
2
```

- Constraints → correctly classify points

### 6 Soft margin (for non-perfectly separable data)

If some points cannot be perfectly separated:

```text
y i (w ⋅ x i + b) ≥1 −ξ i
```

≥ 0→ slack variable

```text
ξ i
```

- Penalizes points inside the margin

#### Summary in simple words

1. SVM tries different hyperplanes (mathematically by solving optimization problem)  
2. It calculates margin = distance between hyperplane and support vectors

```text
(w ⋅ + b) ≥
```

3. Chooses hyperplane that maximizes the margin while satisfyingy x

```text
i i
1
```

4. Support vectors are the points that define the margin  
5. Result: best separating line/plane that classifies classes with maximum confidence. vectors in 2D and show how SVM “checks” which hyperplane is best.

## The Norm in SVM

In SVM, when we talk about maximizing the margin, we use the norm of the weight vector .

```text
w
```

#### 1 What is the norm?

- Norm = “length” or “magnitude” of a vector.  
- In math:

```text
∥w∥= w 2 1 + w 2 2 + ⋯+ w n2
```

- It tells how “big” the weight vector is.

#### 2 How SVM uses it

- Margin formula:

```text
2
```

Margin =

```text
∥w∥
∥w∥
```

- Smaller → bigger margin  
- Bigger margin → better separation between classes  
So in SVM the norm concept is directly used in the optimization:

```text
1 2
```

Minimize ∥w∥

```text
2
```

- This is equivalent to maximizing the margin.

#### 3 Intuition

- Think of as a vector perpendicular to the hyperplane.

```text
w
```

- Its length controls the “steepness” of the hyperplane.  
- Smaller length → hyperplane is balanced and far from support vectors → maximum margin.

#### Short Summary

- SVM uses the norm concept.  
- Objective: minimize the norm of → maximize the distance (margin) between the

```text
w
```

- classes.

```text
w
```

norm affects the hyperplane, which makes this super easy to visualize.

|  | Show more |
|---|---|

### 1 Hyperplane, w, x, b

- Hyperplane → The decision boundary that separates classes.

```text
w ⋅x + b = 0
```

- Equation:  
  - = weight vector (perpendicular to hyperplane)

```text
w
```

  - = input vector (point to classify)

```text
x
```

  - = bias/offset (moves the hyperplane away from origin)

```text
b
```

Decision rule:

```text
f(x) = w ⋅x + b
f(x) > 0
```

- If → one class

```text
f(x) < 0
```

- If → other class

```text
f(x) = 0
```

- If → point lies exactly on hyperplane

### 2 Hard Margin vs Soft Margin

- Hard Margin: Perfect separation, no misclassification. Only works if classes are linearly separable.  
- Soft Margin: Allows some misclassifications. Useful when data cannot be perfectly separated.  
Soft margin makes SVM more flexible for real-world data.

### 3 Non-linear SVM & Kernel

- Some data cannot be separated by a straight line.  
- Solution: Transform data to higher dimensions using a kernel function. Common kernels:  
- Linear → straight line  
- Polynomial → curved line  
- Radial Basis Function (RBF) → more flexible, Gaussian-like  
- Sigmoid → S-shape  
Kernels let SVM create non-linear hyperplanes without manually changing data.

### 4 Hyperparameters in SVM

1. Kernel → decides the transformation to higher dimension  
2. C (Regularization) → controls trade-off between margin width and misclassifications Small C → wider margin, allows some misclassification  
- Large C → narrower margin, tries to classify all points correctly (risk overfitting)  
3. Gamma (γ) → controls influence of a single training point  
- Small γ → smooth decision boundary  
- Large γ → boundary sensitive to individual points → risk overfitting

### 5 How SVM chooses best hyperplane (mathematically)

- SVM maximizes the margin: distance between hyperplane and closest points (support vectors).  
- Optimization problem:

```text
1 2 +
```

Minimize ∥w∥ subject to y (w ⋅ b) ≥1

```text
2 i x i
```

- Support vectors are points that define the margin.

### 6 Overfitting & Underfitting

- Overfitting: Model too complex → fits noise → performs poorly on new data Underfitting: Model too simple → cannot capture patterns → poor performance on both training and testing  
SVM with proper C and γ can balance this.

### 7 Pros and Cons of SVM

Pros:  
- Works for linear & non-linear classification  
- Effective in high-dimensional space  
- Can handle binary & multi-class classification  
Cons:  
- Computationally expensive (especially with kernels)  
- Choosing the right kernel requires experimentation  
- Sensitive to feature scaling → normalize data

### 8 How SVM Classifies a New Point

1. Represent point as vector x

```text
f(x) = w ⋅x + b
```

2. Compute

```text
f(x)
```

3. Decide class based on sign of  
- Positive → one class  
- Negative → other class  
- Zero → on hyperplane

### 9 SVR (Support Vector Regression)

- Same principle as SVM but for regression (predicting continuous values).  
- Feature scaling is very important.  
- Kernels (RBF, Polynomial) are used for non-linear regression.

#### In very simple words

- SVM = draw the best line/plane to separate classes  
- Support vectors = critical points closest to the line  
- Margin = distance between line and support vectors  
- Kernel = magic function to make a straight line separate non-linear data Hyperparameters (C, γ, Kernel) = control the behavior of SVM vectors, margin, and kernel transformation, which makes it extremely easy to visualize.

## Gamma and Initial Weight Vector
### Gamma  in simple words γ

Gamma controls how much one training point affects the boundary.

#### Small gamma

γ small  
Means:  
Each point has influence on a large area.  
Result:  
- Smooth boundary  
- Less complex model  
- Less overfitting risk  
Think:  
Model does not react too much to one single point.

#### Large gamma

γ large  
Means:  
Each point affects only a small nearby area.  
Result:  
- Very curvy boundary  
- Model becomes sensitive to individual points  
- More overfitting risk  
Think:  
Model tries too hard to fit every point.

### Easy example

Imagine points are students.

#### Small gamma

Teacher looks at the whole class pattern.

#### Large gamma

Teacher focuses too much on each individual student.  
So large gamma can memorize data instead of learning pattern.

### About weight vectorw Is selected from dataset? w

No.

```text
w
```

is not selected from the dataset.  
It is not one data point.  
It is a vector learned by the SVM model.

### Where does come from? w

At the start, the algorithm may initialize values automatically.  
Then during training, SVM finds the best:

```text
w
```

and:

```text
b
```

by optimization.  
Meaning:  
SVM adjusts and  until it finds the hyperplane with maximum margin.

```text
w b
```

### Simple meaning

- = actual data point from dataset

```text
x
```

- = learned weight vector

```text
w
```

- = learned bias/shift

```text
b
```

So:

```text
w ⋅x + b = 0
```

is the final learned decision boundary.

### Exam line

Gamma controls the influence of each training point. A small gamma gives a smooth boundary, while a large gamma gives a complex boundary that may overfit. The weight vector is not selected from the dataset; it is learned during

```text
w
```

training by solving an optimization problem to maximize the margin.

## Entropy Problem Solving

for SVM, is not selected from dataset. It is a weight vector learned by

```text
w
```

training. Initially it may start with random/small values, then optimization changes and

```text
w
```

until the margin becomes maximum.

```text
b
```

Now entropy.

### Entropy simple meaning

Entropy means:  
How mixed or impure the data is.  
In Decision Tree, entropy helps decide:  
Which attribute should be selected first?  
The notes say entropy measures impurity, and information gain selects the best attribute by reducing entropy.

### Entropy formula

For two classes Yes/No:  
Entropy(S) = −p log (p ) − log (p )

```text
yes 2 yes p no 2 no
```

Where:  
number of Yes

```text
=
```

pyes  
total samples  
number of No

```text
p no =
```

total samples

### Example: Tennis Dataset

Given:  
- = 9  
- No = 5  
- Total = 14

### Step 1: Find probabilities

```text
= 9 = 0.643
```

pyes

```text
14
p no = 14 5 = 0.357
```

### Step 2: Put in entropy formula

Entropy(S) = −(0.643) log (0.643) − (0.357) log (0.357)

```text
2 2
```

Log values:

```text
log 2 (0.643) ≈ −0.637
log 2 (0.357) ≈ −1.486
```

### Step 3: Multiply

```text
−(0.643)(−0.637) = 0.409
−(0.357)(−1.486) = 0.530
```

### Step 4: Add

Entropy(S) = 0.409 + 0.530  
Entropy(S) = 0.939  
Final:  
Entropy = 0.939

### What does 0.939 mean?

Entropy range is usually:

```text
0 to 1
```

- Entropy = 0 means pure data.  
- Entropy = 1 means very mixed data.  
Here:

```text
0.939
```

means data is highly mixed because Yes and No are both present.

### Pure example

Suppose 5 samples:  
- = 5  
- No = 0

```text
= 1
```

pyes

```text
p no = 0
```

Entropy:  
Entropy = 0  
Meaning:  
No confusion. All answers are Yes.

### Mixed example

Suppose:  
- = 5  
- No = 5

```text
= 0.5
```

pyes

```text
p no = 0.5
```

Entropy = −(0.5) log (0.5) − (0.5) log (0.5)

```text
2 2
= 0.5 + 0.5 = 1
```

Meaning:  
Maximum confusion.

### Information Gain formula

IG = Entropy(parent) −Weighted Entropy(children)  
Simple meaning:  
How much impurity reduced after split.  
Higher IG = better attribute.  
The notes show Outlook has highest information gain, so Outlook becomes root node.

### Very simple memory

Entropy: how mixed data is.  
Information Gain: how much mixing is reduced.  
Best attribute: highest information gain.

## Information Gain: Exam-Style Example

We can use this “job offer decision” dataset for an exam-style problem for Entropy and Information Gain (IG). I will solve it step by step, just like in exams.

### Dataset (Example)

| Salary | Distance | Cab | Accept Offer |
|---|---|---|---|
| High | Near | Yes | Yes |
| High | Near | No | Yes |
| Medium | Near | Yes | Yes |
| Low | Far | No | No |
| Low | Far | Yes | No |
| Medium | Far | No | No |

Target variable: Accept Offer (Yes/No)  
We will compute Entropy first, then Information Gain for the attribute Salary.

### Step 1: Calculate Entropy of the Dataset

Entropy formula:  
Entropy(S) = −p log (p ) − log (p )

```text
yes 2 yes p no 2 no
```

Count Yes and No:  
- = 3  
- No = 3  
- Total = 6

```text
= 3/6 = 0.5
```

pyes

```text
p no = 3/6 = 0.5
```

Entropy:  
Entropy(S) = −(0.5 ⋅log 0.5) − (0.5 ⋅log 0.5)

```text
2 2
= −(0.5 ⋅−1) −(0.5 ⋅−1) = 0.5 + 0.5 = 1
```

Entropy(S) = 1 → maximum impurity (dataset is evenly split).

### Step 2: Compute Entropy for Attribute “Salary”

Salary has 3 values: High, Medium, Low

| Salary | Count | Yes | No |
|---|---|---|---|
| High | 2 | 2 | 0 |
| Medium | 2 | 1 | 1 |
| Low | 2 | 0 | 2 |

#### Step 2a: Entropy for each Salary value

High:

```text
p yes = 2/2 = 1, p no = 0/2 = 0
1) − 0) =
```

Entropy(High) = −(1 ⋅log (0 ⋅log 0

```text
2 2
```

Medium:

```text
p yes = 1/2 = 0.5, p no = 1/2 = 0.5
```

Entropy(Medium) = −(0.5 ⋅log 0.5) − (0.5 ⋅log 0.5) = 1

```text
2 2
```

Low:

```text
p yes = 0/2 = 0, p no = 2/2 = 1
```

Entropy(Low) = −(0 ⋅log 0) − (1 ⋅log 1) = 0

```text
2 2
```

#### Step 2b: Weighted Entropy for Salary

∣subset∣

```text
∑
```

Entropy(Salary) = ⋅Entropy(subset)

```text
∣S∣
```

- High: 2/6 × 0 = 0  
- Medium: 2/6 × 1 = 0.333  
- Low: 2/6 × 0 = 0  
Entropy(Salary) = 0 + 0.333 + 0 = 0.333

### Step 3: Compute Information Gain

IG(Salary) = Entropy(S) −Entropy(Salary)  
IG(Salary) = 1 −0.333 = 0.667  
Information Gain for Salary = 0.667

### Step 4: Repeat for Other Attributes

You would repeat Steps 2–3 for Distance and Cab.  
The attribute with highest IG becomes root node in the decision tree.

#### Summary Table (Exam Style)

| Attribute | Weighted Entropy | Information Gain |
|---|---|---|
| Salary | 0.333 | 0.667 |
| Distance | ... | ... |
| Cab | ... | ... |

Choose the attribute with highest IG for splitting.

#### Quick Exam Tips

1. Always start by calculating overall entropy.  
2. For each attribute, calculate subset entropies.  
3. Compute weighted entropy.  
4. Compute Information Gain = Entropy(parent) - Weighted Entropy.  
5. Highest IG → best attribute → becomes root node. Distance, Cab and leaf nodes “Accept”/“Decline” — like a proper exam answer.
