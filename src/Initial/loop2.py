#-----For loops-----

#prints out the numbers 0,1,2,3,4
for x in range(5):
	print(x)

#prints out the numbers 3,4,5
for x in range(3,6):
	print(x)

#prints out 3,5,7
for x in range(3,8,2):
    print(x)	

 #-----While loops-----

 #prints out 0,1,2,3,4
 count = 0
 while count < 5:
 	print(count)
 	count += 1 #this is the same as count = count + 1 


#-----Break and continue loops-----

#prints out 0,1,2,3,4

count = 0
while True:
	print(count)
	count += 1
	if count >= 5:
		break


#prints out only odd numbers - 1,3,5,7,9
for x in range(10):
	#check if x is even
	if x % 2 == 0:
		continue
	print(x)
