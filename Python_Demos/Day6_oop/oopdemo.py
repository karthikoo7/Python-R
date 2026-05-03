#oop Demo

#class
class Emp:
    pass

e= Emp() #object

print(id(e))
print(type(e))

#---------------------
class Emp:
    '''this is empty emp class'''
    pass

e= Emp() #object

print(id(e))
print(type(e))
print(help(e))
print(help(Emp))

#---------------------
#1 . Instance Variable
e.name="Radha"
print(e.name)

e1=Emp()
print(e1.name)


#2. Constructor

class Emp:
    def __init__(self,no,name):
        self.eno=no
        self.ename=name



e=Emp(10,'Ravi')
print(e.ename,e.eno)

e1=Emp(10)
print(e.eno)



#--------------------------------
class Emp:
    def __init__(self,no=0,name='Test'):
        self.eno=no
        self.ename=name

#    def __init__(self,no):
#       self.eno=no
        


e=Emp(10,'Ravi')
print(e.ename,e.eno)

e1=Emp(13)
print(e1.ename, e1.eno)


#--------------------------------
#3. instance variable using Class variables
class Emp:
    location ="pune" #class variable
    def __init__(self,no=0,name='Test'):
        self.eno=no
        self.ename=name

    def display(self):
        print(self.eno, self.ename,self.location)


e=Emp();

e1=Emp(10,"Radha")

e2=Emp(1,"Ramesh")


e.display() #Emp.display(e)
e1.display()
e2.display()

print("--"*20)
Emp.location="mumbai"

e.display() #Emp.display(e)
e1.display()
e2.display()
print("--"*20)
e.location="Kolhapur"
e.display() #Emp.display(e)
e1.display()
e2.display()



print("--"*20)
Emp.location="Nashik"

e.display() #Emp.display(e)
e1.display()
e2.display()


#------------------------------------------
class Emp:
    location ="pune" #class variable
    def __init__(self,no=0,name='Test'):
        self.eno=no
        self.ename=name

    def display(self):
        print(self.eno, self.ename,self.location)
        
    def setBonus(self,amt):
        if amt>0:
            self.bonus =amt

    def getBonus(self):
        if hasattr(self,'bonus'):
            return self.bonus


e=Emp();

e1=Emp(10,"Radha")
e1.setBonus(8000)

e2=Emp(1,"Ramesh")

e.display() #Emp.display(e)
e1.display()
e2.display()


print(e.getBonus())
print(e1.getBonus())
print(e2.getBonus())


print(getattr(e,'bonus',0))
print(getattr(e1,'bonus'))


e.allowance=1000
print(e.allowance)
del e.allowance

print(e.allowance)



#------------------------------------------
class Emp:
    location ="pune" #class variable
    def __init__(self,no=0,name='Test'):
        self.eno=no
        self.ename=name

    def display(self):
        print(self.eno, self.ename,self.location)
        
    def setBonus(self,amt):
        if amt>0:
            self.bonus =amt

    def getBonus(self):
        if hasattr(self,'bonus'):
            return self.bonus

    def __del__(self):
        print("Destructor called")
        
        
e=Emp();

e1=Emp(10,"Radha")
e1.setBonus(8000)       
        
del e
del e1


lst=[]
for i in range(3):
    no=int(input("Enter no: "))
    name=input("Name of emp: ")
    lst.append(Emp(no,name))
    
    
#----------------------------
for e in lst:
    e.display()
    
        
        