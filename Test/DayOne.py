

s={10,20,30,40,50,60,10}
print(s)
print(type(s))

# len
print(len(s))

#No particular value

# ADDING
s={10,20,30,40,50,60,10}
m={22,33,44}
s.update(m)
print(s)

# REMOVE
s={10,20,30,40,50,60}

s.pop()
print(s)

s.remove(60)
print(s)

s.discard(111)
print(s)


s={10,20,30,40,50,60,10}

x = sorted(s)
print(x)

s={" ","&","7","M","m"}
print(max(s))
print(min(s))


s={1,2,3,4,5}
m={5,6,7,8,9}

# INTERSECTION(COMMON VALUES)
print(s.intersection(m))

# SYMETRIC DIFF(UNCOOMON VALUE IN BOTH THE SET)
print(s.symmetric_difference(m))

# DIFFEREENCE(UNCOMMON VALUES IN SET1)
print(s.difference(m))

u = s.union(m)
print(u)


s={10,20,30,40,50,60,10}

print("---ENAHCHED FOR LOOP---")
for i in s:
    print(i)

print("---ENUMERATOR FOR LOOP---")
for i,j in enumerate(s):
    print(i,"--->",j)























