# Classification Metrics Notes

## Day 13 – Phase 3: Classification Evaluation Metrics

# Introduction

Classification Evaluation Metrics are used to measure the performance of classification machine learning models. These metrics compare the predicted class labels with the actual class labels to determine how accurately the model classifies data.

Different metrics provide different insights into model performance. Depending on the problem, one metric may be more important than another. For example, in medical diagnosis, Recall is often more important than Accuracy because missing a disease can have serious consequences.

---

# Objective of Classification Evaluation Metrics

The objectives of classification evaluation metrics are:

- Measure classification performance.
- Compare different classification models.
- Identify prediction errors.
- Improve model accuracy.
- Evaluate model reliability.
- Select the best classification model.

---

# What are Classification Evaluation Metrics?

Classification Evaluation Metrics are statistical measures used to evaluate how well a classification model predicts class labels.

These metrics compare predicted labels with actual labels and help determine whether the model is making correct decisions.

---

# Accuracy

## Definition

Accuracy measures the percentage of correctly classified observations out of the total observations.

### Formula

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Where:

- TP = True Positive
- TN = True Negative
- FP = False Positive
- FN = False Negative

### Characteristics

- Easy to understand.
- Most commonly used metric.
- Suitable for balanced datasets.

### Advantages

- Simple to calculate.
- Easy to interpret.
- Useful when class distribution is balanced.

### Limitations

- Can be misleading for imbalanced datasets.
- Does not distinguish between different types of errors.

---

# Precision

## Definition

Precision measures how many of the predicted positive observations are actually positive.

### Formula

Precision = TP / (TP + FP)

### Characteristics

- Focuses on False Positives.
- High Precision means fewer false alarms.

### Applications

- Spam Detection
- Fraud Detection
- Recommendation Systems

### Advantages

- Important when False Positives are costly.
- Measures prediction quality.

### Limitations

- Does not consider False Negatives.

---

# Recall (Sensitivity)

## Definition

Recall measures how many actual positive observations were correctly identified.

### Formula

Recall = TP / (TP + FN)

### Characteristics

- Focuses on False Negatives.
- High Recall means most positive cases are detected.

### Applications

- Disease Detection
- Face Recognition
- Security Systems

### Advantages

- Important when missing positive cases is costly.
- Measures detection capability.

### Limitations

- May increase False Positives.

---

# F1-Score

## Definition

F1-Score is the harmonic mean of Precision and Recall.

It provides a balanced measure when both Precision and Recall are important.

### Formula

F1-Score = 2 × (Precision × Recall) / (Precision + Recall)

### Characteristics

- Balances Precision and Recall.
- Useful for imbalanced datasets.

### Advantages

- Better evaluation than Accuracy for imbalanced data.
- Combines two important metrics.

### Limitations

- Does not consider True Negatives.

---

# Specificity

## Definition

Specificity measures how well the model correctly identifies negative observations.

### Formula

Specificity = TN / (TN + FP)

### Characteristics

- Focuses on True Negatives.
- Measures the ability to avoid False Positives.

### Applications

- Medical Testing
- Fraud Prevention
- Quality Control

### Advantages

- Important when False Positives are costly.

### Limitations

- Does not evaluate positive predictions.

---

# Support

## Definition

Support represents the number of actual occurrences of each class in the dataset.

### Importance

- Indicates class distribution.
- Helps interpret Precision, Recall, and F1-Score.
- Useful for identifying class imbalance.

---

# Confusion Matrix

## Definition

A Confusion Matrix is a table that summarizes the performance of a classification model by comparing actual and predicted class labels.

### Components

### True Positive (TP)

Correctly predicted positive observations.

### True Negative (TN)

Correctly predicted negative observations.

### False Positive (FP)

Negative observations incorrectly predicted as positive.

### False Negative (FN)

Positive observations incorrectly predicted as negative.

### Example

| Actual / Predicted | Positive | Negative |
|--------------------|----------|----------|
| Positive | TP | FN |
| Negative | FP | TN |

### Advantages

- Provides complete error analysis.
- Useful for calculating multiple evaluation metrics.

### Limitations

- Can be difficult to interpret for multiclass problems.

---

# Classification Report

## Definition

A Classification Report summarizes multiple evaluation metrics for each class.

It includes:

- Precision
- Recall
- F1-Score
- Support

### Benefits

- Comprehensive evaluation.
- Easy model comparison.
- Widely used in Scikit-learn.

---

# Comparison of Classification Metrics

| Metric | Best Value | Focus |
|---------|------------|----------------------------|
| Accuracy | High | Overall correctness |
| Precision | High | Reduce False Positives |
| Recall | High | Reduce False Negatives |
| F1-Score | High | Balance Precision & Recall |
| Specificity | High | Correctly identify negatives |
| Support | Depends | Number of samples per class |

---

# When to Use Each Metric

### Use Accuracy

- Balanced datasets.
- Equal importance to all classes.

### Use Precision

- Spam Detection.
- Fraud Detection.
- False Positives are expensive.

### Use Recall

- Disease Detection.
- Security Systems.
- Missing positive cases is dangerous.

### Use F1-Score

- Imbalanced datasets.
- Precision and Recall are equally important.

### Use Specificity

- Medical testing.
- Situations where correctly identifying negatives is critical.

---

# Advantages

- Evaluates classification performance.
- Helps compare models.
- Identifies strengths and weaknesses.
- Supports better model selection.
- Improves prediction quality.

---

# Limitations

- Accuracy may be misleading for imbalanced data.
- Different metrics may lead to different conclusions.
- No single metric is suitable for every problem.

---

# Best Practices

- Evaluate models using multiple metrics.
- Analyze the Confusion Matrix.
- Use F1-Score for imbalanced datasets.
- Consider business requirements when choosing metrics.
- Compare training and testing performance.

---

# Real-World Applications

Classification Evaluation Metrics are widely used in:

- Email Spam Detection
- Medical Diagnosis
- Credit Card Fraud Detection
- Customer Churn Prediction
- Employee Attrition Prediction
- Face Recognition
- Sentiment Analysis
- Loan Approval Systems
- Intrusion Detection
- Product Recommendation

---

# Key Learnings

Today I learned:

- The importance of Classification Evaluation Metrics.
- How Accuracy measures overall performance.
- The difference between Precision and Recall.
- Why F1-Score is useful for imbalanced datasets.
- The role of Specificity in identifying negative cases.
- How to interpret a Confusion Matrix.
- The information provided by a Classification Report.

---

# Interview Questions

1. What are Classification Evaluation Metrics?
2. What is Accuracy?
3. What is the difference between Precision and Recall?
4. Why is F1-Score important?
5. What is Specificity?
6. Explain the Confusion Matrix.
7. What is Support?
8. What does the Classification Report contain?
9. Why can Accuracy be misleading?
10. Which metric is best for imbalanced datasets?

---

# Conclusion

Classification Evaluation Metrics are essential for measuring the effectiveness of classification models. Metrics such as Accuracy, Precision, Recall, F1-Score, Specificity, Confusion Matrix, and Classification Report provide valuable insights into model performance. Using multiple metrics together ensures a comprehensive evaluation and helps select the most suitable model for real-world classification problems.