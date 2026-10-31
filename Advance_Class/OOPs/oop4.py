# What is self parameter? Its a reference to the current instance(representative) of the class.
# Its works how? It is used to access properties(methods) that belong to the class
# Why use it? Without self, python is unable to recognize any object properties. 
# We can use any name instead of self also but its good practice to use self.

class Person:
  # self paramter should always be first parameter of any function in the class
  def __init__(self, name,country,city, age=26):
    self.name=name
    self.age=age
    self.city=city
    self.country=country
  # Accessing Property(variables or other objects) with self
  def greet(self):
    # self.name="ABC"
    # self.age +=1
    print("Hello, My name is ", self.name)
  def display(self):
    print(self.name,self.age,self.city,self.country)


# Outside class
p1=Person("Ram", "India", "Kolkata", 24)

p1.display()

p1.greet()

print("--Self --> Other Names--")
# Now self has been overwritten with some other name(say bubun), now later part, other name(say arpan), now arpan has been mapped to bubun which again is mapping to self keyword.
class Person1:
  # self paramter should always be first parameter of any function in the class
  def __init__(bubun, name,country,city, age=26):
    bubun.name=name
    bubun.age=age
    bubun.city=city
    bubun.country=country
  
  def greet(arpan):
    print("Hello, My name is ", arpan.name)


# Outside class
p1=Person("Ram", "India", "Kolkata", 24)

print(p1.name,p1.country,p1.city,p1.age)

p1.greet()