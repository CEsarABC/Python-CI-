import re

pattern = r"bread(eggs)*bread(eggs)*"

if re.match(pattern,'breadbread'):
    print('match found')
if re.match(pattern,'breadeggsbread'):
    print('match found')
if re.match(pattern,'breadeggseggseggseggsbread'):
    print('match found')
if re.match(pattern,'breadeggsbreadeggs'):
    print('match found')
