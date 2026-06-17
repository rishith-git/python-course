#Calculating BMI of a person 

height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print("Your BMI is",BMI)

if BMI <= 18.4:
    print("You are Underweight")
elif BMI <= 24.9:
    print("Its the perfect weight")
elif BMI <= 34.9:
    print("You are overweight")
elif BMI <= 39.9:
     print("You are obese")