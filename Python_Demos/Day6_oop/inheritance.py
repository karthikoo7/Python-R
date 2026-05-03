
#inheritance
class Person:
    pass

class Emp(Person):
    pass


p=Person()
e=Emp()


print(isinstance(e,Emp))
print(isinstance(e,Person))
print(isinstance(p,Person))
print(isinstance(p,Emp))


#----------------------------------

print(issubclass(Emp,Emp))
print(issubclass(Emp,Person))
print(issubclass(Person,Person))
print(issubclass(Person,Emp))

#--------------------------------------------


class Person:
    def __init__(self):
        print("Person Constructor")

class Emp(Person):
    def __init__(self):
       print("Emp Constructor")



p=Person()
e=Emp()


#--------------------------------------------


class Person:
    def __init__(self,id=0,nm=" test "):
        self.id=id
        self.name=nm

class Emp(Person):
    def __init__(self,id=0,nm=" ",sal=0):
       #super().__init__(id,nm)
       Person.__init__(self,id,nm)
       self.sal=sal



emp =Emp()
print(emp.id,emp.name,emp.sal)


emp =Emp(11,"Radha",80808)
print(emp.id,emp.name,emp.sal)


#--------------------------------------------


class Person:
    def __init__(self,id=0,nm=" test "):
        self.id=id
        self.name=nm
        
    def display(self):
        print(self.id,self.name)

class Emp(Person):
    def __init__(self,id=0,nm=" ",sal=0):
       #super().__init__(id,nm)
       Person.__init__(self,id,nm)
       self.sal=sal

    def display(self):
        super().display()
        #Person.display(self)
        print(self.sal)

emp =Emp()
emp.display()

emp =Emp(1,'Ravi',898980)
emp.display()

#--------------------------------------------


class Person:
    def __init__(self,id=0,nm=" test "):
        self.id=id
        self.name=nm
        
    def display(self):
        print(self.id,self.name)
        
    def __str__(self):
        return f"{self.id} , {self.name}"

class Emp(Person):
    def __init__(self,id=0,nm=" ",sal=0):
       #super().__init__(id,nm)
       Person.__init__(self,id,nm)
       self.sal=sal

    def display(self):
        super().display()
        #Person.display(self)
        print(self.sal)
        
    def __str__(self):
        return  super().__str__()+f" {self.sal}"

emp =Emp()
emp.display()

emp =Emp(1,'Ravi',898980)
emp.display()


print(emp)

print(Emp.mro())

print(Emp.__mro__)


#--------------------------------------------
class A:
    id=100
    
class B(A):
    id=200
    
class C(A):
    id=300
    
class D(B,C):
    id=400


print(D.id)

print(D.mro())


#--------------------------------------------
class Account:
    
    def __init__(self,ano,nm,bal,actype):
        self.acno=ano
        self.name=nm
        self.__balance=bal
        self._actype =actype


class Saving(Account):
    def display(self):
        print(self.acno,self.name,self._actype)
    


a= Saving(12,"xyz",9000,"Savings")

a.display()

#--------------------------------------------

class Account:
    int_rate=2.5
    def __init__(self,ano,nm,bal,actype):
        self.acno=ano
        self.name=nm
        self.__balance=bal
        self._actype =actype
    
    @classmethod
    def updateintrate(cls,newrate):
        cls.int_rate=newrate

class Saving(Account):
    def display(self):
        print(self.acno,self.name,self._actype)
    


a= Saving(12,"xyz",9000,"Savings")

a.display()


Account.updateintrate(4.5)

#----------------------------------------------
class Time:
    def __init__(self,hh,mm):
        self.hh=hh
        self.mm=mm
        
    def __str__(self):
        return f"{self.hh}:{self.mm}"
     
    @staticmethod
    def add(t1,t2):
         t3=Time(t1.hh+t2.hh,t1.mm+t2.mm)
         return t3


t1=Time(5,30)
print(t1)

t2=Time(3,20)
print(t2)

t3= Time.add(t1,t2)
print(t3)

