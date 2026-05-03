import pickle


d={'name':'Radha','age':10, 'marks':[10,20,30]}

bytedata= pickle.dumps(d)

print(bytedata)

d1= pickle.loads(bytedata)
print(d1)
print(type(d1))

#-------------------------------------
#pickling
with open("mydata.pkl","wb") as file:
    pickle.dump(d,file)
    print("Data dumped in file.")
    
#unpickling
with open("mydata.pkl","rb") as file:
    d2=pickle.load(file)
    print(d2)
    print(type(d2))