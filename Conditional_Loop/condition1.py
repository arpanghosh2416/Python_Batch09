a= "Hello, World!"

#if True, then execute the block of code inside the if statement
if "Hello" in a:
    print("Hello is present in the string")

#if False:
if "Hello" not in a:
    print("Hello is not present in the string")

if "Hello" in a:
    print("Hello is not present in the string")
    print("Hello is not present in the string1")
    print("Hello is not present in the string2")

x=-3
# Using the variable x as condition
if x:
    print("X is true")

# In Python 0 means False as well as "" false, None represents as False.Empty Collections(list, set..) represent False. Everything else is true.

x="False"
# Using the variable x as condition
if x:
    print("X is true")



#if-elif

x=10
if x>11:
    print(True)
elif x>6:
    print(False)

# Multi if-elif statement
x=10
if x>11:
    print(True)
elif x>6:
    print(False)
elif x>7:
    print("No Idea")
elif x>8:
    print("Get an Idea")


# Mutually Exclusive Conditions.
# Determine the Day using the Day number:
#Calculation of State Electricity Bill where slabs are used.


x=2

if x==1:
    print("Monday")
elif x==2:
    print("Tuesday")
elif x==3:
    print("Wednesday")

# if-multi/single-elif-else


x=7

if x==1:
    print("Monday")
elif x==2:
    print("Tuesday")
elif x==3:
    print("Wednesday")
else:
    print("Invalid Day Number")

# if-else statement
a=3
b=4
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")