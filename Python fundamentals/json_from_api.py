import json
from urllib.request import urlopen
'''using https://www.json-generator.com/# for uploading a json to sever'''

with urlopen("http://www.json-generator.com/api/json/get/cdgbhcLEoi?indent=2") as response:
    source = response.read()

print(type(source))

data = json.loads(source)
print(type(data))
#print(json.dumps(data, indent=2))
print(len(data[0]['name']))

print(data[0])

for x in data:
    name = x['name']
    eyecolor = x['eyeColor']
    print(name +' ,'+ eyecolor)
print(len(x['name']))

new_dictionary = {}

for x in data:
    name = x['name']
    eyecolor = x['eyeColor']
    new_dictionary[name]=eyecolor

print(new_dictionary)

with open('new_people.json','w') as file:
    json.dump(new_dictionary, file, indent=2)
