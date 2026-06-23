#Checking whether the given character is an alphabet or not

char = input("Enter a character : ")
if len(char) != 1:
    print("Please enter exactly one character.")
elif ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
    print(f"'{char}' is an alphabet.")
    if char.isupper():
        print("It is an uppercase letter (A-Z).")
    else:
        print("It is a lowercase letter (a-z).")
else:
    print(f"'{char}' is NOT an alphabet.")