# Using **kwargs allows you to pass a variable number of keyword arguments to a function. The keyword arguments are passed as a dictionary, where the keys are the argument names and the values are the argument values.

def my_function(**kid):
  print("His last name is " + kid["lname"])
  print(type(kid))

my_function(fname = "Tobias", lname = "Refsnes")



def my_function(username, **user_info):
  print("Username:", username)
  print("User Information:")
  for key, value in user_info.items():
    print(key + ":", value)

my_function("john_doe", age=30, email="john@example.com")