start=input("Do you want yo start the game").lower().strip()
if(start=='yes'):
    first=input("Do you want to take left or right").lower().strip()
    if(first=='left' or first=='l'):
        print("You are at the left")
        f1=input("You encountered a monster, do you want to run or attack").lower().strip()
        if(f1=='attack'):
            print("You lost..try again")
            exit()
        else:
            print("Good Job mate!")
            f3=input("Do you want to take car or plane").lower().strip()
            if(f3=='car'):
                print("No petrol")
                print("Woospi..bbye play again")
                exit()
            else:
                print("You missed your flight..bad luck")
                print("Bye")
                exit()

    elif(first=='right' or first=='r'):
        print("You are at the right")
        f2=input("You encountered a dragon, do you want to run or fly")
        if(f2=='run'):
            print("Run dude..what are you waiting for..Christmas!")
        else:
            print("woooooo...you flew")
            exit()
    else:
        print("You are lost")






else:
    print("Too bad!!")