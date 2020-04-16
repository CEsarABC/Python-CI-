'''similar to lists but without indexes'''

def function():
    count = 0
    while count < 5:
        yield count
        count += 1

for x in function():
    print(x)

def generator_evens(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(generator_evens(20)))
