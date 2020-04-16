class Teddy:
    quantity = 200 #object attributes
    size = 20

    def __init__(self, name, color, border):# intance attributes
        self.color = color
        self.name = name
        self.border = border

    def change_color(self): #creating a method to change color
        self.color = 'white'
    def change_border(self, border): #creating a method to modify color
        self.border = border
        if border == 'orange':
            self.border = 'New color'

Teddy_1 = Teddy('TED','red','yellow')
print(Teddy_1.name)
print(Teddy_1.color)
print(Teddy_1.border)

Teddy_1.change_color()
print('here we activate a method which changes color to - {}'.format(Teddy_1.color))

Teddy_2 = Teddy('Roland','green','yellow')
print(Teddy_2.name)
print(Teddy_2.color)

Teddy_2.change_border("orange")
print('here we activate a method which changes the border attribute to - {}'.format(Teddy_2.border))
