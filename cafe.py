#PYTHON MINI PROJECT - CAFE MANAGEMENT                     

menu = {
     "Tea": 30,"Coffee": 40,"Green Tea": 50,"Osmania Biscuits": 20
}

print("---------  Welcome to our KASA'S CAFE  -----------")
print("Tea:30\nCoffee: 40\nGreen Tea: 50\nOsmania Biscuits: 20")

order_item = input("Enter your item:")
order_total = 0

if order_item in menu:
    order_total += menu[order_item]
    order = input("Do you want anything else(Yes/No):")
    if order == "Yes":
        order_item2 = input("Enter your second item:")
        if order_item2 in menu:
            order_total += menu[order_item2]
            print(f"Your oder value: {order_total}")
    else:
        print(f"Your order value: {order_total}")
else:
    print("You entered a wrong item")   

