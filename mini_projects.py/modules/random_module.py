import random


while True:
        a=int(input("Guess the number: "))
        if(a==random.randint(1,10)):
                print("You guessed it right")
                break
        else:
            print("Pls try again")