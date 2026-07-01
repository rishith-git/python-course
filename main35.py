#Using while loop to print sum of numbers

sum = int(input("Enter a number upto which sum should be calculated: "))
total = 0
i = 1
while i <= sum:
    total += i
    i += 1

print("The sum of numbers from 1 to", sum, "is:", total)