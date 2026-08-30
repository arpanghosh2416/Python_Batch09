def changecase(func):
  def inner():
    return func().upper()
  return inner

@changecase
def myfunction():
  return "Hello World"

@changecase
def otherFunction():
  return "Hello Depayan"

print(myfunction())
print(otherFunction())


# Arguments in Decorators
def changecase(func):
  def inner(x):
    return func(x).upper()
  return inner

@changecase
def myfunction(name):
  return "Hello " + name

print(myfunction("Arpan"))


# *args and **kwargs in Decorators
def changecase(func):
  def inner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return inner

@changecase
def myfunction(name,surname):
  return "Hello " + name + " " + surname

print(myfunction("Arpan", surname="Ghosh"))