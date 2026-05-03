
####################### Arrays
a<-array(1:10,dim=c(3,2))
a

summary(a)
length(a)
min(a)
max(a)
sum(a)

################### Subsetting

a<-array(1:16,dim=c(4,4))
a

a[2,4]
a[-2,]
a[,-3]
a[1:2,1:2]
a[-c(1,4),]

######################## DataFrames
#data()

name<- c("ravi","Radhika","Kishor")
age<-c(34,45,67)
marks<-c(56.7,78.4,34)

df<-data.frame(name,age,marks)
df

names(df)
colnames(df)
typeof(df)
class(df)

df$age
df[1:2,]
df[,c("age","name")]
df[,-c(2,3)]

##read.csv("filepath")


summary(df)
length(df)
sum(df$marks)
mean(df$age)

df[which(df$marks<35),]

df[which(df$marks>50 & df$marks<60),]

######################
data()
df = mtcars
df

subset(df,df$mpg>20)
subset(df,(df$mpg>20 & df$am==1))
#subset(df,df$mpg>20)

#########################################

getwd()
setwd("D:/Python LAB/Python_Demos/")

read.csv("stocks.csv")

