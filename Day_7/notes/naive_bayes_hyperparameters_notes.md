# Naive Bayes Hyperparameters Notes

## Day 7 – Naive Bayes Hyperparameters

## What are Hyperparameters?

Hyperparameters are configuration values that are set before training a Machine Learning model. They control how the algorithm learns from the data and can affect the model's performance.

Unlike model parameters, hyperparameters are not learned automatically during training.

---

## Why are Hyperparameters Important?

Hyperparameters help to:

- Improve model accuracy.
- Control the learning process.
- Reduce overfitting and underfitting.
- Improve prediction performance.
- Optimize Machine Learning models.

---

## 1. var_smoothing (Gaussian Naive Bayes)

The `var_smoothing` hyperparameter is used in **Gaussian Naive Bayes**.

It adds a small value to the variance of each feature to improve numerical stability and prevent division by very small numbers.

### Default Value

```python
1e-9
```

### Python Example

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB(var_smoothing=1e-9)
```

### Advantages

- Improves numerical stability.
- Prevents division by zero.
- Makes the model more reliable.

---

## 2. alpha (Multinomial & Bernoulli Naive Bayes)

The `alpha` hyperparameter controls **Laplace Smoothing**.

It prevents zero probabilities by adding a small value to feature counts.

### Default Value

```python
1.0
```

### Python Example

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB(alpha=1.0)
```

### Advantages

- Solves the Zero-Frequency Problem.
- Improves prediction accuracy.
- Handles unseen words effectively.

---

## 3. fit_prior

The `fit_prior` parameter determines whether the model should learn class probabilities from the training data.

### Values

- **True** – Learn prior probabilities from the dataset (default).
- **False** – Use equal prior probabilities for all classes.

### Python Example

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB(fit_prior=True)
```

---

## 4. class_prior

The `class_prior` parameter allows you to manually specify the prior probability for each class.

### Python Example

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB(priors=[0.7, 0.3])
```

In this example:

- Class 0 Prior Probability = 70%
- Class 1 Prior Probability = 30%

---

## Best Practices

- Start with the default hyperparameter values.
- Tune `alpha` for text classification problems.
- Adjust `var_smoothing` only when necessary.
- Use `class_prior` when reliable prior knowledge is available.
- Evaluate different hyperparameter values using validation techniques.

---

## Python Example

```python
from sklearn.naive_bayes import GaussianNB, MultinomialNB

gaussian_model = GaussianNB(var_smoothing=1e-9)

multinomial_model = MultinomialNB(
    alpha=1.0,
    fit_prior=True
)

print("Gaussian Model:", gaussian_model)
print("Multinomial Model:", multinomial_model)
```

---

## Advantages

- Improves model performance.
- Enhances prediction accuracy.
- Prevents numerical instability.
- Handles unseen data effectively.
- Makes the model more reliable.

---

## Limitations

- Incorrect hyperparameter values can reduce accuracy.
- Some hyperparameters require experimentation.
- Performance depends on the quality of the dataset.

---

## Real-World Applications

Naive Bayes hyperparameters are useful in:

- Email Spam Detection
- Sentiment Analysis
- News Classification
- Medical Diagnosis
- Fraud Detection
- Customer Feedback Analysis
- Language Detection
- Document Classification

---

## Key Learnings

Today I learned:

- What hyperparameters are.
- Why hyperparameters are important.
- The purpose of `var_smoothing`.
- The purpose of `alpha`.
- How `fit_prior` works.
- How to use `class_prior`.
- Best practices for selecting hyperparameters.
- Basic implementation using Scikit-learn.

---

## Conclusion

Hyperparameters play an important role in improving the performance of Naive Bayes models. Parameters such as `var_smoothing`, `alpha`, `fit_prior`, and `class_prior` help control the learning process, improve numerical stability, handle unseen data, and enhance prediction accuracy. Proper selection and tuning of these hyperparameters result in more reliable and efficient Machine Learning models for real-world classification tasks.