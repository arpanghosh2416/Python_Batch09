# Decorator with Arguments with Nested Function
def changecase(arg): #arg= "upper"
  def outer(func): #func = myfunction              
    print("Inside outer function", func.__name__) #Meta Data - information about the data.
    print("Inside outer function", func)

    def inner(*args, **kwargs):
      if arg == "upper":
        return func(*args, **kwargs).upper()
      elif arg == "lower":
        return func(*args, **kwargs).lower()
      else:
        return func(*args, **kwargs)
    return inner
  return outer

@changecase("upper")  #arg= "upper"
def myfunction():  # func = myfunction
  return "Hello World"

print(myfunction())


# Multi Decorators
def changecase(func):
  def inner():
    return func().upper()
  return inner

def addgreeting(func):
  def inner():
    return "Hello " + func()
  return inner


@changecase
@addgreeting
def myfunction():
  return "World"

print(myfunction())

# Function Meta Data:

def changecase(func):
  def inner():
    return func().upper()
  return inner

@changecase
def myfunction():
  return " Hello World"


print(myfunction.__name__) # myfunction
print(myfunction.__doc__) # None