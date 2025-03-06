# restaurant menu
menu = {
    "pizza":4.0,
    "hot dog":3.50,
    "soda":1.45,
    "cake":1.70,
    "coffee":0.80
}

cart = []
total = 0

print("--------MENU--------")
for key,value in menu.items():
    print(f"{key}: {value}")
while True:
    food = input("select an item (q to quit): ").lower()
    if food =='q':
        break
    elif food in menu.keys():
        cart.append(food)
        num = float(input("enter number:"))
        total += menu[food]*num
    else:
        print("meal not found!")
print("-----Your Order-----")
for choise in cart:
    print(choise,end=" ")
    print()
print(f"total:${total}")



   


