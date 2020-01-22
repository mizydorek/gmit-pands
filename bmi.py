weight = int(input('Enter weight in kg: '))
height = int(input('Enter height in cm: '))

bmi = round(weight / (height/100) ** 2,2)
print('BMI is', bmi)