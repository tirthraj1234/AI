# Iris Flower Classification using Linear Discriminant Analysis (LDA)

## Day 10 – Mini Project

# Project Introduction

This project demonstrates the implementation of **Linear Discriminant Analysis (LDA)** for dimensionality reduction and **Logistic Regression** for classification using the Iris dataset. The objective is to reduce the original features while preserving maximum class separation and then classify the flower species accurately.

The project includes data preprocessing, feature scaling, dimensionality reduction, model training, evaluation, and visualization.

---

# Project Objective

The objectives of this project are:

- Understand the practical implementation of LDA.
- Reduce the dimensionality of the dataset.
- Improve classification performance.
- Train a Logistic Regression classifier.
- Evaluate the trained model.
- Visualize the transformed dataset.

---

# Dataset Description

The project uses the **Iris Dataset**, one of the most popular datasets in machine learning.

Dataset Information:

- Dataset Name: Iris
- Total Samples: 150
- Features: 4
- Target Classes: 3

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

# Technologies Used

Programming Language:

- Python

Libraries:

- NumPy
- Matplotlib
- Scikit-learn

Scikit-learn Modules:

- load_iris
- train_test_split
- StandardScaler
- LinearDiscriminantAnalysis
- LogisticRegression
- accuracy_score
- confusion_matrix
- classification_report

---

# Project Workflow

The project follows these steps:

1. Import the required libraries.
2. Load the Iris dataset.
3. Split the dataset into training and testing sets.
4. Standardize the input features.
5. Apply Linear Discriminant Analysis (LDA).
6. Reduce the dataset to two linear discriminants.
7. Train the Logistic Regression classifier.
8. Predict the flower species.
9. Evaluate the model.
10. Visualize the transformed data.

---

# Data Preprocessing

Before applying LDA, the dataset is preprocessed.

The preprocessing steps include:

- Loading the dataset.
- Separating features and target labels.
- Splitting the dataset into training and testing sets.
- Standardizing the feature values.

Proper preprocessing improves the model's accuracy and stability.

---

# Feature Scaling

Feature scaling is performed using **StandardScaler**.

Purpose:

- Normalize feature values.
- Remove differences in feature scales.
- Improve the performance of LDA.
- Ensure equal importance for all features.

---

# Applying Linear Discriminant Analysis

Linear Discriminant Analysis is applied to transform the original four features into two linear discriminants.

Benefits:

- Reduces dimensionality.
- Preserves important class information.
- Maximizes class separation.
- Simplifies visualization.

---

# Logistic Regression Classification

After dimensionality reduction, a Logistic Regression classifier is trained using the transformed dataset.

The classifier learns the relationship between the LDA features and the target classes and predicts the flower species for new samples.

---

# Model Prediction

The trained model predicts the flower species for the testing dataset.

The predicted values are compared with the actual values to measure model performance.

---

# Model Evaluation

The model is evaluated using several performance metrics.

## Accuracy Score

Measures the percentage of correctly classified samples.

## Confusion Matrix

Shows the number of:

- True Positives
- True Negatives
- False Positives
- False Negatives

It helps identify prediction errors.

## Classification Report

Provides:

- Precision
- Recall
- F1-Score
- Support

These metrics provide a detailed summary of the classifier's performance.

---

# Data Visualization

The transformed dataset is visualized using a scatter plot.

The visualization shows:

- Linear Discriminant 1 (LD1)
- Linear Discriminant 2 (LD2)
- Different colors for each flower species

This helps understand how effectively LDA separates the classes.

---

# Expected Output

The project generates:

- Accuracy Score
- Confusion Matrix
- Classification Report
- LDA Scatter Plot

These outputs help evaluate the performance of the classification model.

---

# Advantages

- Reduces the number of features.
- Improves classification performance.
- Reduces computational complexity.
- Makes visualization easier.
- Easy to implement using Scikit-learn.
- Suitable for supervised classification problems.

---

# Limitations

- Requires labeled data.
- Assumes normally distributed data.
- Assumes equal covariance among classes.
- Sensitive to outliers.
- Maximum number of components is limited to (Number of Classes − 1).

---

# Real-World Applications

This project demonstrates techniques used in:

- Face Recognition
- Medical Diagnosis
- Customer Segmentation
- Fraud Detection
- Image Classification
- Speech Recognition
- Bioinformatics
- Credit Risk Analysis
- Document Classification

---

# Best Practices

- Standardize features before applying LDA.
- Handle missing values before training.
- Remove outliers if necessary.
- Use train-test split for unbiased evaluation.
- Evaluate the model using multiple performance metrics.
- Visualize the transformed data for better interpretation.

---

# Project Outcome

After completing this project, I successfully:

- Implemented Linear Discriminant Analysis.
- Reduced the dimensionality of the Iris dataset.
- Trained a Logistic Regression classifier.
- Evaluated the model using multiple metrics.
- Visualized the transformed dataset.
- Improved my understanding of supervised dimensionality reduction and classification.

---

# Key Learnings

From this project, I learned:

- Practical implementation of Linear Discriminant Analysis.
- Data preprocessing techniques.
- Importance of feature scaling.
- Dimensionality reduction using LDA.
- Logistic Regression classification.
- Model evaluation techniques.
- Data visualization using Matplotlib.
- Real-world applications of LDA.

---

# Conclusion

This project demonstrates the complete implementation of **Linear Discriminant Analysis (LDA)** for supervised dimensionality reduction and classification. By combining LDA with Logistic Regression, the model effectively reduces feature dimensions while preserving class-discriminative information. The evaluation metrics and visualization confirm the effectiveness of the model, making this project a strong example of applying dimensionality reduction techniques in real-world machine learning tasks.