def abc():
    name = input('enter your name: ')
    age = input('enter your age: ')
    print(name)
    print(age)

abc()

''' in this class we create attributes we can change for every objects
and we create methods to get the data from the object and to print this data '''

'''the first function creates the attributes for the object,
the second function is to change the values whit the input,
the third function is to print those values'''

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self,name,age):
        self.name = name
        self.age = age

    def put_data(self):
        print(self.name)
        print(self.age)

'''creates an object with empty attributes, ask for input for the attributes
gets the data and prints the data '''

student_1 = Student('','')
name = input('Enter your name: ')
age = input('Enter your age: ')

student_1.get_data(name,age)
student_1.put_data()
