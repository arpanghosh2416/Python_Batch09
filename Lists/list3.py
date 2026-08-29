x=[1, "Hello", 3.14, True,1,10]

# Iterative forEach Loop
for i in x:
  print(i)

print()
# Starting range is not there, cannot use the step value
for i in range(len(x)):
  print(x[i])

print()
# Here you can manipulate the iteration using Step value
for i in range(0,len(x),2):
  print(x[i])


print()
# Here you can manipulate the iteration reverse using Step value
for i in range(len(x)-1,0,-2):
  print(x[i])

print()
# List Comprehension
x=[1, "Hello", 3.14, True,1,10]

# x1 = [i for i in x if "Hello" in x]
# x1 = [i for i in x ]
# x1= [x[i] for i in range(len(x))]
# x1= [i for i in range(len(x))] --> print only index
# x1= [i for i in range(len(x)) if type(i) != int]
# x1= [x[i] for i in range(len(x)) if x[i] == x[i]]
# x1= [x[i] for i in range(len(x)) if x[i] == 3.14]
# x1 = [i.upper() for i in x if i == "Hello"]
# x1 = ["hello" for i in x] --> Replace values

x1=[i if i !="Hello" else "Hello World" for i in x]
# Syntax:
# var = [value for index in list_iterable <if condition == True>] --> Condition is like a filter, item gets accepted when TRUE

print(x1)

# print()
# for i in x:
#   if "Hello" in x:
#     print(i)