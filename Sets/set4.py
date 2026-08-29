# Union -> OR; Intersection -> AND

s1={1,2,3,4,10,11}
s2={4,5,6,7,10}
s4={6,7,8,9,10,11}
s3=s1.union(s2,s4)
print(s3)

s3=s1|s2|s4
print(s3)
s1.update(s2,s4)
print(s1)

# Union and Update method are both same


s1={1,2,3,4,10,11}
s2={4,5,6,7,10}
s4={6,7,8,9,10,11}
s3=s1.intersection(s2,s4)
print(s3)
s3=s1&s2&s4
print(s3)

# intersection and intersection_update method are both same
s1.intersection_update(s2,s4)
print(s1)


# DIFFERENCE -> A-B; SYMMETRIC DIFFERENCE -> A^B


s1={1,2,3,4,10,11}
s2={4,5,6,7,10}
s4={6,7,8,9,10,11}
s3=s1.difference(s2)
print(s3)
s3=s1.difference(s2,s4)
print(s3)
s3=s1-s2-s4
print(s3)
s1.difference_update(s2)
print(s1)

s1={1,2,3,4,10,11}
s2={4,5,6,7,10}
s4={6,7,8,9,10,11}
s3=s1.symmetric_difference(s2)
print(s3)
s3=s1^s2
print(s3)
s3=s1.symmetric_difference(s2)
print(s3)
s3=s1^s2
print(s3)

s1.symmetric_difference_update(s2)
print(s1)

s1=frozenset(s1)
print(s1)
print(type(s1))

a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))


a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)


a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)
