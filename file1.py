#Guessing the number game

import random
playing = True
number = (random.randint(0,9))

print("System will generate a number from 0 to 9 and you have to guess it correctly!")
print("If the number you guessd is correct you win!")

while playing:
    guess = int(input("Enter the number you guessed: "))

    if number == guess:
        print("You have guessed the correct number!,You Won!")
        break

    else:
         print("You guessed the wrong number!,Try Again. \n")
