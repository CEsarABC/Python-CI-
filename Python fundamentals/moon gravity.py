earthGravity = 9.807
moonGravity = 1.622
marsGravity = 3.711

weightOnEarth = 83

AverageWeight = weightOnEarth / earthGravity


weightOnMoon = round((AverageWeight * moonGravity), 2)
weightOnMars = round((AverageWeight * marsGravity), 3)

print('my weight on Earth is: ', weightOnEarth)

print('my weight on the moon is: ', weightOnMoon)

print('my weight on mars is: ', weightOnMars)

