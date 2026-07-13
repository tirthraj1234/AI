# import libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# load dataset
df = pd.read_csv("Day_6/dataset/employee_attrition.csv")

print(df.head())

# separate feature and target
X = df[[
    "Experience",
    "Age",
    "Salary",
    "TrainingHours",
    "PerformanceScore"
]]

y = df["Attrition"]

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# create KNN model
model = KNeighborsClassifier(
    n_neighbors=5,
    metric="minkowski"
)

# train model
model.fit(X_train, y_train)

print("Model trained successfully.")

# make prediction
y_pred = model.predict(X_test)

print("Predictions:")
print(y_pred)

# evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# predict a new employee
new_employee = [[3, 27, 36000, 25, 70]]

new_employee = scaler.transform(new_employee)

prediction = model.predict(new_employee)

if prediction[0] == 1:
    print("Employee is likely to Leave the Company.")
else:
    print("Employee is likely to Stay in the Company.")

