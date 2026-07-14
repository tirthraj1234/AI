# Naive Bayes Notes

## Day 7 – Introduction to Naive Bayes

## What is Naive Bayes?

Naive Bayes is a **Supervised Machine Learning algorithm** mainly used for **classification** tasks. It is based on **Bayes' Theorem** and assumes that all input features are independent of each other.

The term **"Naive"** refers to the assumption that every feature contributes independently to the prediction, even though this assumption may not always hold true in real-world datasets.

Naive Bayes is widely used for text classification problems because it is simple, fast, and effective.

---

## How Does Naive Bayes Work?

The Naive Bayes algorithm follows these steps:

1. Collect and prepare the training dataset.
2. Calculate the probability of each class.
3. Calculate the probability of each feature for every class.
4. Apply Bayes' Theorem to compute the probability of each class for a new data point.
5. Select the class with the highest probability as the final prediction.

---

## Features of Naive Bayes

- Supervised Learning algorithm.
- Based on probability theory.
- Uses Bayes' Theorem.
- Assumes feature independence.
- Fast training and prediction.
- Works well with high-dimensional data.

---

## Advantages

- Simple and easy to understand.
- Fast training and prediction.
- Performs well on large datasets.
- Works effectively for text classification.
- Requires less training data.
- Handles multiple classes efficiently.

---

## Limitations

- Assumes all features are independent.
- Performance decreases when features are highly correlated.
- Zero-frequency problems may occur without smoothing.
- Less suitable for complex relationships between features.

---

## Python Library

The Scikit-learn library provides different Naive Bayes models.

Example:

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
```

---

## Real-World Applications

Naive Bayes is commonly used in:

- Email Spam Detection
- Sentiment Analysis
- News Article Classification
- Language Detection
- Medical Diagnosis
- Customer Feedback Analysis
- Document Classification
- Product Review Classification
- Fraud Detection

---

## Advantages Over Some Other Algorithms

- Faster than many complex classification algorithms.
- Requires less computational power.
- Easy to implement.
- Performs well with text data.
- Suitable for real-time prediction systems.

---

## Key Learnings

Today I learned:

- What Naive Bayes is.
- Why it is called "Naive".
- How the Naive Bayes algorithm works.
- The main features of Naive Bayes.
- Advantages and limitations of the algorithm.
- Real-world applications of Naive Bayes.
- Basic implementation using Scikit-learn.

---

## Conclusion

Naive Bayes is a simple, fast, and efficient supervised Machine Learning algorithm used for classification tasks. It is based on Bayes' Theorem and assumes that all features are independent. Despite this assumption, it performs exceptionally well in many practical applications such as spam detection, sentiment analysis, and document classification. Due to its speed, simplicity, and high performance, Naive Bayes remains one of the most widely used classification algorithms in Machine Learning.