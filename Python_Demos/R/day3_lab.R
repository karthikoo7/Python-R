#################################

add<-function(a,b=0){
  a+b
}
add(10,10)

add(b=10,a=1)

add(22)
###########################################################

addition<-function(...){
  v<-c(...)
  sum(v)
}

addition()
addition(1,2,3,4,4)


listing<-function(...){
  v<-c(...)
  cat(v)
}

listing(1,"Karthikeyan Sharma","Dhurandhar",6666)

############################################################

#Tidyverse package

install.packages("tidyverse")
library(tidyverse)


name<-c("Alice","Bob","Charlie","David","Ergosf")
age<-c(25,30,32,45,25)
marks<-c(85,92,78,89,95)

## tibble

df<-data.frame(name,age,marks)
df

tibble(df)
as_tibble(df)


as_tibble(mtcars)

installed.packages()

summary(df)
######################################################
library(tidyverse)

data<-as_tibble(mtcars)
data

arrange(data,carb,hp)

arrange(data,gear)
summarise(data)


select(data,1:4)
colnames(data)
select(data,"cyl","gear")

################ASSingments################################

factorl<-function(n){
  b<-1
  for(i in 1:n){
    b<- b*i
  }
  b
  
}

factorl(7)

factorial(7)

###############################################################


area<-function(n){
  ans<- 3.14*(n**2)
  ans
}
area(5)
###################################################################

abs(-222)
sqrt(49)
ceiling(22.4)

floor(22.8)

##############################################################
## assignments on deplyr functions

library(tidyverse)

starwars

arrange(starwars,eye_color)

###############################################################

arrange(starwars,skin_color,eye_color)

############################################################

arrange(starwars,hair_color,skin_color,eye_color)

###################################################################

arrange(starwars,hair_color,desc(skin_color),eye_color)

#################################################################

starwars %>% select(name,height,hair_color)

###############################################################

starwars %>% select(name,height,hair_color) %>% arrange(height)

#############################################################

starwars %>% filter(height>200)

####################################################################

starwars %>% filter(height>100 & height<200)

#####################################################################

starwars %>% filter(height>100 & height<200 & skin_color=="gold")

####################################################################

starwars %>% filter((height>100 & height<200) | (skin_color=="fair"))

#####################################################################

starwars %>% select(ends_with("color"))



















