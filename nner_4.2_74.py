"""nn with comparing"""
weight = 0.1
lr = 0.01
def neural_network(input, weight):
    prediction = input * weight
    return prediction

number_of_toes = [8.5]
win_or_lose_binary = [1] # (победа!)

input = number_of_toes[0]
true = win_or_lose_binary[0]
# pred = neural_network(input, weight)
# p_up = neural_network(input, weight+lr)
p_dn = neural_network(input, weight-lr)

# error = (pred - true) ** 2
# e_up = (p_up - true) ** 2
e_dn= (p_dn - true) ** 2

# print(round(error, 4))
# print(round(e_up, 4)) # 0.0042 - the best!
print(round(e_dn, 4)) # 0.0552
