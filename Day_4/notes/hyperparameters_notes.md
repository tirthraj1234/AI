# Hyperparameters in Random Forest Notes

## Day 4 – Hyperparameters in Random Forest

## What are Hyperparameters?

Hyperparameters are settings that are defined before training a Machine Learning model. They control how the model learns from the data and can significantly affect its performance.

Unlike model parameters, which are learned automatically during training, hyperparameters are chosen by the developer.

Selecting appropriate hyperparameters helps improve model accuracy, reduce overfitting, and optimize training time.

---

## Why are Hyperparameters Important?

Hyperparameters are important because they:

- Improve model accuracy.
- Reduce overfitting.
- Improve model generalization.
- Control the complexity of the model.
- Optimize training and prediction performance.

---

## Common Hyperparameters in Random Forest

### 1. n_estimators

The `n_estimators` parameter specifies the number of Decision Trees in the Random Forest.

- More trees generally improve accuracy.
- Too many trees increase training time and memory usage.

Example:

```python
RandomForestClassifier(n_estimators=100)
```

---

### 2. max_depth

The `max_depth` parameter limits the maximum depth of each Decision Tree.

- Prevents trees from becoming too deep.
- Helps reduce overfitting.

Example:

```python
RandomForestClassifier(max_depth=5)
```

---

### 3. min_samples_split

The `min_samples_split` parameter defines the minimum number of samples required to split an internal node.

- Higher values produce simpler trees.
- Helps reduce overfitting.

Example:

```python
RandomForestClassifier(min_samples_split=2)
```

---

### 4. min_samples_leaf

The `min_samples_leaf` parameter specifies the minimum number of samples required in a leaf node.

- Prevents the creation of very small leaf nodes.
- Improves model stability.

Example:

```python
RandomForestClassifier(min_samples_leaf=1)
```

---

### 5. max_features

The `max_features` parameter determines the number of features considered when selecting the best split.

Common values include:

- `"sqrt"` – Square root of the total number of features (default for classification).
- `"log2"` – Log base 2 of the total number of features.
- `None` – Use all available features.

Example:

```python
RandomForestClassifier(max_features="sqrt")
```

---

### 6. random_state

The `random_state` parameter controls the randomness of the algorithm.

Using the same random state ensures that the model produces the same results every time it is trained with the same data.

Example:

```python
RandomForestClassifier(random_state=42)
```

---

## Advantages of Hyperparameter Tuning

- Improves prediction accuracy.
- Reduces overfitting.
- Increases model reliability.
- Optimizes training performance.
- Helps build better Machine Learning models.

---

## Limitations

- Finding the best hyperparameters can take time.
- Too much tuning may increase computational cost.
- Incorrect values may reduce model performance.

---

## Real-World Applications

Hyperparameter tuning is used in:

- Customer Churn Prediction
- Employee Salary Prediction
- Loan Approval Systems
- Fraud Detection
- Medical Diagnosis
- Credit Risk Analysis
- Product Recommendation Systems
- Sales Forecasting
- Financial Risk Prediction

---

## Python Example

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features="sqrt",
    random_state=42
)

print(model)
```

---

## Key Learnings

Today I learned:

- What hyperparameters are.
- The difference between model parameters and hyperparameters.
- The purpose of `n_estimators`.
- How `max_depth` helps reduce overfitting.
- The role of `min_samples_split` and `min_samples_leaf`.
- Why `max_features` is important.
- How `random_state` ensures reproducible results.
- The importance of hyperparameter tuning in Machine Learning.

---

## Conclusion

Hyperparameters play a crucial role in the performance of a Random Forest model. Choosing appropriate values for parameters such as `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_features`, and `random_state` helps create accurate, stable, and efficient Machine Learning models. Proper hyperparameter tuning improves prediction quality and is an essential step in developing real-world AI applications.