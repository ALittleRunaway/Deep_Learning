"""Exercise 1"""
def elementwise_multiplication(vec_a, vec_b):
    assert(len(vec_a) == len(vec_b))
    output = 0
    for i in range(len(vec_a)):
        output += (vec_a[i] * vec_b[i])
    return output

def elementwise_addition(vec_a, vec_b):
    assert(len(vec_a) == len(vec_b))
    output = 0
    for i in range(len(vec_a)):
        output += (vec_a[i] + vec_b[i])
    return output

def vector_sum(vec_a):
    output = 0
    for i in vec_a:
        output += i
    return output

def vector_average(vec_a):
    output = 0
    for i in range(len(vec_a)):
        output += vec_a[i]
    output = output / len(vec_a)
    return output


vector_a = [1, 2, 3, 4, 5]
vector_b = [6, 7, 8, 9, 10]
print(elementwise_multiplication(vector_a, vector_b))
print(elementwise_addition(vector_a, vector_b))
print(vector_sum(vector_a))
print(vector_average(vector_a))