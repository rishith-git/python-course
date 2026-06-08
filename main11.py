#Taking input as total amount
total_amount = int(input("Enter the total amount for withdrawal: "))

#Calculating the number of 500, 100 , 50 and 20 notes
num_500 = total_amount // 500
num_100 = (total_amount % 500) // 100
num_50 = ((total_amount % 500) % 100) // 50
num_20 = (((total_amount %500) % 100) % 50) // 20

#Printing the number of notes
print("Number of 500 notes: ", num_500)
print("Number of 100 notes:", num_100)
print("Number of 50 notes:", num_50)
print("Number of 20 notes:", num_20)