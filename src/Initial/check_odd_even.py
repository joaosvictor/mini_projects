# check if a input number is odd or even

# int input
number = int(input('Enter a number: '))

# "%" operator check the remainder of a division 
# so, 8 / 2 = 4. No remainder! 
# otherwise, 8 / 3 = 2,66. It has remainder number!

if number % 2 == 0: # zero represent the "remainder"
    print('{} is Even number'.format(number))
else:
    print('{} is Odd number'.format(number))

# .format() will call the variable, so you put '{}' to the .format find it 
