#List - Ordered, Mutable, Allows Duplicates, Heterogeneous(Data-Types)
x = [1, 2, 3, 4, 5]
x=[1, "Hello", 3.14, True,1,10]
print(x)
print(type(x))
# List Indexing
print(x[0]) #Accessing the first element of the list
print(x[1]) #Accessing the second element of the list

print(len(x)) #Returns the number of items in the list
# List Negative Indexing
print(x[-1]) #Accessing the last element of the list
print(x[-2]) #Accessing the second last element of the list
# List Slicing
print(x[0:3]) #Accessing a range of elements from the list (slicing)
print(x[1:]) #Accessing all elements from the second element to the end of the list
print(x[:3]) #Accessing all elements from the beginning of the list to the third element (exclusive)
print(x[-5:-1]) #Accessing a range of elements from the list using negative indexing (slicing)
print(x[::-1]) #Accessing all elements of the list in reverse order (slicing)
print(x[::-2]) #Accessing all elements of the list with a step of 2 (slicing)
print(x[::2]) #Accessing all elements of the list with a step of 2 (slicing)

# List with condition:
if  "Hello" in x:
  print("\"Hello\" is there in the list")
if  True in x:
  print("\"True\" is there in the list")

x = list((1, "Hello", 3.14, True, 1, 10))
print(x)