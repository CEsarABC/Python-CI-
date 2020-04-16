'''similar to lists but has operations between sets
so join, intersect, or substract '''

number_B = {1,2,3,4,5,6,7,8,10,11}
number_A = {9,10,11,12,13,14}

number_B.add(9)
number_B.remove(2)

print(number_B)

print(5 in number_B)
'''all alements without duplicates'''
print(number_A | number_B)
'''intersection values in both groups'''
print(number_A & number_B)
'''diference opertion'''
print(number_A - number_B)
