# Types of Methods:
'''
Instance Method:
It will use self keywords to access and modify object state and class state. It can access instance variables and class variables. These methods uses objects.

Class Methods:
Method belong to the whole class and not to any specific object. It can access class variables and attributes but not instance variables. It uses @classmethod decorator and uses cls keyword to access class variables and attributes.

Static Methods:
Method belong to the whole class and not to any specific object. It can access class variables and attributes but not instance variables. It uses @staticmethod decorator and does not use self or cls keywords. It is used to perform some utility functions.
'''


class Avengers:

  # Class Variable
  slogan="Avengers Assemble!"

  origin = "Earth's Mightiest Heroes: Avengers"

  # Instance Method
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def show_details(self):
    print(f"Name: {self.name}, Power: {self.power}")

  @classmethod
  def show_slogan(cls):
    # print(cls)
    # print(f"Name: {self.name}") --> This will give error because class method cannot access instance variable.
    print(f"Slogan: {cls.slogan}")
    # print(f"Origin: {cls.origin}")


  @staticmethod
  def show_origin():
    print(f"Origin: {Avengers.origin}")

thor = Avengers("Thor", "God of Thunder")
thor.show_details()
thor.show_slogan()
thor.show_origin()


# print(dir(thor))