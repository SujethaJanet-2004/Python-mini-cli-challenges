# Loops 

import random  # To generate random number
print("Welcome to number guessing game")
random_num = random.randint(1,20)
while True:
    num = int(input("Enter a number to guess from 1 to 20 : "))
    if num < random_num:
        print("Its too low")
    elif num > random_num:
        print("Its too high")
    else:
        print("You have guessed right")
        break