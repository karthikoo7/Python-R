library(tidyverse)
#################################################
mtcars
tbl<-as_tibble(mtcars)
tbl

arrange(tbl,cyl)

################################33

s<-as_tibble(sleep)
s

R.version

####################################################

tidy_dataframe = data.frame(
  S.no = c(1:10),
  Group.1=c(23,345,76,212,88,199,72,35,90,265),
  Group.2=c(117,89,66,334,90,101,178,233,45,200),
  Group.3=c(29,101,239,289,176,320,89,109,199,56))

tidy_dataframe

dfti<-as_tibble(tidy_dataframe)
dfti

#########################

d4<-gather(dfti,"Group.1","Group.2","Group.3",key = "Group Names",value = "Marks")
d4
######################################################

unite(dfti,)
























