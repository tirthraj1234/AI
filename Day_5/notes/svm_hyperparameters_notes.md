# SVM Hyperparameters Notes

## Day 5 – SVM Hyperparameters

## What are Hyperparameters?

Hyperparameters are values that are set before training a Machine Learning model. They control how the model learns from the training data and have a significant impact on its performance.

Unlike model parameters, which are learned automatically during training, hyperparameters are selected by the developer.

Proper hyperparameter tuning helps improve accuracy, reduce overfitting, and build a more reliable model.

---

## Why are Hyperparameters Important?

Hyperparameters help to:

- Improve model accuracy.
- Control model complexity.
- Reduce overfitting and underfitting.
- Improve generalization to new data.
- Optimize training performance.

---

## 1. C Parameter

The **C** parameter is called the **Regularization Parameter**. It controls the balance between maximizing the margin and minimizing classification errors.

### Low C Value

- Creates a wider margin.
- Allows some classification errors.
- Reduces overfitting.
- Better generalization.

Example:

```python
from sklearn.svm import SVC

model = SVC(C=0.1)
```

### High C Value

- Creates a smaller margin.
- Attempts to classify every training sample correctly.
- May increase overfitting.
- More sensitive to noise.

Example:

```python
model = SVC(C=10)
```

---

## 2. Gamma Parameter

The **gamma** parameter determines how much influence each training sample has on the decision boundary.

### Low Gamma

- Creates a smooth decision boundary.
- Better generalization.
- Less complex model.

Example:

```python
model = SVC(kernel="rbf", gamma=0.1)
```

### High Gamma

- Creates a complex decision boundary.
- Fits the training data closely.
- May cause overfitting.

Example:

```python
model = SVC(kernel="rbf", gamma=10)
```

---

## 3. Kernel Parameter

The **kernel** parameter specifies which kernel function SVM should use to classify the data.

Common kernel types include:

- **linear** – Best for linearly separable data.
- **poly** – Suitable for polynomial relationships.
- **rbf** – Best for complex non-linear data.
- **sigmoid** – Similar to neural network activation functions.

Example:

```python
model = SVC(kernel="rbf")
```

---

## Advantages of Hyperparameter Tuning

- Improves prediction accuracy.
- Reduces overfitting.
- Builds more reliable models.
- Improves model performance on unseen data.
- Helps achieve the best balance between bias and variance.

---

## Limitations

- Finding the best values may take time.
- Requires experimentation and validation.
- Incorrect values can reduce model performance.
- Large datasets may increase tuning time.

---

## Python Example

```python
from sklearn.svm import SVC

model = SVC(
    C=1.0,
    gamma="scale",
    kernel="rbf"
)

print(model)
```

---

## Real-World Applications

SVM hyperparameter tuning is used in:

- Spam Email Detection
- Customer Churn Prediction
- Fraud Detection
- Face Recognition
- Image Classification
- Medical Diagnosis
- Sentiment Analysis
- Credit Risk Analysis
- Handwriting Recognition

---

## Key Learnings

Today I learned:

- What hyperparameters are in SVM.
- Why hyperparameter tuning is important.
- The purpose of the **C** parameter.
- The purpose of the **gamma** parameter.
- The purpose of the **kernel** parameter.
- How hyperparameters affect model performance.
- Basic implementation of SVM hyperparameters using Scikit-learn.

---

## Conclusion

Hyperparameters play a vital role in the performance of a Support Vector Machine model. The **C** parameter controls the balance between margin size and classification errors, **gamma** controls the influence of training samples, and the **kernel** determines how the data is transformed for classification. Proper hyperparameter tuning helps create accurate, efficient, and reliable Machine Learning models suitable for real-world applications.