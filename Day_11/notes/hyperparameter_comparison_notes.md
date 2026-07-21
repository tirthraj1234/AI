# Hyperparameter Comparison Notes

## Day 11 – Phase 6: PCA vs LDA Hyperparameter Comparison

# Introduction

Hyperparameters are configuration settings that are defined before training a machine learning model. They control how an algorithm learns from data and directly influence model performance, computational efficiency, and output quality.

In this phase, the important hyperparameters of **Principal Component Analysis (PCA)** and **Linear Discriminant Analysis (LDA)** are studied and compared. Understanding these hyperparameters helps in selecting the appropriate settings for different machine learning problems.

---

# Objective

The objectives of this comparison are:

- Understand the concept of hyperparameters.
- Learn the important hyperparameters of PCA.
- Learn the important hyperparameters of LDA.
- Compare the hyperparameters of both techniques.
- Understand how hyperparameters affect model performance.
- Apply best practices while selecting hyperparameters.

---

# What are Hyperparameters?

Hyperparameters are values that are set before the training process begins. Unlike model parameters, which are learned during training, hyperparameters are chosen by the user and determine how the algorithm operates.

Examples of hyperparameters include:

- Number of components (`n_components`)
- Solver type
- Tolerance (`tol`)
- Shrinkage
- Whitening
- Random state

Choosing suitable hyperparameters improves model accuracy, stability, and efficiency.

---

# PCA Hyperparameters

## 1. n_components

The `n_components` parameter specifies the number of principal components to retain after dimensionality reduction.

Example:

```python
PCA(n_components=2)
```

Purpose:

- Reduces the number of features.
- Preserves the maximum variance.
- Controls the dimensionality of the transformed dataset.

---

## 2. svd_solver

The `svd_solver` parameter specifies the algorithm used to compute the Singular Value Decomposition (SVD).

Common options:

- auto
- full
- arpack
- randomized

Purpose:

- Controls computation speed.
- Improves performance on different dataset sizes.
- Automatically selects the best solver when using `auto`.

---

## 3. whiten

The `whiten` parameter determines whether the transformed components are scaled to have unit variance.

Values:

- True
- False

Purpose:

- Removes differences in component variance.
- Helps improve the performance of some machine learning models.

---

## 4. random_state

The `random_state` parameter ensures reproducible results when randomized algorithms are used.

Example:

```python
PCA(random_state=42)
```

Purpose:

- Produces consistent outputs.
- Useful for experiments and model comparison.

---

# LDA Hyperparameters

## 1. n_components

The `n_components` parameter specifies the number of linear discriminants to retain.

Example:

```python
LinearDiscriminantAnalysis(n_components=2)
```

Purpose:

- Reduces dimensionality.
- Maximizes class separation.

Maximum value:

Number of Classes − 1

---

## 2. solver

The `solver` parameter specifies the algorithm used to solve the LDA optimization problem.

Common options:

- svd
- lsqr
- eigen

Purpose:

- Determines how the model is trained.
- Affects computation speed and numerical stability.

---

## 3. shrinkage

The `shrinkage` parameter regularizes the covariance matrix and helps improve model stability.

Available values:

- None
- auto
- Numeric value

Note:

Shrinkage is supported only with the `lsqr` and `eigen` solvers.

Purpose:

- Reduces overfitting.
- Improves performance on noisy datasets.
- Handles high-dimensional data effectively.

---

## 4. tol

The `tol` parameter defines the convergence tolerance for the SVD solver.

Example:

```python
LinearDiscriminantAnalysis(tol=1e-4)
```

Purpose:

- Controls convergence.
- Stops training when changes become very small.
- Improves computational efficiency.

---

# Hyperparameter Comparison

| Hyperparameter | PCA | LDA |
|---------------|-----|-----|
| n_components | Yes | Yes |
| Solver | SVD Solver | LDA Solver |
| Whiten | Yes | No |
| Shrinkage | No | Yes |
| Tolerance (tol) | No | Yes |
| Random State | Yes | No |

---

# Effects of Hyperparameters

## PCA

- Increasing `n_components` preserves more information.
- Fewer components reduce computational cost.
- `whiten=True` produces components with equal variance.
- Different SVD solvers affect computation speed.
- `random_state` ensures reproducible results.

---

## LDA

- Increasing `n_components` increases the number of discriminant directions.
- The solver affects model stability and speed.
- `shrinkage` improves generalization for noisy datasets.
- Lower `tol` values may require more iterations for convergence.

---

# Best Practices

- Standardize features before applying PCA or LDA.
- Select `n_components` based on the dataset and problem requirements.
- Use `auto` solver in PCA unless a specific solver is needed.
- Use `shrinkage` with `lsqr` or `eigen` solvers when working with noisy data.
- Use `random_state` to obtain reproducible results.
- Evaluate different hyperparameter values using validation techniques.

---

# Real-World Applications

## PCA

- Image Compression
- Data Visualization
- Noise Reduction
- Feature Extraction
- Recommendation Systems
- Financial Data Analysis

---

## LDA

- Face Recognition
- Medical Diagnosis
- Fraud Detection
- Spam Detection
- Customer Classification
- Speech Recognition

---

# Advantages

## PCA

- Reduces dimensionality.
- Preserves maximum variance.
- Improves computational efficiency.
- Handles high-dimensional datasets.
- Easy to implement.

---

## LDA

- Maximizes class separation.
- Improves classification accuracy.
- Uses label information.
- Produces discriminative features.
- Effective for supervised learning tasks.

---

# Key Learnings

Today I learned:

- The meaning of hyperparameters.
- Important PCA hyperparameters and their functions.
- Important LDA hyperparameters and their functions.
- Differences between PCA and LDA hyperparameters.
- How hyperparameters influence model performance.
- Best practices for selecting hyperparameters.

---

# Interview Questions

1. What are hyperparameters in machine learning?
2. What is the purpose of `n_components`?
3. What does the `whiten` parameter do in PCA?
4. Which LDA solvers support `shrinkage`?
5. Why is `random_state` useful?
6. How does `tol` affect model training?
7. Why should hyperparameters be tuned?

---

# Conclusion

Hyperparameters play a vital role in controlling the behavior and performance of machine learning algorithms. PCA and LDA have different hyperparameters because they are designed for different objectives. PCA focuses on preserving variance and provides options such as `n_components`, `svd_solver`, `whiten`, and `random_state`. LDA focuses on maximizing class separation and includes hyperparameters such as `n_components`, `solver`, `shrinkage`, and `tol`. Selecting appropriate hyperparameters helps improve model performance, computational efficiency, and the overall effectiveness of dimensionality reduction techniques.