def countdown(n):
  if n<= 0:
    print("Done!")
  else:
    print(n)
    # print("Testing...",n-1)
    # print("Testing-1 ..",countdown(n-1))
    countdown(n-1)

countdown(5)

print("\n")
def factorial(n):
  if n == 0 or n==1: #Base Case
    return 1
  else:
    # print("Current n:", n)
    # print("Testing...",n-1)
    # print("Testing-1 ..",factorial(n-1))
    # print("Current factorial:", n * factorial(n-1))
    return n * factorial(n-1) #Recursive Case

print(factorial(5))