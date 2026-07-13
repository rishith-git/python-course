#Creating a calculaor function
def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    return a / b

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

print("Select an operation to perfom:")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")

operation = input("Enter your choice (a/b/c/d): ")

if operation == 'a':
    print("sum = ",addition(num_1,num_2))
elif operation == 'b':
    print("diference = ",subtraction(num_1,num_2))
elif operation == 'c':
    print("product = ",multiplication(num_1,num_2))
elif operation == 'd':
    print("quotient = ",division(num_1,num_2))
else:
    print("Invalid choice.")

