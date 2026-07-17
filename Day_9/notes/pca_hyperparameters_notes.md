# PCA Hyperparameters Notes

## Day 9 – PCA Hyperparameters

## What are PCA Hyperparameters?

PCA hyperparameters are configuration settings that control how the Principal Component Analysis (PCA) algorithm works. These values are selected before training and affect the dimensionality reduction process, computational efficiency, and the quality of the transformed data.

Hyperparameters are not learned from the dataset; they are specified by the user.

---

# Why are PCA Hyperparameters Important?

PCA hyperparameters help to:

- Control the number of principal components.
- Improve computational efficiency.
- Preserve important information from the dataset.
- Reduce training time.
- Produce consistent and reliable results.

---

# 1. n_components

The `n_components` parameter specifies the number of principal components to keep after dimensionality reduction.

### Common Values

- `n_components=2` → Keep 2 principal components.
- `n_components=3` → Keep 3 principal components.
- `n_components=0.95` → Keep enough components to preserve approximately 95% of the total variance.

### Example

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
```

### Advantages

- Reduces the number of features.
- Preserves the most important information.
- Improves computational efficiency.

---

# 2. svd_solver

The `svd_solver` parameter specifies the algorithm used to compute the principal components.

### Common Options

- `"auto"` → Automatically selects the appropriate solver.
- `"full"` → Uses Full Singular Value Decomposition.
- `"randomized"` → Faster for large datasets.
- `"arpack"` → Used for certain sparse datasets.

### Example

```python
pca = PCA(
    n_components=2,
    svd_solver="auto"
)
```

### Advantages

- Optimizes computation.
- Improves performance for different dataset sizes.
- Provides flexibility for different applications.

---

# 3. whiten

The `whiten` parameter determines whether the transformed principal components are scaled to have unit variance.

### Values

- `False` (default)
- `True`

### Example

```python
pca = PCA(
    n_components=2,
    whiten=True
)
```

### Advantages

- Produces standardized principal components.
- Can improve the performance of some machine learning algorithms.

### Limitation

- Some variance information may be lost.

---

# 4. random_state

The `random_state` parameter controls randomness when using randomized PCA methods.

It ensures that the same results are produced every time the program is executed.

### Example

```python
pca = PCA(
    n_components=2,
    svd_solver="randomized",
    random_state=42
)
```

### Advantages

- Produces reproducible results.
- Useful for experiments and debugging.

---

# Complete Python Example

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X = iris.data

# Configure PCA
pca = PCA(
    n_components=2,
    svd_solver="auto",
    whiten=False
)

# Apply PCA
X_pca = pca.fit_transform(X)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_pca.shape)
```

---

# Best Practices

- Standardize data before applying PCA.
- Choose `n_components` based on the explained variance ratio.
- Use `"auto"` for `svd_solver` unless a specific solver is needed.
- Enable `whiten=True` only when required by the downstream model.
- Use `random_state` for reproducible experiments.

---

# Advantages

- Reduces dimensionality efficiently.
- Improves model performance.
- Reduces computational cost.
- Supports reproducible experiments.
- Flexible configuration for different datasets.

---

# Limitations

- Incorrect hyperparameter values can reduce performance.
- Whitening may remove some useful variance.
- Choosing the optimal number of components requires experimentation.
- PCA assumes linear relationships between features.

---

# Real-World Applications

PCA hyperparameters are important in:

- Image Compression
- Face Recognition
- Medical Data Analysis
- Financial Forecasting
- Bioinformatics
- Customer Segmentation
- Data Visualization
- Recommendation Systems
- Text Mining

---

# Key Learnings

Today I learned:

- What PCA hyperparameters are.
- The purpose of `n_components`.
- How `svd_solver` affects PCA computation.
- Why `whiten` is used.
- The role of `random_state`.
- Best practices for configuring PCA.
- How to implement PCA hyperparameters using Scikit-learn.

---

# Conclusion

PCA hyperparameters play an important role in controlling how Principal Component Analysis is performed. Parameters such as `n_components`, `svd_solver`, `whiten`, and `random_state` help optimize dimensionality reduction while preserving important information. Selecting appropriate hyperparameter values leads to efficient, reliable, and accurate machine learning models.