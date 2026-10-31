# Just to Compile a program in Python - python -m py_compile <filename>.py
# Just to run a program in Python - python <filename>.py [Compile + Run]
# OR Just to run only- cd __pycache__ && <filename>.cpython-<version>.pyc/ python <filename>.cpython-<version>.pyc

try:
  print(x)
except:
  print("An exception occurred")

print()
print("Multi Exception Handling\n")
# Multi Exception Handling
try:
  print(10/0)
except NameError:
  print("Known Error Occured")
except ArithmeticError:
  print("Arithmetic Error - Cannot divide by Zero")
except: #Catch all other exceptions
  print("An unexpected error occurred")
else: #When no except block gets triggered, then it executes
  print("No Error")

print()
try:
  print(x)
  print(10/0)
except NameError:
  print("Name Error Occured")
except ArithmeticError:
  print("Arithmetic Error - Cannot divide by Zero")
except: #Catch all other exceptions
  print("An unexpected error occurred")
else:
  print("Status - Success")
finally:
  print("Always execute no matter what!!")
