# Distance Metrics in KNN Notes

## Day 6 – Distance Metrics in K-Nearest Neighbors (KNN)

## What are Distance Metrics?

Distance Metrics are mathematical methods used to calculate the distance between two data points. In the K-Nearest Neighbors (KNN) algorithm, these metrics help identify the nearest neighbors to a new data point.

The nearest neighbors are then used to make predictions for classification or regression tasks.

---

## Why are Distance Metrics Important?

Distance Metrics are important because they:

- Identify the nearest data points.
- Improve prediction accuracy.
- Help classify new data correctly.
- Affect the overall performance of the KNN model.

Choosing the appropriate distance metric can significantly improve model performance.

---

## 1. Euclidean Distance

Euclidean Distance is the straight-line distance between two points. It is the default and most commonly used distance metric in KNN.

### Formula

```
Distance = √((x₂ - x₁)² + (y₂ - y₁)²)
```

### Characteristics

- Simple and easy to calculate.
- Suitable for continuous numerical data.
- Works well when features are properly scaled.

### Python Example

```python
from math import sqrt

A = (2, 3)
B = (5, 7)

distance = sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)

print(distance)
```

---

## 2. Manhattan Distance

Manhattan Distance measures the distance by moving horizontally and vertically, similar to traveling through city streets arranged in a grid.

### Formula

```
Distance = |x₂ - x₁| + |y₂ - y₁|
```

### Characteristics

- Uses horizontal and vertical movement.
- Less sensitive to large differences in feature values.
- Useful for grid-based data.

### Python Example

```python
A = (2, 3)
B = (5, 7)

distance = abs(B[0] - A[0]) + abs(B[1] - A[1])

print(distance)
```

---

## 3. Minkowski Distance

Minkowski Distance is a generalized distance metric that includes both Euclidean and Manhattan Distance.

- When **p = 1**, it becomes Manhattan Distance.
- When **p = 2**, it becomes Euclidean Distance.

It provides flexibility for different types of datasets.

### Characteristics

- Generalized distance measure.
- Flexible and widely used.
- Can adapt to different values of **p**.

---

## Comparison of Distance Metrics

| Distance Metric | Best For | Characteristics |
|-----------------|----------|-----------------|
| Euclidean | Continuous numerical data | Straight-line distance |
| Manhattan | Grid-based or city-block data | Horizontal and vertical movement |
| Minkowski | Flexible applications | General form of Euclidean and Manhattan |

---

## Advantages of Distance Metrics

- Easy to understand and implement.
- Help identify similar data points.
- Improve prediction accuracy.
- Support both classification and regression tasks.
- Flexible for different datasets.

---

## Limitations

- Sensitive to feature scales.
- Performance depends on selecting the appropriate metric.
- Large datasets increase computation time.
- Irrelevant features can reduce accuracy.

---

## Real-World Applications

Distance Metrics are used in:

- Employee Attrition Prediction
- Customer Recommendation Systems
- Medical Diagnosis
- Fraud Detection
- Image Recognition
- Face Recognition
- Product Recommendation
- Pattern Recognition
- Document Classification

---

## Key Learnings

Today I learned:

- What Distance Metrics are.
- Why Distance Metrics are important in KNN.
- The concepts of Euclidean, Manhattan, and Minkowski Distance.
- Differences between the three distance metrics.
- How Distance Metrics affect KNN model performance.
- Basic Python implementation of Distance Metrics.

---

## Conclusion

Distance Metrics are a fundamental part of the K-Nearest Neighbors (KNN) algorithm. They determine which training samples are closest to a new data point and directly influence the model's predictions. Understanding Euclidean, Manhattan, and Minkowski Distance helps in selecting the most appropriate metric for different Machine Learning problems and improves the accuracy of KNN models.