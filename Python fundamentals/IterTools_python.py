from itertools import count, accumulate, takewhile

'''count'''
for i in count(15):
    print(i)

    if i >= 20:
        break

'''accumulate'''
numbers = list(accumulate(range(8)))

print(numbers)

'''takewhile'''
print(list(takewhile(lambda x: x <= 10, numbers)))
