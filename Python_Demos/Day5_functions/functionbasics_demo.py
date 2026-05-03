#empty function
def greetuser():
    pass

def greet():
    print("Welcome ")

greet()

print(greet())

#------------------------
def greet(name):
    print(" Welcome ", name)
    
greet("Radha")
greet("Students")

#------------------------
#docstring
def greet(name):
    ''' this is greet function taking name as parameter
    use to greet users'''
    print(" Welcome ", name)
    
greet("Radha")
greet("Students")

print(greet.__doc__)

print(help(greet))

#------------------------
def sqr(n):
    return n*n


res= sqr(5)
print(res)

print(sqr(10))
    
#------------------------
def calc(a,b):
    return a+b,a-b,a*b,a/b

a,s,m,d = calc(10,5)
print(a,s,m,d)

res=calc(100,5)
print(res)   
    
#--------------------------
calculator=calc
print(type(calc))
print(type(calculator))
    
res=calculator(100,5)
print(res)    
    
#--------------------------

def add(a,b):
    print(a+b)

add(5,3)    
add(5.9,3)  
add(5,3.4)  
add(5.7,3.1)  
add([5,3],[4,5])  
add((5,1,3),(2,3,4))  
add("welcome", " all")  
    
    
#------------------------
def calc(a,b):
    return a+b,a-b,a*b,a/b

a,*s = calc(10,5)
print(a,s)    
    







