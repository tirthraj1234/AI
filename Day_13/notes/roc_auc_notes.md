# ROC Curve and AUC Notes

## Day 13 – Phase 4: ROC Curve & AUC

# Introduction

ROC (Receiver Operating Characteristic) Curve and AUC (Area Under the Curve) are important evaluation techniques used for binary classification models. They measure how well a model distinguishes between positive and negative classes across different classification thresholds.

Unlike Accuracy, ROC-AUC evaluates the model over all possible threshold values, making it especially useful for imbalanced datasets.

---

# Objective of ROC Curve and AUC

The objectives are:

- Evaluate binary classification models.
- Measure the model's ability to distinguish between classes.
- Compare multiple classification models.
- Select the best classification threshold.
- Analyze prediction performance across different decision thresholds.

---

# What is ROC Curve?

The Receiver Operating Characteristic (ROC) Curve is a graphical representation of a classification model's performance.

It plots:

- True Positive Rate (TPR) on the Y-axis.
- False Positive Rate (FPR) on the X-axis.

Each point on the curve represents a different classification threshold.

---

# Why is ROC Curve Important?

ROC Curve helps us:

- Evaluate classification models.
- Compare multiple models.
- Choose the best threshold.
- Visualize classification performance.
- Understand the trade-off between detecting positives and avoiding false alarms.

---

# True Positive Rate (TPR)

## Definition

True Positive Rate measures the proportion of actual positive samples correctly predicted by the model.

It is also called:

- Recall
- Sensitivity

### Formula

TPR = TP / (TP + FN)

### Interpretation

High TPR means:

- More positive cases are correctly detected.
- Better detection capability.

### Applications

- Disease detection
- Fraud detection
- Spam filtering
- Employee attrition prediction

---

# False Positive Rate (FPR)

## Definition

False Positive Rate measures the proportion of actual negative samples incorrectly predicted as positive.

### Formula

FPR = FP / (FP + TN)

### Interpretation

Low FPR means:

- Fewer false alarms.
- Better classification performance.

---

# Relationship Between TPR and FPR

A good classifier should have:

- High TPR
- Low FPR

This produces a ROC curve close to the upper-left corner.

---

# AUC (Area Under the Curve)

## Definition

AUC measures the total area under the ROC Curve.

It represents the probability that the model correctly ranks a randomly chosen positive instance higher than a randomly chosen negative instance.

---

# AUC Score Range

| AUC Score | Interpretation |
|------------|----------------|
| 1.00 | Perfect Classifier |
| 0.90 – 0.99 | Excellent Model |
| 0.80 – 0.89 | Good Model |
| 0.70 – 0.79 | Fair Model |
| 0.60 – 0.69 | Poor Model |
| 0.50 | Random Guessing |

---

# Threshold Selection

## What is a Threshold?

A threshold is the probability value used to classify an observation into a positive or negative class.

Default threshold:

0.5

---

# Effect of Threshold

### Lower Threshold

- More positive predictions
- Higher Recall
- More False Positives

### Higher Threshold

- Fewer positive predictions
- Higher Precision
- More False Negatives

Selecting the threshold depends on the business problem.

---

# ROC Curve Interpretation

### Excellent Model

- Curve stays close to the upper-left corner.
- High TPR and Low FPR.
- Large AUC.

### Average Model

- Curve lies between the diagonal and upper-left corner.

### Poor Model

- Curve close to the diagonal.

### Random Classifier

- Diagonal line.
- AUC = 0.50.

### Perfect Classifier

- Passes through the upper-left corner.
- AUC = 1.00.

---

# Advantages of ROC Curve

- Independent of classification threshold.
- Useful for imbalanced datasets.
- Compares multiple models.
- Easy graphical interpretation.
- Shows trade-off between TPR and FPR.

---

# Advantages of AUC

- Single performance score.
- Easy model comparison.
- Measures discrimination ability.
- Independent of threshold.

---

# Limitations

- Mainly designed for binary classification.
- May be less informative than Precision-Recall curves in extremely imbalanced datasets.
- Does not indicate optimal threshold directly.

---

# Best Practices

- Use ROC-AUC along with Accuracy, Precision, Recall, and F1-Score.
- Compare ROC curves of multiple models.
- Select thresholds based on business requirements.
- Analyze the confusion matrix together with ROC-AUC.

---

# Real-World Applications

ROC Curve and AUC are widely used in:

- Medical diagnosis
- Credit card fraud detection
- Customer churn prediction
- Employee attrition prediction
- Loan approval systems
- Email spam detection
- Cybersecurity intrusion detection
- Risk assessment
- Insurance claim prediction
- Financial forecasting

---

# Key Learnings

Today I learned:

- What the ROC Curve represents.
- How TPR and FPR are calculated.
- How AUC measures model performance.
- The importance of threshold selection.
- How to interpret different ROC curves.
- Why ROC-AUC is useful for evaluating classification models.

---

# Interview Questions

1. What is a ROC Curve?
2. What does AUC represent?
3. What is the difference between TPR and FPR?
4. Why is ROC-AUC preferred for imbalanced datasets?
5. What does an AUC score of 0.5 indicate?
6. What is the default classification threshold?
7. How does changing the threshold affect Precision and Recall?
8. What is the ideal ROC Curve?
9. Can ROC-AUC be used for multiclass classification?
10. Why should ROC-AUC be used with other evaluation metrics?

---

# Conclusion

ROC Curve and AUC are powerful evaluation tools for binary classification models. The ROC Curve visualizes the relationship between the True Positive Rate and False Positive Rate across different thresholds, while AUC summarizes the model's ability to distinguish between classes using a single score. Together, they help data scientists compare models, choose suitable thresholds, and build more reliable machine learning systems.