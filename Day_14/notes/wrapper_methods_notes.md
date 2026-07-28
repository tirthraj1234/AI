# Wrapper Methods Notes

## Day 14 – Phase 3: Wrapper Methods

# Introduction

Wrapper Methods are Feature Selection techniques that evaluate different combinations of features by repeatedly training and testing a Machine Learning model. Unlike Filter Methods, Wrapper Methods use the performance of a learning algorithm to determine which features are the most useful.

Since the model itself is involved in feature selection, Wrapper Methods generally produce better feature subsets. However, they require more computational time because the model is trained multiple times.

---

# Objective of Wrapper Methods

The main objectives of Wrapper Methods are:

- Select the best subset of features.
- Improve prediction accuracy.
- Remove unnecessary features.
- Reduce overfitting.
- Optimize model performance.
- Identify feature interactions.
- Build more reliable Machine Learning models.

---

# What are Wrapper Methods?

Wrapper Methods search for the best combination of features by repeatedly training a Machine Learning model.

Instead of using only statistical measures, these methods evaluate how different feature subsets affect model performance.

The subset that gives the highest prediction accuracy is selected.

---

# Characteristics of Wrapper Methods

- Model-dependent.
- Computationally expensive.
- High feature selection accuracy.
- Considers interactions between features.
- Suitable for small and medium-sized datasets.
- Requires repeated model training.

---

# Forward Selection

## Definition

Forward Selection begins with an empty feature set and adds one feature at a time.

At each step, the feature that provides the greatest improvement in model performance is added.

The process continues until no significant improvement is observed or the desired number of features is selected.

---

## Working Principle

1. Start with no features.
2. Train the model using each feature individually.
3. Select the best-performing feature.
4. Add another feature that improves performance the most.
5. Repeat until the stopping criterion is reached.

---

## Advantages

- Easy to understand.
- Faster than exhaustive search.
- Avoids unnecessary features.
- Produces good feature subsets.

---

## Limitations

- May miss the globally optimal feature combination.
- Computationally expensive for many features.

---

# Backward Elimination

## Definition

Backward Elimination starts with all available features and removes the least useful feature one at a time.

After each removal, the model is retrained and evaluated.

The process continues until only the most important features remain.

---

## Working Principle

1. Start with all features.
2. Train the model.
3. Remove the least important feature.
4. Retrain the model.
5. Repeat until the desired subset is obtained.

---

## Advantages

- Evaluates all features initially.
- Often finds strong feature subsets.

---

## Limitations

- Slow for datasets with many features.
- Requires multiple model evaluations.

---

# Recursive Feature Elimination (RFE)

## Definition

Recursive Feature Elimination (RFE) is one of the most widely used Wrapper Methods.

It repeatedly trains a model and removes the least important feature until the required number of features remains.

---

## Working Principle

1. Train the model.
2. Calculate feature importance.
3. Remove the least important feature.
4. Retrain the model.
5. Repeat until the required number of features is selected.

---

## Advantages

- Produces highly relevant feature subsets.
- Works with many Machine Learning algorithms.
- Easy to use with Scikit-learn.

---

## Limitations

- Computationally expensive.
- Slower than Filter Methods.

---

# Sequential Feature Selection (SFS)

## Definition

Sequential Feature Selection automatically selects features based on model performance.

It has two approaches:

### Forward Sequential Selection

- Starts with no features.
- Adds features one by one.

### Backward Sequential Selection

- Starts with all features.
- Removes features one by one.

---

## Advantages

- Flexible feature selection.
- Produces high-quality feature subsets.
- Considers model performance during selection.

---

## Limitations

- Requires repeated training.
- Computationally intensive for large datasets.

---

# Comparison of Wrapper Methods

| Method | Starting Point | Process | Best Use Case |
|----------|----------------|----------|---------------|
| Forward Selection | No features | Add features | Medium-sized datasets |
| Backward Elimination | All features | Remove features | Small datasets |
| RFE | All features | Recursive removal | General Machine Learning tasks |
| Sequential Feature Selection | Configurable | Add or remove features | Flexible feature selection |

---

# Advantages of Wrapper Methods

- High prediction accuracy.
- Better feature selection.
- Detects feature interactions.
- Optimizes model performance.
- Produces reliable feature subsets.
- Model-specific optimization.

---

# Limitations of Wrapper Methods

- High computational cost.
- Slower than Filter Methods.
- Not suitable for very large datasets.
- Requires repeated model training.

---

# Best Practices

- Apply Wrapper Methods after preprocessing.
- Use Cross Validation for reliable evaluation.
- Compare multiple Wrapper Methods.
- Avoid excessive feature removal.
- Balance model performance and computational cost.

---

# Real-World Applications

Wrapper Methods are used in:

- Healthcare diagnosis
- Disease prediction
- Employee performance prediction
- Employee salary prediction
- Customer churn prediction
- Credit risk analysis
- Fraud detection
- Image classification
- Text classification
- Recommendation systems
- Financial forecasting

---

# Key Learnings

Today I learned:

- The concept of Wrapper Methods.
- The difference between Forward Selection and Backward Elimination.
- The working of Recursive Feature Elimination (RFE).
- Sequential Feature Selection techniques.
- Advantages and limitations of Wrapper Methods.
- Practical implementation using Scikit-learn.

---

# Interview Questions

1. What are Wrapper Methods?
2. How do Wrapper Methods differ from Filter Methods?
3. What is Forward Selection?
4. What is Backward Elimination?
5. Explain Recursive Feature Elimination (RFE).
6. What is Sequential Feature Selection?
7. Why are Wrapper Methods computationally expensive?
8. What are the advantages of Wrapper Methods?
9. What are the limitations of Wrapper Methods?
10. Where are Wrapper Methods used in real-world applications?

---

# Conclusion

Wrapper Methods are powerful Feature Selection techniques that evaluate feature subsets by repeatedly training Machine Learning models. Although they require more computational resources than Filter Methods, they often produce more accurate and reliable feature subsets. Techniques such as Forward Selection, Backward Elimination, Recursive Feature Elimination (RFE), and Sequential Feature Selection are widely used to improve model performance and reduce unnecessary features in practical Machine Learning applications.