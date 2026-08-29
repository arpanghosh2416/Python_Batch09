#String Mehtods

txt = "hello World!"

print(txt.capitalize()) #First letter is capitalized
print(txt.casefold()) #Converts string into lower case
print(txt.lower()) #Converts string into lower case
print(txt.upper()) #Converts string into upper case
print(txt.center(100)) #Returns a centered string
print(txt.count("o")) #Returns the number of times a specified value occurs in a string
print(txt.encode()) #Returns an encoded version of the string
print(txt.endswith("!")) #Returns true if the string ends with the specified value
txt = "It\tPython and Java!"
print(txt) #default value of tab is 8 i.e equivalent of expantabs(8)
print(txt.expandtabs(10)) #Sets the tab size of the string
txt = "hello World!"
print(txt.find("O")) #Searches the string for a specified value and returns the position of where it was found. -1 if not found, index will be not in that range.
txt = "The price of 1 Dollar is {price:.1f} dollars" 
print(txt.format(price = 10.5)) #Formats specified values in a string
txt = "hello World!"
print(txt.index("World")) #Searches the string for a specified value and returns the position of where it was found. ValueError if not found, index will be in that range.

print(txt.isalnum()) #Returns True if all characters in the string are alphanumeric
print(txt.isalpha()) #Returns True if all characters in the string are in the alphabet
print(txt.isdecimal()) #Returns True if all characters in the string are decimals
print(txt.isdigit()) #Returns True if all characters in the string are digits
print(txt.isascii()) #Returns True if all characters in the string are ascii characters
print(txt.islower()) #Returns True if all characters in the string are lower case
print(txt.isupper()) #Returns True if all characters in the string are upper case
print(txt.isprintable()) #Returns True if all characters in the string are printable
a1= "                   "
print(a1.isspace()) #Returns True if all characters in the string are whitespaces
print(txt.isnumeric()) #Returns True if all characters in the string are numeric
print(txt.isidentifier()) #Returns True if the string is an identifier
print(txt.istitle()) #Returns True if the string follows the rules of a title
print(txt.title)
txt = txt.encode()
print(memoryview(txt)) #Returns a memory view object of the given argument
txt = "Hello Sam!"
print(txt.title())

#use a dictionary to with ascii codes {83: "S", 80:P}
mydict = {83: 80}
txt = "Hello Sam!"
print(txt.translate(mydict)) #Returns a translated string