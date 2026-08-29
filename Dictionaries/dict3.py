# Loop with Dictionaries:

thisdict={
  "name": "Arpan Ghosh",
  "Company": "TCS",
  "Role": ("Software Engineer","Cyber Operations"),
  "Interests":["Coding", "Web Development", "Data Science"]
}


# 1) Print all keys in dictionary

# for-Each Loop:
for i in thisdict:
  print(i) # i stands for keys, not index
print()

for i in thisdict.keys():
  print(i) # i stands for keys, not index
print()
# Print all values in dictionary
for i in thisdict:
  print(thisdict[i]) # i stands for keys, not index
print()
for i in thisdict.values():
  print(i) # i stands for values, not index
print()
# Print all key-value pairs in dictionary

print("First WAY:")
for i in thisdict.items():
  print(i) # i stands for key-value pairs, not index

print("Second WAY:")
for i,j in thisdict.items():
  print(f"{i}: {j}") 