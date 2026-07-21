# PCA vs LDA Comparison Notes

## Day 11 – Phase 2: PCA vs LDA Comparison

# Introduction

Principal Component Analysis (PCA) and Linear Discriminant Analysis (LDA) are two widely used dimensionality reduction techniques in machine learning. Although both reduce the number of input features, they have different objectives and are used in different scenarios.

PCA is an **unsupervised** technique that preserves the maximum variance in the data, whereas LDA is a **supervised** technique that maximizes the separation between different classes.

Understanding the differences between PCA and LDA helps in selecting the most suitable technique for a given machine learning problem.

---

# Mathematical Difference

## Principal Component Analysis (PCA)

PCA transforms the original dataset into a new coordinate system by finding directions that capture the maximum variance.

It performs the following operations:

1. Standardize the dataset.
2. Compute the covariance matrix.
3. Calculate eigenvalues and eigenvectors.
4. Sort eigenvalues in descending order.
5. Select the top principal components.
6. Transform the dataset into the new feature space.

PCA focuses only on feature variance and does not use class labels.

---

## Linear Discriminant Analysis (LDA)

LDA transforms the dataset by finding directions that maximize the separation between different classes.

It performs the following operations:

1. Standardize the dataset.
2. Compute the Within-Class Scatter Matrix (SW).
3. Compute the Between-Class Scatter Matrix (SB).
4. Solve the generalized eigenvalue problem.
5. Select the most significant linear discriminants.
6. Transform the dataset into a lower-dimensional space.

LDA uses class labels during the transformation process.

---

# Objective Function

## PCA Objective

The main objective of PCA is to preserve the maximum variance in the dataset.

Characteristics:

- Maximizes information.
- Removes redundant features.
- Creates orthogonal principal components.
- Ignores class labels.

Best suited for:

- Data compression
- Visualization
- Noise reduction
- Feature extraction

---

## LDA Objective

The main objective of LDA is to maximize class separation.

Characteristics:

- Uses class labels.
- Maximizes between-class variance.
- Minimizes within-class variance.
- Improves classification performance.

Best suited for:

- Classification
- Pattern recognition
- Medical diagnosis
- Face recognition

---

# Data Requirements

## PCA

Requires:

- Input features only (X)

Does not require:

- Target labels (y)

Since PCA is unsupervised, it can be applied to both labeled and unlabeled datasets.

---

## LDA

Requires:

- Input features (X)
- Target labels (y)

LDA cannot be applied without class labels because it needs them to calculate class separation.

---

# Variance Maximization

## PCA

PCA preserves the directions with the highest variance.

The first principal component captures the maximum variance.

Each subsequent principal component captures the remaining variance while remaining orthogonal to the previous components.

Higher variance generally indicates more useful information.

---

## LDA

LDA is not concerned with preserving variance.

Instead, it focuses on:

- Increasing the distance between different classes.
- Reducing the spread within each class.

The goal is better discrimination rather than higher variance.

---

# Class Separation

## PCA

PCA does not consider class labels.

Therefore:

- Different classes may overlap.
- Separation between classes is not guaranteed.

---

## LDA

LDA explicitly maximizes class separation.

Advantages:

- Better clustering of classes.
- Reduced overlap.
- Improved classification accuracy.

---

# Output Components

## PCA

Produces:

**Principal Components (PCs)**

Characteristics:

- Ordered by explained variance.
- Orthogonal to each other.
- Number of components can be selected up to the original number of features.

---

## LDA

Produces:

**Linear Discriminants (LDs)**

Characteristics:

- Maximize class separation.
- Number of discriminants is limited to:

Maximum Components = Number of Classes − 1

Example:

- 3 classes → Maximum 2 discriminants
- 4 classes → Maximum 3 discriminants

---

# Performance Comparison

## PCA Performance

Advantages:

- Fast computation.
- Handles large datasets.
- Effective for visualization.
- Removes multicollinearity.

