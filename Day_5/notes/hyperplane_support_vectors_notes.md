# Hyperplane & Support Vectors Notes

## Day 5 – Hyperplane & Support Vectors

## What is a Hyperplane?

A Hyperplane is the decision boundary used by the Support Vector Machine (SVM) algorithm to separate different classes in a dataset.

The objective of SVM is to find the optimal hyperplane that divides the data while maximizing the distance (margin) between the classes.

The shape of the hyperplane depends on the number of features:

- In 2-dimensional data, the hyperplane is a straight line.
- In 3-dimensional data, the hyperplane is a flat plane.
- In higher dimensions, it is called a hyperplane.

---

## What is the Optimal Hyperplane?

The optimal hyperplane is the one that separates the classes with the maximum possible margin.

A larger margin helps the model classify new data more accurately and reduces the chance of overfitting.

---

## What are Support Vectors?

Support Vectors are the data points that are closest to the hyperplane.

These points are the most important observations in the dataset because they determine the position and direction of the decision boundary.

If the support vectors change, the hyperplane also changes.

---

## How Do Hyperplane and Support Vectors Work Together?

The Support Vector Machine algorithm works as follows:

1. Load the training dataset.
2. Identify the support vectors.
3. Find the optimal hyperplane.
4. Maximize the margin between the classes.
5. Use the hyperplane to classify new data.

The support vectors directly influence where the hyperplane is placed.

---

## Example

Suppose we want to classify employees into:

- High Performer
- Low Performer

SVM identifies the employees closest to the decision boundary as support vectors and places the hyperplane between the two groups with the maximum margin.

---

## Advantages

- Produces accurate classification.
- Maximizes the margin for better generalization.
- Uses only important data points (support vectors).
- Reduces overfitting.
- Works well with high-dimensional datasets.

---

## Limitations

- Training becomes slower for large datasets.
- Sensitive to noisy data.
- Selecting the correct kernel and parameters is important.
- Difficult to visualize in higher dimensions.

---

## Python Example

```python
from sklearn import datasets
from sklearn.svm import SVC

X, y = datasets.load_iris(return_X_y=True)

model = SVC(kernel="linear")
model.fit(X, y)

print("Number of Support Vectors:", model.n_support_)
print("Support Vector Indices:", model.support_)
```

---

## Real-World Applications

Hyperplanes and Support Vectors are used in:

- Spam Email Detection
- Face Recognition
- Image Classification
- Medical Diagnosis
- Fraud Detection
- Customer Churn Prediction
- Text Classification
- Handwriting Recognition
- Sentiment Analysis

---

## Key Learnings

Today I learned:

- What a Hyperplane is.
- What an Optimal Hyperplane is.
- What Support Vectors are.
- How Support Vectors determine the Hyperplane.
- The relationship between Hyperplanes and Support Vectors.
- Advantages and limitations of using SVM.
- Practical implementation using Scikit-learn.

---

## Conclusion

Hyperplanes and Support Vectors are the foundation of the Support Vector Machine algorithm. The hyperplane acts as the decision boundary, while the support vectors define its position. By maximizing the margin between classes, SVM achieves accurate and reliable classification, making it one of the most effective algorithms for many real-world machine learning applications.