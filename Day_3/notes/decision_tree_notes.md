# Decision Tree Notes

## Day 3 – Decision Tree

## What is a Decision Tree?

A Decision Tree is a **Supervised Machine Learning algorithm** used for both **classification** and **regression** problems. It makes decisions by asking a series of questions about the input data and splits the data into smaller groups based on the answers. The final prediction is made at the leaf node.

The structure of a Decision Tree resembles an upside-down tree, making it easy to understand and visualize.

---

## How Does a Decision Tree Work?

A Decision Tree works in the following steps:

1. Start with the entire dataset.
2. Select the best feature to split the data.
3. Divide the dataset into smaller subsets.
4. Repeat the splitting process for each subset.
5. Stop when the stopping condition is met.
6. Make the final prediction at the leaf node.

---

## Components of a Decision Tree

### 1. Root Node

The Root Node is the first node of the tree where the decision-making process begins.

Example:

```
Experience > 5 Years?
```

---

### 2. Decision Node

A Decision Node is an internal node where another condition is checked.

Example:

```
Performance Rating > 4?
```

---

### 3. Leaf Node

A Leaf Node is the final node that provides the prediction or output.

Example:

```
Promote
```

or

```
Do Not Promote
```

---

### 4. Branch

A Branch connects one node to another and represents the outcome of a decision.

---

## Types of Decision Trees

### Classification Decision Tree

Used when the target variable is categorical.

Examples:

- Spam Detection
- Customer Churn Prediction
- Loan Approval
- Employee Promotion

---

### Regression Decision Tree

Used when the target variable is continuous.

Examples:

- House Price Prediction
- Sales Forecasting
- Temperature Prediction

---

## Splitting Criteria

Decision Trees use different methods to decide the best feature for splitting the data.

The most common splitting methods are:

- Entropy
- Information Gain
- Gini Index

These methods help create the most accurate and efficient tree.

---

## Advantages of Decision Tree

- Easy to understand and interpret.
- Simple to visualize.
- Handles both numerical and categorical data.
- Requires little data preprocessing.
- Can solve both classification and regression problems.
- Works well with non-linear relationships.

---

## Limitations of Decision Tree

- Can easily overfit the training data.
- Sensitive to small changes in the dataset.
- Large trees become difficult to understand.
- May not perform well on very complex datasets.

---

## Real-World Applications

Decision Trees are widely used in:

- Employee Promotion Prediction
- Loan Approval Systems
- Credit Risk Analysis
- Medical Diagnosis
- Fraud Detection
- Customer Churn Prediction
- Student Performance Analysis
- Insurance Claim Prediction
- Product Recommendation Systems

---

## Python Libraries Used

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

---

## Key Learnings

Today I learned:

- What a Decision Tree is.
- How a Decision Tree works.
- Components of a Decision Tree.
- Difference between Classification and Regression Decision Trees.
- Advantages and limitations of Decision Trees.
- Common applications of Decision Trees.
- Basic Python libraries required to implement Decision Trees.

---

## Conclusion

A Decision Tree is one of the most popular Machine Learning algorithms because it is simple, easy to understand, and effective for both classification and regression tasks. It makes decisions by splitting data into smaller groups and is widely used in business, healthcare, finance, and many other industries for predictive analysis.