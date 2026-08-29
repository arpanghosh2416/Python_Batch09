x=["Arpan", "Depayan", "Dipan", "Disha","Aindrilla", "Rimi","Poulami", "Arijit", "arpan"]

x.sort(reverse=True)
print(x)


'''
1) Sorting must be done for same data types:
Exception: Complex data types cannot be sorted.

2) False, True --> Ascending order; Hence False is a default value in boolean.
3) By Default Ascending order.
4) String:
a) Gets Compared by ASCII values and not the letters/alphabets. This whole thing is done in background process.

'''


# If you want to customize the Sort Function


def test(n):
  return abs(n-50)

x=[100,50,65,82,23,32]
x.sort(key=test)
print(x)





x=["Arpan", "Depayan", "Dipan", "Disha","Aindrilla", "Rimi","Poulami", "Arijit", "arpan"]

x.sort(key=str.upper,reverse=True)
print(x)



x=["Arpan", "Depayan", "Dipan", "Disha","Aindrilla", "Rimi","Poulami", "Arijit", "arpan"]

x.reverse() #Order Reverse; not sorting
print(x)