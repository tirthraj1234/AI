# Types of Naive Bayes Notes

## Day 7 – Types of Naive Bayes

## What are the Types of Naive Bayes?

Naive Bayes has different variants based on the type of data being used. Choosing the correct type improves the model's accuracy and performance.

The three main types of Naive Bayes are:

1. Gaussian Naive Bayes
2. Multinomial Naive Bayes
3. Bernoulli Naive Bayes

Each variant is designed for a specific type of dataset.

---

## 1. Gaussian Naive Bayes

Gaussian Naive Bayes assumes that numerical features follow a **normal (Gaussian) distribution**.

It is mainly used for continuous numerical data.

### Suitable For

- Employee datasets
- Medical diagnosis
- Iris flower dataset
- Customer prediction
- Financial analysis

### Python Example

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
```

### Advantages

- Works well with continuous numerical data.
- Simple and fast.
- Requires less computational power.

### Limitations

- Assumes data follows a normal distribution.
- Performance may decrease if this assumption is not true.

---

## 2. Multinomial Naive Bayes

Multinomial Naive Bayes is designed for **count-based or frequency-based data**.

It is widely used in Natural Language Processing (NLP).

### Suitable For

- Email spam detection
- Text classification
- News classification
- Document categorization
- Word frequency analysis

### Python Example

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
```

### Advantages

- Excellent for text classification.
- Works well with word count data.
- Fast training and prediction.

### Limitations

- Not suitable for continuous numerical data.
- Requires count or frequency features.

---

## 3. Bernoulli Naive Bayes

Bernoulli Naive Bayes is used for **binary features**, where values are typically **0 or 1**, **True or False**, or **Yes or No**.

### Suitable For

- Binary text classification
- Presence or absence of words
- Recommendation systems
- Boolean datasets

### Python Example

```python
from sklearn.naive_bayes import BernoulliNB

model = BernoulliNB()
```

### Advantages

- Best for binary data.
- Simple to implement.
- Fast prediction.

### Limitations

- Not suitable for continuous data.
- Less effective for count-based features.

---

## Comparison of Naive Bayes Types

| Type | Data Type | Common Applications |
|------|-----------|---------------------|
| Gaussian Naive Bayes | Continuous numerical data | Medical diagnosis, employee prediction, Iris dataset |
| Multinomial Naive Bayes | Count or frequency data | Spam detection, document classification, sentiment analysis |
| Bernoulli Naive Bayes | Binary (0/1, Yes/No) data | Binary classification, recommendation systems |

---

## How to Choose the Right Type?

- Use **Gaussian Naive Bayes** for continuous numerical data.
- Use **Multinomial Naive Bayes** for text and word-count data.
- Use **Bernoulli Naive Bayes** for binary features.

Selecting the appropriate variant based on the dataset improves model performance and prediction accuracy.

---

## Real-World Applications

The different types of Naive Bayes are used in:

- Email Spam Detection
- Sentiment Analysis
- News Article Classification
- Language Detection
- Medical Diagnosis
- Fraud Detection
- Customer Feedback Analysis
- Product Review Classification
- Document Categorization

---

## Advantages

- Easy to understand and implement.
- Fast training and prediction.
- Supports multiple types of datasets.
- Performs well on classification tasks.
- Efficient for large datasets.

---

## Limitations

- Assumes feature independence.
- Performance depends on selecting the correct variant.
- Less suitable for highly correlated features.
- May require preprocessing for better results.

---

## Key Learnings

Today I learned:

- The three main types of Naive Bayes.
- The purpose of Gaussian Naive Bayes.
- The purpose of Multinomial Naive Bayes.
- The purpose of Bernoulli Naive Bayes.
- How to choose the correct Naive Bayes variant.
- Real-world applications of each type.
- Basic implementation using Scikit-learn.

---

## Conclusion

Naive Bayes provides three main variants—Gaussian, Multinomial, and Bernoulli—to handle different types of data. Selecting the appropriate variant based on the dataset is essential for achieving accurate and reliable predictions. These algorithms are widely used in machine learning applications such as spam detection, sentiment analysis, medical diagnosis, and document classification because they are simple, efficient, and computationally fast.