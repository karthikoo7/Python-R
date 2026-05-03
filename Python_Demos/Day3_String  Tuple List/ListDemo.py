



lst=[] #empty list

lst1=[1,2,3,4,5]

lst2=[1,23.45,(1,2,3)]

print(lst)

print(lst1)
print(lst2)

print("------------------------")


t1=(1,2,[3,4])

print(t1)

(t1[2]).append(5)
print(t1)


#t1[2]=100 #Error
print(t1)


#--------------------------------------
a,*b=10,20,30
print(a)
print(b)
print("-----------"*3)


*a,b=10,20,30
print(a)
print(b)
print("-----------"*3)



a,*b,c=10,20,30,40,50
print(a)
print(b)
print(c)
print("-----------"*3)

a,b=[100,200]
print(a)
print(b)

#--------------------------------------
lst=[1,2,3,4,5]

#1
print(lst)

#2

for i in lst:
    print(i)


#3
for i in range(len(lst)):
    print(i, lst[i])


#--------------------------------------
#add element  
lst=[]
for i in range(5):
    no=int(input("ENter list ele: "))
    lst.append(no)

print(lst)

lst.insert(2,500)
print(lst)

lst.insert(-1,300)
print(lst)

#--------------------------------------
lst=[1,2,3,4,5]

lst[3]=100
print(lst)

lst[1:4]= 10,20,30

print(lst)

lst=['s','p','w']

print(lst)
#--------------------------------------
#delete
lst=[1,2,3,4,5]
print(lst)
del lst[1]
print(lst)
del lst[2:4]
print(lst)
del lst

print(lst)


#--------------------------------------
#delete
lst=[1,2,3,4,5]
print(lst)

print(lst.pop())
print(lst)


print(lst.pop(2))
print(lst)

print("----------------------------")
lst.remove(4)
print(lst)

print("---------clear-------------------")
lst.clear()
print(lst)
#--------------------------------------
#List Operators

l1=['a','b']
l2=['c','d']

print(l1+l2)

print(l1*3)

print(l1== l2)

print('a' in l1)

print(l1 is l2)


#--------------------------------------


#function

lst=["pune","satara","nagpur","beed"]

print(len(lst))
print(min(lst))
print(max(lst))
print(list((1,2,3)))
#--------------------------------------

#methods
lst=[2,4,6,7,1,9]
print(lst)
lst.sort()
print(lst)

print(lst.sort()) #None

lst.reverse()
print(lst)



lst2=[10,100]

lst.extend(lst2)
print(lst)
print(lst2)

#count
#index

#--------------------------------------
#list comprehenssion
lst1=[x for x in range(1,101)]
print(lst1)

lst1=[x for x in range(1,101) if x%7==0]
print(lst1)

lst=[1,2,3,4,5]
lst2=[x*x for x in lst]
print(lst2)


lst=["pune","satara","nagpur","beed"]
lst2=[x.upper() for x in lst]
print(lst2)

lst3=[x[:3] for x in lst]
print(lst3)
#-----------------------------------------
#unique Element
lst=[1,3,4,5,2,4,3,7,8,9,3]
print(set(lst)) # 1,3,4,5,2,7,8,9



lst1=[]

for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)