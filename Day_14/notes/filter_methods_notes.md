# Filter Methods Notes

## Day 14 – Phase 2: Filter Methods

# Introduction

Filter Methods are one of the most commonly used Feature Selection techniques in Machine Learning. They evaluate the importance of features using statistical measures before training a machine learning model. Since these methods are independent of any specific algorithm, they are fast, computationally efficient, and suitable for high-dimensional datasets.

Filter Methods help reduce dataset size, remove irrelevant features, and improve model performance.

---

# Objective of Filter Methods

The main objectives are:

- Select relevant features.
- Remove irrelevant and redundant features.
- Reduce dimensionality.
- Improve model performance.
- Reduce computational cost.
- Speed up model training.
- Improve model interpretability.

---

# What are Filter Methods?

Filter Methods select features based on statistical characteristics rather than machine learning model performance.

These methods rank features according to statistical scores, and the highest-ranked features are selected for training.

Unlike Wrapper Methods, Filter Methods do not repeatedly train a model.

---

# Characteristics of Filter Methods

- Independent of machine learning algorithms.
- Fast execution.
- Low computational cost.
- Suitable for large datasets.
- Easy to implement.
- Good for preprocessing before model training.

---

# Variance Threshold

## Definition

Variance Threshold removes features whose variance is below a predefined threshold.

Features with very little variation usually provide little useful information for prediction.

---

## Working Principle

1. Calculate the variance of each feature.
2. Compare the variance with a threshold value.
3. Remove features below the threshold.
4. Keep features above the threshold.

---

## Advantages

- Very fast.
- Removes constant features.
- Reduces dataset size.
- Easy implementation.

---

## Limitations

- Ignores the target variable.
- High variance does not always imply high importance.

---

# Correlation-Based Feature Selection

## Definition

Correlation measures the relationship between two numerical variables.

Highly correlated features often provide similar information, so one of them can be removed to reduce redundancy.

---

## Correlation Values

- +1 → Perfect positive correlation.
- 0 → No correlation.
- -1 → Perfect negative correlation.

---

## Advantages

- Removes redundant features.
- Improves efficiency.
- Easy to interpret.

---

## Limitations

- Detects only linear relationships.
- Threshold selection may vary depending on the dataset.

---

# Chi-Square Test

## Definition

The Chi-Square (χ²) Test measures the relationship between categorical input features and a categorical target variable.

Features with higher Chi-Square scores are considered more important.

---

## Working Process

1. Calculate observed and expected frequencies.
2. Compute the Chi-Square statistic.
3. Rank features.
4. Select the top-ranking features.

---

## Advantages

- Fast execution.
- Effective for classification problems.
- Simple feature ranking.

---

## Limitations

- Works only with non-negative values.
- Suitable mainly for categorical data.

---

# ANOVA F-Test

## Definition

ANOVA (Analysis of Variance) evaluates whether numerical feature values differ significantly across target classes.

Higher F-scores indicate stronger relationships between a feature and the target.

---

## Working Principle

1. Calculate variance between groups.
2. Calculate variance within groups.
3. Compute the F-score.
4. Rank features based on F-score.

---

## Advantages

- Suitable for continuous features.
- Fast and efficient.
- Easy feature ranking.

---

## Limitations

- Assumes normally distributed data.
- Primarily detects linear differences.

---

# Mutual Information

## Definition

Mutual Information measures how much information a feature provides about the target variable.

It can detect both linear and non-linear relationships.

---

## Working Principle

1. Measure dependency between feature and target.
2. Assign an importance score.
3. Rank features.
4. Select the most informative features.

---

## Advantages

- Detects complex relationships.
- Works with numerical and categorical features.
- Effective for many real-world datasets.

---

## Limitations

- More computationally expensive than correlation.
- Scores may be harder to interpret.

---

# Comparison of Filter Methods

| Method | Feature Type | Uses Target Variable | Best Use Case |
|----------|--------------|----------------------|---------------|
| Variance Threshold | Numerical | No | Remove low-variance features |
| Correlation | Numerical | No | Remove redundant features |
| Chi-Square | Categorical | Yes | Classification problems |
| ANOVA F-Test | Numerical | Yes | Continuous features in classification |
| Mutual Information | Numerical & Categorical | Yes | Detect linear and non-linear relationships |

---

# Advantages of Filter Methods

- Fast execution.
- Independent of machine learning algorithms.
- Easy to implement.
- Reduces overfitting.
- Improves training speed.
- Suitable for large datasets.
- Removes irrelevant features.
- Reduces dimensionality.

---

# Limitations of Filter Methods

- Ignore feature interactions.
- May not select the optimal feature subset.
- Depend only on statistical measures.
- Some methods have assumptions about the data.

---

# Best Practices

- Clean and preprocess data before feature selection.
- Remove duplicate features.
- Combine Filter Methods with Wrapper or Embedded Methods when appropriate.
- Validate selected features using Cross Validation.
- Compare multiple feature selection techniques before choosing one.

---

# Real-World Applications

Filter Methods are widely used in:

- Medical diagnosis.
- Employee performance prediction.
- Employee salary prediction.
- Customer churn prediction.
- Loan approval systems.
- Fraud detection.
- Credit risk analysis.
- Image classification.
- Text classification.
- Stock market prediction.
- Recommendation systems.

---

# Key Learnings

Today I learned:

- The concept of Filter Methods.
- How Variance Threshold removes low-variance features.
- How Correlation identifies redundant features.
- How the Chi-Square Test ranks categorical features.
- How ANOVA F-Test evaluates numerical features.
- How Mutual Information measures feature importance.
- The advantages and limitations of different Filter Methods.

---

# Interview Questions

1. What are Filter Methods in Feature Selection?
2. Why are Filter Methods considered fast?
3. What is the purpose of Variance Threshold?
4. How does Correlation-Based Feature Selection work?
5. When should the Chi-Square Test be used?
6. What is the ANOVA F-Test?
7. What is Mutual Information?
8. Which Filter Method detects non-linear relationships?
9. What are the advantages of Filter Methods?
10. What are the limitations of Filter Methods?

---

# Conclusion

Filter Methods are efficient Feature Selection techniques that identify important features using statistical measures before model training. Methods such as Variance Threshold, Correlation Analysis, Chi-Square Test, ANOVA F-Test, and Mutual Information help reduce dimensionality, improve model performance, and decrease computational cost. They are widely used as the first step in many machine learning workflows because of their speed, simplicity, and effectiveness.