# WHat is Generator in Python?
# Generator is a function which gives multiple results; that can be iterated over one at a time. It uses the yield statement to return values one at a time, instead of returning all values at once like a normal function. Can pause and resume its execution. It is memory efficient as it generates values on the fly and does not store them in memory.

# Simple Generator Example
def test_gen():
  yield 1
  yield 2
  yield 3

for i in test_gen():
  print(i)


# Auto Generator Example
def auto_gen(n):
  count = 0
  while count <= n:
    yield count
    count += 1

for i in auto_gen(5):
  print(i)

# Note: return terminates the function and raises StopIteration exception, while yield pauses the function and returns a value. The next time the generator is called, it resumes execution from where it left off; can be called multiple times to get the next value in the sequence.

print()
def large_seq(n):
  for i in range(n):
    yield i

# for i in large_seq(100000000000000000000000):
#   print(i)

gen = large_seq(1000000)
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# With next keyword, you can manually iterate through the generator. It will raise StopIteration exception when there are no more values to yield.


def test_gen():
  yield 1
  yield 2
  yield 3

print()
gen = test_gen()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# print(next(gen))  # Raises StopIteration exception