#Creating a code to calculate continuous nth power of a number using loops

num = int(input("Enter a number: "))
power = int(input("Enter the power: "))
result = 1
for i in range(power):
    result *= num
    print(f"{num} raised to the power of {i + 1} is: {result}")