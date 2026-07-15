#Calculating the total bill at a restaurant

def total_bill(total_amount,tip_percentage=20):
    tip_amount = total_amount * (tip_percentage/100)
    print(total_amount + tip_amount)
    
total_bill(150)
    