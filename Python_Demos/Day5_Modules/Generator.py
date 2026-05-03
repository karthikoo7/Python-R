
def getValue():
    print("A")
    yield 10
    print("B")
    yield 20
    print("C")
    yield 30
    
g=getValue()
print(g)
print(type(g))


print(next(g))
print(next(g))
print(next(g))

#----------------------
for i in getValue():
    print(i)
    
#-----------------------

def getSquare():
    for i in range(1,101):
        yield i*i


g=getSquare()

for i in range(1,11):
    print(next(g))

#-----------------------
def getNew(no):
    while True:
        yield no
        no+=1


g= getNew(1)

print(next(g))
print(next(g))
print(next(g))

print("--"*20)

import math_util as mu
print(mu.pi)

print(mu.iseven(8))
print(mu.factorial(8))

print("--"*20)
print(next(g))
print(next(g))
print(next(g))





