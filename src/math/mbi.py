name  = str(input('Your name: '))
height_m = float(input('Put your height: '))
weight_kg = float(input('Put your weight: '))

bmi = weight_kg / (height_m ** 2)
print("{} your bmi is: {}".format(name,bmi))
if bmi < 25:
	print('you are not overweight')#off
else:
    print('is overweight')
    
