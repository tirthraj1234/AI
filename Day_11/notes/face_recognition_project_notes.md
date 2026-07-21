# Face Recognition Project Notes

## Day 11 – Phase 7: Face Recognition using PCA

# Introduction

Face recognition is a biometric technology that identifies or verifies a person based on facial features. It is widely used in modern security systems, smartphones, surveillance, attendance systems, and identity verification. Machine learning techniques such as Principal Component Analysis (PCA) and Linear Discriminant Analysis (LDA) help reduce the dimensionality of facial image data while preserving important information.

This project demonstrates a simple face recognition system using the Olivetti Faces dataset, PCA for feature extraction, and Logistic Regression for classification.

---

# Project Objective

The main objectives of this project are:

- Load a face image dataset.
- Preprocess and standardize the images.
- Reduce dimensionality using PCA.
- Train a classification model.
- Predict the identity of unseen faces.
- Evaluate model performance using standard metrics.

---

# Dataset Description

Dataset Name:

- Olivetti Faces Dataset

Dataset Information:

- Total Images: 400
- Number of People: 40
- Images per Person: 10
- Image Size: 64 × 64 pixels
- Total Features per Image: 4096

Each image is converted into a one-dimensional feature vector before applying machine learning algorithms.

---

# Libraries Used

- NumPy
- Scikit-learn

Modules Used:

- fetch_olivetti_faces
- train_test_split
- StandardScaler
- PCA
- LogisticRegression
- accuracy_score
- confusion_matrix
- classification_report

---

# Project Workflow

1. Load the face dataset.
2. Split the dataset into training and testing sets.
3. Standardize the feature values.
4. Apply PCA to reduce dimensionality.
5. Train a Logistic Regression classifier.
6. Predict the test data.
7. Evaluate model performance.

---

# Data Preprocessing

Before training the model:

- Images are converted into numerical feature vectors.
- Feature scaling is performed using StandardScaler.
- Data is divided into training and testing datasets.

This improves the performance of PCA and the classifier.

---

# PCA in Face Recognition

Principal Component Analysis is used to:

- Reduce image dimensions.
- Preserve maximum variance.
- Remove redundant information.
- Reduce computational complexity.
- Speed up model training.

The transformed features are known as **Principal Components**.

---

# LDA in Face Recognition

Linear Discriminant Analysis can also be used after PCA or directly on labeled data.

Advantages:

- Maximizes separation between different people.
- Produces highly discriminative features.
- Improves recognition accuracy.
- Suitable for supervised learning.

In many face recognition systems, PCA is used for dimensionality reduction, while LDA is applied to improve class separation.

---

# Classification Model

Model Used:

- Logistic Regression

The classifier learns patterns from the reduced feature set produced by PCA and predicts the identity of unknown face images.

---

# Performance Evaluation

The model is evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

These metrics measure how accurately the system recognizes different faces.

---

# Advantages

- Reduces image dimensionality.
- Faster model training.
- Lower memory usage.
- Improved computational efficiency.
- Good recognition performance.
- Easy to implement using Scikit-learn.

---

# Limitations

- PCA may lose some facial information.
- Lighting and facial expressions can affect accuracy.
- Occlusions (glasses, masks, etc.) may reduce performance.
- Requires good quality training images.
- Logistic Regression may not achieve the highest possible accuracy for complex face recognition tasks.

---

# Real-World Applications

- Smartphone Face Unlock
- Attendance Management Systems
- Airport Security
- Banking Authentication
- CCTV Surveillance
- Criminal Identification
- Access Control Systems

---

# Best Practices

- Standardize data before applying PCA.
- Select an appropriate number of principal components.
- Use high-quality face images.
- Balance the training dataset.
- Evaluate the model using multiple performance metrics.
- Experiment with different classifiers for better accuracy.

---

# Key Learnings

Today I learned:

- How face recognition systems work.
- How PCA reduces image dimensions.
- How LDA improves class separation.
- How to train a classifier using reduced features.
- How to evaluate a face recognition model.
- Real-world applications of PCA and LDA in computer vision.

---

# Interview Questions

1. Why is PCA used in face recognition?
2. What is the purpose of feature scaling?
3. Why is Logistic Regression suitable for this project?
4. What are Principal Components?
5. How does LDA improve recognition accuracy?
6. What evaluation metrics are used in face recognition?
7. What are the limitations of PCA?

---

# Conclusion

This project demonstrated a simple face recognition system using the Olivetti Faces dataset, Principal Component Analysis (PCA), and Logistic Regression. PCA successfully reduced the dimensionality of the facial images while preserving useful information, making the classification process more efficient. The project also highlighted the role of LDA in improving class separation for supervised learning tasks. This practical implementation provides a strong foundation for understanding real-world face recognition systems and dimensionality reduction techniques in machine learning.