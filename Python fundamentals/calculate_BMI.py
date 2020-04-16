print('This is your BMI calculator program')

def bmi_calculator():
    height = int(input('Enter your Height: '))
    weight = int(input('Enter your weight: '))
    bmi = weight / (height * height)
    print('Your BMI is: ')
    print (bmi)

bmi_calculator()

def bmi_calculator1(height, weight):
    bmi = weight / (height * height)
    print('Your BMI is: ')
    print (bmi)

bmi_calculator1(3,3)

def calculate_BMI(new_weight, new_height):
    new_bmi = new_weight/(pow(new_height, 2))
    return new_bmi

weight = float(input('Enter weight in Kgs'))
height = float(input('Enter height in meters'))
bmi = calculate_BMI(weight, height)
print(bmi)
