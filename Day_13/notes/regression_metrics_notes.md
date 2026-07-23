# Regression Metrics Notes

## Day 13 – Phase 2: Regression Evaluation Metrics

# Introduction

Regression Evaluation Metrics are statistical measures used to evaluate the performance of regression machine learning models. These metrics compare the predicted values with the actual values and help determine how accurately a model makes predictions.

Different metrics focus on different aspects of prediction error. Selecting the appropriate evaluation metric depends on the problem, business requirements, and the importance of prediction accuracy.

---

# Objective of Regression Evaluation Metrics

The objectives of regression evaluation metrics are:

- Measure prediction accuracy.
- Compare different regression models.
- Identify prediction errors.
- Improve model performance.
- Select the best regression model.
- Evaluate model reliability.

---

# What are Regression Evaluation Metrics?

Regression Evaluation Metrics are mathematical formulas used to calculate the difference between actual values and predicted values.

A regression model is considered better when prediction errors are smaller and evaluation scores indicate better performance.

---

# Mean Absolute Error (MAE)

## Definition

Mean Absolute Error (MAE) measures the average absolute difference between actual values and predicted values.

It treats every error equally without considering its direction.

### Formula

MAE = (Σ |Actual − Predicted|) / n

where:

- Actual = True value
- Predicted = Model prediction
- n = Number of observations

### Characteristics

- Easy to understand.
- Uses absolute differences.
- Same unit as the target variable.
- Less sensitive to outliers than MSE.

### Advantages

- Simple interpretation.
- Easy to calculate.
- Works well with linear errors.
- Less affected by extreme values.

### Limitations

- Does not penalize large errors strongly.
- May not highlight significant prediction mistakes.

---

# Mean Squared Error (MSE)

## Definition

Mean Squared Error (MSE) measures the average squared difference between actual and predicted values.

Since errors are squared, larger errors receive a much higher penalty.

### Formula

MSE = (Σ (Actual − Predicted)²) / n

### Characteristics

- Always positive.
- Penalizes large errors.
- Widely used during model optimization.

### Advantages

- Useful for optimization algorithms.
- Strongly penalizes large prediction errors.
- Differentiable and mathematically convenient.

### Limitations

- Sensitive to outliers.
- Unit becomes squared, making interpretation less intuitive.

---

# Root Mean Squared Error (RMSE)

## Definition

Root Mean Squared Error (RMSE) is the square root of Mean Squared Error.

It converts the error back to the original unit of the target variable.

### Formula

RMSE = √MSE

### Characteristics

- Same unit as the target variable.
- Penalizes large errors.
- Easy to interpret.

### Advantages

- Commonly used in regression problems.
- Provides meaningful error values.
- Highlights significant prediction errors.

### Limitations

- Sensitive to outliers.
- Large errors have greater influence.

---

# R² Score (Coefficient of Determination)

## Definition

R² Score measures how well the regression model explains the variation in the target variable.

Its value generally ranges from 0 to 1.

### Interpretation

- R² = 1 → Perfect prediction
- R² = 0 → Model explains no variation
- Higher R² indicates better performance

### Characteristics

- Measures goodness of fit.
- Higher values indicate better models.
- Commonly used for comparing regression models.

### Advantages

- Easy to compare models.
- Indicates explained variance.
- Widely accepted metric.

### Limitations

- Does not indicate prediction error directly.
- Can increase simply by adding more features.

---

# Adjusted R² Score

## Definition

Adjusted R² improves R² by considering the number of features used in the model.

It penalizes unnecessary features that do not improve model performance.

### Why is Adjusted R² Needed?

Adding more features often increases the R² Score, even if those features are not useful.

Adjusted R² solves this problem by rewarding only meaningful features.

### Characteristics

- More reliable than R².
- Penalizes unnecessary variables.
- Useful for multiple regression.

### Advantages

- Prevents overestimating model performance.
- Better for comparing models with different numbers of features.

### Limitations

- Slightly more complex to calculate.
- Mainly useful for multiple regression.

---

# Comparison of Regression Metrics

| Metric | Lower is Better | Sensitive to Outliers | Unit |
|---------|-----------------|-----------------------|------|
| MAE | Yes | Low | Original Unit |
| MSE | Yes | High | Squared Unit |
| RMSE | Yes | High | Original Unit |
| R² Score | No (Higher is Better) | No | Unitless |
| Adjusted R² | No (Higher is Better) | No | Unitless |

---

# When to Use Each Metric

### Use MAE when:

- Equal importance is given to all errors.
- You need an easily interpretable metric.

### Use MSE when:

- Large errors should be penalized more heavily.
- Training optimization algorithms.

### Use RMSE when:

- Error should be expressed in the original unit.
- Large prediction errors are important.

### Use R² Score when:

- Comparing regression models.
- Measuring explained variance.

### Use Adjusted R² when:

- Multiple independent variables are used.
- Comparing models with different numbers of features.

---

# Advantages of Regression Evaluation Metrics

- Measure prediction quality.
- Help compare models.
- Improve model selection.
- Detect prediction errors.
- Support performance optimization.
- Provide objective evaluation.

---

# Limitations

- No single metric is suitable for every problem.
- Some metrics are sensitive to outliers.
- Different metrics may rank models differently.
- Interpretation depends on the application.

---

# Best Practices

- Evaluate models using multiple metrics.
- Do not rely on only one evaluation metric.
- Compare training and testing performance.
- Use Adjusted R² for multiple regression.
- Consider business requirements when selecting metrics.

---

# Real-World Applications

Regression evaluation metrics are used in:

- House Price Prediction
- Sales Forecasting
- Stock Price Prediction
- Demand Forecasting
- Weather Prediction
- Medical Cost Estimation
- Energy Consumption Prediction
- Employee Salary Prediction
- Insurance Premium Prediction
- Financial Analysis

---

# Key Learnings

Today I learned:

- The importance of regression evaluation metrics.
- How MAE measures average prediction error.
- Why MSE penalizes large errors.
- The purpose of RMSE.
- How R² measures explained variance.
- Why Adjusted R² is preferred for multiple regression.
- The strengths and limitations of each regression metric.

---

# Interview Questions

1. What are Regression Evaluation Metrics?
2. What is Mean Absolute Error (MAE)?
3. What is the difference between MAE and MSE?
4. Why is RMSE commonly used?
5. What does R² Score indicate?
6. Why is Adjusted R² better than R²?
7. Which metric is most sensitive to outliers?
8. When should MAE be preferred?
9. What are the limitations of MSE?
10. Why should multiple evaluation metrics be used?

---

# Conclusion

Regression Evaluation Metrics are essential for assessing the performance of regression models. Metrics such as MAE, MSE, RMSE, R² Score, and Adjusted R² provide different perspectives on model accuracy and prediction quality. Using multiple evaluation metrics allows data scientists to better understand model behavior, compare algorithms, and select the most suitable model for real-world applications.