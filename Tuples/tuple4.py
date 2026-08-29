x = (1, "Hello", 3.14, True, 1, 10)
# forEach Loop in Tuple:
for i in x:
  print(i) #Printing the value of i
print("\n")
for i in range(0,len(x),2):
  print(x[i]) #Printing the value of x[i]


print("\n")
i=0
while i < len(x):
  print(x[i]) #Printing the value of i
  i += 1



x = (1, "Hello", 3.14, True, 1, 10)
x1=(20,30,40)

# Join Tuples
x2=x+x1
print(x2) #Printing the value of x2

# Multiply tuples
x2 = x2*2
print(x2) #Printing the value of x2


x3 = x2.count(1)
print(x3)

x3 = x2.index(10)
print(x3)