''' a function that calls itself'''
'''factorial of 5 = 5*4*3*2*1'''

def factorial(x):
    if x == 1:
        return 1
    else:
        return x*(factorial(x - 1))

print(factorial(5))

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

deliver_presents_recursively(houses)

addresses = ['address_1','address_2','address_3','address_4']
def delivering_pizzas(addresses):
    if len(addresses) == 1:
        adress = addresses[0]
        print('Delivering pizza to: ', adress)
    else:
        half = len(addresses) // 2
        first_half = addresses[:half]
        second_half = addresses[half:]

        delivering_pizzas(first_half)
        delivering_pizzas(second_half)

delivering_pizzas(addresses)
