import functools

# functools.wrap to preserve the original function's metadata when it is decorated. This is important for debugging and introspection, as it allows the decorated function to retain its original name, docstring, and other attributes.

def changecase(func):
  @functools.wraps(func)
  def inner():
     print(func)
     return func().upper()
  return inner

@changecase
def myfunction():
  return " Hello World"


print(myfunction.__name__)
print(myfunction())
print(myfunction)

