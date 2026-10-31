# Practical Example
# Imagine Car Engine is Inner class and Car is the outer class

class Car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
    self.engine=self.Engine() #Initialize Inner class object

  class Engine:
    def __init__(self):
      self.status="Off"

    def start(self):
       self.status="On"
       print("Engine Started and Running")

    def stop(self):
      self.status="Off"
      print("Engine Stopped")

  def drive(self):
    if self.engine.status=="On":
      print("Car is Moving")
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Engine is not Running")


car=Car("Ford", "Mustang")
car.drive()
car.engine.start()
car.drive()
