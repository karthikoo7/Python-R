pi=3.14

def iseven(n):
    return n%2==0


def ispositive(n):
    return n>0

def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
