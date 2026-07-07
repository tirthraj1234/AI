# Logistic Regression Notes

## Day 2 – Logistic Regression

## What is Logistic Regression?

Logistic Regression is a supervised Machine Learning algorithm used for **classification problems**. It predicts the probability that an input belongs to a particular class. The output is usually either **0** or **1**, making it suitable for binary classification tasks.

Although it is called "Regression," it is mainly used for **classification** rather than predicting continuous values.

---

## Why is Logistic Regression Important?

Logistic Regression is important because:

- Simple and easy to understand.
- Fast to train and predict.
- Produces probability values.
- Works well for binary classification.
- Widely used in business and healthcare applications.

---

## How Logistic Regression Works

Logistic Regression first calculates a linear equation using the input features. It then applies the **Sigmoid Function** to convert the output into a probability value between **0 and 1**.

The model compares the probability with a threshold (usually 0.5):

- Probability ≥ 0.5 → Class 1
- Probability < 0.5 → Class 0

---

## Sigmoid Function

The Sigmoid Function converts any real number into a probability between **0 and 1**.

### Formula

```
P = 1 / (1 + e^(-z))
```

Where:

- **P** = Probability
- **e** = Euler's Number
- **z** = Linear combination of input features

---

## Decision Boundary

A Decision Boundary is the threshold used to classify data into different classes.

Common threshold:

- Probability ≥ 0.5 → Positive Class (1)
- Probability < 0.5 → Negative Class (0)

Example:

| Probability | Prediction |
|-------------|------------|
| 0.92 | 1 |
| 0.75 | 1 |
| 0.48 | 0 |
| 0.15 | 0 |

---

## Types of Classification

### Binary Classification

Binary Classification has only two possible output classes.

Examples:

- Yes / No
- Pass / Fail
- Purchased / Not Purchased
- Spam / Not Spam

---

### Multi-Class Classification

Multi-Class Classification has more than two output classes.

Examples:

- Cat
- Dog
- Bird

Logistic Regression can also be extended to handle multi-class classification.

---

## Difference Between Linear Regression and Logistic Regression

| Linear Regression | Logistic Regression |
|-------------------|---------------------|
| Used for Regression problems. | Used for Classification problems. |
| Predicts continuous values. | Predicts categories or classes. |
| Output can be any numerical value. | Output is a probability between 0 and 1. |
| Example: Salary Prediction | Example: Customer Purchase Prediction |

---

## Advantages of Logistic Regression

- Easy to understand and implement.
- Fast training and prediction.
- Produces probability scores.
- Suitable for binary classification.
- Performs well on linearly separable data.
- Requires less computational power.

---

## Limitations of Logistic Regression

- Not suitable for complex non-linear relationships.
- Sensitive to outliers.
- Requires feature scaling for better performance.
- Performance decreases when classes overlap significantly.

---

## Evaluation Metrics

Common evaluation metrics for Logistic Regression include:

- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1 Score

These metrics help measure the performance of the classification model.

---

## Real-World Applications

Logistic Regression is used in:

- Customer Purchase Prediction
- Email Spam Detection
- Credit Card Fraud Detection
- Loan Approval Prediction
- Medical Disease Prediction
- Customer Churn Prediction
- Employee Attrition Prediction
- Sentiment Analysis

---

## Python Libraries Used

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

---

## Key Learnings

Today I learned:

- What Logistic Regression is.
- Difference between Regression and Classification.
- How the Sigmoid Function works.
- What a Decision Boundary is.
- Binary and Multi-Class Classification.
- Advantages and limitations of Logistic Regression.
- Real-world applications of Logistic Regression.
- Common evaluation metrics for classification models.

---

## Conclusion

Logistic Regression is one of the most popular supervised Machine Learning algorithms for classification problems. It predicts probabilities using the Sigmoid Function and classifies data into different categories. Due to its simplicity, speed, and effectiveness, it is widely used in finance, healthcare, marketing, cybersecurity, and many other industries.