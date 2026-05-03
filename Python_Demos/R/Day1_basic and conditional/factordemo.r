v<-c("Pass","Fail","Pass","Fail","Pass","Pass")
f<-factor(v)
print(v)

print(f)
summary(f)
levels(f)

f1<-factor(v,levels = c("Pass","Fail","Absent"))
f1
summary(f1)


v<-c("low","med","high","high","med","med")
f<-factor(v,levels = c("low","med","high"),ordered = T)
print(f)