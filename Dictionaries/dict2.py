thisdict={
  "name": "Arpan Ghosh",
  "Company": "TCS",
  "Role": ("Software Engineer","Cyber Operations"),
  "Interests":["Coding", "Web Development", "Data Science"]
}
print(thisdict)
# Update Dictionary using update() method
thisdict.update({"Company": "Young Architects"})
print(thisdict)

thisdict.update({"Age": 25})
print(thisdict)


# Removing items from the dictionary
thisdict.pop("Age")
print(thisdict)

thisdict.update({"Age": 25})
print(thisdict)

thisdict.popitem() #Removes the last inserted item from the dictionary
print(thisdict)

thisdict.update({"Age": 25})
print(thisdict)

del thisdict["Age"] #Removes the item with the specified key name
print(thisdict)


thisdict.clear() #Removes all the items from the dictionary
print(thisdict)


del thisdict #Deletes the dictionary completely

# print(thisdict) #This will raise an error because the dictionary no longer exists