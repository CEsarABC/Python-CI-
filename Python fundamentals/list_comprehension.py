'''creating a rule for my list, list comprehension helps us
create automated lists '''

list = [x**2 for x in range(10) if x**2 % 2 == 0]
print(list)

# You can either use loops:
squares = []

for x in range(10):
    squares.append(x**2)

print (squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Or you can use list comprehensions to get the same result:
squares = [x**2 for x in range(10)]

print (squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

list1 = [3,4,5]

multiplied = [item*3 for item in list1]

print (multiplied)
[9,12,15]

listOfWords = ["this","is","a","list","of","words"]

items = [ word[0] for word in listOfWords ]

print (items)

list1 = [x.lower() for x in ["A","B","C"]]
print(list1)

string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print (numbers)

# Then create the filter by using list comprehension:

fh = open("write.txt", "r")

result = [i for i in fh if "written" in i]

print (result)

'''Now, let's see how we can use list comprehension in functions.'''
# Create a function and name it double:
def double(x):
  return x*2
list2 = [double(x) for x in range(10)]
print(list2)

list3 = [double(x) for x in range(10) if x%2==0]
print(list3)

list4 = [x+y for x in [10,30,50] for y in [20,40,60]]
print(list4)
