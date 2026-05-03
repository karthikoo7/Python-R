library("tidyverse")
table4a

gather(table4a,'1999','2000',key="year",value="cases")

gather(table4a,key="year",value="cases",-country)


pivot_longer(table4a,cols='1999':'2000',names_to = "year",values_to = "cases")
#------------------------------------------------------------------

table2

spread(table2,key="type",value = "count")

pivot_wider(table2,names_from = "type",values_from = "count")
#--------------------------------------------------------------
#separate
table3

separate(table3,col="rate",into=c("cases","population"),remove=F)

separate(table3,col="rate",into=c("cases","population"),remove=F,convert = T)


separate(table3,col="rate",into=c("cases","population"),remove=T,convert = T)

separate(table3,col="year",into=c("century","yr"),remove=F,convert = T,sep=2)

#---------------------------------------------------------------------------
tbl <-separate(table3,col="year",into=c("century","yr"),remove=F,convert = T,sep=2)
tbl

unite(tbl,"newyear","century","yr",sep = "")

tbl<-separate(table3,col="rate",into=c("cases","population"),remove=F)
tbl

unite(tbl,"rate1","cases","population")

unite(tbl,"rate1","cases","population",sep="$")
#-------------------------------------------------------------
data <- data.frame(
  gender = c("Male", "Female", "Female"),
  product = c("A", "B", "C"),
  value = c(10, 20, 15)
)
data
df<-complete(data,gender,product)
mn<-mean(df$value,na.rm=T)
mn
complete(data,gender,product,fill=list(value=mn))
#---------------------------------------------
data <- data.frame(
  gender = c("Male", "Female", "Female"),
  product = c("A", "B", "C"),
  value = c(10, 20, 15)
)
data

data %>%
  complete(gender,product)

data %>%
  complete(gender,product)%>%
  fill(value)


data %>%
  complete(gender,product)%>%
  fill(value,.direction="up")



