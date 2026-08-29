# Tuple with condition:

x = (1, "Hello", 3.14, True, 1, 10)
if  "Hello" in x:
  print("\"Hello\" is there in the tuple")
if  True in x:
  print("\"True\" is there in the tuple")



# How to change values in TUPLE:
'''
STEP1: Convert the tuple into a list using list() function
STEP2: Change the values in the list(append, insert, remove, pop, extend, etc.)
STEP3: Convert the list back into a tuple using tuple() function
'''

x = (1, "Hello", 3.14, True, 1, 10)

x1 = list(x) #Converting the tuple into a list
x1[1] = "World" #Changing the value at index 1 in the list
x = tuple(x1) #Converting the list back into a tuple
print(x) #Printing the updated tuple

# del x[2] #This will give an error because we cannot delete an element from a tuple directly
# x.clear() #This will give an error because we cannot clear a tuple directly
del x
# print(x) #This will give an error because the tuple has been deleted