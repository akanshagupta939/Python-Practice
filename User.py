from array import *
count=int(input("Number of names you want to enter"))
arr_name=[]
def count_text(arr_name):
    c=0
    for char in arr_name:
        c=c+1
    print("value of ",arr_name, "is ",c)


for i in range(count):

    arr=input("Enter the name")
    arr_name.append(arr)
    count_text(arr_name)
print(arr_name)








