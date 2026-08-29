a= "Hello, World!"

# for loop does not require indexing variable beforehand.

# Only Strings
# forEach Loop
for i in a:
    if i==",":
        continue
    print(i, end="") #end="" is used to print the output in the same line

print("\n") 
# len can take any collections and return integer
# Only Collections(like list, set..)
for i in range(len(a)):
    if a[i]==",":
        break
    print(a[i], end="")


for x in range(6): # range(0,6)
  if x == 3: pass
  print(x)
else:
  print("Finally finished!")