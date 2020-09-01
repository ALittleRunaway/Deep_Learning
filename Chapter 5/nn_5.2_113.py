"""Continue"""
def neural_network(input, weights):
    out = 0
    for i in range(len(input)):
        out += (input[i] * weights[i])
    return out

def ele_mul(scalar, vector):
    out = [0, 0, 0]
    for i in range(len(out)):
        out[i] = scalar * vector[i]
    return out


toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

win_or_loose_binary = [1, 1, 0, 1]
true = win_or_loose_binary[0] # goal prediction

alpha = 0.01
weights = [.1, .2, -.1]
input = [toes[0], wlrec[0], nfans[0]]

for iter in range(3):
    pred = neural_network(input, weights)

    error = (pred - true) ** 2
    delta = pred - true

    weight_deltas = ele_mul(delta, input)

    print(f"Iteration: {iter + 1}")
    print(f"Prediction: {pred}")
    print(f"Error: {error}")
    print(f"Delta: {delta}")
    print(f"Weights: {weights}")
    print(f"Weight Deltas: \n{weight_deltas}\n")

    for i in range(len(weights)):
        weights[i] -= alpha * weight_deltas[i]
