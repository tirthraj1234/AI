import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

df = pd.read_csv("Day_3/dataset/employee_promotion.csv")# load dataset

print(df.head())

# separating features and target
X = df[["Age", "Experience", "Performance"]]

y = df["Promotion"]

# splitting dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# creating decision tree model
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

# train the model
model.fit(X_train, y_train)

# making predictions
y_pred = model.predict(X_test)

print("Predictions:", y_pred)

# evaluating  the model
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print("\nConfusion Matrix")

print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")

print(classification_report(y_test, y_pred))

# predicting a new employee
new_employee = [[34, 6, 4]]

prediction = model.predict(new_employee)

if prediction[0] == 1:
    print("Employee is likely to be promoted.")
else:
    print("Employee is not likely to be promoted.")

# visualizing the decision tree
plt.figure(figsize=(10, 6))

plot_tree(
    model,
    feature_names=["Age", "Experience", "Performance"],
    class_names=["No Promotion", "Promotion"],
    filled=True
)

plt.show()