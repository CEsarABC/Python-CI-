import json

'''converting a string into a jason and accessing the data'''
people_string = '''
{
  "states": [
    {
      "name": "Alabama",
      "abbreviation": "AL",
      "area_codes": ["205", "251", "256", "334", "938"]
    },
    {
      "name": "Alaska",
      "abbreviation": "AK",
      "area_codes": ["907"]
    }
    ]
}

'''
data = json.loads(people_string)
print(data)
print(type(data))
print(data['states'])
print(data['states'][0]['name'])
print('-------------------------------')
for state in data['states']:
    print(state['name'])
print('-------------------------------')
for state in data['states']:
    if state['name'] == 'Alaska':
        state['new'] = 'new'
print(data['states'])
print('-------------------------------')
for state in data['states']:
    if state['name'] == 'Alabama':
        state['area_codes'].append(666)
print(data['states'])
print('-------------------------------')

'''dump a python object into a json file
and giving it a format'''

new_string = json.dumps(data,indent=2, sort_keys=True)
print(new_string)
