# LDA Hyperparameters Notes

## Day 10 – LDA Hyperparameters

## Introduction

Hyperparameters are configuration settings that control how a Linear Discriminant Analysis (LDA) model works before training begins. Choosing appropriate hyperparameters helps improve model performance, computational efficiency, and dimensionality reduction.

---

## What are Hyperparameters?

Hyperparameters are values that are set before training the model. They are not learned from the data but are chosen by the developer to control the learning process.

In LDA, the most commonly used hyperparameters are:

- n_components
- solver
- shrinkage
- store_covariance
- priors
- tol

---

## 1. n_components

The `n_components` parameter specifies the number of linear discriminants (new features) to keep after dimensionality reduction.

### Syntax

```python
lda = LinearDiscriminantAnalysis(n_components=2)
```

### Key Points

- Reduces the number of features.
- Must be less than or equal to **(Number of Classes − 1)**.
- Commonly used values are 1 or 2 for visualization.
- Helps simplify high-dimensional datasets.

---

## 2. solver

The `solver` parameter specifies the algorithm used to compute the LDA transformation.

### Available Solvers

- `svd` (Default)
- `lsqr`
- `eigen`

### Example

```python
lda = LinearDiscriminantAnalysis(solver="svd")
```

### Solver Comparison

| Solver | Description |
|---------|-------------|
| svd | Fast, efficient, and suitable for most datasets. |
| lsqr | Supports shrinkage and large datasets. |
| eigen | Supports shrinkage and covariance estimation. |

---

## 3. shrinkage

The `shrinkage` parameter improves covariance estimation, especially for high-dimensional or noisy datasets.

### Options

- None (Default)
- "auto"
- Decimal values between 0 and 1

### Example

```python
lda = LinearDiscriminantAnalysis(
    solver="lsqr",
    shrinkage="auto"
)
```

### Note

Shrinkage is supported only with:

- lsqr
- eigen

---

## 4. store_covariance

The `store_covariance` parameter determines whether the covariance matrix should be stored after training.

### Example

```python
lda = LinearDiscriminantAnalysis(store_covariance=True)
```

### Benefits

- Useful for analysis.
- Helps inspect covariance values.
- Mainly used for research and debugging.

---

## 5. priors

The `priors` parameter allows you to specify prior probabilities for each class.

### Example

```python
lda = LinearDiscriminantAnalysis(
    priors=[0.5, 0.3, 0.2]
)
```

If not specified, LDA automatically calculates class probabilities from the training data.

---

## 6. tol

The `tol` parameter defines the convergence tolerance for the SVD solver.

### Example

```python
lda = LinearDiscriminantAnalysis(
    tol=1e-4
)
```

Smaller values provide higher precision but may increase computation time.

---

## Python Example

```python
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create LDA model
lda = LinearDiscriminantAnalysis(
    n_components=2,
    solver="svd"
)

# Fit and transform
X_lda = lda.fit_transform(X, y)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_lda.shape)
```

---

## Best Practices

- Standardize data before applying LDA (recommended).
- Choose `n_components` carefully based on the number of classes.
- Use `svd` for most practical applications.
- Use `lsqr` or `eigen` when shrinkage is required.
- Handle missing values before training.
- Evaluate model performance after dimensionality reduction.

---

## Advantages

- Improves classification performance.
- Reduces the number of features.
- Faster model training.
- Supports dimensionality reduction and classification.
- Easy to implement using Scikit-learn.

---

## Limitations

- Assumes normally distributed data.
- Assumes equal covariance among classes.
- Sensitive to outliers.
- Maximum components are limited to (Number of Classes − 1).

---

## Real-World Applications

LDA hyperparameters are useful in:

- Face Recognition
- Medical Diagnosis
- Customer Classification
- Fraud Detection
- Speech Recognition
- Bioinformatics
- Credit Risk Analysis
- Image Classification
- Document Classification

---

## Key Learnings

Today I learned:

- What hyperparameters are in LDA.
- The purpose of `n_components`.
- Different LDA solvers.
- How shrinkage improves covariance estimation.
- The use of `store_covariance`.
- The purpose of `priors` and `tol`.
- Best practices for configuring LDA.

---

## Conclusion

LDA hyperparameters control how the model performs dimensionality reduction and classification. Selecting appropriate values for parameters such as `n_components`, `solver`, and `shrinkage` helps improve model performance and computational efficiency. Understanding these hyperparameters is essential for building effective machine learning models using Linear Discriminant Analysis.