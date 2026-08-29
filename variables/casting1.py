#Numeric Casting in Python
x=1
y=2.33
z=1j

#covert int to float
a=float(x)
print(a)
print(type(a))

#covert float to int
a=int(y)
print(a)

#covert int to complex
a=complex(x)
print(a)

#convert float to complex
a=complex(y)
print(a)

#convert complex to int
# a=int(z) #int() argument must be a string, a bytes-like object or a real number, not 'complex'
# print(a)
#convert complex to float
# a=float(z) # float() argument must be a string or a real number, not 'complex'
# print(a)