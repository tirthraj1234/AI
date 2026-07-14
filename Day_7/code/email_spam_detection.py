# import libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# load dataset
df = pd.read_csv("Day_7/dataset/spam_dataset.csv")

print(df.head())

# separate feature and target
X = df["Message"]

y = df["Label"]

# convert text to numbers
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(X)

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# create model
model = MultinomialNB()

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

# predict a new email
new_email = [
    "Congratulations! You have won a free laptop."
]

new_email = vectorizer.transform(new_email)

prediction = model.predict(new_email)

print("Prediction:", prediction[0])

