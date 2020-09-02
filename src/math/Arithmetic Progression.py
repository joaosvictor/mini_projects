#by João Victor
from time import sleep
#import the library

print('---- Super Arithmetic Progression ----')

#Setting up the variables
term1 = int(input('What the first term ? '))
cmdifference = int(input('Common difference ? '))
amount = int(10)
plus = int(10)
suM = int(0)
counter = (0)

#loop while to do the process
while counter < amount:
    counter = counter + 1
    for i in range(counter, amount +1 ):
        if i == 0:
            suM = term1
        else:
            suM = suM + cmdifference
        print(suM - cmdifference, end=' => ')

    #putting the continnue of AP
    plus = int(input('More terms ? '))
    amount = counter + plus
    if plus == 0:
        amount = counter + plus

#finishing the code 
print('Finishing...')
sleep(1)
print('==================================')
print('Program ended! To the next! ')
