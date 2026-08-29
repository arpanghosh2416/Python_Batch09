# One Liner if statement
a=5
b=3
if a>b:
  print("a is greater than b")

if a>b: print("a is greater than b")


# One Liner if-else statement
# <Body of If statement> if <Condition> else <Body of else> => Conditional Expression(ternary operator)

print("a is greater than b") if a>b else print("b greater than A")

# Assign the value with if-else statement

x="a is greater than b" if a>b else "b greater than A"

print(x)
print(type(x))

# variable = <value_if_body> if condition else <value_else_body> ; whichever will be true, variable will hold that value.


'''
x=7

if x==1:
    print("Monday")
elif x==2:
    print("Tuesday")
elif x==3:
    print("Wednesday")
else:
    print("Invalid Day Number")
'''

x=2
print("Monday") if x==1 else print("Tuesday") if x==2 else print("Wednesday") if x==3 else print("Invalid Day Number")


x=2
day = "Monday" if x==1 else "Tuesday" if x==2 else "Wednesday" if x==3 else "Invalid Day Number"
print(day)

# Setting default value:

username=""
# username="Arpan"
dis_name = username if username else "Guest"
print("Welcome", dis_name)

a=5
b=2
c=7
if a>b and c>a:
  print("Both conditions are True")

if a>b or c>a:
  print("Any either condition is True")

if not a>b and c>a:
  print("Both conditions are True")
else:
  print(False)


if (a>b or c>a) and (a>b and not c<a):
  print("Both conditions are True")



# Auth System:

username="Arpan"
pwd="Arpan123"

is_verified = True
if username and pwd and is_verified:
  print("Access Granted")
else:
  print("Access Denied")
