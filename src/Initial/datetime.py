# import the library 
import datetime

# Def the x as a variable and catching the datetime now(today)
x = datetime.datetime.now()

# print the day, year and the name of the day
print(x.day)
print(x.year)
print(x.strftime("%A"))
