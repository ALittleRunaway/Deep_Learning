"""Обучение просто уменьшает ошибку"""
weight, goal_pred, input = (0.0, 0.8, 0.5)

for iteration in range(4):

    pred = input * weight
    # error = (pred - goal_pred) ** 2
    error = ((input * weight) - goal_pred) ** 2
    delta = (pred - goal_pred)
    weight_delta = input * delta
    weight = weight - weight_delta
    print(f'Error: {error}; Prediction: {pred}; Weight: {weight}')
