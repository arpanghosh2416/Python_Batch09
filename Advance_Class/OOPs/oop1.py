'''
OOP:

4 Principle of OOP:
1) Polymorphism 2) Inheritance 3) Abstraction 4) Encapsulation

Class is made of:
1) Object(Attributes) 3) Method(Behaviour)
'''

# Creating Class only
class Test:
  x=5 #class property
  y=6
  z=7

# Create Objects:
p1=Test()
print(p1)
print(type(p1))
print(p1.x)

# delete an object
del p1
# print(p1)

# Multiple Objects
p1=Test()
p2=Test()
p3=Test()
print(p1.x)
print(p2.y)
print(p3.z)
sum = p1.x+p2.y+p3.z
print("Sum is:",sum)



class Test1:
  pass