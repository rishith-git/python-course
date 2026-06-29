# Printing sum of numbers using loops

n = int(input("Enter the number upto which the sum is required: "))

total = 0
for i in range(1, n + 1):
  total = total + i
print("The sum of numbers from 1 to", n, "is", total)