'''
Types of Inheritance in Python:
1) Single Inheritance
2) Multiple Inheritance
3) Multilevel Inheritance
4) Hierarchical Inheritance
5) Hybrid Inheritance
'''


class Marvel:
  def __init__(self, name):
    self.name = name

  def show_details(self):
    print(f"Name: {self.name}")

class Avengers(Marvel):
  def __init__(self, name, team):
    super().__init__(name)
    self.team = team

  def show_details(self):
    print(f"Name: {self.name} Team: {self.team}")

class NewAvengers(Avengers):
  def __init__(self, name, team, potato_stuff):
    super().__init__(name, team)
    self.potato_stuff = potato_stuff

class FantasticFour(Marvel):
  def __init__(self, name, team):
    super().__init__(name)
    self.team = team

  def show_details(self):
    print(f"Name: {self.name} Team: {self.team}")

class XMen(Marvel):
  def __init__(self, name, team):
    super().__init__(name)
    self.team = team

  def show_details(self):
    print(f"Name: {self.name} Team: {self.team}")


team = Avengers("Marvel", "Avengers")
team.show_details()

fantastic_four = FantasticFour("Marvel", "Fantastic Four")
fantastic_four.show_details()

xmen = XMen("Marvel", "X-Men")
xmen.show_details()

new_avengers = NewAvengers("Marvel", "New Avengers", "Big Potato Stuff")
new_avengers.show_details()




'''
Parent1(Properties)+Parent2(Properties) = Child(Properties+Methods)
Mark 1 + Mark 2 = Mark 3 suit

'''

class Mark1:
  def __init__(self, name, feature1):
    self.name = name
    self.feature1 = feature1

  def show_details(self):
    print(f"Name: {self.name}, Feature 1: {self.feature1}")

class Mark2:
  def __init__(self, name, feature2):
    self.name = name
    self.feature2 = feature2

  def show_details(self):
    print(f"Name: {self.name}, Feature 2: {self.feature2}")


class Mark3(Mark1, Mark2):
  def __init__(self, name, feature1, feature2, feature3):
    Mark1.__init__(self, name, feature1)
    Mark2.__init__(self, name, feature2)
    self.feature3 = feature3

  def show_details(self):
    print(f"Name: {self.name}, Feature 1: {self.feature1}, Feature 2: {self.feature2}, Feature 3: {self.feature3}")

ironman = Mark3("Ironman", "Flight", "Repulsor Beam", "Titanium Plating")
ironman.show_details()
