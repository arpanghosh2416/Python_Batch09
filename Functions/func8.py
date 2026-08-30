def changecase(func):
  def inner():
    return func().upper()
  return inner

# Decorators
@changecase
def test():
  return "Hello World"

# Without Decorators
# test = changecase(test)
print(test())