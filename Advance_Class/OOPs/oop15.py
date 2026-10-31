# Name Mangling

class Person:
  
  def __init__(self, name, age):
    self.name=name
    self.__age=age

p1=Person("Arpan", 25)
print(p1._Person__age) # Not Recommended
# You can access Private Properties using mangled name. But defeats the purpose of Encapsulation.
