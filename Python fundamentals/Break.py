fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
counter = 0

while counter <= len(fruits) - 1:
    if fruits[counter] == "peach":
        break
    print(fruits[counter])
    counter += 1

print("Iteration has been completed")

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
counter = 0

for fruit in fruits:
    if fruit == "peach":
        break
    print(fruit)

print("Iteration has been completed")