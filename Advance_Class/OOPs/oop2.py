# Constructor
class Test:
  # By Default when you initiate a class, this constructor method will remain by default.
  def __init__(self):
   pass

p1=Test()
print(p1)


class Test:
  # Defualt Contrutor / No-Argument Contructor
  def __init__(self):
    pass
  x=5

p1=Test()
print(p1)
print(p1.x)

print()
# Parameterized Constructor
class Test:
  # __init__ is a constructor method which will be automatically called when you create object. 
  # We can pass arguments in constructor to initialize our objects that are important, and it will be initialized, when the object is created, with initial values.
  def __init__(self,x):
    self.x=x

p1=Test(5)
print(p1.x)


print()
class Person:
  def __init__(self, name, age):
    self.name=name
    self.age=age

p1=Person("Ram", 24)
p1=Person("Arpan", 26) #You are able to set initial values.
# p1.name="Depayan" You can always change the value
print(p1.name)
print(p1.age) #Accessing Properties of an object using dot notation

print()
class Person:
  pass

p1=Person()
p1.name="Ram"
p1.age=24 

p1.name="Arpan"
p1.age=26 #Modifying Properties of an object using dot notation
print(p1.name)
print(p1.age)
del p1.age #Deleting Properties of an object using del keyword
# print(p1.age)
# print(p1.name)



