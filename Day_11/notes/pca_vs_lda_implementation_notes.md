# PCA vs LDA Implementation Notes

## Day 11 – Phase 3: PCA vs LDA Implementation

# Introduction

This implementation demonstrates the practical use of **Principal Component Analysis (PCA)** and **Linear Discriminant Analysis (LDA)** using the Iris dataset. Both techniques are used for dimensionality reduction, but they work differently and serve different purposes.

PCA reduces dimensions by preserving the maximum variance in the dataset without using class labels, whereas LDA reduces dimensions by maximizing the separation between different classes using class labels.

The objective of this implementation is to compare both techniques on the same dataset and understand their outputs.

---

# Objective

The objectives of this implementation are:

- Load the Iris dataset.
- Standardize the input features.
- Apply Principal Component Analysis (PCA).
- Apply Linear Discriminant Analysis (LDA).
- Compare the transformed datasets.
- Understand the difference between Principal Components and Linear Discriminants.

---

# Dataset Description

The Iris dataset is one of the most popular datasets used for machine learning.

Dataset Information:

- Dataset Name: Iris
- Total Samples: 150
- Number of Features: 4
- Number of Classes: 3

Input Features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Target Classes:

- Setosa
- Versicolor
- Virginica

---

# Libraries Used

The following Python libraries are used in this implementation:

- NumPy
- Scikit-learn

Scikit-learn Modules:

- load_iris
- StandardScaler
- PCA
- LinearDiscriminantAnalysis

---

# Feature Scaling

Before applying PCA and LDA, feature scaling is performed using **StandardScaler**.

Feature scaling converts all features to a common scale with:

- Mean = 0
- Standard Deviation = 1

### Why Feature Scaling?

- Removes differences in feature scales.
- Improves dimensionality reduction.
- Prevents larger-valued features from dominating the analysis.
- Produces more reliable results.

---

# PCA Implementation

Principal Component Analysis is applied after feature scaling.

Implementation Steps:

1. Load the dataset.
2. Standardize the features.
3. Create the PCA object.
4. Select the number of principal components.
5. Transform the dataset.

Example:

```python
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
```

The transformed dataset contains two principal components that preserve the maximum variance.

---

# LDA Implementation

Linear Discriminant Analysis is applied after feature scaling.

Implementation Steps:

1. Load the dataset.
2. Standardize the features.
3. Create the LDA object.
4. Select the number of linear discriminants.
5. Fit the model using both features and target labels.
6. Transform the dataset.

Example:

```python
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)
```

The transformed dataset contains two linear discriminants that maximize class separation.

---

# Comparison of Results

After applying both techniques:

## PCA

- Produces Principal Components.
- Preserves maximum variance.
- Does not use target labels.
- Suitable for visualization and preprocessing.

## LDA

- Produces Linear Discriminants.
- Maximizes class separation.
- Uses target labels.
- Suitable for classification tasks.

Both techniques reduce the dataset from four features to two components, but their objectives and outputs are different.

---

# Output

The program displays:

- Original dataset shape.
- PCA transformed dataset shape.
- LDA transformed dataset shape.
- First few PCA components.
- First few LDA components.

Example Output:

```
Original Dataset Shape : (150, 4)

PCA Shape : (150, 2)

LDA Shape : (150, 2)
```

---

# Advantages

## PCA

- Reduces dimensionality.
- Preserves maximum variance.
- Removes redundant features.
- Improves computational efficiency.
- Useful for visualization.

## LDA

- Improves class separation.
- Enhances classification performance.
- Uses class labels effectively.
- Produces discriminative features.
- Suitable for supervised learning.

---

# Real-World Applications

## PCA Applications

- Image Compression
- Data Visualization
- Noise Reduction
- Feature Extraction
- Recommendation Systems
- Financial Data Analysis

## LDA Applications

- Face Recognition
- Medical Diagnosis
- Spam Detection
- Customer Classification
- Fraud Detection
- Speech Recognition

---

# Best Practices

- Always standardize the dataset before applying PCA or LDA.
- Choose the appropriate number of components based on the problem.
- Use PCA when labels are unavailable.
- Use LDA for supervised classification tasks.
- Compare transformed data visually whenever possible.
- Evaluate model performance after dimensionality reduction.

---

# Key Learnings

Today I learned:

- How to implement PCA using Scikit-learn.
- How to implement LDA using Scikit-learn.
- The importance of feature scaling.
- The difference between Principal Components and Linear Discriminants.
- How PCA and LDA transform the same dataset differently.
- Practical applications of both dimensionality reduction techniques.

---

# Conclusion

This implementation demonstrated the practical use of PCA and LDA on the Iris dataset. Both techniques successfully reduced the number of features from four to two, but each achieved this using a different objective. PCA preserved the maximum variance without considering class labels, while LDA maximized the separation between different classes using labeled data. This comparison provides a clear understanding of when each technique should be used in machine learning projects.