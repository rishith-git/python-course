#Building a game of guessing numbers

secret_number = 43
x = 0
i = 1
while i <= 5:
    guess_number = int(input("Enter your guess number between 1 to 50: "))
    
    if guess_number == secret_number:
     print("You guessed the number correctly!")
     x = 1
     break
    else:
     print("You are close to the number by", abs(secret_number - guess_number),"units , try again!")
i = i + 1
if x == 0:
    print("All 5 attempts are exhausted , the secret number was", secret_number)