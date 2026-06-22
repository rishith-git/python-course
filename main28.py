num1 = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))

average = (num1 + num2) / 2
print(average)

if num1 > average:
    print("num1 is greater than average")
elif num2 > average:
    print("num2 is greater than average")
else:
    print("Neither of num1 and num2 are greater then average")
