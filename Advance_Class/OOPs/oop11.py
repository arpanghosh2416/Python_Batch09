# Encapsulation:
# Binding data and functions into a single unit.
class Person:
  def __init__(self, userid, pwd):
    self.id=userid
    # I have to make it encapsulated - To achieve it, I have to make pwd as private property
    self.__pwd=pwd

    # GETTER and SETTER

  def get_pwd(self): #Get your Password
    return self.__pwd
  
  def set_pwd(self, newpwd): #Will set a new pwd if needed
    self.__pwd=newpwd

  def display(self):
    print(self.id)
    # print(self.pwd)
    # print(self.__pwd)
    print(self.get_pwd())

x=Person("Arpan", 123)
x.display()

x.set_pwd(456)
x.display()


x2 = Person("ABC", 789)
x2.display()
