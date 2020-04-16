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

'''this class is inheriting the attributes from Student class and now
science student can access all atributes and methods'''

class ScienceStudent(Student):

    def science(self):
        print('this is the science method')

a = ScienceStudent('cesar','34')
a.science()
a.put_data()
