# Private Methods

class Calculator:
  def __init__(self):
    self.result=0

  def __validate(self, num): # Private Method
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid Number")

cal =Calculator()
cal.add("abc")
print(cal.result)
cal.add(10)
print(cal.result)
# cal.__validate(5)
