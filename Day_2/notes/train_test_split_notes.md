# Train-Test Split Notes

## Day 2 – Train-Test Split

## What is Train-Test Split?

Train-Test Split is a technique used in Machine Learning to divide a dataset into two parts: a training set and a testing set. The training set is used to train the model, while the testing set is used to evaluate the model's performance on unseen data.

---

## Why is Train-Test Split Important?

Train-Test Split is important because:

- Prevents the model from memorizing the data.
- Helps evaluate how well the model performs on new data.
- Reduces the chances of overfitting.
- Provides a fair measurement of model accuracy.
- Helps build reliable and generalizable Machine Learning models.

---

## Training Data

The training dataset is the portion of data used to teach the Machine Learning model. The model learns patterns and relationships between input features and the target variable from this data.

Example:

If a dataset contains 100 records and an 80:20 split is used, then 80 records will be used for training.

---

## Testing Data

The testing dataset is the portion of data used to evaluate the trained Machine Learning model. The model has never seen this data before, making it useful for measuring prediction performance.

Example:

If a dataset contains 100 records and an 80:20 split is used, then 20 records will be used for testing.

---

## Common Train-Test Split Ratios

| Training Data | Testing Data |
|---------------|--------------|
| 80% | 20% |
| 70% | 30% |
| 75% | 25% |
| 90% | 10% |

The most commonly used ratio is **80% for training** and **20% for testing**.

---

## Train-Test Split in Python

The `train_test_split()` function from Scikit-learn is used to split the dataset.

Example:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### Parameters

- **X** – Input features.
- **y** – Target variable.
- **test_size=0.2** – Uses 20% of the data for testing.
- **random_state=42** – Ensures the same data split every time the program runs.

---

## Advantages of Train-Test Split

- Prevents overfitting.
- Evaluates model performance on unseen data.
- Improves model reliability.
- Makes performance measurement more realistic.
- Easy to implement using Scikit-learn.

---

## Real-World Applications

Train-Test Split is used in:

- Customer Purchase Prediction
- House Price Prediction
- Sales Forecasting
- Credit Risk Analysis
- Fraud Detection
- Medical Diagnosis
- Recommendation Systems
- Employee Attrition Prediction

---

## Key Learnings

Today I learned:

- What Train-Test Split is.
- Why datasets are divided into training and testing sets.
- The difference between training data and testing data.
- Common train-test split ratios.
- How to use the `train_test_split()` function in Scikit-learn.
- The importance of `test_size` and `random_state`.

---

## Conclusion

Train-Test Split is an essential step in Machine Learning. It allows a model to learn from one portion of the dataset and be evaluated on another, helping measure its ability to make accurate predictions on new, unseen data. This process improves model reliability and helps prevent overfitting.