v<-c(1,2,3,4,5,6)
v
print(class(v))
print(typeof(v))

#--------------------------------------
v<-c(1L,2L,3L,4L,5L,6L)
v
print(class(v))
print(typeof(v))

v<-1:5
v

v<-seq(1,10)
v

v<-seq(1,10,by=0.5)
v

v<-rep(1:2,times=3)
v


v<-rep(1:2,each=3)
v

v<-rep(1:2,each=3,times=2)
v
#--------------------------------------
table(v)
sum(v)
min(v)
max(v)
mean(v)
sd(v)
unique(v)
sort(v)
rev(v)
sort(v,decreasing = T) #descending order
range(v)

#--------------------------------------
v<-11:20
v
#index
v[5]
v[-5]
v[1:3]
v[-c(1:3)]
v[c(1,5,6)]
v[-c(1,5,6)]
#value
v[v==15]
v[v>15]
v[v>12 & v<17]

v[v %in%c(11,17,21)]
#--------------------------------------
v<-c('apple'=10,'banana'=20)
v['apple']
#-------------------------
v+5
v-3
v*2

v1<-c(1,2)
v1

v+v1
v-v1

#-------------------------
