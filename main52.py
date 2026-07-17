# Using the break keyword

word = input("Enter a word: ")

for i in word:
    if i == "A" or i == "a":
     print("The letter A is found")
     break
    else:
     print("The letter A is not found")
