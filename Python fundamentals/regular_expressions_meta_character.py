import re
'''allows multiple repetitions * '''
pattern = r"eggs(bacon)*"

if re.match(pattern,"eggs"):
    print('match found')
if re.match(pattern,"eggsbacon"):
    print('match found')
if re.match(pattern,"eggsbaconbacon"):
    print('match found')
if re.match(pattern,"eggsbaconbaconbaconbacon"):
    print('match found')
