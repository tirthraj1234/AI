# Bayes' Theorem & Probability Notes

## Day 7 – Bayes' Theorem & Probability

## What is Probability?

Probability is the measure of the likelihood that an event will occur. It is represented by a value between **0 and 1**.

- **0** → Impossible event
- **1** → Certain event

### Formula

```
Probability = Number of Favorable Outcomes / Total Number of Outcomes
```

### Example

A bag contains **3 red balls** and **2 blue balls**.

- Probability of selecting a red ball = **3/5 = 0.6**
- Probability of selecting a blue ball = **2/5 = 0.4**

---

## Types of Probability

### 1. Marginal Probability

Marginal Probability is the probability of a single event occurring without considering any other event.

Example:

```
P(A)
```

---

### 2. Joint Probability

Joint Probability is the probability of two events occurring together.

Example:

```
P(A ∩ B)
```

---

### 3. Conditional Probability

Conditional Probability is the probability of an event occurring given that another event has already occurred.

Example:

```
P(A | B)
```

---

## What is Bayes' Theorem?

Bayes' Theorem is a mathematical formula used to calculate the probability of an event based on prior knowledge of related events. It is the foundation of the Naive Bayes algorithm and helps update probabilities when new information becomes available.

---

## Bayes' Theorem Formula

```
P(A | B) = (P(B | A) × P(A)) / P(B)
```

---

## Components of Bayes' Theorem

- **P(A | B)** – Posterior Probability (Probability of A given B)
- **P(B | A)** – Likelihood (Probability of B given A)
- **P(A)** – Prior Probability (Initial probability of A)
- **P(B)** – Evidence (Probability of B)

---

## Practical Example

Suppose:

- 1% of people have a disease.
- A medical test correctly detects the disease 95% of the time.
- The test gives a false positive 5% of the time.

Bayes' Theorem is used to calculate the probability that a person actually has the disease after receiving a positive test result.

---

## Python Example

```python
# Bayes' Theorem Example

P_A = 0.01      # Prior Probability
P_B_given_A = 0.95
P_B = 0.06

P_A_given_B = (P_B_given_A * P_A) / P_B

print("Posterior Probability:", P_A_given_B)
```

---

## Applications

Bayes' Theorem is widely used in:

- Email Spam Detection
- Medical Diagnosis
- Fraud Detection
- Sentiment Analysis
- Weather Forecasting
- Customer Behavior Prediction
- Risk Analysis
- Recommendation Systems
- Document Classification

---

## Advantages

- Simple and easy to understand.
- Works well with probability-based problems.
- Forms the foundation of the Naive Bayes algorithm.
- Updates predictions when new evidence is available.
- Useful for decision-making under uncertainty.

---

## Limitations

- Requires accurate prior probabilities.
- Assumes reliable probability estimates.
- Results depend on the quality of input data.
- Can be less effective if assumptions are incorrect.

---

## Key Learnings

Today I learned:

- What probability is.
- Different types of probability.
- The concept of conditional probability.
- Bayes' Theorem and its formula.
- The components of Bayes' Theorem.
- How Bayes' Theorem works with a practical example.
- Basic implementation of Bayes' Theorem using Python.
- Real-world applications of Bayes' Theorem.

---

## Conclusion

Bayes' Theorem is a fundamental concept in probability and Machine Learning. It provides a mathematical approach to updating probabilities based on new evidence. The theorem serves as the foundation of the Naive Bayes algorithm and is widely used in applications such as spam detection, medical diagnosis, fraud detection, and text classification. Understanding Bayes' Theorem is essential for building probability-based Machine Learning models.