x=["Arpan", "Depayan", "Dipan", "Disha","Aindrilla", "Rimi","Poulami", "Arijit", "arpan"]


x1=x.copy()
print(x1)


x1 = list(x)
print(x1)


x1=x[:]
print(x1)


# Join Lists

x1=[1,2,3]
x2=["A","B","C"]

x3 = x1+x2
print(x3)

# Another way of joining lists without using any 3rd variable - list
for i in x2:
    x1.append(i)
print(x1)


'''
Functions in List:
1) append 2) clear 3) copy 4) count 5) extend 6) index 7) insert 8) pop 9) remove 10) reverse 11) sort
'''



x=[1,1.14,1,2]
x1 = x.count(1)
print(x1)