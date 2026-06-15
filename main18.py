#Checking whether I can buy an item or not
budget = int(input("Enter your budget: "))
item_price = int(input("Enter the price of the item: "))

if item_price <= budget :
    remaining_amount = budget-item_price
    print(remaining_amount)
    print("You can buy the item.")
else:
    print("You cannot buy the item.")



