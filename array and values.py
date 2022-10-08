

cars = ["Ford", "Volvo", "BMW"]

x= cars [0]
l = len(cars)
print(cars)
print(x)
cars [0]= "toyota"
print(cars)
print(l)
for i in cars:
    print(cars)
    if i =="Volvo":
        break
print("break statement finished")

from array import *
vals = array ("i",[5,9,4,7,3])
print (vals)

vals = array ("i",[5,9,4,7,3])
newarr= array (vals.typecode ,(a for a in vals))
for e in newarr:
    print(e)
print("for loop end")


vals = array ("i",[5,9,4,7,3])
newarr= array (vals.typecode ,(a for a in vals))

i= 0
while i<len(newarr):
    print(newarr[i])
    i = i+1












from array import *
arr = array('i',[])
n =int(input("enter values of an list"))
for i in range(n):
    x=int(input("enter the next values"))
    arr.append(x)

print (arr)
