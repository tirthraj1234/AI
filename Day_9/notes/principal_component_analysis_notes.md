# Principal Component Analysis (PCA) Notes

## Day 9 – Principal Component Analysis (PCA)

## What is PCA?

Principal Component Analysis (PCA) is a **Feature Extraction** technique used for **Dimensionality Reduction**. It transforms a dataset with many features into a smaller set of new features called **Principal Components** while preserving as much important information (variance) as possible.

PCA helps simplify complex datasets, reduce computational cost, improve model performance, and make data easier to visualize.

---

# Why is PCA Used?

PCA is used to:

- Reduce the number of features.
- Remove redundant and correlated features.
- Improve computational efficiency.
- Reduce overfitting.
- Simplify high-dimensional datasets.
- Visualize data in 2D or 3D.
- Improve machine learning model performance.

---

# What are Principal Components?

Principal Components are new features created by combining the original features.

Characteristics of Principal Components:

- They are uncorrelated with each other.
- The first principal component captures the maximum variance.
- The second principal component captures the next highest variance.
- Each component is orthogonal (independent) to the others.

---

# How PCA Works

PCA generally follows these steps:

1. Standardize the dataset.
2. Calculate the covariance matrix.
3. Compute eigenvalues and eigenvectors.
4. Sort the eigenvalues in descending order.
5. Select the top principal components.
6. Transform the original dataset into the new feature space.

---

# Covariance Matrix

The covariance matrix measures how two features vary together.

### Interpretation

- Positive covariance → Both features increase or decrease together.
- Negative covariance → One feature increases while the other decreases.
- Zero covariance → No relationship between the features.

The covariance matrix helps PCA identify the directions with the highest variance.

---

# Eigenvalues

Eigenvalues measure the amount of variance explained by each principal component.

Characteristics:

- Larger eigenvalues indicate more important principal components.
- Components with higher eigenvalues retain more information.
- Used to decide how many principal components to keep.

---

# Eigenvectors

Eigenvectors define the direction of the principal components.

Characteristics:

- Represent the direction of maximum variance.
- Determine how original features are combined.
- Each principal component has its own eigenvector.

---

# Standardization Before PCA

PCA is sensitive to the scale of the data. Therefore, features should usually be standardized before applying PCA.

Example:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

# Python Example

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X = iris.data

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_pca.shape)
```

---

# Advantages of PCA

- Reduces the number of features.
- Removes correlated features.
- Improves computational efficiency.
- Reduces storage requirements.
- Helps reduce overfitting.
- Makes data visualization easier.
- Improves model training speed.

---

# Limitations of PCA

- Principal components are difficult to interpret.
- Some information is lost during dimensionality reduction.
- PCA assumes linear relationships between features.
- Sensitive to feature scaling.
- May not perform well for highly non-linear data.

---

# Real-World Applications

PCA is widely used in:

- Image Compression
- Face Recognition
- Medical Data Analysis
- Bioinformatics
- Financial Data Analysis
- Recommendation Systems
- Text Mining
- Data Visualization
- Customer Behavior Analysis

---

# Key Learnings

Today I learned:

- What Principal Component Analysis (PCA) is.
- Why PCA is used in Machine Learning.
- The concept of Principal Components.
- How PCA works step by step.
- The role of the covariance matrix.
- The importance of eigenvalues and eigenvectors.
- Why data standardization is important before PCA.
- How to implement PCA using Scikit-learn.

---

# Conclusion

Principal Component Analysis (PCA) is one of the most widely used dimensionality reduction techniques in Machine Learning. It transforms high-dimensional data into a smaller set of principal components while preserving most of the important information. PCA improves model efficiency, reduces computation time, simplifies visualization, and is widely used in applications such as image compression, face recognition, and data analysis.