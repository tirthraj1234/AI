# Linear Discriminant Analysis (LDA) Notes

## Day 10 – Linear Discriminant Analysis (LDA)

## What is Linear Discriminant Analysis (LDA)?

Linear Discriminant Analysis (LDA) is a **supervised machine learning** technique used for **dimensionality reduction** and **classification**. It reduces the number of features while maximizing the separation between different classes in the dataset.

Unlike PCA, which ignores class labels, LDA uses the target labels to find the best feature combinations that separate classes.

---

## Why is LDA Used?

LDA is used to:

- Reduce the number of features.
- Maximize class separability.
- Improve classification performance.
- Reduce computational complexity.
- Remove redundant information.
- Visualize high-dimensional data.

---

## Working Principle of LDA

LDA works by:

1. Calculating the mean of each class.
2. Computing the Within-Class Scatter Matrix.
3. Computing the Between-Class Scatter Matrix.
4. Finding eigenvalues and eigenvectors.
5. Selecting the most important linear discriminants.
6. Projecting the original data into a lower-dimensional space.

The objective is to maximize the distance between different classes while minimizing the spread within the same class.

---

## Supervised Learning

LDA is a **supervised learning** algorithm because it requires labeled data during training.

Input:
- Features (X)
- Target Labels (y)

The class labels help LDA identify the directions that best separate the classes.

---

## Difference Between PCA and LDA

| PCA | LDA |
|-----|-----|
| Unsupervised learning | Supervised learning |
| Does not use class labels | Uses class labels |
| Maximizes variance | Maximizes class separation |
| Used for feature extraction | Used for feature extraction and classification |
| Focuses on data representation | Focuses on class discrimination |

---

## Advantages of LDA

- Reduces feature dimensions.
- Improves classification accuracy.
- Uses class information effectively.
- Reduces computational cost.
- Easy to implement.
- Useful for visualization.
- Helps reduce overfitting.

---

## Limitations of LDA

- Assumes data is normally distributed.
- Assumes equal covariance among classes.
- Sensitive to outliers.
- Not suitable for highly non-linear data.
- Performance decreases if assumptions are violated.

---

## Python Example

```python
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Apply LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_lda.shape)
```

---

## Real-World Applications

LDA is commonly used in:

- Face Recognition
- Medical Diagnosis
- Fraud Detection
- Customer Classification
- Document Classification
- Image Recognition
- Bioinformatics
- Credit Risk Analysis
- Speech Recognition

---

## Best Practices

- Standardize data before applying LDA (recommended).
- Use labeled datasets.
- Remove missing values.
- Handle outliers carefully.
- Evaluate the model using classification metrics.

---

## Key Learnings

Today I learned:

- What Linear Discriminant Analysis (LDA) is.
- Why LDA is used.
- The working principle of LDA.
- The difference between PCA and LDA.
- The advantages and limitations of LDA.
- How to implement LDA using Scikit-learn.
- Real-world applications of LDA.

---

## Conclusion

Linear Discriminant Analysis (LDA) is a powerful supervised dimensionality reduction technique that improves class separation while reducing the number of features. It is widely used in classification tasks because it preserves the most discriminative information in the dataset. LDA is especially useful in applications such as face recognition, medical diagnosis, and customer classification, where accurate class separation is important.