Limitations:

- Ignores class labels.
- May reduce classification accuracy.

---

## LDA Performance

Advantages:

- Better classification accuracy.
- Uses label information.
- Produces highly discriminative features.

Limitations:

- Requires labeled data.
- Sensitive to outliers.
- Assumes normally distributed classes.

---

# Advantages

## PCA Advantages

- Unsupervised learning.
- Preserves maximum variance.
- Reduces computational complexity.
- Removes redundant features.
- Useful for visualization.
- Easy to implement.

---

## LDA Advantages

- Supervised learning.
- Improves classification performance.
- Maximizes class separation.
- Produces meaningful features.
- Effective for prediction tasks.

---

# Limitations

## PCA Limitations

- Does not use class labels.
- Components are difficult to interpret.
- Sensitive to feature scaling.
- May lose useful class information.

---

## LDA Limitations

- Requires labeled data.
- Assumes normal distribution.
- Assumes equal covariance among classes.
- Sensitive to outliers.
- Maximum components are limited by the number of classes.

---

# Workflow Comparison

## PCA Workflow

1. Load dataset.
2. Standardize features.
3. Compute covariance matrix.
4. Calculate eigenvalues and eigenvectors.
5. Select principal components.
6. Transform the data.
7. Train the model (optional).

---

## LDA Workflow

1. Load dataset.
2. Standardize features.
3. Compute Within-Class Scatter Matrix.
4. Compute Between-Class Scatter Matrix.
5. Calculate eigenvalues and eigenvectors.
6. Select linear discriminants.
7. Transform the data.
8. Train the classifier.

---

# Real-World Comparison

| Problem | PCA | LDA |
|----------|-----|-----|
| Image Compression | ✅ | ❌ |
| Data Visualization | ✅ | ✅ |
| Noise Reduction | ✅ | ❌ |
| Customer Segmentation | ✅ | ❌ |
| Face Recognition | ❌ | ✅ |
| Medical Diagnosis | ❌ | ✅ |
| Fraud Detection | ❌ | ✅ |
| Document Classification | ❌ | ✅ |
| Image Classification | ❌ | ✅ |

---

# Complete Comparison Table

| Feature | PCA | LDA |
|---------|-----|-----|
| Full Form | Principal Component Analysis | Linear Discriminant Analysis |
| Learning Type | Unsupervised | Supervised |
| Uses Labels | No | Yes |
| Objective | Maximize Variance | Maximize Class Separation |
| Input Data | Features Only | Features + Labels |
| Output | Principal Components | Linear Discriminants |
| Feature Extraction | Yes | Yes |
| Classification | No | Yes |
| Best Use | Visualization & Compression | Classification |
| Maximum Components | Number of Features | Number of Classes − 1 |

---

# Best Practices

- Standardize data before applying PCA or LDA.
- Use PCA when labels are unavailable.
- Use LDA when the goal is classification.
- Evaluate model performance after dimensionality reduction.
- Choose the appropriate number of components based on the dataset.
- Visualize transformed data to understand the results.

---

# Key Learnings

Today I learned:

- The mathematical differences between PCA and LDA.
- The objective of each technique.
- Data requirements for PCA and LDA.
- How PCA preserves variance.
- How LDA maximizes class separation.
- The differences in output components.
- Performance comparison of PCA and LDA.
- Advantages and limitations of both techniques.
- Real-world applications and use cases.

---

# Conclusion

Principal Component Analysis (PCA) and Linear Discriminant Analysis (LDA) are powerful dimensionality reduction techniques with different objectives. PCA is mainly used to preserve the maximum variance in the data without considering class labels, making it suitable for visualization, compression, and preprocessing. LDA, on the other hand, uses class labels to maximize class separation, making it highly effective for supervised classification tasks. Selecting the appropriate technique depends on the availability of labeled data and the specific goals of the machine learning problem.