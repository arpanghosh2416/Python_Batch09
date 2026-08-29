x = (1, "Hello", 3.14)

(a,b,c) = x

print(a) #Printing the value of a
print(b) #Printing the value of b
print(c) #Printing the value of c

x = (1, "Hello", 3.14, True, 1, 10)
(a,b,*c) = x

print(a) #Printing the value of a
print(b) #Printing the value of b
print(c) #Printing the value of c

x = (1, "Hello", 3.14, True, 1, 10)
(a,*b,c) = x

print(a) #Printing the value of a
print(b) #Printing the value of b
print(c) #Printing the value of c