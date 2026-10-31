# lambda arguments: expression
# expression : a+b
x = lambda a,b : a+b

print(x(10,20))
# print(x()) <lambda>() missing 2 required positional arguments: 'a' and 'b'

x= lambda :10+10
print(x())

# Why Lambda functions are used?
# When u use anonymous function for a short period of time, you can use a lambda function instead of defining a full function using def. This is especially useful in situations where you need a simple function for a short duration, such as in higher-order functions like map(), filter(), and reduce().




def test(n,a):
    return a*n

x = test(2,5)
print(x)
x=test(3,5)
print(x)

def test(n):
    return lambda a : a*n

doubler = test(2)
tripler = test(3)
print(doubler(5))
print(tripler(5))


# anonymous function is a function that is defined without a name. In Python, anonymous functions are defined using the lambda keyword. Lambda functions can take any number of arguments but can only have one expression. The expression is evaluated and returned when the function is called.



num =[1,2,3,4,5,6,7,8,9]
double = list(map(lambda x : x*2,num))
print(double)


def myfunc(n):
    num = [1,2,3,4,5,6,7,8,9]
    num1 = []
    for i in num:
        double = i*n
        num1.append(double) 
    print(num1)

myfunc(2)

num =[1,2,3,4,5,6,7,8,9]
odd = list(filter(lambda x : x%2!=0,num))
print(odd)


stu = [("Arpan", 20), ("Depayan", 21), ("Dipan", 22), ("Disha", 23), ("Aindrilla", 24), ("Rimi", 25), ("Poulami", 26), ("Arijit", 27), ("arpan", 28)]

sort_stu= sorted(stu, key=lambda x : x[1])
print(sort_stu)

word = ["apple", "banana", "cherry", "date"]
sorted_word = sorted(word, key=lambda x : len(x))
print(sorted_word)

# Custom sorting where Lambda is used as a key function to sort the list of tuples based on the second element of each tuple. The sorted() function takes the list and the key parameter, which is a lambda function that extracts the second element (age) from each tuple for sorting.