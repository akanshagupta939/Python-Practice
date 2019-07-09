import random
word=input("Enter a word").lower().strip()
x=random.choice(word)
print("You have ", len(word), "guesses!")



def guess():
    for i in range(len(word)):
        guess = input("Enter your guess").lower().strip()
        validate(guess)
        if (guess == x):
            print("Guess was right ", guess)
            exit()
        else:
            print("Unfortunately the guess was not right, try again")

def validate(v):
    if v in word:
        print("Its a valid word")
    else:
        print("Not valid, try again")
        guess()

guess()
