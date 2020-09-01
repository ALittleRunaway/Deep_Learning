"""remembering"""
weight = 0.0
goal_pred = 0.8
input = 2
alpha = 0.1

for iteration in range(20):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    weight_delta = input * (pred - goal_pred)
    weight -= weight_delta * alpha
    print(f"Prediction: {pred}; Error: {error}")