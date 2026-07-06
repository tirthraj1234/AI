# Pandas Notes

## Day 1 – Pandas Fundamentals

### What is Pandas?

Pandas is a Python library used for data manipulation and analysis. It helps us read, organize, clean, filter, and analyze data efficiently. It supports different file formats such as CSV, Excel, JSON, and SQL databases.

---

## What is a DataFrame?

A DataFrame is a two-dimensional table with rows and columns. It is the most commonly used data structure in Pandas and is similar to an Excel spreadsheet or a database table.

Example:

| Name | Age | Department | Salary |
|------|-----|------------|--------|
| Alice | 25 | HR | 30000 |
| Bob | 30 | IT | 45000 |

---

## What is a Series?

A Series is a one-dimensional data structure in Pandas. It contains a single column of data with an index.

Example:

```python
import pandas as pd

salary = pd.Series([30000, 45000, 40000])
print(salary)
```

---

## Why is Pandas Important for Machine Learning?

Pandas is important because it helps prepare data before training a Machine Learning model. It allows us to:

- Read datasets from CSV and Excel files.
- Clean and organize data.
- Handle missing values.
- Filter and sort data.
- Select specific rows and columns.
- Perform data analysis.
- Prepare data for Machine Learning algorithms.

Without clean and organized data, Machine Learning models cannot produce accurate results.

---

## Pandas Functions Used Today

The following Pandas functions were used:

- `pd.read_csv()` – Read a CSV file.
- `head()` – Display the first 5 rows.
- `tail()` – Display the last 5 rows.
- `info()` – Show dataset information.
- `describe()` – Display statistical summary.
- `columns` – Display column names.
- `drop()` – Remove columns.
- `to_csv()` – Save a DataFrame to a CSV file.

---

## Practical Tasks Completed

- Created a sample employee dataset.
- Read the CSV file using Pandas.
- Displayed the first and last rows.
- Checked dataset information.
- Viewed statistical summary.
- Selected single and multiple columns.
- Filtered employees based on salary.
- Added a Bonus column.
- Removed the Bonus column.
- Saved the updated dataset as a new CSV file.

---

## Advantages of Pandas

- Easy to use.
- Fast and efficient.
- Handles large datasets.
- Supports data cleaning and preprocessing.
- Integrates well with NumPy and Scikit-learn.
- Widely used in Data Science and Machine Learning.

---

## Real-World Applications

- Customer Data Analysis
- Sales Reporting
- Financial Analysis
- Business Intelligence
- HR Analytics
- Healthcare Data Analysis
- Data Cleaning for Machine Learning

---

## Key Learnings

Today I learned:

- What Pandas is.
- What a DataFrame is.
- What a Series is.
- How to read a CSV file.
- How to inspect a dataset.
- How to filter data.
- How to add and remove columns.
- How to save a DataFrame as a CSV file.

---

## Conclusion

Pandas is one of the most important Python libraries for Data Science and Machine Learning. It makes data handling simple and efficient, allowing us to clean, analyze, and prepare datasets before building Machine Learning models.