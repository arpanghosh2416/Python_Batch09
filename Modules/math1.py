x = min(5,10)
y = max(5,10)
print(x)
print(y)


x= abs(-7.25)
print(x)

x= pow(4,3)
print(x)


import math
x= math.sqrt(64) #returns double value
print(x)

x=math.ceil(1.4) #returns the smallest integer greater than or equal to 1.4
print(x)
x=math.floor(1.4) #returns the largest integer less than or equal to 1.4
print(x)


x=math.pi
print(x)
# Want to convert the value of pi to 2 decimal places
x=round(x,2)
print(x)
print(type(x))

# This is not a good way to format a number to 2 decimal places as it returns a float value. We can use string formatting to convert the float value to a string with 2 decimal places.
x= x.__format__('.2f') #String formatting to 2 decimal places
print(x)
print(type(x))
