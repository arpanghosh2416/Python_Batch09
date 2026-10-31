class Person:
  # self paramter should always be first parameter of any function in the class
  def __init__(self, name):
    self.name=name

  def greet(self):
    return "Hello, " + self.name 
# Calling other methods with self
  def welcome(self):
    msg = self.greet() #None if u have used print syntax
    print(msg + " Welcome to our class!!")


# Outside class
p1=Person("Ram")

p1.welcome()
