'''writing in functions function recall callback '''

def add_ten(x):
    return x + 10

def twice(func, arg):
    return func(func(arg))

print(twice(add_ten,3))

'''in this case the first functon returns the structure we
want to use, f then becomes a function that uses the arguments
provided and pass them down'''

def cal(f,x,y):
    return f(x,y)

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

print(cal(add, 10, 20))
print(cal(sub, 20, 15))
