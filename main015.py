#Creating a program to calculate the circumference of a circle

pi = 3.14

radius = float(input("Enter the radius of a circle for which the circumference should be calculated: "))

def circumference():
    return 2 * pi * radius

print(f"The circumference is: {circumference()}")