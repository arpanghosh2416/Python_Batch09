# Inheritance
# Parent Class
class Person:
  college="IEM"
  def __init__(self, name, age):
    self.name=name
    self.age=age

  def display(self):
    print(self.name,self.age)
    print(self.college)

# print("From Parent Class")
# x=Person("Arpan", 25)
# x.display()

# When in Child Class, __init__ function is written, then the child no longer inherits the Parent Properties. For that there are two ways to achieve Constructor Overriding.

# Child Class
class Student(Person):
  def __init__(self, s_name, s_age,year):
    # 1st way:
    # Person.__init__(self, s_name, s_age) #Parent Method Call
    # 2nd way:
    super().__init__(s_name, s_age) #Parent Method Call
    self.graduate_year=year

  def display(self):
    super().display() #Parent Method Call in a normal method
    print(self.graduate_year)
    

print("From Child Class:")
s1 = Student("Depayan", 23,2025)
s1.display()
