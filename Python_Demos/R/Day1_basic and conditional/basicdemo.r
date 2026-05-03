a<-10
a
class(a)
s<-"Welcome"
class(s)
#----------------------
a<-10
b<-5
a+b
a%%b
a%/%b
a/b
#---------------------
name<-readline("Enter name: ")
cat("Welcome ", name)

v<-scan(what=double())
v


v<-scan(n=4,what=double())
v
#------------------------------
1:10

n<-10
for (i in 1:10){
  print(n*i)
}

if(n%%2==0){
  print("even")
}
else{
  print("Odd")
}
#------------------------------
n<-2
res<-switch(n,"One","Two","Three")
print(res)
#------------------------------
a<-10
b<-5
ch<-readline("Enter chice")
switch (ch,
  "add" = cat(a+b),
  "sub"=cat(a-b),
  print("Invalid")
)

#------------------------------
#loop
n<-1
repeat{
  print("Hello")
  if (n>10)
    break
  n<-n+1
}
n<-1
while(n<10){
  print(n*n)
  n<-n+1
}
#---------------------------------------------