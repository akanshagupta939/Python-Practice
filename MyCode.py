import math
x= int(input("Enter the number"))
root =int(math.sqrt(x))
for i in range(2,root):
    if(x%i==0):
        print(str(x) + " is not prime")
        break
else:
    print(str(x) + " is prime")


