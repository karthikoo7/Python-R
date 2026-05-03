print("Hello World")
#--------------------------------------	
a=int(input("ENter no"))
if a>0:
    print("a is +ve")
else:
    print("a is  -ve")
#--------------------------------------	
a,b,c=10,20,30	
if a>b and a>c:
    print("A is greater")
elif b>c:
    print("B is greater")
else:
    print("C is greater")

#--------------------------------------
if a>b:
    if a>c:
        print("A is big")
    else:
        print("C is Big")
elif b>c:
    print("b is Big")
else:
    print("c is big")
	
#--------------------------------------


#Short Hand If

a= int (input("Enter no: "))


if a%2==0:print("Even")


#Short Hand If else

print("even") if a%2==0 else print("Odd")

#--------------------------------------

#match
no =int(input(" Enter no"))

match no:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Invalid ")
#-------------------------------------------------- 
fruit="avacado11"

match fruit:
    case "banana" | "apple":
        print("Regular Fruits")
    case "mango" | "avacado":
        print("Special Fruits")
    case _:
        print("No fruits ")
#--------------------------------------------------         
age = 20

match age:
    case age if age < 18:
        print("Minor")
    case age if age >= 18:
        print("Adult")
              

