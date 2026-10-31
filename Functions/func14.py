# Fibonacci sequence

# 0,1,1,2,3,5,8,13,21,....n

# We can use recursion to find the nth number in the Fibonacci sequence.

def fibonacci(n):
  if n<=1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7)) # 7th number in the Fibonacci sequence is 13.

# All Fibonacci numbers up to n but in recursion

# 0,1,1,2,3,5,8,13,21,....n
#  Step 1: Initialize a list to store the Fibonacci numbers.
# Step 2: Initialize the first two Fibonacci numbers in the list. [0,1]
# Step 3: Add the sequence numbers, n-1 and n-2, to the list until we reach the nth number.
def fibonacci_sequence(n):
  if n<=0: #base case
    return [] # breaking the recursion
  elif n==1: #base case
    return [0]
  elif n==2: #base case
    return [0,1]
  else: #recursive case
    seq = fibonacci_sequence(n-1)
    print(seq)
    seq.append(seq[-1] + seq[-2])
    return seq

print(fibonacci_sequence(7)) # First 7 Fibonacci numbers are [0, 1, 1, 2, 3, 5, 8]