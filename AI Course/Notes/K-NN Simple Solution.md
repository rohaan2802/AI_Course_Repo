# K-NN Simple Solution

## K-NN: Short Worked Solution
### Q1 Given Test Point T = (5,5)

Training data:

| Point | (x1,x2) | Class |
|---|---|---|
| P1 | (2,6) | G |
| P2 | (6,3) | Y |
| P3 | (8,7) | Y |
| P4 | (3,2) | G |

#### a) Using L1 (Manhattan), k = 1

Formula:

```text
∣x 1 − a∣+ ∣x − 2 b∣
```

For T = (5,5)  
- P1 = |5-2| + |5-6| = 3 + 1 = 4  
- P2 = |5-6| + |5-3| = 1 + 2 = 3 P3 = |5-8| + |5-7| = 3 + 2 = 5 P4 = |5-3| + |5-2| = 2 + 3 = 5 Nearest = P2

#### b) Using L2 (Euclidean), k = 3

Formula:

```text
(x 1 −a) + (x 2 2 −b) 2
```

- P1 = √((5-2)² + (5-6)²) = √10 = 3.16 P2 = √((5-6)² + (5-3)²) = √5 = 2.24 P3 = √((5-8)² + (5-7)²) = √13 = 3.61 P4 = √((5-3)² + (5-2)²) = √13 = 3.61 Nearest 3 points:  
1. P2 = Y  
2. P1 = G  
3. P3 = Y  
Votes:  
- Y = 2  
- G = 1

### Q2 Dataset = 20,000 Images

Split:  
- Training = 70%  
- Validation = 15%  
- Testing = 15%

#### a) Validation Images

```text
20000 × 15% = 3000
```

#### b) Time for 5-NN on Test Set

Test set:

```text
20000 × 15% = 3000
```

Training set:

```text
20000 × 70% = 14000
```

Each test image compares with all training images:

```text
3000 × 14000 = 42, 000, 000
```

Each distance = 0.03 ms  
Total time:

```text
42, 000, 000 × 0.03 = 1, 260, 000 ms
```

Convert to minutes:

```text
1, 260, 000/1000 = 1260 sec
1260/60 = 21 min
```

### Final Answers

#### Q1

a) Y  
b) Y

#### Q2

a) 3000 images  
b) 21 minutes
