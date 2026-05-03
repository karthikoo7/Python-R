############ Its Labbing Time! Assignment Questions -> Data Objects

l<-c(78,85,62,90,55)
l

length(l)
max(l)
min(l)

###################
cat("Secnond Questtion")
l
sum(l)
max(l)
min(l)
sd(l)
median(l)
var(l)
mean(l)

#########################
math<-c(70,85,60)
science<-c(65,80,75)
math
science
cat("Total")
d<-math+science
d
avg<-d%/%2
avg
##########################

colors<-c("red","green","blue","yellow","purple")
colors[c(2,4)]

colors[-3]

##############################

temperatures<-c(32,28,30,35,40,22,25)
s<-temperatures[temperatures>30]
s
length(s)
##ans<-which(temperatures>30)
##length(ans)

############################################

student<-list(Name="Sneha",Age=21,Marks=c(78,85,92))
student

##############################################

student["Name"]
m<-student["Marks"]
m
mean(student$Marks)

###########################################

colors<-c("red","blue","green","blue","red","green","blue")
color_factor<-factor(colors)
levels(color_factor)
summary(color_factor)

###############################################

rating<-c("Good","Excellent","Average","Good","Average","Excellent")
new_factor<-factor(rating,levels =c("Average","Good","Excellent"),ordered=TRUE)
new_factor
new_factor[1]>new_factor[3]

#########################################################

first<-c(1,2,3,4)
second<-c("A","B","C","D")

rbind(first,second)
cbind(first,second)

#######################################################

m<-matrix(1:15,nrow=5,ncol=3,byrow = TRUE)
m

m[2,3]
m[1,]
m[,2]

#####################################################

d1<-array(1:10)
d1

d2<-array(1:10,dim = c(5,2))
d2

## 4D array 
d4<-array(1:36,dim = c(3,4,3))
d4

######################################################

name<-c("Alice","Bob","Charlie","David","Ergosf")
age<-c(25,30,32,45,25)
marks<-c(85,92,78,89,95)

df<-data.frame(name,age,marks)
df

###########################################################

df["age"]

##########################################################

df[c("name","marks")]

##########################################################

df["marks">90]

#########################################################

df[df["name"]=="Bob"]
df[df$name == "Bob",]

############################################################

df[df$name != "Charlie",]

##############################################################

df[1,c(2,3)]

################################################################

df[,c(2,3)]

################################################################

df[df$age>25,]

############################################################