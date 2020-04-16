'''change the behaviour of a multiplication operator
to do addition'''

class Number(object):
    """docstring for Number."""

    def __init__(self, x):
        self.x = x
    def __mul__(self,other):
        x = self.x + other.x
        return x

number_1 = Number(3)
number_2 = Number(2)

print(number_1 * number_2)
