'''we can no access the variable unless is included in a method '''

class HiddeVariable:
    __hidden_number = 2

    def add(self,Increment):
        self.__hidden_number += Increment
        print(self.__hidden_number)
    def printit(self):
        print(self.__hidden_number)


myObject = HiddeVariable()
myObject.add(5)


try:
    print(myObject.__hidden_number)


except:
    print('we can not print the hidden variable')

myObject.printit()
