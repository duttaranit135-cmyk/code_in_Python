s={1,5,32,54,5,5,5,"ranit"}

e=set()# dont use s={} as it will create an empty dictionary

print(s,type(s))

s.add(566)
print(s)
s.clear()
print(s)


s1={1,55,22,1,55,21}
s2={1,36,55,22,56,70}

print(s1.union(s2))
print(s1.intersection(s2))
