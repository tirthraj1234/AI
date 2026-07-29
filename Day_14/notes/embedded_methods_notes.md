# Embedded Methods Notes

## Day 14 – Phase 4: Embedded Methods

# Introduction

Embedded Methods are Feature Selection techniques in which feature selection is performed automatically during the training of a Machine Learning model. Unlike Filter Methods, which rely on statistical tests, and Wrapper Methods, which repeatedly train models, Embedded Methods integrate feature selection directly into the learning algorithm.

These methods provide a balance between computational efficiency and prediction accuracy, making them widely used in real-world Machine Learning applications.

---

# Objective of Embedded Methods

The primary objectives are:

- Select important features during model training.
- Improve prediction accuracy.
- Reduce overfitting.
- Eliminate irrelevant features.
- Build efficient Machine Learning models.
- Reduce computational complexity.
- Improve model interpretability.

---

# What are Embedded Methods?

Embedded Methods combine feature selection and model training into a single process.

The algorithm automatically determines which features contribute most to the prediction task while fitting the model.

Unlike Wrapper Methods, Embedded Methods do not require repeated training on multiple feature subsets.

---

# Characteristics of Embedded Methods

- Feature selection occurs during model training.
- Model-dependent approach.
- Faster than Wrapper Methods.
- More accurate than many Filter Methods.
- Considers interactions between features.
- Produces optimized feature subsets.

---

# Lasso Regression (L1 Regularization)

## Definition

Lasso (Least Absolute Shrinkage and Selection Operator) is a regression technique that adds an L1 regularization penalty to the model.

It reduces the coefficients of less important features and can shrink some coefficients exactly to zero.

Features with zero coefficients are automatically removed from the model.

---

## Working Principle

1. Train the regression model.
2. Apply the L1 penalty.
3. Shrink feature coefficients.
4. Remove features with zero coefficients.
5. Keep only the most important features.

---

## Advantages

- Performs automatic feature selection.
- Produces simpler models.
- Reduces overfitting.
- Easy to interpret.

---

## Limitations

- May remove useful correlated features.
- Sensitive to the choice of the alpha parameter.

---

# Ridge Regression (L2 Regularization)

## Definition

Ridge Regression adds an L2 regularization penalty to the model.

Instead of removing features, Ridge reduces the magnitude of feature coefficients.

All features remain in the model, but less important features receive smaller coefficients.

---

## Working Principle

1. Train the regression model.
2. Apply the L2 penalty.
3. Shrink coefficients.
4. Keep all features.

---

## Advantages

- Handles multicollinearity effectively.
- Reduces overfitting.
- Produces stable models.

---

## Limitations

- Does not perform feature elimination.
- All features remain in the final model.

---

# Elastic Net

## Definition

Elastic Net combines the strengths of Lasso and Ridge Regression by using both L1 and L2 regularization.

It performs feature selection while maintaining model stability.

---

## Working Principle

1. Train the model.
2. Apply both L1 and L2 penalties.
3. Select important features.
4. Shrink coefficients of less important features.

---

## Advantages

- Performs feature selection.
- Handles correlated features better than Lasso.
- Produces stable models.
- Reduces overfitting.

---

## Limitations

- Requires tuning multiple hyperparameters.
- More complex than Lasso or Ridge alone.

---

# Decision Tree Feature Importance

## Definition

Decision Trees automatically calculate the importance of each feature while building the tree.

Features that contribute more to reducing impurity receive higher importance scores.

---

## Working Principle

1. Split the data using the best feature.
2. Measure impurity reduction.
3. Assign importance scores.
4. Rank features based on importance.

---

## Advantages

- Automatic feature ranking.
- Easy to interpret.
- Supports non-linear relationships.
- Works with numerical and categorical data.

---

## Limitations

- Can be biased toward features with many unique values.
- Results may vary with different tree structures.

---

# Random Forest Feature Importance

## Definition

Random Forest calculates feature importance by averaging the contribution of each feature across many Decision Trees.

This provides more reliable importance scores than a single Decision Tree.

---

## Working Principle

1. Train multiple Decision Trees.
2. Calculate feature importance in each tree.
3. Average the importance scores.
4. Rank features.

---

## Advantages

- Stable feature ranking.
- Handles large datasets.
- Supports complex relationships.
- Reduces overfitting.

---

## Limitations

- Less interpretable than a single Decision Tree.
- Requires more computational resources.

---

# Comparison of Embedded Methods

| Method | Performs Feature Selection | Best Use Case |
|----------|---------------------------|---------------|
| Lasso Regression | Yes | Selecting important features |
| Ridge Regression | No | Handling multicollinearity |
| Elastic Net | Yes | Correlated features |
| Decision Tree | Yes | Feature ranking |
| Random Forest | Yes | Stable feature importance |

---

# Advantages of Embedded Methods

- High prediction accuracy.
- Faster than Wrapper Methods.
- Automatic feature selection.
- Handles feature interactions.
- Reduces overfitting.
- Produces optimized feature subsets.
- Efficient for medium and large datasets.

---

# Limitations of Embedded Methods

- Algorithm-dependent.
- Different models may select different features.
- Requires parameter tuning.
- Less flexible than Filter Methods.

---

# Best Practices

- Scale numerical features before using regularization methods.
- Tune alpha and l1_ratio using Cross Validation.
- Compare multiple Embedded Methods.
- Validate feature importance using different models.
- Combine with domain knowledge before removing features.

---

# Real-World Applications

Embedded Methods are widely used in:

- Employee salary prediction
- Employee attrition prediction
- Customer churn prediction
- Medical diagnosis
- Credit risk analysis
- Fraud detection
- House price prediction
- Stock market analysis
- Recommendation systems
- Predictive maintenance

---

# Key Learnings

Today I learned:

- The concept of Embedded Methods.
- How Lasso performs feature selection.
- How Ridge reduces coefficient values.
- How Elastic Net combines L1 and L2 regularization.
- How Decision Trees calculate feature importance.
- How Random Forest ranks features.
- Practical implementation using Scikit-learn.

---

# Interview Questions

1. What are Embedded Methods?
2. How do Embedded Methods differ from Filter and Wrapper Methods?
3. What is Lasso Regression?
4. What is Ridge Regression?
5. What is Elastic Net?
6. Why does Lasso perform feature selection?
7. How is feature importance calculated in Decision Trees?
8. Why is Random Forest Feature Importance more stable?
9. What are the advantages of Embedded Methods?
10. Where are Embedded Methods used in real-world applications?

---

# Conclusion

Embedded Methods are efficient Feature Selection techniques that perform feature selection during model training. Algorithms such as Lasso Regression, Elastic Net, Decision Trees, and Random Forest automatically identify the most relevant features while improving model performance and reducing overfitting. These methods are widely used because they provide an excellent balance between computational efficiency and prediction accuracy.