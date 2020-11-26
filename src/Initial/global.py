#Global tuturial 

x = 1 #global variable

def add():
	print(x)
add()	

#############################

x = 1 #global variable 

def add():
	x = x + 2 #increment x by 2
	print(x)
add()

#############################	

x = 0 #global variable

def add():
	global x 
	x = x + 2 
	print('inside add():', x)
add()
print('In main:', x)

#############################

# Using a global variable in nested function

def too():
	x = 20

	def exp():
		global x
		x = 25
	print('Before calling bar: ', x)
	print('Calling bar now')
	exp()
	print('After calling bar: ', x)
too()
print('x in main: ', x)
