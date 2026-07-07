# Encoding Categorical Data Notes

## Day 2 – Encoding Categorical Data

## What is Categorical Data?

Categorical data consists of text or labels that represent different categories instead of numerical values. Machine Learning algorithms cannot process text directly, so categorical data must be converted into numerical form before training a model.

### Examples

- Gender (Male, Female)
- Department (HR, IT, Finance)
- City (Ahmedabad, Surat, Rajkot)
- Country (India, USA, Canada)

---

## Why is Encoding Required?

Machine Learning algorithms perform mathematical calculations and work only with numerical data. Encoding converts categorical values into numbers so that the algorithms can understand and process them.

### Benefits of Encoding

- Converts text data into numerical values.
- Makes data suitable for Machine Learning algorithms.
- Improves model performance.
- Enables mathematical computations on categorical features.

---

## Types of Encoding

### 1. Label Encoding

Label Encoding assigns a unique numerical value to each category.

### Example

| Gender | Encoded Value |
|---------|---------------|
| Male | 1 |
| Female | 0 |

### Python Example

```python
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df["Gender"] = label_encoder.fit_transform(df["Gender"])
```

### When to Use

- Binary categories (Yes/No, Male/Female)
- Categories with a natural order (Low, Medium, High)

---

### 2. One-Hot Encoding

One-Hot Encoding creates a separate column for each category and represents the presence of a category using 1 (True) and its absence using 0 (False).

### Example

Original Data

| Department |
|------------|
| HR |
| IT |
| Finance |

After One-Hot Encoding

| Department_Finance | Department_HR | Department_IT |
|--------------------|---------------|---------------|
| 0 | 1 | 0 |
| 0 | 0 | 1 |
| 1 | 0 | 0 |

### Python Example

```python
df = pd.get_dummies(df, columns=["Department"])
```

### When to Use

- Categories with no natural order.
- Features such as City, Department, Country, Product Category.

---

## Difference Between Label Encoding and One-Hot Encoding

| Label Encoding | One-Hot Encoding |
|----------------|------------------|
| Converts categories into numbers. | Creates separate columns for each category. |
| Suitable for ordered or binary categories. | Suitable for unordered categories. |
| Uses a single column. | Uses multiple columns. |

---

## Advantages of Encoding

- Converts categorical data into numerical format.
- Makes datasets compatible with Machine Learning models.
- Improves prediction accuracy.
- Preserves useful information from categorical features.

---

## Real-World Applications

- Customer Purchase Prediction
- Employee Management Systems
- Loan Approval Prediction
- HR Analytics
- Fraud Detection
- Recommendation Systems
- Healthcare Analytics

---

## Key Learnings

Today I learned:

- What categorical data is.
- Why encoding is necessary.
- How Label Encoding works.
- How One-Hot Encoding works.
- The difference between Label Encoding and One-Hot Encoding.
- When to use each encoding technique.

---

## Conclusion

Encoding is an essential step in data preprocessing. It converts categorical data into numerical values that Machine Learning algorithms can understand. Choosing the correct encoding method helps improve model performance and ensures accurate predictions.