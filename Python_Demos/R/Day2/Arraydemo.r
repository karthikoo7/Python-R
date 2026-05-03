a<-array(dim=c(10))
a

a<-array(12,dim=c(10))
a

a<-array(10,dim=c(3,2))
a

a<-array(1:10,dim=c(3,2))
a

a<-array(1:20,dim=c(5,2,2))
a
#------------------------------
a<-array(1:10,dim=c(3,2))
a

summary(a)
length(a)
min(a)
max(a)
sum(a)
#----------------------------
#subsetting array
a<-array(1:16,dim=c(4,4))
a

a[2,4]
a[-2,]
a[,-3]
a[1:2,1:2]
a[-c(1,4),]
#-------------------------------
