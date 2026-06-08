#Marks obtained by the student
math_marks = int(input("Enter the marks obtained in mathematics: "))
science_marks = int(input("Enter the marks obtained in science: "))
english_marks = int(input("Enter the marks obtained in english: "))
total_marks = math_marks+science_marks+english_marks
print("The total marks obtained by the student is: ", total_marks)

#Calculating the percentage
percentage = total_marks / 300 * 100
print("The percentage of marks obtained by the student is: ", percentage)