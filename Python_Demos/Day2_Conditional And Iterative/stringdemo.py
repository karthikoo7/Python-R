


#--------------------------------------

s='Hello'

s1="Welcome all 'student'"

s2=''' Welcome all
       to know it'''

s3=""" Welcome all
     'students'
       to know it"""

print(s)
print(s1)
print(s2)
print(s3)

#del s[0] error
#s[0]='y' error

s="Hi"
print(s)

del s

#print(s)


#--------------------------------------

s="Welcome"

#1
print(s)

print()
#2
for i in s:
    print(i)

print()
#3
print(s[0])
print(s[1])

print()

#4
for i in range(0,len(s)):
    print(i, s[i])
#--------------------------------------

s="Welcome"
s[4:]
'ome'
s[:3]
'Wel'
s[-1]
'e'
s[-3]
'o'
s[-5:-1]
'lcom'
s[-5:]
'lcome'
s[:-3]
'Welc'
s[::-1]
'emocleW'
s[1:-1]
'elcom'
s[1:10]
'elcome'
s[10]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[10]
IndexError: string index out of range

#--------------------------------------
#string OPerators

s="hi"
s1="Hello"

print(s+s1)
print(s*3)
print(s==s1)
print(s>s1)

print("He" in s1)

#--------------------------------------

#string Formating

name="Ravi"
age=32
marks=86.6

#1. %

print("My name is %s, age is %d, Marks are %f"%(name,age,marks))

#2 Format
#2.1 Default

print("1. My name is {}, age is {}, Marks are {}".format(name,age,marks))

#2.2 Positional

print("2. My name is {0}, age is {1}, Marks are {2}. Thanks {0}".format(name,age,marks))

#2.3 Keyword

print("3. My name is {n}, age is {a}, Marks are {m}".format(n=name,a=age,m=marks))



#3


print(f" 1. My name is {name}, age is {age}, Marks are {marks}, after 10 yrs my age is {age+10}")

#--------------------------------------


