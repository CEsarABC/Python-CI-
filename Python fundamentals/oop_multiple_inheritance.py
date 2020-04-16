'''class c inherits all methods from A and B'''

class A:
    def a_method(self):
        print('this is a A method')

class B:
    def b_method(self):
        print('this is a B method')

class C(A,B):
    def c_method(self):
        print('this is a C method')

c_object = C()

c_object.a_method()
c_object.b_method()
c_object.c_method()
