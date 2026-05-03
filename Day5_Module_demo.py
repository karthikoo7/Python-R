import calc as c
import sys
# another method to directly import and use functions from another module directly in this file
from calc import ispositive,iseven,isodd,isnegative,add,mul,sub,divide

from list_function import display_list,displayLower,displayUpper,reverse_list,alternate_list,displayDuplicate,unique

## print(calc.add(10,5))
print(c.iseven(8))

## use and append path of module directory if module not in current working directory
print(sys.path)

## testing
print(add(100,20))
print(sub(100,20))
print(mul(100,20))
print(divide(100,20))
print(isodd(107))
print(ispositive(-122))

print('*'*1000)

## Q2

l1 = [1,1,2,2,3,4,5,5,6,7]
l2 = ['hello','karthik','here']

#display_list(l1)
displayUpper(l2)
displayLower(l2)
displayDuplicate(l1)
reverse_list(l1)
reverse_list(l2)
alternate_list(l1)
unique(l1)









