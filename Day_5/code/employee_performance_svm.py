# import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# load dataset
df = pd.read_csv("Day_5/dataset/employee_performance.csv")

print(df.head())

# separating feature and target
X = df[[
    "Experience",
    "TrainingHours",
    "ProjectsCompleted",
    "PerformanceScore"
]]

y = df["HighPerformer"]

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# creating svm model
model = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale"
)

# train model
model.fit(X_train, y_train)

print("Model trained successfully.")

# make predictions
y_pred = model.predict(X_test)

print("Predictions:")

print(y_pred)

# evaluating the model
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print("\nConfusion Matrix")

print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")

print(classification_report(y_test, y_pred))

# predicting a new employee
new_employee = [[6, 45, 7, 84]]

prediction = model.predict(new_employee)

if prediction[0] == 1:
    print("High Performer")
else:
    print("Low Performer")

