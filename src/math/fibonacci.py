def FibRecusion(n):
	if n<=1:
		return n
	else:
		return(FibRecusion(n-1)+FibRecusion(n-2))
	
	
nterms = int(input("enter the terms: "))#take i

if nterms <= 0:#check if the number is valid 
	print('please enter a positive integer')
else:
	print('Fibonacci sequence: ')
	for i in range (nterms):
		print(FibRecusion(i))
