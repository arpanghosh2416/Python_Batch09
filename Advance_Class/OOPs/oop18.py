#Abstract Method
'''
Abstract Class:
A class that cannot be instantiated  or that means for an abstract class we cannot create any objects and is meant to be subclassed. It can contain abstract methods that must be implemented by subclasses.

Abstract Method:
An abstract method is a method that is declared, but contains no implementation. Abstract methods are meant to be overridden in derived classes. An abstract method can only be defined in an abstract class. If a subclass does not implement all the abstract methods of its parent class, then it will also be considered an abstract class and cannot be instantiated.

Abstract method is defined using the @abstractmethod decorator from the abc module. The abstract method can be called from the subclass but cannot be called from the abstract class. The abstract method can be overridden in the subclass and can have its own implementation.
'''

from abc import ABC, abstractmethod


class Vehicle(ABC):

  @abstractmethod
  def start(self):
    pass

  @abstractmethod
  def stop(self):
    pass

class Petrol_Car(Vehicle):

  def start(self):
    print("Car started with ignition key")

  def stop(self):
    print("Car stopped with brake pedal")

petrolCar = Petrol_Car()
petrolCar.start()
petrolCar.stop()

class Electric_Car(Vehicle):

  def start(self):
    print("Car started with on button")

  def stop(self):
    print("Car stopped with off button")

electricCar = Electric_Car()
electricCar.start()
electricCar.stop()