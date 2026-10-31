class Person:
  college="IEM" # class property - shared by all objects
  def __init__(self, name, age):
    self.name=name  # instance/object property - exclusive inside init property only
    self.age=age
  
  # self.name="Arpan" self cannot be a class property.
  def display(self): # display is also a instance property
      print(self.name,self.age)
      # print(self.college)

  # def test():
  #    print(species)
  #    print(name)
  #    print(age)

p1=Person("Arpan",25)
p2=Person("Dipayan", 23)
p1.display()
print(p1.college)
p2.display()
p2.college="UEM" #Modify class property with object
print(p2.college)
print()
Person.college="NIT" #Modify class property but no involvement of the object
p1.display()
print(p1.college)
p2.display()
print(p2.college)
p1.state= "Hyderabad"
print(p1.state)
# print(p2.state)