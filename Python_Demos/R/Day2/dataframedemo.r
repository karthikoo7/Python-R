name<- c("Ravi","Radha","Kishor")
age<-c(34,45,67)
marks<-c(56.7,78.4,34)

df<-data.frame(name,age,marks)
df

names(df)
colnames(df)
typeof(df)
class(df)
#----------------------------------------------
df$age
df[1:2,]
df[,c("age","name")]
df[,-c(1,2)]
#----------------------------------------
df<- read.csv("C:\\Snehal\\CDAC\\Feb26\\PGCP-BDA\\Python\\Demos\\R\\Day2\\ds\\Cars93.csv")
df


df<- read.csv("C:\\Snehal\\CDAC\\Feb26\\PGCP-BDA\\Python\\Demos\\R\\Day2\\ds\\pizza.csv")
df
#---------------------------------------------------------
data()
mtcars
df<-mtcars
df

colnames(df)
df$mpg
#----------------------------------------------
name<- c("Ravi","Radha","Kishor")
age<-c(34,45,67)
marks<-c(56.7,78.4,34)

df<-data.frame(name,age,marks)
df
summary(df)
str(df)
min(df$age)
sum(df$marks)
mean(df$marks)
#---------------------------------------
df

df[which(df$marks<35),]
df[which(df$marks>50 & df$marks<60),]
df[which(df$marks>50 & df$marks<60),c(1,3)]
#---------------------------------------
data()
df=mtcars
df
subset(df,df$mpg>20)
subset(df,(df$mpg>20 & df$am==1))
subset(df,(df$mpg>20 & df$am==1),select=c("mpg","cyl","am"))
attach(df)
subset(df,(mpg>20 & am==1),select=c("mpg","cyl","am"))
detach(df)
-------------------------------------------------
getwd()

setwd("C:\\Snehal\\CDAC\\Feb26\\PGCP-BDA\\Python\\Demos\\R\\Day2\\ds")

getwd()
df<-read.csv("Cars93.csv")
df

------------------------------------------------
v<-c(12,0/0,NA,Inf,-Inf,45/0)
is.na(v)
is.nan(v)
is.finite(v)
is.infinite(v)
#-----------------------------------------------------------