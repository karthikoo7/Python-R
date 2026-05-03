# step2
import mysql.connector

# Step3
con = mysql.connector.Connect(host="localhost", user="root", password="12345")
print("Con established !")

cur = con.cursor()

cur.execute("show databases")

for db in cur:
    print(db)

# --------------------------------------------------
con = mysql.connector.Connect(host="localhost",
                              user="root", password="12345", database="aug25")
print("Con established !")

cur = con.cursor()

cur.execute("show tables")

for db in cur:
    print(db)

# create Table
cur.execute(
    "Create table employee(empno int auto_increment primary key,name varchar(50),salary float(6,2))")

cur.execute("show tables")

for db in cur:
    print(db)
# --------------------------------------------------

# insert records


cur.execute("insert into employee(name,salary)values(%s,%s)",
            ('Ravi', 6000.45))
con.commit()
print(cur.rowcount)
# --------------------------------------------------

# insert multiple records
lst=[]
for i in range(5):
    nm=input("Enter name")
    sal= float(input("ENter sal "))
    lst.append((nm,sal))
    
cur.executemany("insert into employee(name,salary)values(%s,%s)",
            lst)
con.commit()
print(cur.rowcount)

#---------------------------------------------
cur.execute("select * from employee")
for r in cur:
    print(r)


cur.execute("select * from employee")    
lst= list(cur.fetchmany(3))
print(lst)
#------------------------------------------

import mysql.connector

# Step3
con = mysql.connector.Connect(host="localhost", user="root", password="12345",database="aug25")
print("Con established !")

cur = con.cursor()
cur = con.cursor()
cur.execute("select * from employee")    
#lst= list(cur.fetchmany(3))
lst= list(cur.fetchone())
print(lst)

cur.close()
con.close()
