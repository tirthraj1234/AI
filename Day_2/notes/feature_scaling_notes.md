# Feature Scaling Notes

## Day 2 – Feature Scaling

## What is Feature Scaling?

Feature Scaling is a data preprocessing technique used to bring all numerical features to a similar range. It helps Machine Learning algorithms perform better by ensuring that no feature with a larger value dominates the learning process.

---

## Why is Feature Scaling Important?

Feature Scaling is important because:

- Improves the performance of Machine Learning models.
- Speeds up the training process.
- Prevents features with larger values from dominating smaller values.
- Improves the accuracy of distance-based algorithms.
- Helps optimization algorithms converge faster.

---

## Types of Feature Scaling

### 1. Standardization (Z-Score Scaling)

Standardization transforms data so that it has:

- Mean = 0
- Standard Deviation = 1

### Formula

```
Z = (X - Mean) / Standard Deviation
```

### Python Example

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
```

### When to Use

- Data follows a normal distribution.
- Algorithms like Logistic Regression, SVM, Neural Networks, and PCA.

---

### 2. Normalization (Min-Max Scaling)

Normalization scales all values to a fixed range, usually between **0 and 1**.

### Formula

```
X' = (X - Min) / (Max - Min)
```

### Python Example

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)
```

### When to Use

- Data does not follow a normal distribution.
- Algorithms such as KNN and Neural Networks.
- When all features should be in the same range.

---

## Difference Between Standardization and Normalization

| Standardization | Normalization |
|-----------------|---------------|
| Mean becomes 0 and standard deviation becomes 1. | Values are scaled between 0 and 1. |
| Values may be negative or greater than 1. | Values always remain between 0 and 1. |
| Suitable for normally distributed data. | Suitable when feature values have different ranges. |

---

## Algorithms That Require Feature Scaling

Feature Scaling is recommended for:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Neural Networks
- K-Means Clustering
- Principal Component Analysis (PCA)

Algorithms that generally do **not** require Feature Scaling:

- Decision Tree
- Random Forest
- XGBoost
- LightGBM

---

## Advantages of Feature Scaling

- Improves model accuracy.
- Reduces training time.
- Prevents bias toward larger feature values.
- Improves convergence of optimization algorithms.
- Produces more stable Machine Learning models.

---

## Real-World Applications

Feature Scaling is commonly used in:

- Customer Purchase Prediction
- Credit Risk Analysis
- Medical Diagnosis
- Image Recognition
- Recommendation Systems
- Fraud Detection
- Sales Forecasting

---

## Key Learnings

Today I learned:

- What Feature Scaling is.
- Why Feature Scaling is important.
- The difference between Standardization and Normalization.
- How to apply StandardScaler and MinMaxScaler.
- Which Machine Learning algorithms require Feature Scaling.
- How Feature Scaling improves model performance.

---

## Conclusion

Feature Scaling is an important data preprocessing step in Machine Learning. It ensures that all numerical features contribute equally to the learning process. Choosing the correct scaling technique improves model accuracy, training speed, and overall performance.