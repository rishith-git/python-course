#Checking profit or loss

cost_price = int(input("Enter the cost price of the item: "))
selling_price = int(input("Enter the selling price of the item: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss:", loss)
else:
    print("No profit, no loss.")