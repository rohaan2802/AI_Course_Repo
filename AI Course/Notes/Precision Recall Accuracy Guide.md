# Precision Recall Accuracy Guide

|  | Upgrade |
|---|---|

## Choosing Between Precision, Recall and Accuracy

A simple way to decide is to ask:  
"Which mistake is more costly?"  
There are two types of mistakes:  
- False Positive (FP): Predicting YES when the answer is actually NO.  
- False Negative (FN): Predicting NO when the answer is actually YES.

#### 1. Use Accuracy

When classes are balanced and both types of mistakes are equally important.

```text
TP + TN
```

Accuracy =

```text
TP + TN + FP + FN
```

Example:  
- Student pass/fail prediction  
- 50% pass, 50% fail  
- Both mistakes have similar importance  
If accuracy = 95%, that's meaningful.

#### 2. Use Precision

When False Positives are costly.

```text
TP
```

Precision =

```text
TP + FP
```

It answers:  
- "Out of all positive predictions, how many were actually positive?"  
Examples:  
- Spam detection  
  - Marking an important email as spam is bad.  
- Predicting a person is a criminal.  
- Approving a loan to risky customers.  
Example:  
Suppose AI says 100 emails are spam.  
Only 90 are actually spam.  
Precision = 90/100 = 90%  
So precision focuses on avoiding false alarms.

#### 3. Use Recall

When False Negatives are costly.

```text
TP
```

Recall =

```text
TP + FN
```

It answers:  
- "Out of all actual positives, how many did we find?"  
Examples:  
- Cancer detection  
- Fraud detection  
- Terrorist detection  
- Disease screening  
If a cancer patient is missed, that is very serious.  
Example:  
100 people actually have cancer.  
System finds only 80.  
Recall = 80/100 = 80%  
So recall focuses on not missing important cases.

#### Quick Memory Trick

| Metric | Important When | Want to Reduce |
|---|---|---|
| Accuracy | Balanced data and equal costs | Both FP and FN |
| Precision | False positives are dangerous | FP |
| Recall | False negatives are dangerous | FN |

#### Real-World Examples

| Problem | Metric |
|---|---|
| Cancer detection | Recall |
| Fraud detection | Recall |
| Spam filter | Precision |
| Loan approval | Precision |
| Face unlock on phone | Precision |
| General balanced classification | Accuracy |

#### Interview/Exam Rule

Ask:  
1. Classes balanced and no special cost? → Accuracy  
2. False Positive expensive? → Precision  
3. False Negative expensive? → Recall  
That's usually enough to choose the correct metric in most exam questions.

## When a False Positive or a False Negative Costs More

A very easy trick is:

#### Ask yourself

"What happens if the model says YES when it should have said NO?" → False Positive (FP)  
"What happens if the model says NO when it should have said YES?" → False Negative (FN)  
Then see which mistake causes more damage.

#### Example 1: Cancer Detection

Actual: Cancer  
Prediction: No Cancer  
This is a False Negative (FN).  
Result:  
- Patient goes home untreated.  
- Disease may spread.  
Very dangerous.  
So FN is more costly → Focus on Recall.

#### Example 2: Spam Detection

Actual: Important Email  
Prediction: Spam  
This is a False Positive (FP).  
Result:  
- Important email may be missed.  
Costly.  
So FP is more costly → Focus on Precision.

#### Example 3: Fraud Detection

Actual: Fraud Transaction  
Prediction: Normal Transaction  
This is a False Negative (FN).  
Result:  
- Fraudster gets away with money.  
Costly.  
So FN is more costly → Focus on Recall.

#### Example 4: Face Unlock

Actual: Stranger  
Prediction: Owner  
This is a False Positive (FP).  
Result:  
- Unauthorized person gets access.  
Very dangerous.  
So FP is more costly → Focus on Precision.

#### Fast Exam Trick

Think:

| Question | Costly Error |
|---|---|
|  | FN → Recall |
| "Missing a positive case is dangerous?" |  |
|  | FP → Precision |
| "Giving a positive result to a negative case is dangerous?" |  |

#### One-Line Memory

- Recall = "Don't miss important positives." → Reduce FN  
·Precision=Don'traisefalsealarms."-→ReduceFp  
So whenever you're confused, imagine the consequences of each mistake and choose the metric that minimizes the more harmful one.
