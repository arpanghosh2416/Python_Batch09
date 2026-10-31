# Generator Expressions

# List Comprehension vs Generator Expression

list_comp = [x * x for x in range(5)]
print(list_comp)  # Output: [0, 1, 4, 9, 16]

gen_exp = (x * x for x in range(5))
print(gen_exp)  # Output: <generator object <genexpr> at 0x...>
print(list(gen_exp))  # Output: [0, 1, 4, 9, 16]

print()
total = sum(x * x for x in range(5))
print(total)  # Output: 30

print()
def fibo():
  a, b = 0, 1 # One-line initialization of variables
  while True:
    yield a
    a, b = b, a + b # a=b, b=a+b is a one-line swap of values


gen = fibo()
for i in range(10):
  print(next(gen), end=" ")  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34