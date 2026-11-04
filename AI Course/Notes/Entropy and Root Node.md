# Entropy and Root Node

In a decision tree, the root node is chosen based on entropy and information gain:  
1. Entropy measures the disorder or impurity in a dataset. It is defined as:

```text
c
∑
```

Entropy(S) = − log

```text
p i 2 p i
i=1
```

where is the proportion of samples in class  and  is the number of classes.

```text
p i i c
```

2. To select the root node, you calculate the information gain for each feature:

```text
∣S v ∣
∑
```

Entropy(S )  
IG(S, A) = Entropy(S) −

```text
∣S∣ v
v∈Values(A)
```

- = whole dataset

```text
S
```

  - = a feature/attribute

```text
A
```

  - = subset of where feature has value

```text
S v S A v
```

3. Which node becomes the root?  
  - The feature that maximizes information gain (or equivalently, minimizes entropy after the split) is chosen as the root node.  
  - In other words:  
    - If a feature splits the dataset into subsets that are pure (entropy close to 0), it has high information gain → more likely to be root.  
    - Features with low information gain (subsets still mixed, high entropy) are less likely to be root.  
Rule of thumb:  
- Root node = feature with lowest entropy after splitting (or highest  
- information gain).  
Intuition:  
- You want the root node to “explain” the most about your target classes. Lower entropy means less uncertainty in the split. features and which one becomes root. It makes it very clear.

#### Information Gain (IG) Formula

```text
∑ ∣S v ∣ ×
```

IG(S, A) = Entropy(S) − Entropy(S )

```text
∣S∣ v
v∈Values(A)
```

#### Where

- IG(S,A) = Information Gain of attribute A  
- Entropy(S) = Entropy of the whole dataset  
- Values(A) = All possible values of attribute A  
- |Sᵥ| = Number of samples in subset Sᵥ  
- |S| = Total number of samples in dataset  
- Entropy(Sᵥ) = Entropy of subset Sᵥ

#### Entropy Formula

```text
n
∑
```

Entropy(S) = − log (p )

```text
p i 2 i
i=1
```

where:  
  - = Probability of class

```text
p i i
```

#### Shortcut for Exam

Information Gain = Parent Entropy −Weighted Average Child Entropy

#### Root Node Selection

Choose the attribute with the Highest Information Gain  
or equivalently,  
Choose the attribute that gives the Lowest Entropy after splitting

## Parent Node and the Dataset

exactly!  
- Parent = the entire dataset before the split.  
- Child subsets = the parts you get after splitting the dataset based on a feature. So in the IG formula:

```text
∣S v ∣
∑
```

Entropy(S )  
IG(S, A) = Entropy(Parent S) −

```text
∣S∣ v
v∈Values(A)
```

- Entropy(Parent S) = entropy of the whole dataset before any split  
- S_v = subset of data for a specific value of feature A  
Intuition: You measure how much “uncertainty” decreases when you split the parent dataset by feature A. The more it decreases → higher IG → more likely to be the root node. entropy, child entropies, and IG. It’s very clear visually.
