import json

# Json to Object
# Json:
x='{"name": "Arpan Ghosh", "Company": "TCS", "Role": "Software Engineer", "Interests":"Software Engineer"}'
# Parsing(Converting Json to Dictionary) this json object to a dictionary
y = json.loads(x)

print(y) #Return Dictionary
print(y["name"])

# Object to Json
# Now this is a dictionary
x = {"name": "Arpan Ghosh", "Company": "TCS", "Role": "Software Engineer", "Interests":"Software Engineer"}
# Parsing(Converting Dictionary to Json) this dictionary to a json object
y = json.dumps(x)
print(y) #Return String
print(type(y)) #Return String

'''
Convert Python objects to JSON strings, and parse JSON strings into Python objects. The json module provides an easy way to encode and decode data in JSON format.
These objects are: list, dict, str, int, float, bool, and None. The json module can also be used to convert Python objects into JSON strings and vice versa. The json module provides the following methods:
- json.loads(): Parse a JSON string into a Python object.
- json.dumps(): Convert a Python object into a JSON string.
'''

print(json.dumps({"name": "Arpan Ghosh", "Company": "TCS", "Role": "Software Engineer", "Interests":"Software Engineer"})) #Return String
print(json.dumps(["apple", "bananas"])) #Return String
print(json.dumps(("apple", "bananas"))) #Return String
print(json.dumps("hello")) #Return String
print(json.dumps(42)) #Return String


# Json:
x='["apple", "bananas"]'
# Parsing(Converting Json to List) this json object to a list
y = json.loads(x)

print(y) #Return List
print(y[0]) #Return First Element of the List
print(type(y))