s1={1,True,3.5,"Hello"}

# forEach loop to iterate through the set
for i in s1:
    print(i)

# This will raise an error because sets are not subscriptable
# for i in range(0,len(s1),2):
#     print(s1[i])

# i=0
# while i < len(s1):
#     print(s1[i])
#     i+=1


print("Hello" in s1) # True
print("Hello" not in s1) # False


# Change the items in set - Not possible because set is immutable
# Convert into List and change it and back to set.
s1={1,2,3,4,5}
l1=list(s1)
l1[0]=10
s1=set(l1)
print(s1) # {10, 2, 3, 4, 5}