# PCA vs LDA Notes

## Day 11 – PCA vs LDA Introduction

## Introduction

Dimensionality reduction is a machine learning technique used to reduce the number of input features while preserving the most useful information. It helps simplify datasets, reduce computation time, improve visualization, and enhance model performance.

Two of the most widely used dimensionality reduction techniques are **Principal Component Analysis (PCA)** and **Linear Discriminant Analysis (LDA)**. Although both reduce the number of features, they have different objectives and are used in different situations.

This lesson introduces PCA and LDA, explains their differences, and discusses when each technique should be used.

---

# What is PCA?

**Principal Component Analysis (PCA)** is an **unsupervised** dimensionality reduction technique that transforms the original features into a new set of uncorrelated variables called **Principal Components**.

The main objective of PCA is to preserve the maximum variance present in the dataset while reducing the number of features.

### Characteristics

- Unsupervised learning technique.
- Does not require class labels.
- Reduces feature dimensions.
- Preserves maximum variance.
- Creates orthogonal principal components.
- Useful for visualization and preprocessing.

---

# What is LDA?

**Linear Discriminant Analysis (LDA)** is a **supervised** dimensionality reduction technique that transforms the original features into **Linear Discriminants**.

The main objective of LDA is to maximize the separation between different classes while minimizing the variation within the same class.

### Characteristics

- Supervised learning technique.
- Requires labeled data.
- Maximizes class separation.
- Reduces dimensionality.
- Commonly used before classification.
- Produces discriminant components.

---

# Why Compare PCA and LDA?

Although PCA and LDA both reduce dimensionality, they are designed for different purposes.

Comparing them helps us understand:

- When to use PCA.
- When to use LDA.
- Which technique performs better for different datasets.
- How supervised and unsupervised methods differ.
- Which method is suitable for visualization.
- Which method improves classification performance.

Understanding these differences helps in selecting the most appropriate dimensionality reduction technique.

---

# Supervised vs Unsupervised Learning

## Supervised Learning

Supervised learning uses labeled data for training.

Characteristics:

- Requires input data and target labels.
- Learns from known outputs.
- Used for classification and regression.
- Example: Linear Discriminant Analysis (LDA).

Examples:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine
- Linear Discriminant Analysis

---

## Unsupervised Learning

Unsupervised learning works without target labels.

Characteristics:

- Uses only input features.
- Finds hidden patterns.
- Performs clustering or dimensionality reduction.
- Example: Principal Component Analysis (PCA).

Examples:

- PCA
- K-Means Clustering
- Hierarchical Clustering
- DBSCAN

---

# Dimensionality Reduction Overview

Dimensionality reduction is the process of decreasing the number of input features while preserving important information.

## Benefits

- Reduces computational cost.
- Speeds up model training.
- Removes redundant features.
- Reduces noise.
- Improves visualization.
- Helps prevent overfitting.
- Simplifies large datasets.

---

# Feature Extraction Concepts

Feature extraction creates new features from the original dataset.

Instead of selecting existing features, new features are generated that contain most of the useful information.

### PCA Feature Extraction

- Creates Principal Components.
- Preserves maximum variance.
- Ignores class labels.

### LDA Feature Extraction

- Creates Linear Discriminants.
- Maximizes class separation.
- Uses class labels.

---

# Applications of PCA

PCA is widely used in:

- Image Compression
- Face Recognition
- Data Visualization
- Noise Reduction
- Feature Extraction
- Bioinformatics
- Financial Data Analysis
- Pattern Recognition
- Data Preprocessing

---

# Applications of LDA

LDA is widely used in:

- Face Recognition
- Medical Diagnosis
- Customer Classification
- Fraud Detection
- Image Classification
- Speech Recognition
- Credit Risk Analysis
- Document Classification
- Bioinformatics

---

# Advantages of PCA

- Reduces feature dimensions.
- Removes redundant information.
- Preserves maximum variance.
- Works without labeled data.
- Improves computational efficiency.
- Useful for visualization.

---

# Advantages of LDA

- Maximizes class separation.
- Improves classification accuracy.
- Reduces dimensionality.
- Uses class information effectively.
- Suitable for supervised learning.
- Produces discriminative features.

---

# Limitations of PCA

- Does not consider class labels.
- May not improve classification accuracy.
- Principal components can be difficult to interpret.
- Sensitive to feature scaling.

---

# Limitations of LDA

- Requires labeled data.
- Assumes normally distributed data.
- Assumes equal covariance among classes.
- Sensitive to outliers.
- Maximum number of components is limited to (Number of Classes − 1).

---

# PCA vs LDA Summary

| Feature | PCA | LDA |
|----------|-----|-----|
| Learning Type | Unsupervised | Supervised |
| Uses Class Labels | No | Yes |
| Objective | Maximize Variance | Maximize Class Separation |
| Output | Principal Components | Linear Discriminants |
| Best For | Data Compression & Visualization | Classification |
| Requires Labels | No | Yes |

---

# Best Practices

- Use PCA when class labels are unavailable.
- Use LDA for classification tasks with labeled data.
- Standardize features before applying PCA or LDA.
- Choose the appropriate number of components.
- Evaluate the transformed data using suitable metrics.

---

# Key Learnings

Today I learned:

- What Principal Component Analysis (PCA) is.
- What Linear Discriminant Analysis (LDA) is.
- The difference between supervised and unsupervised learning.
- The concept of dimensionality reduction.
- Feature extraction techniques.
- Why PCA and LDA are compared.
- Applications, advantages, and limitations of both techniques.

---

# Conclusion

Principal Component Analysis (PCA) and Linear Discriminant Analysis (LDA) are powerful dimensionality reduction techniques used in machine learning. PCA focuses on preserving the maximum variance in the data without using class labels, making it suitable for unsupervised tasks. LDA, on the other hand, uses class labels to maximize class separation, making it highly effective for supervised classification problems. Understanding the strengths and limitations of both techniques helps in selecting the most appropriate method for different machine learning applications.