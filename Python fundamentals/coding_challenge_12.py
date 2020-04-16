'''create a super class (computer), with two sub classes
(desktop)(laptop), define two methods in computer class
(getspecs)(displayspecs)'''

class Computer:
    company = 'American Megatrends'
    year = 2019
    Tax_code = 'XD34-0009'
    Licence = 'Ak-sell-2019'

    def __init__(self, processor, ram_size, memory_size):
        self.processor = processor
        self.ram_size = ram_size
        self.memory_size = memory_size

    def getspecs(self):
        print('Enter the deails: ')
        self.processor = input('Prossesor: ')
        self.ram_size = input('Ram size: ')
        self.memory_size = input('Memory size: ')
    def displayspecs(self):
        print('the following equitment comes with {} of Ram, an {} Prossesor, and {} of memory, case {}'
        .format(self.ram_size,self.processor,self.memory_size, self.casecolor))
        #print(self.processor)
        #print(self.ram_size)
        #print(self.memory_size)
    def licences(self):
        print('Rights to: {}, {}, Tax code {}, Enterpice licence {}'.format(self.company, self.year, self.Tax_code, self.Licence))

class Laptop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor
    def getCaseColor(self):
        self.casecolor = input('give me a case color: ')
    def display_case(self):
        print(self.casecolor)
    def equitment_laptop(self):
        print('type laptop')

class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor
    def getCaseColor(self):
        self.casecolor = input('give me a case color: ')
    def display_case(self):
        print(self.casecolor)
    def equitment_desktop(self):
        print('Type Desktop')

# number_1 = Laptop('')
# number_1.getspecs()
# number_1.getCaseColor()
# number_1.displayspecs()
# ##number_1.display_case()
# number_1.equitment_laptop()
#
# print(number_1.company)
#
# number_1.licences()

number_2 = Desktop('')
number_2.getspecs()
number_2.getCaseColor()
number_2.displayspecs()
#number_1.display_case()
number_2.equitment_desktop()

print(number_2.company)

number_2.licences()
