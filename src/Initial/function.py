#-----Function python-----
#function in python = def 

#calling a function
def my_function():
	print("Hello from a function")
my_function()

#Arguments
def my_function(fname):
	print(fname + ", Here we go!")

my_function("John")
my_function("Leon")
my_function("Toby")

#Number of arguments
def my_function(fname, lname):
	print(fname + " " + lname)

my_function("Angela", "Cena")

#Keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#Return values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))	

#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
