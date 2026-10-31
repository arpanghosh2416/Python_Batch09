class Person:
  college="IEM"
  def __init__(self, name, age):
    self.name=name
    self.age=age
    print(self)
  # def __init__(self, name1):
  #    self.name1=name1
  

p1 = Person("Arpan",25)
# print(p1)

p2= Person("Dipayan",23)

# print(p2)


'''
In Python, self represents the specific instance of the class that you just created. It is not a special keyword (you could technically name it anything, though self is the strict standard), but rather a naming convention for the first parameter of an instance method.
Here is exactly what self does and what it returns:

What self Does

When you write a class, it acts as a blueprint. When you create an object from that blueprint, you are creating an "instance."
self binds the attributes and methods to that specific instance. It allows the object to remember its own data and access its own methods.


What self Returns

By default, self doesn't "return" anything because it is a parameter (an input), not a function.
However, if you print self inside a method, it evaluates to the memory address and identity of the current object.
'''