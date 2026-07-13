# K-Nearest Neighbors (KNN) Notes

## Day 6 – Introduction to K-Nearest Neighbors (KNN)

## What is KNN?

K-Nearest Neighbors (KNN) is a **Supervised Machine Learning algorithm** used for both **classification** and **regression** tasks.

KNN predicts the output of a new data point by finding the **K nearest neighbors** in the training dataset. For classification, it assigns the class that is most common among the nearest neighbors. For regression, it predicts the average value of the nearest neighbors.

KNN is called a **Lazy Learning** algorithm because it does not build a model during training. Instead, it stores the training data and makes predictions only when new data is provided.

---

## How Does KNN Work?

The KNN algorithm follows these steps:

1. Load the training dataset.
2. Choose the value of **K** (number of neighbors).
3. Calculate the distance between the new data point and all training data.
4. Find the **K nearest neighbors**.
5. For classification, select the majority class.
6. For regression, calculate the average of the nearest neighbors.
7. Return the predicted result.

---

## Types of KNN

### 1. KNN Classification

Used when the target variable is categorical.

**Example Applications:**

- Spam Email Detection
- Employee Attrition Prediction
- Disease Classification

---

### 2. KNN Regression

Used when the target variable is continuous.

**Example Applications:**

- House Price Prediction
- Sales Forecasting
- Temperature Prediction

---

## Advantages of KNN

- Simple and easy to understand.
- Easy to implement.
- No training phase is required.
- Works for both classification and regression.
- Performs well on small datasets.
- Can model complex decision boundaries.

---

## Limitations of KNN

- Prediction is slow for large datasets.
- Sensitive to irrelevant features.
- Requires feature scaling for better performance.
- Choosing the correct value of **K** is important.
- Uses more memory because it stores all training data.

---

## Python Libraries Used

```python
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

---

## Real-World Applications

KNN is widely used in:

- Employee Attrition Prediction
- Customer Recommendation Systems
- Medical Diagnosis
- Image Recognition
- Face Recognition
- Fraud Detection
- Credit Risk Analysis
- Product Recommendation
- Pattern Recognition

---

## Key Learnings

Today I learned:

- What K-Nearest Neighbors (KNN) is.
- How KNN works.
- The difference between KNN Classification and KNN Regression.
- Advantages and limitations of KNN.
- Why KNN is called a Lazy Learning algorithm.
- Real-world applications of KNN.
- Basic Python libraries required to implement KNN.

---

## Conclusion

K-Nearest Neighbors (KNN) is a simple and effective supervised Machine Learning algorithm used for both classification and regression. It predicts the output based on the nearest data points in the training dataset. Although KNN is easy to understand and implement, its performance depends on selecting the appropriate value of **K** and applying proper feature scaling. It is widely used in recommendation systems, healthcare, finance, and many other real-world applications.