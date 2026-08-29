# Dictionaries - Ordered, Changeable, Does not allow duplicates, Heterogeneous(Data-Types)
# Does not allow duplicates means that the dictionary cannot have two items with the same key. If you try to create a dictionary with duplicate keys, the last value will overwrite the previous one.

thisdict={
  "name": "Arpan",
  "name": "Arpan Ghosh",
  "Company": "TCS",
  "Role": "Software Engineer",
  "Interests":"Software Engineer"
}

print(thisdict)
print(thisdict["name"])
print(thisdict["Company"])

print(len(thisdict)) #Returns the number of items in the dictionary
print(type(thisdict))




thisdict={
  "name": "Arpan Ghosh",
  "Company": "TCS",
  "Role": ("Software Engineer","Cyber Operations"),
  "Interests":["Coding", "Web Development", "Data Science"]
}
print(thisdict["Role"])

# Accessing the values of the dictionary using keys
x=thisdict["Interests"]
print(x)
print(type(x))
x=thisdict["Role"]
print(x)
print(type(x))


x=thisdict.get("Company")
print(x)

x=thisdict.keys()
print(x)

thisdict["age"] = 25
print(thisdict)

x=thisdict.keys()
print(x)


x=thisdict.values()
print(x)

x=thisdict.items()
print(x)


# Update Values of any key in the dictionary
thisdict["Company"] = "Young Architects"
print(thisdict)



# Check if a key exists in the dictionary
if "name" in thisdict:
  print("Yes, 'name' is one of the keys in the thisdict dictionary")