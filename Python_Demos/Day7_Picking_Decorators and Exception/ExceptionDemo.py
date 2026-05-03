a=int(input("Enter no1: "))
b=int(input("Enter no2: "))
res=a/b
print(res)

#print("abc"+10)

#lst=[]
#lst[5]
#-------------------------------------
try:
    a=int(input("Enter no1: "))
    b=int(input("Enter no2: "))
    res=a/b
    print(res)
except:
    print("error occured.")
print("Thank you.")

#-------------------------------------
try:
    a=int(input("Enter no1: "))
    b=int(input("Enter no2: "))
    res=a/b
    print(res)
except Exception as e:
    print("error occured. : ",e)
print("Thank you.")





#-------------------------------------
try:
    a=int(input("Enter no1: "))
    b=int(input("Enter no2: "))
    res=a/b
    print(res)
except ValueError as e:
    print("error occured. : ",e)
except ZeroDivisionError as e:
    print("error occured. : ",e)
print("Thank you.")



#-------------------------------------
try:
    a=int(input("Enter no1: "))
    b=int(input("Enter no2: "))
    res=a/b
except ValueError:
    a=10
    b=5
except ZeroDivisionError:
    b=1
    
finally:
    res=a/b
    print(res)
print("Thank you.")

#-------------------------------------
while(1):
    try:
        a=int(input("Enter no1: "))
        b=int(input("Enter no2: "))
        res=a/b
        print(res)
    except ValueError as e:
        print("error occured. : ",e)
    except ZeroDivisionError as e:
        print("error occured. : ",e)
    else:
        break
print("Thank you.")

#-------------------------------------
while(1):
    try:
        a=int(input("Enter no1: "))
        b=int(input("Enter no2: "))
        res=a/b
        print(res)
    except( ValueError, ZeroDivisionError) as e:
        print("error occured. : ",e)
    else:
        break
print("Thank you.")


#-----------------------------------

age= int(input("ENter age : "))
if age< 18:
    raise Exception("Invalid Age")
print("Thank you")


#---------------------------------
class InvalidAge(Exception):
    def __init__(self,msg="Invalid age"):
        self.errmsg=msg
    
    def __str__(self):
        return f"Error Occured {self.errmsg}"



age= int(input("ENter age : "))
if age< 18:
    raise InvalidAge("You are under 18 come after you became 18.")
elif age>150:
    raise InvalidAge("Take rest...")

print("Thank you")








