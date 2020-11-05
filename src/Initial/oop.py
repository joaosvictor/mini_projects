# Python Object-Oriented Programming

# setting up the class and making de oop
class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com '

	def fullname(self):
		return '{} {}'.format(self.first, self.last)#here goes the full name method

	
# setting up  the employees
emp_1 = Employee('Jhon', 'Leon', 8552)
emp_2 = Employee('Michael', 'Billy', 8789)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp1.fullname())#here you can print the full name of de "def fullname()"
'''
#The hard way,  you can use this way but is more line of code than the other type 
#atibutes of emp1
emp_1.first = 'John'
emp_1.last = 'Leon'
emp_1.email = 'JohnLeon@company.com'
emp_1.pay = 8552

#atibutes of emp2
emp_2.first = 'Michael'
emp_2.last = 'Billy'
emp_2.email = 'MichaelBilly@company.com'
emp_2.pay = 8789
'''

	
