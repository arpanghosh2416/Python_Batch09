# LEGB rule: Local, Enclosing, Global, Built-in
'''
1. Local: Variables defined within a function and accessible only within that function.
2. Enclosing: Variables defined in the local scope of enclosing functions, accessible to nested functions
3. Global: Variables defined at the top level of the module, accessible throughout the module.
4. Built-in: Variables that are pre-defined in Python, accessible in all modules.
'''

x="Global variable x"

def outer():
    x="Enclosing variable x"
    def inner():
        x="Local variable x"
        print(x)  # This will print "Local variable x" because the local scope takes precedence over enclosing and global scopes
    inner()
    print(x)  # This will print "Enclosing variable x" because the enclosing scope takes precedence over the global scope
outer()
print(x)  # This will print "Global variable x" because the global scope is accessed when there are no local or enclosing variables with the same name