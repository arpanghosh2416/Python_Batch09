def myfunc():
    print("Hello from myfunc!")
    global x
    x=300 #must declare x as global to modify the global variable x and have to initialize it before using it in innerFucn()
    def innerFucn():
        print("Hello from innerFunc!")
        print(f"x = {x}")
       


    innerFucn()

myfunc()
print(x)

print()
def func1():
    # nonlocal x2
    # x2="Jane"
    x1="Jane"
    def func2():
        nonlocal x1
        x1="John" #Local Variable x1 if it was non-local it would have been an enclosing variable for func2() and would have modified the value of x1 in func1()
    func2()
    return x1

print(func1())
# print(x2)  # This will raise a NameError because x2 is not defined in the global scope
# print(x1)  # This will raise a NameError because x1 is not defined in the global scope

