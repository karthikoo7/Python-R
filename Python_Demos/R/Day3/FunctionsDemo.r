add<-function(a,b)
{
  a+b
}

add(2,4)
add(b=12,a=14)
#------------------------------------
add<-function(a,b=0)
{
  a+b
}
add(2)
add(b=12,a=14)
#--------------------------------------
add<-function(...)
{
  v<-c(...)
  sum(v)
}

add()
add(1,2,3,4,5)
add(23,45)

#-------------------------------

display<-function(...)
{
  lst<-list(...)
  lst
}

display(1,"hgjhgj",c(1,2,3))
#--------------------------------------

v<-c(1,8,3,5,7,2,4,10)
ifelse(v%%2==0,"Even","Odd")

str(v)
summary(v)

#-------------------------------------
abs(-2)
sqrt(64)
log(2)
exp(0.6931472)
ceiling(12.6)
round(12.6)
floor(12.6)
#---------------------------
s="weLCOme"
nchar(s)
tolower(s)
toupper(s)
substr(s,2,5)
substring(s,4)
#---------------------------
substr(s,2,6)<-"hello"
s
#--------------------
s
grep("e",c(s,"apple","banana","greps"))
