# Model Evaluation Notes

## What is Model Evaluation?

Model Evaluation is the process of measuring how well a Machine Learning model performs on unseen data. It helps determine whether the model makes accurate and reliable predictions.

---

## Accuracy

Accuracy is the percentage of correct predictions made by the model.

Formula:

Accuracy = Correct Predictions / Total Predictions

Used when the dataset is balanced.

---

## Confusion Matrix

A Confusion Matrix compares actual values with predicted values.

It contains:

- True Positive (TP)
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)

It helps understand where the model makes mistakes.

---

## Precision

Precision measures how many predicted positive cases are actually positive.

Formula:

Precision = TP / (TP + FP)

High Precision is important when false positives are costly.

Example:

- Spam Detection
- Fraud Detection

---

## Recall

Recall measures how many actual positive cases are correctly identified.

Formula:

Recall = TP / (TP + FN)

High Recall is important when false negatives are costly.

Example:

- Disease Detection
- Cancer Prediction

---

## F1-Score

F1-Score is the harmonic mean of Precision and Recall.

Formula:

F1 = 2 × (Precision × Recall) / (Precision + Recall)

It provides a balanced evaluation when both Precision and Recall are important.

---

## Applications

- Customer Purchase Prediction
- Fraud Detection
- Spam Detection
- Medical Diagnosis
- Loan Approval
- Credit Risk Analysis

---

## Key Learnings

- Learned how to evaluate classification models.
- Understood Accuracy, Precision, Recall, and F1-Score.
- Learned how to interpret a Confusion Matrix.
- Used Classification Report in Scikit-learn.

---

## Conclusion

Model Evaluation helps measure the quality of a Machine Learning model. Selecting the correct evaluation metric depends on the business problem and the importance of different types of prediction errors.