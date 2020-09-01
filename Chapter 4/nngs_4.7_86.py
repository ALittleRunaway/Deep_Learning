"""Ищем нижнюю точку на графике"""
weight, goal_pred, input = (0.0, 0.8, 1.1)

for iteration in range(4):
    print(f'-----\nWeight: {weight}')
    pred = input * weight
    error = (pred - goal_pred) ** 2
    # error = ((input * weight) - goal_pred) ** 2
    delta = (pred - goal_pred)
    weight_delta = input * delta
    weight = weight - weight_delta
    print(f'Error: {error}; Prediction: {pred};')
    print(f'Delta: {delta}; Weight Delta: {weight_delta};')