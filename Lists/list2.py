x=[1, "Hello", 3.14, True,1,10]

#Manual change / direct change

x[1] = "Arpan"
print(x)

# Change with Slicing
x[0:2] = [100,"Hello"]
print(x)
x[6:] = ["Depayan", False, 2.20, 1j]
print(x)

x[6:] = ["Python"]
print(x)


# Using Functions

x=[1, "Hello", 3.14, True,1,10]
y = ["1",2,True,"JAVA", "Arpan"]
x.insert(2,"Python")
print(x)
x.append("World")
print(x)
x.extend(y) #Merging two lists
print(x)

y={1,2,3}
x.extend(y) #Merging a list and a set
print(x)

y=(4,5,6)
x.extend(y) #Merging a list and a tuple
print(x)


x.remove(1)
print(x)


x.pop(len(x)-1)
print(x)

x.pop()
print(x)

del x[len(x)-1]
print(x)

# Memory clear
# del x

x.clear()
print(x)