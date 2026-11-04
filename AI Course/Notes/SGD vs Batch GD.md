# SGD vs Batch GD

## Stochastic vs Batch Gradient Descent
### Batch Gradient Descent (BGD)

In Batch Gradient Descent, we use the whole dataset at once to update weights.

#### Simple idea

- Read all training examples  
- Calculate total error  
- Update weights one time

#### Example

Suppose we have marks of 1000 students.  
Batch GD:  
1. Check all 1000 students  
2. Find average error  
3. Update model once

#### Characteristics

- More accurate and stable  
- But slower for huge data  
- Needs more memory

### Stochastic Gradient Descent (SGD)

In Stochastic Gradient Descent, we update weights using one training example at a time.

#### Simple idea

- Take 1 example  
- Calculate error  
- Immediately update weights

#### Example

Again with 1000 students:  
SGD:  
1. Check student 1 → update  
2. Check student 2 → update  
3. Check student 3 → update  
4. Continue...

#### Characteristics

- Faster  
- Uses less memory  
- But updates are noisy/jumpy

### Easy Analogy

Imagine learning basketball shots:  
- Batch GD:  
- Watch recordings of all shots first, then improve technique once.  
- SGD:  
- After every single shot, immediately correct yourself.

### Main Difference

| Feature | Batch GD | SGD |
|---|---|---|
| Data used | Whole dataset | One example |
| Speed | Slower | Faster |
| Memory | More | Less |
| Updates | Stable | Noisy |
| Best for | Small datasets | Large datasets |

Gradient descent mainly tries to minimize error by moving weights toward minimum loss.  
Central formula:

```text
w new = w old − η ∂w ∂L
```

Where:  
η= learning rate  
L= loss/error  
w= weight/parameter
