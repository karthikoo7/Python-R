#Required
def add(a,b):
    print(a+b)
    
add(3,5)
add(3)

#Default
def add(a,b=0,c=0):
    print(a+b)
    
add(3,5)
add(3)

#keyword

def add(a=0,b=0,c=0):
    print(a+b+c)
    
add(a=3,c=5)
add(3,b=3)


def display(id,nm,sal):
    print(f" Emp id is {id} name is {nm} and salary is {sal}")

display(4,"Ravi",7000)
display(id=3,nm="Ravi",sal=87979)
display(nm="Ravi",sal=87979,id=3)
display(3,nm="Ravi",sal=87979)

#variable length

def add(*b):
    sum=0
    print(b)
    print(type(b))
    for i in b:
        sum += i
    print(sum)
        

add()
print("--"*10)
add(1)
print("--"*10)
add(1,2,3,4,5,6,7,8,9,10)

#**kwargs

def display(rolno, nm, **marks):
    print(f" Rol no:{rolno}\n Name:{nm}")
    print(marks)
    print(type(marks))
    for k,v in marks.items():
        print(k," = ", v)

print("--"*10)
display(12,"Ravi", c=12,java=20)
print("--"*10)
display(11,"Radha", python=12,cpp=20,java=30)

#-----------------------------------------


#lambda

sqr=lambda x:x*x
print("--"*10)
print(sqr(5))
print("--"*10)
print(sqr(15))


add = lambda a,*b: a+sum(b)

print(add(2,3,4,5,6))


total = lambda **kwargs: sum(kwargs.values())
print(total(c=12,java=20))
print(total(python=12,cpp=20,java=30))
print(total(c=10))

#-------------------------------------
#builtin
print(abs(-3))
print("32+4")
print(eval("32+4"))



print(all([True, False]))
print(any([True, False]))
print("--"*10)
print(all([True, True]))
print(any([False, False]))
#-------------------------------------
#map

def sqr(n):
    return n*n

lst=[1,3,4,10,7]

print(map(sqr,lst))

print(list(map(sqr,lst)))

print(*(map(sqr,lst)))


#----------------

print(list(map(lambda n:n*n,lst)))
#----------------
lst=["Monday","Tuesday","Wednesday"]

print(list(map(lambda s:s[:3],lst)))


lst=["Monday","Tuesday","Wednesday"]

print(list(map(len,lst)))


lst=["Monday","Tuesday","Wednesday"]

print(list(map(str.upper,lst)))


a,b,c = list(map(int,input("enter3 nos: ").split()))
print(a,b,c)

#-------------------------------------
#filter

lst=[1,2,3,0,-2,-3,-4,9,6]

def isPositive(n):
    return n>0

print(list(filter(isPositive,lst)))


print(list(filter(lambda x:x<0,lst)))


#-------------------------------------
lst=["ABCD","pqr","LMN","xyz"]

print(list(filter(str.isupper,lst)))

print(list(filter(lambda x: len(x)==3,lst)))


#--------------------------
sum=0 #global

def add(a,b):
    global sum
    sum=a+b #local
    return sum

print(sum)
res= add(3,4)
print(sum)





























