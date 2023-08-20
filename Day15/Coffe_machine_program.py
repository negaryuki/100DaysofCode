from data import MENU, resources
                                          
espresso_resources = MENU["espresso"]["ingredients"]
latte_resources = MENU["latte"]["ingredients"]
cappuccino_resources = MENU["cappuccino"]["ingredients"]

profit = 0
is_on = True


def resource_checker(order_ingredients):
	
	for i in order_ingredients:
		if order_ingredients[i] >= resources[i]:
			print("insufficient resources")
			return False
	return True	
	
def insert_coin(order_drink):
    quarters = float(input("How many quarters?")) * 0.25
    dimes = float(input("How many dimes?")) * 0.1
    nickles = float(input("How many nickles?")) * 0.05
    pennies = float(input("How many pennies?")) * 0.01

    total_coins = quarters + dimes + nickles + pennies

    if total_coins == order_drink["cost"]:
        print(f"Here is your {order_drink}. Enjoy!")
        global profit
        profit += order_drink["cost"]
        return True

    elif total_coins > order_drink["cost"]:
        change = round((total_coins - order_drink["cost"]), 2)
        profit += order_drink["cost"]
        print(f'Here is your change: {change}$.')
        return True
    elif total_coins < order_drink["cost"]:
        print("Sorry that's not enough money. Money refunded.")	
        return False
	

while is_on:
	
	choice = input('Welcome to the Moonbucks Coffe Machine\n '
                     '“What would you like? (espresso/latte/cappuccino):').lower()
                     
	if choice == "off":
		is_on =False
	
	elif choice =='report':
		print(f'Water: {resources["water"]}')
		print(f'Milk: {resources["milk"]}')
		print(f'Coffee: {resources["coffee"]}')
		print(f'Money: {profit}')
		
	else:
		drink = MENU[choice]
		if resource_checker(drink['ingredients']) == True:
			if insert_coin(drink):
				print ("here you are")
	
	
