class Teddy:
    quantity = 200 #attribute all objects
    size = 20 #attribute all objects

    #instance attributes we can change for every object
    def __init__(self, color, name):
        self.color = color
        self.name = name


Teddy_1 = Teddy('brown','Oscar')

print(Teddy_1)
print(Teddy_1.quantity)
print(Teddy_1.name)
print(Teddy_1.color)

Teddy_2 = Teddy('red','Amandine')

print(Teddy_2)
print(Teddy_2.quantity)
print(Teddy_2.name)
print(Teddy_2.color)
