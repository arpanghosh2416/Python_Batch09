# Polymorphism
print("Polymorphism without Inheritance: Same Method but Different Class : -")
class Car:
  def __init__(self, brand, model):
    self.brand=brand
    self.model = model

  def move(self):
    print("Driving!!!")

class Boat:
  def __init__(self, brand, model):
    self.brand=brand
    self.model = model

  def move(self):
    print("Sailing!!!")

class Plane:
  def __init__(self, brand, model):
    self.brand=brand
    self.model = model

  def move(self):
    print("Flying!!!")

# Diff Class with same method:
c1=Car("Ford","Mustang")
b1= Boat("Ibiza", "Touring 20")
p1=Plane("Boeing", "747")

# Same method name but different classes.
for x in (c1,b1,p1):
  print(x.brand, ", ",x.model, end="\n")
  x.move()


print("Polymorphism with Inheritance:")
class Vehicle:
  def __init__(self, brand, model):
    self.brand=brand
    self.model = model

  def move(self):
    print("Driving!!!")

class Car(Vehicle): # The child class inherits the methods from the parent class.
  pass

class Boat(Vehicle):
  def move(self):
    print("Sailing!!!")

class Plane(Vehicle):
  def move(self):
    print("Flying!!!")

c1=Car("Ford","Mustang")
b1= Boat("Ibiza", "Touring 20")
p1=Plane("Boeing", "747")

for x in (c1,b1,p1):
  print(x.brand, ", ",x.model, end="\n")
  x.move()