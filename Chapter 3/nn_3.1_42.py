"""I create my first neural network"""
weight = 0.1
def neural_network(input, weight):
    """Calculates the prediction"""
    prediction = input * weight
    prediction = round(prediction, 2)
    # prediction = format(prediction, '6.2f')
    return prediction

number_of_toes = [8.5, 9.5, 10, 9]
input = number_of_toes[0]
pred = neural_network(input, weight)
print(pred)