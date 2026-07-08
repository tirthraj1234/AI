# Entropy Notes

## Day 3 – Entropy

## What is Entropy?

Entropy is a measure of **uncertainty**, **impurity**, or **disorder** in a dataset. It is used in Decision Trees to determine how mixed the data is before making a split.

A Decision Tree aims to reduce entropy at every split so that the data becomes more organized and belongs to a single class.

- **High Entropy** → Data is highly mixed.
- **Low Entropy** → Data is more organized.
- **Zero Entropy** → Data is completely pure.

---

## Why is Entropy Important?

Entropy helps a Decision Tree choose the best feature for splitting the dataset. The feature that reduces entropy the most is selected because it creates purer groups and improves prediction accuracy.

---

## Entropy Formula

The mathematical formula for Entropy is:

```
Entropy(S) = - Σ Pi × log₂(Pi)
```

Where:

- **S** = Dataset
- **Pi** = Probability of each class
- **log₂** = Logarithm with base 2

---

## Entropy Values

| Entropy Value | Meaning |
|---------------|---------|
| 0 | Completely Pure Data |
| Between 0 and 1 | Partially Mixed Data |
| 1 | Completely Mixed Data (Binary Classification) |

---

## Example

Suppose a dataset contains:

| Promotion |
|-----------|
| Yes |
| Yes |
| No |
| No |

Probability:

- P(Yes) = 2/4 = 0.5
- P(No) = 2/4 = 0.5

Entropy:

```
Entropy = -(0.5 × log₂0.5 + 0.5 × log₂0.5)

Entropy = 1
```

This means the dataset is completely mixed.

---

## Interpretation

### Entropy = 0

- All records belong to the same class.
- The dataset is pure.
- No further splitting is required.

### Entropy = 1

- Data is evenly distributed between classes.
- Maximum uncertainty exists.
- More splitting is required.

---

## Advantages of Entropy

- Measures the impurity of data.
- Helps Decision Trees choose the best split.
- Improves model accuracy.
- Makes classification more effective.
- Reduces uncertainty during training.

---

## Limitations of Entropy

- Requires logarithmic calculations, making it slightly slower.
- Can be computationally expensive for very large datasets.
- Mainly used with Decision Tree algorithms.

---

## Real-World Applications

Entropy is used in:

- Employee Promotion Prediction
- Loan Approval Systems
- Customer Churn Prediction
- Fraud Detection
- Medical Diagnosis
- Email Spam Detection
- Credit Risk Analysis
- Product Recommendation Systems

---

## Python Example

```python
import math

p_yes = 0.5
p_no = 0.5

entropy = -(p_yes * math.log2(p_yes) + p_no * math.log2(p_no))

print(entropy)
```

---

## Key Learnings

Today I learned:

- What Entropy is.
- Why Entropy is important in Decision Trees.
- How Entropy measures impurity.
- The Entropy formula.
- How to calculate Entropy.
- Real-world applications of Entropy.
- Basic Python implementation for calculating Entropy.

---

## Conclusion

Entropy is a fundamental concept in Decision Trees that measures the uncertainty or impurity of a dataset. A Decision Tree uses Entropy to select the best feature for splitting the data, helping create more accurate and reliable Machine Learning models.