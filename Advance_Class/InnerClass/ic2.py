class Outer:
  #Outer class
  def __init__(self):
    self.name="Arpan"
  # Accessing Outer class from Inner Class
  class Inner:
    def __init__(self,outer):
      self.outer=outer

    def inner_method(self):
      print(f"Outer class name: {self.outer.name}")

outer=Outer()
inner=outer.Inner(outer)
inner.inner_method()