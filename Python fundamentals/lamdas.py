'''anonimus functions'''

def square(x):
    return x**2

print(square(4))

result = (lambda x: x**2)(16)
print(result)

calculation = (lambda x: x*(x+5)**2)(5)
print(calculation)
