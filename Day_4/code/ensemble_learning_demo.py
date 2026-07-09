models = ["Decision Tree", "Decision Tree", "Decision Tree"]

predictions = ["Approve", "Approve", "Reject"]

final_prediction = max(set(predictions), key=predictions.count)

print("Predictions:", predictions)
print("Final Prediction:", final_prediction)