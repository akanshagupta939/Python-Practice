import random

def roll():
    for i in range(1):
        x=random.randint(1,6)
    print(x)

(input("Roll the dice"))
roll()

dec=str(input("Do you want to roll again"))
print(dec)
if(str(dec)=='y'):
    roll()
else:
    print("bye")
    exit()

