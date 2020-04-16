try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print('there is a divide by 0 error')

try:
    a = 0
    b = 0
    print (a/b)
except:
    print('second example')
finally:
    print('the code continues')


    def divide(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("There is a divide by zero error")
            return 0


    x = float(input('Enter a number'))
    y = float(input('Enter value by which you want to divide the number'))
    result = divide(x, y)
    print(result)
