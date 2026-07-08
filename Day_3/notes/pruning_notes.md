# Overfitting and Pruning Notes

## Day 3 – Overfitting & Pruning

## What is Overfitting?

Overfitting occurs when a Machine Learning model learns the training data too well, including its noise and unnecessary details. As a result, the model performs very well on the training data but performs poorly on new, unseen data.

### Characteristics of Overfitting

- Very high training accuracy.
- Low testing accuracy.
- Poor generalization.
- Complex and deep Decision Tree.

---

## What is Underfitting?

Underfitting occurs when a model is too simple to learn the patterns present in the training data. As a result, it performs poorly on both the training and testing datasets.

### Characteristics of Underfitting

- Low training accuracy.
- Low testing accuracy.
- Unable to capture important patterns.
- Oversimplified model.

---

## Difference Between Overfitting and Underfitting

| Overfitting | Underfitting |
|--------------|--------------|
| Learns training data too well, including noise. | Does not learn enough from the training data. |
| High training accuracy. | Low training accuracy. |
| Low testing accuracy. | Low testing accuracy. |
| Complex model. | Simple model. |

---

## What is Pruning?

Pruning is the process of reducing the size of a Decision Tree by removing unnecessary branches that do not improve prediction accuracy. It helps create a simpler model that performs better on unseen data.

The main goal of pruning is to reduce overfitting and improve the model's ability to generalize.

---

## Types of Pruning

### 1. Pre-Pruning (Early Stopping)

Pre-Pruning stops the growth of the Decision Tree before it becomes too large.

Common parameters used in Scikit-learn:

- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- `max_leaf_nodes`

Example:

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=3)
```

---

### 2. Post-Pruning

Post-Pruning allows the tree to grow completely and then removes unnecessary branches.

In Scikit-learn, Post-Pruning is performed using the `ccp_alpha` parameter.

Example:

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(ccp_alpha=0.01)
```

---

## Advantages of Pruning

- Reduces overfitting.
- Improves model generalization.
- Creates a simpler and more understandable Decision Tree.
- Reduces model complexity.
- Improves prediction performance on unseen data.

---

## Limitations of Pruning

- Excessive pruning may reduce model accuracy.
- Selecting the correct pruning parameters can be difficult.
- Too much pruning may lead to underfitting.

---

## Real-World Applications

Pruning is used in:

- Employee Promotion Prediction
- Loan Approval Systems
- Medical Diagnosis
- Fraud Detection
- Customer Churn Prediction
- Credit Risk Analysis
- Insurance Risk Prediction
- Student Performance Analysis

---

## Key Learnings

Today I learned:

- What Overfitting is.
- What Underfitting is.
- The differences between Overfitting and Underfitting.
- What Pruning is and why it is important.
- The difference between Pre-Pruning and Post-Pruning.
- How to use `max_depth` and `ccp_alpha` in Scikit-learn.
- How pruning improves the performance of Decision Trees.

---

## Conclusion

Overfitting reduces the performance of a Decision Tree on new data by making it too complex. Pruning helps solve this problem by removing unnecessary branches and simplifying the tree. A well-pruned Decision Tree is easier to understand, performs better on unseen data, and provides more reliable predictions.