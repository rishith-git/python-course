#Building a calculator

#Defining addition function

    
def add(a,b):
   return a+b
   

#Defining subtraction function

def subtract(a,b):
    return a-b
    

#Defining multiplication function

def multiply(a,b):
    return a*b


#Defining division function

def divide(a,b):
    return a/b

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(add(a,b))
    print(subtract(a,b))
    print(multiply(a,b))
    print(divide(a,b))
except ValueError:
    print("Please enter a valid number: ")
except ZeroDivisionError:
    print("Division by zero is not allowed")







