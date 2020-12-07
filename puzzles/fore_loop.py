# https://www.youtube.com/watch?v=ee1bXLDN60U&t=5077s
# https://pypi.org/project/clang/


'''
for i in range(10):
	print(i)
>>> 0,1,2,3,4,5,6,7,8,9


# the goal is: 
>>>  0,4,8

'''
# should work in this type, I guess
import sys

for i in range(10):
    if i % 4 == 0:
	print(i)
		
		
for i in range(10):
    if i % 1 == 1:
	i += 4 
	print(i)
