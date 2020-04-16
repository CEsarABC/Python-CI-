Names1 = ['cesar', 'augusto', 'felipe', 'gonzalo', 'rodrigo', 'roberto','gustavo']

Names2 = ['gonzales', 'bernal','corredor','sanabria','skywalker']

def RandomNames():
    print(Names1 + Names2)


RandomNames()

mylist=['a','b','c','d','e']
myorder=[3,2,0,1,4]
mylist = [ mylist[i] for i in myorder]
print mylist

import random
x = [1,2,3,4,5]
random.shuffle(x)
x
[5, 2, 4, 3, 1]
