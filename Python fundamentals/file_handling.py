# file = open("demo.txt","w")
# # write something in the file
# file.close()

'''shows all content'''
file1 = open("demo.txt","r")
content = file1.read()
file1.close()
print(content)


# '''reads just 10 spaces from the start'''
# file1 = open("demo.txt","r")
# content = file1.read(10)
# file1.close()
# print(content)

'''reads just 1 line from the start'''
file1 = open("demo.txt","r")
content2 = file1.readline()
file1.close()
print (content2)

'''loops through every letter'''
for line in content2:
    print(line)

''' here the document is opened and closed '''
line = open("demo.txt","r").readlines()[1]
print(line)
line = open("demo.txt","r").readlines()[4]
print(line)
line = open("demo.txt","r").readlines()[-1]
print(line)
