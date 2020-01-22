weight = int(input('Enter weight: '))
height = int(input('Enter height: '))

bmi = round(weight / (height/100) ** 2,2)
print('BMI is ' + str(bmi))