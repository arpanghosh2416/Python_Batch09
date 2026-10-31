# Encapsulation use to protect and validate data:

class Student:
  def __init__(self,name):
    self.name=name
    self.__grade=0 # __(double underscore) represents private

  # Setter - Validate then set data
  def set_grade(self, grade):
    if 0<=grade<=100:
      self.__grade=grade
    else:
      print("Grade must be between 0 and 100")

  # Getter
  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >=60:
      return "Pass"
    else:
      return "Failed"

s1 = Student("Arpan")
s1.set_grade(40)
# print(s1.__grade)
print(s1.get_grade())
print(s1.get_status())
