library("tidyverse")
mtcars
tbl<-as_tibble(mtcars)
tbl

summarise(tbl, avg_mpg=mean(mpg))
summarise(tbl, avg_mpg=mean(mpg), max_mpg=max(mpg),min_mpg=min(mpg))
summarise(tbl, avg_mpg=mean(mpg), max_mpg=max(mpg),min_mpg=min(mpg)
          ,avg_hp=mean(hp), max_hp=max(hp),min_hp=min(hp))

tbl%>%
  group_by(gear) %>%
  summarise(avg_mpg=mean(mpg))
            
tbl%>%
group_by(gear) %>%
  summarise(avg_mpg=mean(mpg),max_mpg=max(mpg),min_mpg=min(mpg))

#----------------------------------------------------------------
df1<-data.frame(Id=c(1,2,3),Name=c("Ravi","Ajit","Krushna"))
df2<-data.frame(Id=c(1,2,4),Marks=c(56.7,67.3,80.5))

df1
df2

inner_join(df1,df2,by="Id")
left_join(df1,df2,by="Id")
right_join(df1,df2,by="Id")
full_join(df1,df2,by="Id")
#-----------------------------------------------------------------
