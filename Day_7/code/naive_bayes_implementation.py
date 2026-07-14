# import libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# load dataset
df = pd.read_csv("Day_7/dataset/student_result.csv")

print(df.head())

# separate feature and target
X = df[[
    "StudyHours",
    "Attendance",
    "Assignments"
]]

y = df["Result"]

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# create naive bayes model
model = GaussianNB()

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

# predict a new student result 
new_student = [[5, 78, 6]]

prediction = model.predict(new_student)

print("Prediction:", prediction[0])

