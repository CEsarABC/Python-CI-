
# First, we just need a for loop. Our for loop will iterate through the range of numbers between 99 and 0,
# stepping in -1. Each iteration of the loop will get closer to 0. On the following two lines we just declare
# two string variables (line_one and line_two). Instead of including the number of bottles of beer in the string,
#  we’ve used placeholders ({0}). And line_two has the newline escape character at the end
# so we’ll have a clear line break between the verse. Then we just print out line_one, which
# is formatted to include the number from the current iteration of the loop.


for number in range(99, 0, -1):
    line_one = "{0} bottle(s) of beer on the wall. {0} bottle(s) of beer"
    line_two = "Take one down, pass it around. {0} bottle(s) of beer on the wall\n"

    print(line_one.format(number))
    print(line_two.format(number - 1))

print('No more bottles of beer on the wall, no more bottles of beer.\n'
      'We’ve taken them down and passed them around; now we’re drunk and passed out!')