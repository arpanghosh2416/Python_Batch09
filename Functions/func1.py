def test(n):
  print(n)

test("Hello World")
test(1)
test(1.14)

# Argument in Function Brackets is know as Formal Argument
# Call Argument --> Actual Arguments

# If u want to directly print it, then use print function; If you want to use the value in a variable and then utilize it somewhere, then use return function.

# Positional Arguments
def test1(n,m):
  return n+m

result = test1(5,10)
print(result)


#Default Arguments/Parameters

def test2(n, m=5):
  return n+m

result = test2(5)
print(result)

result = test2(5,10)
print(result)


# Keyword Arguments

def test3(n, m):
  print(n+m)
        
test3(n=5, m=10)

# Mixing Positional and Keyword Arguments:
def test4(n, m, p):
  print(n+m+p)

test4(5, m=10, p=15)


# Dictionary as an Argument in Function
def test5(n):
  print(n)

test5({"name": "Alice", "age": 30})


def test5(n):
  print("Name:", n["name"])
  print("Age:", n["age"])

data={"name": "Alice", "age": 30}
test5(data)


# Only Positional Arguments:

def test6(n, m, /):
  print(n+m)


test6(5, 10)


# Only Keyword Arguments:
def test7(*, n, m):
  print(n+m)

test7(n=5, m=10)


# Combining ONLY Positional and ONLY Keyword Arguments:
def test8(n, m,/, *, p, q):
  print(n+m+p+q)

test8(5, 10, p=15, q=20)