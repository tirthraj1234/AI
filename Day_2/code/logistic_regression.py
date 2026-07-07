import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

df = pd.read_csv("Day_2/dataset/customer_purchase.csv")# read dataset

print(df.head())

# separate feature and target
X = df[["Age", "Salary"]]

y = df["Purchased"]

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()# create logistic regression model

model.fit(X_train, y_train)# train the model

y_pred = model.predict(X_test)# predict

print(y_pred)

accuracy = accuracy_score(y_test, y_pred)# accuracy

print("Accuracy:", accuracy)

cm = confusion_matrix(y_test, y_pred)# confusion matrix

print("\nConfusion Matrix")

print(cm)

print("\nClassification Report")

print(classification_report(y_test, y_pred))# classification report

# predict new customer
new_customer = [[33, 48000]]

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("Customer is likely to purchase.")
else:
    print("Customer is not likely to purchase.")

