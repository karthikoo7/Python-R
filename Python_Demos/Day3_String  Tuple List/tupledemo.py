#--------------------------------------

t1=() #empty
t2=(1,2,3,4)
a=10
b=20
t3=(a,b)

t4=1,2,3

print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))

#--------------------------------------

t5=(10)
print(type(t5))

t6=(10,)
print(type(t6))
#--------------------------------------


t=(10,20,30,1,2,3)

#1
print(t)

#2
for i in t:
    print(i)

#3 
for i in range(len(t)):
    print(t[i])

print("--"*30)
print(len(t))
print(min(t))
print(max(t))
print(tuple([100,"ABC",67.5]))


#--------------------------------------
t1=(1,2)
t2=(10,20)

print(t1+t2)
print(t1*4)

print(t1==t2)
print(t1<t2)

print(20 in t2)
print(20 in t1)


#--------------------------------------
t1=(1,2)
t2=(10,20)
t3=t1

print(t1 is t2)
print(id(t1))
print(id(t2))

print("-------------------")
print(t1 is t3)
print(id(t1))
print(id(t3))

#--------------------------------------
t1=(1,2)
t2=(10,20,10,10,30)
t3=t1

print(t2.count(10))
print(t2.index(20))

#--------------------------------------
