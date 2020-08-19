"""Compare"""
knob_weight = 0.5
input = 0.5
goal_pred = 0.8

pred = input * knob_weight
print(pred)
error = (pred - goal_pred) ** 2
print(round(error, 3))
