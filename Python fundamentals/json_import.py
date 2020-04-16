import json

'''opening a external json file,
importing the data, modifying the data and
saving everything in a new json file'''

with open('states.json') as file:
    data = json.load(file)

print(type(data))

for state in data['states']:
    print(state['name'] + ', '+ state['abbreviation'])

for state in data['states']:
    del state['area_codes']

with open('new_states.json','w') as file1:
    json.dump(data, file1, indent=2)
