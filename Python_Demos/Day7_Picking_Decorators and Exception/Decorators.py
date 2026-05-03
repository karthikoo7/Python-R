def greet():
    print("Hello")
    
greet()

test=greet
test()


def greet1():
    print("Hi")

def extra_info():
    print("Before function call: ")
    greet()
    print("After Function call")
    
extra_info()

#---------------------------------------------------------
def extra_info(func):
    print("Before function call: ")
    func()
    print("After Function call")
    
extra_info(greet)
print("--"*20)
extra_info(greet1)

#---------------------------------------------------------
def extra_info(func):
    def inner():
        print("Before function call: ")
        func()
        print("After Function call")
    return inner 



greet =extra_info(greet)
greet()

greet1=extra_info(greet1)
greet1()

#---------------------------------------------------------
def extra_info(func):
    def inner():
        print("Before function call: ")
        func()
        print("After Function call")
    return inner 

@extra_info
def greet():
    print("Hello")
    
greet()
#---------------------------------
#syntax:
    
def decorator(func):
    def wrapper(*args,**kwargs):
        print("Befor Function call")
        func(*args,**kwargs)
        print("After Function call")
    return wrapper

#----------------------------------------
#decorator for functioin with parameter

#---------------------------------------------------------
def extra_info(func):
    def inner(name):
        print("Before function call: ")
        func(name)
        print("After Function call")
    return inner 

@extra_info
def greet(name):
    print("Hello ",name)
    
greet("Sita")

#---------------------------------------------------------
def decorators(func):
    def inner(no):
        print("Before function call: ")
        res =func(no)
        print("After Function call")
        return res
    return inner 

@decorators
def sqr(n):
    return n*n

@decorators
def cube(n):
    return n*n*n    


print(sqr(5))


print(cube(5))

#---------------------------------------
import time
def checkExecutionTime(func):
    def inner():
        start = time.time()
        func()
        end=time.time()
        print("Time required for execution is: ",end-start)
    return inner


@checkExecutionTime
def printSqr():
    for i in range(1,1000):
        print(i*i)

printSqr()

printSqr()


