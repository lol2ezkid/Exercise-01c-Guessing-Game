#!/usr/bin/env python3
import sys, random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"



number = random.randrange(1,11)
count = 0
guess = -1
while guess != number:
    count = count + 1
    guess = input("Guess a number from 1 to 10: ")
    try: 
        guess = int(guess)
        if guess != number:
            print("Not quite, please try again!")
        if guess >= 11: 
            print("That number is too big!")
        if guess <= 0:
            print("That number is too small!")
        if count >= 3:
            print("Keep trying you got this!")    
    except:
        print("Please enter a number!")
print("Great job! You got it! You were able to guess the number in " + str(count) + " tries.")
