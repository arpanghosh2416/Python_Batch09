import json

x={
  "name": "Arpan Ghosh",
  "Interests": "Software Engineer",
  "Job": [
    {
      "Company": "TCS",
      "Role": "Software Engineer",
      "Interests": "Software Engineer"
    }
  ],
  "married": False,
  "single": True,
  "age": 25,
}

print(json.dumps(x)) #Return String
print()
print(json.dumps(x, indent=4)) #Return String with Indentation
print()
print(json.dumps(x, indent=4, separators=("; ", " = "))) #Return String with Indentation and Custom Separators
print()
print(json.dumps(x, indent=4, sort_keys=True)) #Return String with Indentation and Sorted Keys