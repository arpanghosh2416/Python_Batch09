# Arbitrary Arguments:

def my_function(*kids):
  print("The youngest child is " + kids[2])
  print(type(kids))
  for i in kids:
    print(i)

my_function("Emil", "Tobias", "Linus")


def my_function(greet, *kids):
  print(type(kids))
  for i in range(len(kids)):
    print(greet, kids[i])

my_function("Hello","Emil", "Tobias", "Linus")