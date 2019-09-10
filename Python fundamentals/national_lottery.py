from random import randint
import random

'''the idea is to create a lottery generator which gives an array of numbers,
which doesn't repeat in the list of old arrays'''

''' file io will help to store the old numbers an from the text file we can
recreate the past_numbers array to make the program compare arrays and make a
new number if the previous is already in the past_numbers array'''

past_numbers = []

'''this is simple and does the job, uses a list then a loop with range of 10,
crates a variable which is a number created by randit with range, uses a
conditional to avoid repeating numbers and then appends the number to a list'''

def new_lottery_function():
    list=[]
    for i in range(10):
        r = randint(1,50)
        if r not in list:
            list.append(r)
            list.sort()
    return(list)

new_number = (new_lottery_function())
# new_lottery_function()
# past_numbers.append(new_number)
#
# new_lottery_function()
# past_numbers.append(new_number)
'''past numbers are wrong because everytime randit finds the same number
that number doesn't get in to the list and the number of elements is reduced
because randit runs 10 times'''
for i in range(4):
    list = (new_lottery_function())
    new_lottery_function()
    past_numbers.append(list)

#print("I\'m wrong less numbers")
#print(past_numbers)


#--------------------------------------
def check_numbers_new():
    list = []
    list.sort()
    for number in range(1,51):
        #r = randint(1,50)
        if number not in list:
            list.append(number)

    print(list)

#check_numbers_new()
#--------------------------------------
'''giving a list of numbers and using sample to get always 10 random numbers
they dont repeat because they are chosen from one list, avoiding the elimination
of repeating numbers, we garantee that the numbers are in a full list'''
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]


produced_numbers = []

def new_lottery_best():
    x_number = random.sample(list_numbers,6)
    x_number.sort()
    return x_number

x_new = (new_lottery_best())

for i in range(4):
    x = (new_lottery_best())
    new_lottery_best()

    produced_numbers.append(x)


print("I\'m Right all numbers")
print(produced_numbers)
