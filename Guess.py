import random
r=int(input("Enter the range for guess game"))
x=random.randint(1,r)
def user_input():
    y=int(input("Guess the number"))
    validate(y)
    return y

def check(t,x):
    if(x>t):
        print("value is low, try again")
        user_input()
    elif(x<t):
        print("value is high, try again")
        user_input()
    elif(x==t):
        print("guess is right")
        exit()
def validate(a):
    if(a>r):
        print("Enter another value in the range of ",r)
        user_input()
    else:
        check(a,x)

user_input()


