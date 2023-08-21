from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Step 1: Print Report
#Step 2: Check resoources sufficient?
#Step 3: Process Coin
#Step 4: Check transaction succesful
#Step 5: Make Coffee

money_machine = MoneyMachine()
coffee_maker =CoffeeMaker()
menu = Menu()
is_on = True

while	is_on:
	options = menu.get_items()
	choice = input(f'what would you like? {options}').lower()
	
	if choice == "off":
		is_on = False
	elif choice == "report":
		money_machine.report()
		coffee_maker.report()
		
	else:
		drink = menu.find_drink(choice)
		if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
				coffee_maker.make_coffee(drink)		 
		 
		
