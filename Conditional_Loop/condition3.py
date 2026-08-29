x=40
if x>10:
  print("x is greater than 10")
  if x>20:
    print("x is greater than 20")
  elif x>30:
    print("x is greater than 30")
  else:
    print("x is less than 30")
else:
  print("x is less than 10")


x=11
if x>10:
  pass # As if statement cannot be empty, and also you don't want to pass any kind of content, pass is used to avoid any errors. Pass is null operation, nothing happens when it executes
else:
  print(x)