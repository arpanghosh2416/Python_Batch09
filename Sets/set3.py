s1={1,2,3}
print(s1)

s1.add(4)
print(s1)



s1={1,2,3}
s1.update([4,5,6])
print(s1)

s1={1,2,3}
s1.update((4,5,6))
print(s1)


s1={1,2,3}
s2={4,5,6}
s1.update(s2)
print(s1)



s1.remove(2)
print(s1)

s1.discard(3)
print(s1)

s1.pop()
print(s1)
s1.pop()
print(s1)


del s1
# print(s1)