#set demo

# unordered collection of Unique element
s={1,2,3,4,15,2,4,6,7,90}
print(s)
print(type(s))

s={}
print(type(s)) #<class 'dict'>

s=set() #empty set
print(type(s))
#-------------------------------------------
#Add
print(s)
s.add(12)
s.add(5)
s.add(10)

print(s)

s.update([6,8])
print(s)
#-------------------------------------------
#delete
s.remove(8)
print(s)

s.discard(5)
print(s)


s.remove(18)
print(s)

s.discard(15)
print(s)
#-------------------------------------------
#display
print(s)

for i in s:
    print(i)
#-------------------------------------------
s1={1,2,3,4}
s2={3,4,5,6}

print(s1.union(s2))#{1, 2, 3, 4, 5, 6}
print(s1 | s2) #{1, 2, 3, 4, 5, 6}


print(s1.intersection(s2))#{ 3, 4}
print(s1 & s2) #{ 3, 4}

print(s1.difference(s2)) #{1, 2}
print(s1-s2) #{1, 2}

print(s2.difference(s1)) #{5, 6}
print(s2-s1) #{5, 6}


dir(set)


#---------------------------------
s={1,2,3,4,5}
fs=frozenset(s)
print(fs)
print(type(fs))

fs.add(10) #AttributeError: 'frozenset' object has no attribute 'add'
fs.remove(2) #AttributeError: 'frozenset' object has no attribute 'remove'

#---------------------------------






