# KNN Model Evaluation Notes

## Day 6 – KNN Model Evaluation

## What is Model Evaluation?

Model Evaluation is the process of measuring how well a Machine Learning model performs on unseen data. It helps determine the accuracy, reliability, and overall effectiveness of the model before it is used in real-world applications.

For KNN, model evaluation is performed after making predictions on the test dataset.

---

## Why is Model Evaluation Important?

Model evaluation helps to:

- Measure prediction accuracy.
- Compare different Machine Learning models.
- Detect overfitting and underfitting.
- Improve model performance.
- Build reliable and accurate prediction systems.

---

## 1. Accuracy

Accuracy is the percentage of correctly predicted observations out of the total observations.

### Formula

```
Accuracy = Correct Predictions / Total Predictions
```

### Python Example

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
```

---

## 2. Confusion Matrix

A Confusion Matrix is a table that compares the actual values with the predicted values.

It helps understand how many predictions are correct and where the model makes mistakes.

### Components

- **True Positive (TP):** Correctly predicted positive cases.
- **True Negative (TN):** Correctly predicted negative cases.
- **False Positive (FP):** Incorrectly predicted positive cases.
- **False Negative (FN):** Incorrectly predicted negative cases.

### Python Example

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print(cm)
```

---

## 3. Precision

Precision measures how many of the predicted positive cases are actually positive.

### Formula

```
Precision = TP / (TP + FP)
```

High precision means the model makes fewer false positive predictions.

---

## 4. Recall

Recall measures how many actual positive cases are correctly identified by the model.

### Formula

```
Recall = TP / (TP + FN)
```

High recall means the model successfully identifies most positive cases.

---

## 5. F1-Score

F1-Score is the harmonic mean of Precision and Recall.

It provides a balanced measure when both precision and recall are important.

### Formula

```
F1-Score = 2 × (Precision × Recall) / (Precision + Recall)
```

---

## 6. Classification Report

A Classification Report summarizes the model's performance by displaying:

- Precision
- Recall
- F1-Score
- Support (number of actual samples for each class)

### Python Example

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

---

## Business Interpretation

For the Employee Attrition Prediction project:

- High accuracy indicates the model predicts employee attrition effectively.
- High precision reduces false alerts for employees predicted to leave.
- High recall helps identify most employees who are likely to leave.
- A good F1-Score provides a balance between precision and recall.

These metrics help organizations make informed decisions about employee retention.

---

## Advantages of Model Evaluation

- Measures model performance.
- Improves prediction reliability.
- Helps compare multiple models.
- Detects prediction errors.
- Supports better business decisions.

---

## Limitations

- Accuracy alone may not be sufficient for imbalanced datasets.
- Evaluation depends on the quality of the test data.
- Different metrics are needed for different business problems.

---

## Real-World Applications

Model evaluation is used in:

- Employee Attrition Prediction
- Medical Diagnosis
- Fraud Detection
- Customer Churn Prediction
- Credit Risk Analysis
- Email Spam Detection
- Image Classification
- Product Recommendation
- Disease Prediction

---

## Key Learnings

Today I learned:

- What model evaluation is.
- Why model evaluation is important.
- How to calculate accuracy.
- The purpose of a confusion matrix.
- The meaning of precision, recall, and F1-Score.
- How to generate a classification report.
- How evaluation metrics help improve Machine Learning models.

---

## Conclusion

Model Evaluation is an essential step in the Machine Learning workflow. Metrics such as Accuracy, Confusion Matrix, Precision, Recall, F1-Score, and the Classification Report provide valuable insights into the performance of a KNN model. Proper evaluation helps build reliable, accurate, and effective Machine Learning solutions for real-world applications.