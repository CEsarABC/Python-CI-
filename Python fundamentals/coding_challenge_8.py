'''list out the odd numbers from 1 to 100
using lists in python'''

def challenge():
    for x in range(1,100):
        if x % 2 == 0:
            print(x)
challenge()

list2 = [x**2 for x in range(10) if x**2 % 2 == 0]
print(list2)

new_list = list(range(1,100))
odds_list = []

for x in new_list:
    if x % 2 != 0:
        odds_list.append(x)
print(odds_list)
