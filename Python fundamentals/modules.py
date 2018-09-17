from random import randint

print(randint(0, 100),'\n')

countDown = 10
while countDown >= 0:
    print(randint(0,20))
    countDown -= 1


def lottery_generator():
    numbers = []
    for number in range(0, 10):
        numbers.append(randint(1, 50))
    return numbers


print('this weeks winning lottery numbers are %s' % lottery_generator())
