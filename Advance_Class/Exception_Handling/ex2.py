x=10

if not type(x) is int:
  raise TypeError("Only integers are allowed")

x=-1

if x<0:
  raise Exception("Negative numbers Exception")

# raise is the keyword to trigger custom made exceptions