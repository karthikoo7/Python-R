#Dictionary

d={}
print(type(d))

d={1:10,2:20,3:30}
print(d)

d={'NAme':'Ravi','Age':34,'Marks':56.6,10:[1,2,3]}
print(d)

d= dict(a=1,b=2)
print(d)
#-----------------------------
#Display

#1
print(d)

#2
for i in d:
    print(i)

#3
for i in d:
    print(i,d[i])
    
#4
for i in d.keys():
    print(i)

#5
for i in d.values():
    print(i)  
    
#6
for i in d.items():
    print(i)

#7
for k,v in d.items():
    print(k,v)
#-------------------------------------
#Insert , Update

d={}
for i in range(3):
    key=input("ENter Key")
    value=input("Enter Value")
    #d[key]=value
    d.update({key:value})

print(d)

#-------------------------------------
#merge
d={'a':1,'b':2}
d1={'c':3,'d':4}

d.update(d1)
print(d)

#**
d={'a':1,'b':2}
d1={'c':3,'d':4,'b':10}

d3={**d,**d1}
print(d3)

d4=d |d1
print(d4)

#-------------------------------------
d={'a': 1, 'b': 10, 'c': 3, 'd': 4}

del d['a']
print(d)

print(d.pop('b'))
print(d)

print(d.popitem())
print(d)

d.clear()
print(d)

del d
#-------------------------------------
#operators
d={'a': 1, 'b': 10, 'c': 3, 'd': 4}
d1={'a': 1, 'b': 10, 'c': 3, 'd': 4}

print(d['a'])
print(d==d1)

print('b' in d)
print('b1' in d)
#-------------------------------------
#Functions
d={'a': 1, 'b': 10, 'c': 3, 'd': 4}
print(len(d))
print(min(d))
print(max(d))
print(max(d.values()))

#-------------------------------------
#methods
d={'a': 1, 'b': 10, 'c': 3, 'd': 4}

print(d.get('a'))
print(d.get('a1'))
print(d.get('a1',10))
print(d)

print(d['a1'])
#--------------------------------
print(d)
print(d.setdefault('a',100))
print(d.setdefault('a1',100))
print(d)

#--------------------------------

lst=[1,2,3,4,5]
d1=dict.fromkeys(lst)
print(d1)

d1=dict.fromkeys(lst,100)
print(d1)

#------------------------------------------------
#Advance Functions

#1 Zip

lst=[1,2,3,4,5]
lst1=[10,20,30,40,50]

d= dict(zip(lst,lst1))
print(d)


lst=[1,2,3,4,5,6,7,8,9]
lst1=[10,20,30,40,50]

d= dict(zip(lst,lst1,strict=False))
print(d)

#----------------------------
d={10: 100, 21: 200, 3: 300, 14: 400, 5: 500}
print(d)
print(dict(sorted(d.items())))

print(dict(reversed(d.items())))

#----------------------------
#Dict comprehenssion
d ={k:k*k for k in range(1,21)}
print(d)


d ={k:k*k for k in range(1,21) if k%3==0}
print(d)


d ={k:[k*k,k**3] for k in range(1,21)}
print(d)


d={'a': 1, 'b': 10, 'c': 3, 'd': 4}

d1={v:k for k,v in d.items()}
print(d1)


d={'id':10,'city':'Pune'}

d['Location']=d.pop('city')
print(d)




