# Random Forest Notes

## Day 4 – Random Forest

## What is Random Forest?

Random Forest is a **Supervised Machine Learning algorithm** used for both **classification** and **regression** tasks. It is an ensemble learning algorithm that combines the predictions of multiple Decision Trees to produce a more accurate and reliable result.

Instead of relying on a single Decision Tree, Random Forest creates many Decision Trees and combines their predictions using voting (for classification) or averaging (for regression).

---

## Why is it Called Random Forest?

The algorithm is called **Random Forest** because:

- **Random**: Each Decision Tree is trained using a random sample of the dataset and a random subset of features.
- **Forest**: The model consists of many Decision Trees working together.

This randomness helps improve accuracy and reduces overfitting.

---

## How Does Random Forest Work?

1. Select random samples from the training dataset.
2. Build multiple Decision Trees using these samples.
3. Each tree makes its own prediction.
4. Combine the predictions of all trees.
   - Classification: Majority Voting
   - Regression: Average Prediction
5. Return the final prediction.

---

## Types of Random Forest

### 1. Random Forest Classifier

Used when the target variable is categorical.

Examples:

- Spam Detection
- Customer Churn Prediction
- Loan Approval
- Employee Promotion

---

### 2. Random Forest Regressor

Used when the target variable is continuous.

Examples:

- House Price Prediction
- Sales Forecasting
- Salary Prediction
- Stock Price Prediction

---

## Advantages of Random Forest

- High prediction accuracy.
- Reduces overfitting compared to a single Decision Tree.
- Works well with large datasets.
- Handles both numerical and categorical data.
- Supports both classification and regression tasks.
- Provides feature importance.
- Handles missing values effectively.
- Robust to noise in the data.

---

## Limitations of Random Forest

- Slower than a single Decision Tree.
- Requires more memory.
- Difficult to interpret because it contains many trees.
- Training time increases as the number of trees increases.

---

## Python Libraries Used

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

---

## Real-World Applications

Random Forest is widely used in:

- Employee Salary Prediction
- Loan Approval Systems
- Fraud Detection
- Credit Risk Analysis
- Customer Churn Prediction
- Medical Diagnosis
- Disease Prediction
- Product Recommendation Systems
- Stock Market Prediction
- Insurance Risk Analysis

---

## Key Learnings

Today I learned:

- What Random Forest is.
- Why it is called Random Forest.
- How Random Forest works.
- Difference between Random Forest Classifier and Regressor.
- Advantages and limitations of Random Forest.
- Real-world applications of Random Forest.
- Basic Python libraries required to implement Random Forest.

---

## Conclusion

Random Forest is one of the most powerful and widely used Machine Learning algorithms. By combining multiple Decision Trees, it produces more accurate and stable predictions while reducing overfitting. It is suitable for both classification and regression problems and is commonly used in business, healthcare, finance, and many other industries.