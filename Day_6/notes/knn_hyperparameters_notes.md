# KNN Hyperparameters Notes

## Day 6 – KNN Hyperparameters

## What are Hyperparameters?

Hyperparameters are settings that are defined before training a Machine Learning model. They control how the algorithm works and have a significant impact on the model's performance and prediction accuracy.

In the K-Nearest Neighbors (KNN) algorithm, selecting the correct hyperparameters helps improve the quality of predictions and model efficiency.

---

## Why are Hyperparameters Important?

Hyperparameters help to:

- Improve prediction accuracy.
- Control model complexity.
- Reduce overfitting and underfitting.
- Optimize model performance.
- Improve generalization to new data.

---

## 1. n_neighbors

The **n_neighbors** parameter specifies the number of nearest neighbors (K) used to make a prediction.

### Characteristics

- Small values may cause overfitting.
- Large values may cause underfitting.
- Common values are **3**, **5**, and **7**.

### Example

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5)
```

---

## 2. weights

The **weights** parameter determines how much influence each neighbor has on the prediction.

### Types

### Uniform

- All neighbors have equal importance.

Example:

```python
model = KNeighborsClassifier(weights="uniform")
```

### Distance

- Closer neighbors have greater influence than farther neighbors.

Example:

```python
model = KNeighborsClassifier(weights="distance")
```

---

## 3. algorithm

The **algorithm** parameter specifies how the nearest neighbors are searched.

### Available Options

- **auto** – Automatically selects the best search algorithm.
- **ball_tree** – Efficient for high-dimensional datasets.
- **kd_tree** – Efficient for low-dimensional datasets.
- **brute** – Compares every training sample.

### Example

```python
model = KNeighborsClassifier(algorithm="auto")
```

---

## 4. metric

The **metric** parameter defines the method used to calculate the distance between data points.

### Common Metrics

- Euclidean
- Manhattan
- Minkowski

### Example

```python
model = KNeighborsClassifier(metric="euclidean")
```

---

## Advantages of Proper Hyperparameter Selection

- Improves prediction accuracy.
- Reduces overfitting.
- Improves model reliability.
- Optimizes KNN performance.
- Enhances generalization on unseen data.

---

## Limitations

- Finding the best hyperparameters requires experimentation.
- Incorrect values can reduce accuracy.
- Performance depends on the dataset.
- Large datasets may require additional tuning.

---

## Python Example

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(
    n_neighbors=5,
    weights="uniform",
    algorithm="auto",
    metric="minkowski"
)

print(model)
```

---

## Real-World Applications

KNN hyperparameter tuning is used in:

- Employee Attrition Prediction
- Customer Recommendation Systems
- Medical Diagnosis
- Fraud Detection
- Credit Risk Analysis
- Face Recognition
- Image Classification
- Product Recommendation
- Pattern Recognition

---

## Key Learnings

Today I learned:

- What hyperparameters are in KNN.
- The purpose of **n_neighbors**.
- The difference between **uniform** and **distance** weights.
- The role of the **algorithm** parameter.
- Different distance metrics used in KNN.
- How hyperparameters affect model performance.
- Basic implementation of KNN hyperparameters using Scikit-learn.

---

## Conclusion

Hyperparameters play an important role in the K-Nearest Neighbors (KNN) algorithm. Parameters such as **n_neighbors**, **weights**, **algorithm**, and **metric** determine how the model identifies nearest neighbors and makes predictions. Selecting appropriate hyperparameters helps improve accuracy, reduce errors, and build reliable Machine Learning models for real-world applications.