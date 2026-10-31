# import module1 #importing module1.py file in module2.py file
# Re-Name a module1.py file as module1 and import it in module2.py file
import module1 as m1

m1.greet("Arpan")

# Variables from module1
a=m1.person1["age"]
print(a)
b=m1.person1["country"]
print(b)
c=m1.person1["name"]
print(c)

# Using dir() for custom made module
x= dir(m1)
print(x)  

'''
Syntax:
Only function:
module_name.function_name()

With class and function:
module_name.class_name.function_name()
'''
