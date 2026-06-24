#Printing the current bill

units = int(input("Enter the no.of units consumed: "))

if units <= 50 :
    current_bill = units*2.60
    total_amount = current_bill + 25
    print(total_amount)
    #Tax cost is 25 RUPEES.
elif 50 < units <= 100 :
    current_bill = 130 + ((units-50) * 3.25)
    total_amount = current_bill + 35
    print(total_amount)
    #Tax cost is 35 RUPEES.
elif units <= 200 :
    current_bill = 130 + 162.5 + ((units-100) * 5.26)
    total_amount = current_bill + 45
    print(total_amount)
    #Tax cost is 45 RUPEES
else:
    # For units above 200: first 50 at 2.60, next 50 at 3.25, next 100 at 5.26, remaining at 8.45
    current_bill = 130 + 162.5 + (100 * 5.26) + ((units - 200) * 8.45)
    total_amount = current_bill + 55
    print(total_amount)
    #Tax cost is 55 RUPEES.