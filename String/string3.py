#String Formatting with Wild Characters / Escape Characters
txt = "She said,\"Hello!\" and I said, \"Hi!\""
print(txt)
txt = "It\'s Python!"
print(txt)

txt = "This is a backslash: \\"
print(txt)

txt = "She said,\"Hello!\" and\nI said, \"Hi!\""
print(txt)

txt = "It\rPython and Java!"
print(txt)

txt = "It\tPython and Java!"
print(txt)
txt = "It\tPython \band Java!"
print(txt)

# Form Feed
txt = "It\fPython"
print(txt)

# Octal and Hexadecimal Values
txt = "\110\145\154\154\157"
print(txt)

txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
