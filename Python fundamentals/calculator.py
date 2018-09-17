
print('this is a calculator for python')
print('please chose an option')
print('''\

      add(1) multiply(2) substract(3) divide(4)
      
''')

op = float(input('please chose operation: '))
first = float(input('your first number: '))
second = float(input('your second number: '))

if op != (1,2,3,4):
    print('no no')

elif op == 1:
    print(first + second)
elif op ==2:
    print(first * second)
elif op ==3:
    print(first - second)
elif op ==4:
    print(first / second)
else:
    print('use just numbers for your operation!!')

print(type(op))