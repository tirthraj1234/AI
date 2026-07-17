# Explained Variance Notes

## Day 9 – Explained Variance in PCA

## What is Explained Variance?

Explained Variance is the amount of information (variance) retained by each principal component after applying Principal Component Analysis (PCA). It indicates how much of the original dataset's variability is captured by each principal component.

A principal component with a higher explained variance preserves more important information from the original data.

---

## Why is Explained Variance Important?

Explained Variance helps to:

- Measure the importance of each principal component.
- Decide how many principal components should be retained.
- Reduce the number of features while preserving useful information.
- Improve computational efficiency.
- Simplify high-dimensional datasets.

---

## Explained Variance Ratio

The **Explained Variance Ratio** represents the percentage of the total variance explained by each principal component.

### Example

| Principal Component | Explained Variance Ratio |
|---------------------|--------------------------|
| PC1 | 72% |
| PC2 | 20% |
| PC3 | 6% |
| PC4 | 2% |

In this example:

- PC1 captures most of the information.
- PC1 and PC2 together capture **92%** of the total variance.

---

## Cumulative Explained Variance

Cumulative Explained Variance is the total variance explained by multiple principal components combined.

### Example

| Components | Cumulative Variance |
|------------|---------------------|
| PC1 | 72% |
| PC1 + PC2 | 92% |
| PC1 + PC2 + PC3 | 98% |
| PC1 + PC2 + PC3 + PC4 | 100% |

A common practice is to retain enough principal components to explain approximately **90–95%** of the total variance.

---

## Choosing the Number of Principal Components

When selecting the number of principal components:

- Retain components that explain most of the variance.
- Aim for about **90–95%** cumulative explained variance.
- Avoid selecting too many components, as it reduces the benefits of dimensionality reduction.
- Avoid selecting too few components, as important information may be lost.

---

## What is a Scree Plot?

A Scree Plot is a graph that displays the explained variance ratio for each principal component.

It helps identify the point where adding more components contributes only a small increase in explained variance.

The point where the graph starts to flatten is often used to choose the optimal number of principal components.

---

## Python Example

```python
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data

# Apply PCA
pca = PCA()
pca.fit(X)

# Print Explained Variance Ratio
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Scree Plot
plt.plot(
    range(1, len(pca.explained_variance_ratio_) + 1),
    pca.explained_variance_ratio_,
    marker="o"
)

plt.title("Scree Plot")
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")

plt.show()
```

---

## Advantages

- Helps identify important principal components.
- Reduces unnecessary features.
- Improves model efficiency.
- Reduces computational cost.
- Makes data visualization easier.
- Helps avoid overfitting.

---

## Limitations

- Some information may be lost after dimensionality reduction.
- Choosing the optimal number of components requires analysis.
- Explained variance does not always guarantee better prediction performance.
- PCA assumes linear relationships between features.

---

## Real-World Applications

Explained Variance is useful in:

- Image Compression
- Face Recognition
- Medical Diagnosis
- Financial Analysis
- Bioinformatics
- Customer Behavior Analysis
- Data Visualization
- Recommendation Systems
- Text Mining

---

## Best Practices

- Standardize data before applying PCA.
- Use the explained variance ratio to evaluate component importance.
- Retain enough components to explain about **90–95%** of the variance.
- Use a Scree Plot to help determine the optimal number of components.

---

## Key Learnings

Today I learned:

- What Explained Variance is.
- The meaning of the Explained Variance Ratio.
- How Cumulative Explained Variance is calculated.
- How to choose the number of principal components.
- The purpose of a Scree Plot.
- How to implement Explained Variance in Python using Scikit-learn.
- The advantages, limitations, and applications of Explained Variance.

---

## Conclusion

Explained Variance is an essential concept in Principal Component Analysis (PCA). It helps measure how much information each principal component preserves from the original dataset. By using the Explained Variance Ratio, Cumulative Explained Variance, and Scree Plot, we can choose an appropriate number of principal components, reduce dimensionality effectively, and improve the efficiency of machine learning models.