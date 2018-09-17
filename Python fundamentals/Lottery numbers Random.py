from random import randint


def lottery_generator():
    numbers = []
    for number in range(0, 10):
        numbers.append(randint(1, 50))
    return numbers


print("This weeks winning lottery numbers are %s" % lottery_generator())