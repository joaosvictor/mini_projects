#By joão victor; 
#Hanoi Tower Solver 

#setting up the function move: it'll move the discs 
def move(f,t) :
  print('Move disc from {} to {}!'.format(f,t))

'''
move('A','C')  
'''

#setting up the function moveVia: it'll move for sample from a to b. it's a via to pass
def movieVia(f,v,t) :
  move(f,v)
  move(v,t)

'''
movieVia('A','B','C')  
''' 

#the main function that will be able to show the solution.
def hanoi(n,f,h,t) :
  if n == 0 :
    pass #pass in python = do nothing
  else:
    hanoi(n-1,f,t,h)
    move(f,t)
    hanoi(n-1,h,f,t)

hanoi(4,'A','B','C')
