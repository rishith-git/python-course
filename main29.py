#Taking input for the student's eligibility for exam


medical_cause = input("Did you have a medical cause? (Y/N)").strip().upper()

if medical_cause == 'Y':
    print("You are eligible for the exam.")
else:
    #Check for the attendance
    attend = int(input("Enter you attendance pecentage: "))
    if attend >= 75 :
        print("You are eligible for the exam.")
    else :
        print("You are nt allowed for the exam.")

