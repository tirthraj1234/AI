# Bagging & Bootstrap Sampling Notes

## Day 4 – Bagging & Bootstrap Sampling

## What is Bagging?

Bagging (Bootstrap Aggregating) is an Ensemble Learning technique that trains multiple Machine Learning models using different random samples of the same dataset. The predictions from all models are combined to produce a more accurate and reliable final result.

Random Forest uses Bagging to create multiple Decision Trees and combines their predictions using majority voting (for classification) or averaging (for regression).

---

## What is Bootstrap Sampling?

Bootstrap Sampling is a technique used to create multiple random samples from the original dataset **with replacement**.

"With replacement" means that after selecting a data record, it is placed back into the dataset before the next selection. As a result, the same record can be selected multiple times, while some records may not be selected at all.

---

## How Does Bagging Work?

1. Start with the original training dataset.
2. Create multiple bootstrap samples using random sampling with replacement.
3. Train a separate Decision Tree on each bootstrap sample.
4. Each Decision Tree makes its own prediction.
5. Combine all predictions.
   - **Classification:** Majority Voting
   - **Regression:** Average Prediction

---

## Example of Bootstrap Sampling

Original Dataset:

```
[1, 2, 3, 4, 5]
```

Bootstrap Sample:

```
[2, 5, 2, 1, 4]
```

In this example:

- Record **2** appears twice.
- Record **3** does not appear.
- This is normal because sampling is performed with replacement.

---

## Why Does Random Forest Use Bagging?

Random Forest uses Bagging because it:

- Reduces overfitting.
- Improves prediction accuracy.
- Increases model stability.
- Reduces the effect of noisy data.
- Produces better generalization on unseen data.

---

## Advantages of Bagging

- Improves prediction accuracy.
- Reduces overfitting.
- Increases model stability.
- Handles large datasets effectively.
- Works well with noisy data.
- Easy to parallelize because each model is trained independently.

---

## Limitations of Bagging

- Requires more memory.
- Training is slower than using a single model.
- More computationally expensive.
- Harder to interpret multiple models.

---

## Difference Between Bagging and Boosting

| Bagging | Boosting |
|---------|----------|
| Models are trained independently. | Models are trained sequentially. |
| Uses bootstrap sampling. | Focuses on correcting previous model errors. |
| Reduces variance. | Reduces both bias and variance. |
| Example: Random Forest | Examples: XGBoost, AdaBoost, LightGBM, CatBoost |

---

## Real-World Applications

Bagging is used in:

- Employee Salary Prediction
- Loan Approval Systems
- Fraud Detection
- Customer Churn Prediction
- Medical Diagnosis
- Credit Risk Analysis
- Insurance Risk Prediction
- Product Recommendation Systems

---

## Python Example

```python
import random

employees = [1, 2, 3, 4, 5]

bootstrap_sample = random.choices(employees, k=5)

print("Original Dataset:", employees)
print("Bootstrap Sample:", bootstrap_sample)
```

---

## Key Learnings

Today I learned:

- What Bagging is.
- What Bootstrap Sampling is.
- The meaning of sampling with replacement.
- How Random Forest uses Bagging.
- The advantages and limitations of Bagging.
- The difference between Bagging and Boosting.
- A basic Python implementation of Bootstrap Sampling.

---

## Conclusion

Bagging is an important Ensemble Learning technique that improves the performance of Machine Learning models by combining predictions from multiple models trained on different bootstrap samples. Random Forest uses Bagging to create multiple Decision Trees, resulting in higher accuracy, better stability, and reduced overfitting compared to a single Decision Tree.