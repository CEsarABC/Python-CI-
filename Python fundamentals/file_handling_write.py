file = open("write.txt","w")
file.write("this is the text writen in the file\n")
file.close()

file = open("write.txt","r")
content = file.read()
print(content)

file = open("write.txt","a")
file.write("this is the new text writen in the file\n")
file.close()

def write_to_file():
    text = input('Please write something: ')
    file = open("input.txt","a")
    file.write(text)
    file.write("\n")
    file.close()

write_to_file()
