# make a game using while loop where user have to guess a number until he/she guess it right
import random
# generate a random number between 1 to 10
num = random.randint(1,100)
guess = int(input("guess a number between 1 to 100 : >>> "))
tries = 0
while True:
    if num == guess:
        print(f"you guessed it right in {tries} tries")
        tries = tries + 1
        break
    elif num > guess:
        print("your are little higher")
        tries = tries + 1
    elif num < guess:
        print("your are little lower")
        tries = tries + 1
    else:
        tries = tries + 1
    print("sorry you are wrong")
    guess = int(input("guess a number between 1 to 100 : >>>"))
