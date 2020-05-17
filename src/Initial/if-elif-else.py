#Examples if/elif/else python

#an if clause
a = 1
b = 2
if a < b :
 	print('a is less than b')
 	print('a is definitely less than b')
print('Not sure if a is less than b') 	
########################################
c = 3
d = 4
if c < d :
	print('c is less than d')
else:
    print('c is NOT less than d')	
    print("I don't think c is less than d")
print('outside the if block')
########################################
e = 7
f = 8
if e < f :
	print('e is less than f')
elif e == f:
	print('e is equal to f')
elif e > f +  10:
	print('e is greater than f by more than 10 ')
else:
	print('e is not greater than f')
########################################
g = 7
h = 8
if g < h :
	print('g is less than h')
else:
	if g == h:
		print('g is equal to h')
	else:
	    print('g is greater than h')	 
########################################
name  = str(input('Your name: '))
height_m = float(input('Put your height: '))
weight_kg = float(input('Put your weight: '))

bmi = weight_kg / (height_m ** 2)
print('bmi: ')
print(bmi)
if bmi < 25:
	print(name) 
	print('is not overweight')
else:
    print(name)
    print('is overweight')	
    
