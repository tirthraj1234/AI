# Data Preprocessing Notes

## Day 2 – Data Preprocessing

## What is Data Preprocessing?

Data Preprocessing is the process of cleaning, organizing, and transforming raw data into a format that can be used to train a Machine Learning model. It is one of the most important steps in the Machine Learning workflow because the quality of the data directly affects the performance of the model.

---

## Why is Data Preprocessing Important?

Data preprocessing is important because:

- Improves the accuracy of Machine Learning models.
- Removes errors and inconsistencies from data.
- Handles missing values.
- Converts categorical data into numerical form.
- Scales numerical features to a similar range.
- Reduces noise in the dataset.
- Prepares the data for training and testing.

Well-prepared data helps the model learn better and make more accurate predictions.

---

## Steps of Data Preprocessing

### 1. Import the Dataset

Load the dataset into Python using libraries such as Pandas.

Example:

```python
import pandas as pd

data = pd.read_csv("data.csv")
```

---

### 2. Explore the Dataset

Understand the dataset by checking:

- Number of rows and columns
- Data types
- Missing values
- Statistical summary

Common functions:

- `head()`
- `tail()`
- `info()`
- `describe()`

---

### 3. Handle Missing Values

Real-world datasets often contain missing values.

Common methods:

- Remove rows containing missing values.
- Replace missing values with the mean.
- Replace missing values with the median.
- Replace missing values with the most frequent value (mode).

---

### 4. Encode Categorical Data

Machine Learning algorithms work with numbers, not text.

Example:

| Gender |
|---------|
| Male |
| Female |

Can be converted into:

| Gender |
|---------|
| 1 |
| 0 |

Common encoding methods:

- Label Encoding
- One-Hot Encoding

---

### 5. Feature Scaling

Feature Scaling brings numerical values into a similar range.

Example:

| Age | Salary |
|----|---------|
| 25 | 30000 |
| 30 | 800000 |

Since Salary is much larger than Age, scaling helps the model treat both features fairly.

Common methods:

- Standardization
- Normalization (Min-Max Scaling)

---

### 6. Split the Dataset

Divide the dataset into:

- Training Set
- Testing Set

A common split is:

- 80% Training Data
- 20% Testing Data

The training set is used to train the model, while the testing set is used to evaluate its performance.

---

## Real-World Example

Suppose a company wants to predict whether a customer will purchase a product.

Dataset:

| Age | Salary | City | Purchased |
|-----|--------|------|-----------|
| 25 | 30000 | Ahmedabad | Yes |
| 30 | Missing | Surat | No |
| 35 | 50000 | Rajkot | Yes |

Before training the model:

- Fill the missing salary.
- Convert city names into numerical values.
- Convert "Yes" and "No" into 1 and 0.
- Scale Age and Salary if needed.
- Split the data into training and testing sets.

---

## Advantages of Data Preprocessing

- Improves model accuracy.
- Reduces prediction errors.
- Makes data consistent.
- Removes unnecessary information.
- Helps Machine Learning models learn efficiently.
- Produces better and more reliable predictions.

---

## Applications

Data preprocessing is used in:

- Customer Purchase Prediction
- House Price Prediction
- Fraud Detection
- Medical Diagnosis
- Sales Forecasting
- Credit Risk Analysis
- HR Analytics
- Recommendation Systems

---

## Key Learnings

Today I learned:

- What Data Preprocessing is.
- Why preprocessing is important.
- The steps involved in preprocessing.
- How to handle missing values.
- How to encode categorical data.
- Why feature scaling is required.
- Why datasets are split into training and testing sets.

---

## Conclusion

Data Preprocessing is an essential step in Machine Learning. It ensures that the dataset is clean, consistent, and ready for model training. Proper preprocessing improves the accuracy, reliability, and performance of Machine Learning models.