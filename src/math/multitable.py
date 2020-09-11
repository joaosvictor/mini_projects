
value = int(input('Enter a number in the multiplication table: '))  
aux = 0  
print('*' * 18)  
print('Multiplication table of {}'.format(value))  
print('*' * 18)  
while(aux <= 10):  
  print('{0} X {1} = {2}'.format(aux, value, (aux * value)))  #this will x your value number times the rest of the multitable.
  aux = aux + 1 
  #
