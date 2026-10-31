class Person:
  # __init__ function will have default values
  def __init__(self, name, age=26):
    self.name=name
    self.age=age

p1=Person("Ram",24)
p2=Person("Arpan") #You are able to set initial values.
# p1.name="Depayan" You can always change the value
print(p1.name)
print(p1.age)
print()
print(p2.name)
print(p2.age)


# Multiple Parameters

class Person:
  # __init__ function will have default values
  def __init__(self, name,country,city, age=26):
    self.name=name
    self.age=age
    self.city=city
    self.country=country

p1=Person("Ram", "India", "Kolkata", 24)

print(p1.name,p1.country,p1.city,p1.age)
