thisdict={
  "name": "Arpan Ghosh",
  "Company": "TCS",
  "Role": ("Software Engineer","Cyber Operations"),
  "Interests":["Coding", "Web Development", "Data Science"]
}

# Copying a dictionary
portfolio = thisdict.copy()
print(portfolio)


# Copying a dictionary using dict() constructor
portfolio2 = dict(thisdict)
print(portfolio2)





# NESTED DICTIONARY:
career = {
  "company1":{
    "Name": "Arpan Ghosh",
    "Company": "Deloitte",
    "Role": ("Software Engineer","Cyber Operations"),
    "Experience": 2.5
  },
  "company2":{
    "Name": "Arpan Ghosh",
    "Company": "TCS",
    "Role": ["Software Engineer", "System Engineer"],
    "Experience": 1.5
  },
  "company3":{
    "Name": "Arpan Ghosh",
    "Company": "Young Architects",
    "Role": "CEO & Founder",
    "Experience": "N/A"
  }
}

print(career)
del career
# print(career["company3"]) # This will throw an error because the dictionary has been deleted

company1={
    "Name": "Arpan Ghosh",
    "Company": "Deloitte",
    "Role": ("Software Engineer","Cyber Operations"),
    "Experience": 2.5
  }
company2={
    "Name": "Arpan Ghosh",
    "Company": "TCS",
    "Role": ["Software Engineer", "System Engineer"],
    "Experience": 1.5
  }
company3={
    "Name": "Arpan Ghosh",
    "Company": "Young Architects",
    "Role": "CEO & Founder",
    "Experience": "N/A"
  }

print()
career = {
  "company1": company1,
  "company2": company2,
  "company3": company3
}

print(career)


print()
# Access items in a nested dictionary:
print(career["company1"]["Role"])


# Using Loop:
print()
for i, obj in career.items():
  print(f"{i}: {obj}")


# Using Nested FOR LOOP:

for i, obj in career.items():
  print(i)

  for y in obj:
    print(f"{y}: {obj[y]}")


company3={
    "Name": "Arpan Ghosh",
    "Company": "Young Architects",
    "Role": "CEO & Founder",
    "Experience": "N/A"
  }

# x1=company3.setdefault("Role","Founder")
# print("X1:")
# print(x1)
# print(company3)


x = company3.setdefault("Partership",3)
print()
print(x)
print(company3)

x = company3.update({"Partership": 4})
print()
print(company3)

x=('key1','key2','key3')
y=0

thisdict = dict.fromkeys(x,y)
print()
print(thisdict)

print()

x=('key1','key2','key3')

thisdict = dict.fromkeys(x)
print()
print(thisdict)
