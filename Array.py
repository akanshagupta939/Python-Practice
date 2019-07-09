from array import *

vals=array( 'i' ,[4,5,5,8,5,2,3,6,9,77,1,22,55,3])

new=array(vals.typecode, (x for x in vals))


arr=array('i',[])
size=int(input("Enter the length of array"))

for i in range(size):
    x=int(input("Enter the value for index"))
    arr.append(x)
print(arr)

y=int(input("Search what you want to"))

index=0
for e in arr:
    if(y==e):
        print("index of ", str(y),"is", str(index))
        print(arr.index(y))
        break
    index=index+1



