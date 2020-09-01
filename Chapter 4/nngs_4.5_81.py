"""Градиентный спуск"""
weight = 0.1
alpha = 0.01
def neural_nerwork(input, weight):
    prediction = input * weight
    return prediction

number_of_toes = [8.5]
win_or_loose_binsry = [1] # win

input = number_of_toes[0]
goal_pred = win_or_loose_binsry[0]

pred = neural_nerwork(input, weight)

error = (pred - goal_pred) ** 2 # Среднеквадратическая ошибка
delta = pred - goal_pred # Чистая ошибка
weight_delta = input * delta # как direction_and_amount из пред. скрипта
weight -= weight_delta * alpha # тот же градиентный спуск, alpha - корректировка веса, для контроля скорости обучения
print(weight)
