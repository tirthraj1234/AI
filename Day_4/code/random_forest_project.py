import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
import matplotlib.pyplot as plt

#load dataset
df = pd.read_csv("Day_4/dataset/employee_salary.csv")

print(df.head())

#separate feature and target
X = df[["Age", "Experience", "Education", "Performance"]]

y = df["Salary"]

#split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#creating random forest model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)

#train the model
model.fit(X_train, y_train)

#make predictions
y_pred = model.predict(X_test)

print("Predictions:", y_pred)

#evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

#feature 
importance = model.feature_importances_

features = X.columns

for feature, score in zip(features, importance):
    print(feature, ":", round(score, 3))

#feature chart
plt.figure(figsize=(8,5))

plt.bar(features, importance)

plt.title("Feature Importance")

plt.xlabel("Features")

plt.ylabel("Importance Score")

plt.show()

#predict new employee
new_employee = [[35, 8, 3, 5]]

prediction = model.predict(new_employee)

if prediction[0] == 1:
    print("High Salary")
else:
    print("Low Salary")

