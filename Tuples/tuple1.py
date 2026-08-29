#Tuple - Ordered, Immutable, Allows Duplicates, Heterogeneous(Data-Types)

tup = (1, 2, 3, 4, 5)
print(tup)
tup = (1, "Hello", 3.14, True, 1, 10)
print(tup)
print(type(tup))
print(len(tup)) #Returns the number of items in the tuple
# Tuple Indexing
print(tup[-1]) #Accessing the last element of the list
print(tup[-2]) #Accessing the second last element of the list
# List Slicing
print(tup[0:3]) #Accessing a range of elements from the list (slicing)
print(tup[1:]) #Accessing all elements from the second element to the end of the list
print(tup[:3]) #Accessing all elements from the beginning of the list to the third element (exclusive)
print(tup[-5:-1]) #Accessing a range of elements from the list using negative indexing (slicing)
print(tup[::-1]) #Accessing all elements of the list in reverse order (slicing)
print(tup[::-2]) #Accessing all elements of the list with a step of 2 (slicing)
print(tup[::2]) #Accessing all elements of the list with a step of 2 (slicing)


tup2=(6,)
print(type(tup2)) #Returns the type of the variable
tup3=(6)
print(type(tup3)) #Returns the type of the variable

tup = (1, 2, 3, 4, 5)
tup=("a", "b", "c", "d", "e")
tup= (True, False, True, False)
tup=(4+5j, 3+2j, 1+0j)
print(tup)
tup=(3.14, 2.71, 1.41, 0.577)
print(tup)



tup = tuple((1, "Hello", 3.14, True, 1, 10))