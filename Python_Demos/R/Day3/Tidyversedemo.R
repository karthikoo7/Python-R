library("tidyverse")
mtcars
data<-as_tibble(mtcars)
data

arrange(data,carb,hp)
arrange(data,desc(carb),hp)

df<-read.csv("C:\\Snehal\\CDAC\\Feb26\\PGCP-BDA\\Python\\Demos\\R\\Day2\\ds\\cars2018.csv")
data<-as_tibble(df)
data
res<-arrange(data,Gears)
print(res,n=Inf)
print(res,n=50)
#---------------------------------------------
#select
select(data,1:4)

colnames(data)

select(data , "Gears":"Drive")

select(data,c("Model","Gears","Drive"))

select(data,-c("Model","Gears","Drive"))

select (data,starts_with("Model"))

select (data,ends_with("Cyl"))
#------------------------------------------------------
#filter
data
filter(data,Transmission=="Manual")
filter(data, Model=="FIAT 124 Spider")

filter(data, Model=="FIAT 124 Spider" & Transmission=="Automatic")


filter(data,Model=="Chevrolet CAMARO" & Transmission=="Automatic")

arrange(filter(data,Model=="Chevrolet CAMARO" & Transmission=="Automatic"),Gears,Cylinders)

select(arrange(filter(data,Model=="Chevrolet CAMARO" & Transmission=="Automatic"),Gears,Cylinders)
,"Model":"Gears")
#-----------------------------------------------
#rename

rename(data,"Mindex" ="Model.Index")
data

#-----------------------------------------------
#mutate
data
data1<-mutate(data,"New.Ethanol"=Max.Ethanol+5)
data1
#----------------------------------------------------------
select(arrange(filter(data,Model=="Chevrolet CAMARO" & Transmission=="Automatic"),Gears,Cylinders)
       ,"Model":"Gears")

data %>%
  filter(Model=="Chevrolet CAMARO" & Transmission=="Automatic") %>%
  arrange(Gears,Cylinders) %>%
  select("Model":"Gears")




