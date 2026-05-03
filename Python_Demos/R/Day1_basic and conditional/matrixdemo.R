m<-matrix(10,2,3)
m


m<-matrix(1:10,5,2)
m


m<-matrix(1:10,6,2)
m

m<-matrix(1:10,5,2,byrow = T)
m

a<-1:5
b<-11:15
c<-21:25

m<-cbind(a,b,c)
m

m<-rbind(a,b,c)
m


a<-1:7
b<-11:15
c<-21:25

m<-cbind(a,b,c)
m


m<-matrix(1:20,5,4,byrow = T)
m

m[,3]
m[3,]
m[2,3]

m[,3]
m[,3,drop=F]

m[1:3,3]
m[1:3,1:3]
m[,-2]