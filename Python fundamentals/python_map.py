'''map is used to apply a function to every element in a list'''

def add(x):
    return x + 2

new_list = [10,20,30,40]

other_list = list(map(add,new_list))
print(other_list)

another_lambda = list(map(lambda x: x + 2, new_list))
print(another_lambda)

def multiply(x):
    return x*x
def add1(x):
    return x+x

funcs = [multiply, add1]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
