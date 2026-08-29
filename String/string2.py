#String Array
a= "Hello, World!"

print(a[0])
print(a[1])
# Slicing
print(a[2:5])
print(len(a))
print(a[:5])
print(a[2:5]) #2:len(a)
print(a[-5:-2]) #index is reversed

#in is a keyword in python which is used to check if a value is present in a sequence or not. It returns True if the value is found in the sequence, otherwise it returns False.
print("Hello" in a) #True


# Functions in String
a1= "           Hello,          World!        "
print(a1)
print(a1.upper()) #HELLO, WORLD!
print(a1.lower()) #hello, world!
print(a1.strip()) #Hello, World! --> removes any whitespace from the beginning and end

a1= "Hello, World!"
print(a1.replace("Hello", "Hi")) #Hi, World! --> replaces the old string with the new string
a1= "Hello, World!"
print(a1.split(" ")) #['Hello', ' World!'] --> splits the string into a list of substrings based on the specified separator (in this case, a comma)

# String Concatenation
a="Hello"
b="World"
print(a+b) #HelloWorld --> concatenation of two strings
print(a+", "+b) #Hello World --> concatenation of two strings with a space in between


age = 27
# txt = "My age is" + age #TypeError: can only concatenate str (not "int") to str
txt = "My age is " + str(age) #My age is 27 --> concatenation of string and integer (age is converted to string using str() function)
print(txt)

# F-Strings

age = 25 #age is an integer variable
txt = f"My age is {age}" #My age is 25 --> f-string is used to format the string and insert the value of age variable in the string
print(txt)


price = 95.54
txt = f"The price of 1 Dollar is {price:.1f} dollars" #The price is 95.54 dollars --> f-string is used to format the string and insert the value of price variable in the string with 2 decimal places
print(txt)

txt = f"The price of 1 Dollar is {price + 2} dollars"  #The price is 95.54 dollars --> f-string is used to format the string and insert the value of price variable in the string with 2 decimal places 
print(txt) 