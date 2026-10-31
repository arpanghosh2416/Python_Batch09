# Protected Properties

class Person:
  
  def __init__(self, name, age):
    self._name=name # _(single underscore) represents protected
    self._age=age

  def display(self):
    print(self._name)
    print(self._age)

p1=Person("Arpan", 25)
p1.display()
print(p1._name) # Can access, but should not

# Note : _(single underscore) is a convention for programmer, like to tell the coders that it should be used internally and Python does not have any restriction.