#Escape Sequence
s=" Hello \"Radha\", Welcome \n How Are you";
print(s)

#--------------------------------------

#Functions
s="hello all StudenTSS"
print(len(s))
print(min(s))
print(max(s))

a=12343215
if(str(a)==str(a)[::-1]):
    print("Pallindrome")
else:
    print("Not Pallindrome")

#--------------------------------------
s="this  iS MY page"
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.upper())
print(s.lower())
print(s.index("is"))
print(s.rindex("e"))
print(s.find("is1"))
print(s.rfind("e1"))
print(s.count("i"))
print(s.replace(" ","_"))

#--------------------------------------
#Find Vowel and Consonants Count

s=input("Enter string")

vcnt=0
ccnt=0
for i in s:
    if i.isalpha():
        if i in "aeiouAEIOU":
            vcnt+=1
        else:
            ccnt+=1

print (vcnt, ccnt)

#--------------------------------------

    

