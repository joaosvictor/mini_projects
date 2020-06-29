#loops and iterations:
#-----For loops-----

#simple for with break and continue and loop into loop
nums = [1,2,3,4,5]

for num in nums:
	for letter in 'abc':
		print(num, letter)
	
	if num == 3:
		print('Found!')
		#continue loop it will print found in '3' and continue after
		break # here i create a break if find number '3'
	print(num)
	
	#Range loop in for 
for i in range (1, 11):
	print(i)

#-----While loops-----

x = 0
while True:
#	if x == 5:
#		break 
	print(x)
	x += 1 

#---complex---
def my_range(start, end, step):
	while start <= end:
		yield start
		start += step
for x in my_range(1,10,0.5):
	print(x)
