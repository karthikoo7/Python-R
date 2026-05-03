no= int(input("Enter no"))
a=1
while a<=10:
    print(a*no)
    a+=1
else:
    print("Done with table printing")
    


#--------------------------------------
no= int(input("Enter no"))
a=1
while a<=10:
    print(a*no)
    a+=1
    if a==5:
        break
else:
    print("Done with table printing")


#--------------------------------------
range(1,10)
range(1, 10)
list(range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(10,1,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]
list(range(10,0,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#--------------------------------------
lst=[1,2,3,4,5]

for i in lst:
    print(i,"=",i*i)


for s in "Welcome":
    print(s)

#--------------------------------------
no=int(input("Enter no of lines"))

for i in range(1,no+1):
    for k in range(i):
        print("* ",end='')
    print()


for i in range(1,no+1):
    for k in range(i):
        print(i," ",end='')
    print()



for i in range(1,no+1):
    for k in range(i):
        print(k+1," ",end='')
    print()



for i in range(1,no+1):
    for sp in range(no,i,-1):
        print(" ",end="")
    for k in range(i):
        print("* ",end='')
    print()


#--------------------------------------
