class Calculator:
  def add(self,a,b):
    return a+b
  def mult(self, a, b):
    return a*b

calc = Calculator()
cal1 = Calculator()
# print(calc)
print(calc.add(1,2))
print(calc.mult(2,2))

calc.mult = None
# print(calc.mult(2,2)) # crash
print(cal1.mult(2,2))
del Calculator.mult
# print(cal1.mult(2, 2)) # will crash


print("Without __str__ method:")
# __str__ methods

class Person:

  def __init__(self, name, age):
    self.name=name
    self.age=age

p1 = Person("Arpan",25)
print(p1) # prints the memory location


print("With __str__ method:")

class Person:
  # Magic Methods / dunder(double underscore) methods
  # Why Magic Methods? 
  # Because they are automatically invoked/inherited, and you do not call these magic methods directly. It is automatically called when you create an object.
  def __init__(self, name, age):
    self.name=name
    self.age=age
  def __str__(self):
    # self.age +=1
    return f"{self.name} is {self.age} years old"

p1 = Person("Arpan",25)
print(p1)


'''
__repr__[__str__ almost] ; __eq__ [Compares the equality of two objects]; __add__[Addition of two objects]; __len__[Length of an object] ; __lt__[Comparison of objects - less than]; __contains__[in operator]; __call__[call an object like a function]

'''