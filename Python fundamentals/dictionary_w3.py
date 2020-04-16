thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print('\n')

x = thisdict["model"]
x = thisdict.get("model")

thisdict["year"] = 2018

for x in thisdict:
  print(x)

print('\n')

for x in thisdict:
  print(thisdict[x])

print('\n')

for x in thisdict.values():
  print(x)

print('\n')

for x, y in thisdict.items():
  print(x, y)

print('\n')

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print('\n')

thisdict.pop("model")
print(thisdict) 
