# Set - Unordered, Unindexed and Immutable, No duplicates allowed; allows heterogeneous data types
s1={1,2,3}
s1={1,2,1}
print(s1) # {1,2} - duplicates are removed

s1={True,1,3.5,"Hello"}

s1={1,True,3.5,"Hello"}
# print(s1[0]) # TypeError: 'set' object is not subscriptable
print(s1)
print(type(s1)) # <class 'set'>

s1=set((1,2,3,4,5))
print(s1)