def myfunc():
    print("Hello from myfunc!")
    x=300 #Enclosing Variable x
    def innerFucn():
        print("Hello from innerFunc!")
        print(f"x = {x}")

    innerFucn()

myfunc()

# print(x)  # This will raise a NameError because x is not defined in this scope

print()
x1=200 #Global Variable x1
def myfunc():
    print("Hello from myfunc!")
    x=300
    def innerFucn():
        print("Hello from innerFunc!")
        print(f"x = {x}")
        print(f"x1 = {x1}")


    innerFucn()

myfunc()
print(x1)  # This will print 200 because x1 is defined in the global scope


print()
x=200
def myfunc():
    print("Hello from myfunc!")
    x=300
    def innerFucn():
        print("Hello from innerFunc!")
        print(f"x = {x}")
       


    innerFucn()

myfunc()
print(x)  # This will print 200 because x is defined in the global scope