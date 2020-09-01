"""Градиентный спуск"""
weight = 0.5
input = 0.5
goal_pred = 0.8

for iteration in range(20):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    direction_and_amount = (pred - goal_pred) * input
    # (pred - goal_pred) - чистая ошибка
    # если это положит. число - то прогноз слишком велик и наоборот
    # чем больше число - тем сильнее промах
    weight = weight - direction_and_amount

    print(f'Error: {error}; Prediction: {pred} ({round(pred, 2)})')
