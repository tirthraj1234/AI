# Support Vector Machine (SVM) Notes

## Day 5 – Support Vector Machine (SVM)

## What is Support Vector Machine (SVM)?

Support Vector Machine (SVM) is a **Supervised Machine Learning algorithm** mainly used for **classification** problems, but it can also be used for **regression** tasks.

The main objective of SVM is to find the **best decision boundary**, called a **hyperplane**, that separates different classes with the maximum possible margin. A larger margin generally helps the model perform better on new, unseen data.

---

## How Does SVM Work?

SVM works by:

1. Taking the training dataset.
2. Finding the best hyperplane that separates different classes.
3. Maximizing the margin between the classes.
4. Using support vectors (the closest data points) to define the decision boundary.
5. Predicting the class of new data based on which side of the hyperplane it falls.

---

## Types of SVM

### 1. Linear SVM

Linear SVM is used when the data can be separated by a straight line (or hyperplane).

**Example Applications:**

- Spam Email Detection
- Binary Text Classification
- Customer Classification

---

### 2. Non-Linear SVM

Non-Linear SVM is used when the data cannot be separated by a straight line. It uses kernel functions to transform the data into a higher-dimensional space where it becomes separable.

**Example Applications:**

- Face Recognition
- Image Classification
- Handwriting Recognition

---

## Advantages of SVM

- High prediction accuracy.
- Works well with high-dimensional data.
- Effective for both linear and non-linear classification.
- Reduces overfitting by maximizing the margin.
- Can handle complex decision boundaries using kernels.

---

## Limitations of SVM

- Training can be slow for very large datasets.
- Choosing the correct kernel and parameters can be difficult.
- Performance decreases when classes overlap significantly.
- Requires more computational resources for large datasets.

---

## Python Libraries Used

```python
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

---

## Real-World Applications

Support Vector Machine is used in:

- Spam Email Detection
- Face Recognition
- Image Classification
- Medical Diagnosis
- Customer Churn Prediction
- Fraud Detection
- Text Classification
- Handwriting Recognition
- Sentiment Analysis
- Bioinformatics

---

## Key Learnings

Today I learned:

- What Support Vector Machine (SVM) is.
- The objective of SVM.
- How SVM works.
- The difference between Linear and Non-Linear SVM.
- Advantages and limitations of SVM.
- Real-world applications of SVM.
- Basic Python libraries required to implement SVM.

---

## Conclusion

Support Vector Machine (SVM) is a powerful supervised Machine Learning algorithm used mainly for classification tasks. It works by finding the optimal hyperplane that separates different classes while maximizing the margin between them. SVM performs well on high-dimensional data and can solve both linear and non-linear problems using kernel functions. It is widely used in industries such as healthcare, finance, cybersecurity, and computer vision.