fruits = ('apple','mango','peach','banana')

print(fruits[0])

try:
    fruits[0] = 'lemon'
except:
    print('Is a tuple and is unmutable')
finally:
    print(fruits)
