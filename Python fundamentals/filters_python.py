'''filters with lambdas'''

new_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

result = list(filter(lambda x: x % 2 == 0, new_list))
print(result)

result_1 = list(filter(lambda x: x % 2 == 1, new_list))
print(result_1)
