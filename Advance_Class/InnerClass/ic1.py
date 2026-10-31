class Outer:
  def __init__(self):
    self.name="Outer Class"
  # Creation of Inner Class inside Outer Class
  class Inner:
    def __init__(self):
      self.name="Inner Class"

    def inner_method(self):
      print("This is Inner class Method")

outer=Outer()
print(outer.name)
# Accessing Inner Class from the outside
inner=outer.Inner() #inner=Outer().Inner()
inner.inner_method()