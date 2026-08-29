#Types of Operators: Arithmetic Operators, Assignment Operators, Comparison Operators, Logical Operators, Identity Operators, Membership Operators, Bitwise Operators, Ternary Operators, Operator Precedence, Operator Associativity



#Arithmetic Operators
print(100+50)
print(100-50)
print(100*50)
print(100/50) #Returns the quotient of a division as a float
print(100%49) #Returns the remainder of a division
print(100//49) #Returns the quotient of a division, removing the decimal part(int) --> Floor Division
print(100**2) #Returns the value of x to the power of y


#Assignment Operators
x = 5
print(x)  
x += 3 #x = x + 3
print(x) 
x -= 3 #x = x - 3
print(x)
x *= 3 #x = x * 3
print(x)
x /= 3 #x = x / 3
print(x)
x %= 3 #x = x % 3
print(x) 
x %= 3 #x = x % 3
print(x)
x //= 3 #x = x // 3
print(x)
x **= 3 #x = x ** 3
print(x)
x=5
x &= 3 #x = x & 3
print(x)
x=5
x |= 3 #x = x | 3
x=5
x ^= 3 #x = x ^ 3
print(x)
x=5
x >>= 3 #x = x >> 3
print(x)
x=5
x <<= 3 #x = x << 3
print(x)
print(x := 5) #x = x : 5 #walrus operator, assigns values to variables as part of a larger expression. It is used in situations where you want to assign a value to a variable and use that value within the same expression. The walrus operator allows you to do this in a more concise way, without having to write the variable assignment on a separate line. It is often used in loops and conditional statements to simplify code and improve readability.

#Ternary Operators
a = 30
b = 20
x = a if a > b else b #x = a if condition else b
print(x)

#Comparison Operators
print(10 > 5) #Greater than
print(10 < 5) #Less than
print(10 == 5) #Equal to
print(10 != 5) #Not equal to
print(10 >= 5) #Greater than or equal to
print(10 <= 5) #Less than or equal to

#Chaining Comparison Operators
x = 10
print(5 < x <= 15) #Returns True if x is greater than 5 and less than 15
print(5 < x and x <= 15) #Returns True if x is greater than 5 and less than 15 < 15)

#Logical Operators
print(10 > 5 and 10 < 20) #Returns True if both statements
print(10 > 5 or 10 < 5) #Returns True if one of the statements is true
print(not(10 > 5 and 10 < 20)) #Returns False if both statements are true

#Identity Operators
x = 10
y = 10
#Equivalent to x == y
print(x is y) #Returns True if both variables are the same object
print(x is not y) #Returns False if both variables are the same object


#Membership Operators(deals with sequences like lists, tuples, strings)
x = "Hello World"
print('H' in x) #Returns True if a sequence with the specified value is present in the object
print('h' in x) #Returns False if a sequence with the specified value is not
print('h' not in x) #Returns True if a sequence with the specified value is not present in the object

# Bitwise Operators
x = 5 #In binary: 0101
y = 3 #In binary: 0011

x &= 3 #x = x & 3 #Bitwise AND: Compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, it is set to 0.
print(x)
x=5
x |= 3 #x = x | 3 #Bitwise OR: Compares each bit of the first operand to the corresponding bit of the second operand. If either bit is 1, the corresponding result bit is set to 1. Otherwise, it is set to 0.
x=5
x ^= 3 #x = x ^ 3 #Bitwise XOR: Compares each bit of the first operand to the corresponding bit of the second operand. If the bits are different, the corresponding result bit is set to 1. Otherwise, it is set to 0.
print(x)
x=5
x >>= 1 #x = x >> 1 #Bitwise Right Shift: Shifts the bits of the first operand to the right by the number of positions specified by the second operand [Signed Right Shift].
print(x)
x=5
x <<= 1 #x = x << 1 #Bitwise Left Shift: Shifts the bits of the first operand to the left by the number of positions specified by the second operand. [Zero fill Left Shift: Shifts the bits of the first operand to the left by the number of positions specified by the second operand. The empty positions on the right are filled with zeros.]
print(x)


#Operator Precedence
'''
1) Highest Precedence: Parentheses ()
2) Exponentiation **
3) Unary operators +x, -x, ~x
4) Multiplication *, Division /, Floor Division //, Modulus %
5) Addition +, Subtraction -
6) Bitwise Shift Operators <<, >>
7) Bitwise AND &
8) Bitwise XOR ^
9) Bitwise OR |
10) Comparison Operators ==, !=, >, <, >=, <=; Membership Operators in, not in; Identity Operators is, is not
11) Logical NOT not
12) Logical AND and
13) Logical OR or
14) Lowest Precedence: Assignment Operators =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=

Evaluation of expressions is done according to the operator precedence. Operators with higher precedence are evaluated before operators with lower precedence. If two operators have the same precedence, they are evaluated from left to right (left associativity) or from right to left (right associativity) depending on the operator.
'''

print(10 + 5 - 2) #10+5 ; 15-2 = 13