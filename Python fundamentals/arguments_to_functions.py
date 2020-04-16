def function(x,y):
    if x < y:
        return(x - y)
    elif x == y:
        return(x)
    else:
        return(x - y)

print(function(2,5))
print(function(6,3))
print(function(8,8))

def adds(a,b):
    c = a + b
    return c

def rests(a,b):
    c = a - b
    return c

f = adds(3,3)
g = rests(6,4)

def multiply_both(f,g):
    x = f * g
    return x

resultA = multiply_both(adds(3,3),rests(6,4))

print(multiply_both(f,g))

print(resultA)
