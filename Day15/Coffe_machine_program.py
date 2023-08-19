# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
# ---------------------------------------------------------------------------------------
from data import MENU, resources

espresso_price = float(1.5)
latte_price = float(2.5)
cappuccino_price = float(3.0)
drink_choice = input('Welcome to the Moonbucks Coffe Machine\n '
                     '“What would you like? (espresso/latte/cappuccino):').lower()


def resource_checker():
    """ this function checks whether there are enough resources or not"""

    if drink_choice == 'espresso':
        resource_used = MENU("espresso")
        water = resources("water") - resource_used("water")
        milk = resources("milk") - resource_used("milk")
        coffee = resources("coffee") - resource_used("coffee")
        return water, milk, coffee


def print_report():
    if drink_choice == "report":
        resource_checker()
        print(resources)


def order_drink():
    """ this function asks the user what drink they want"""

    if drink_choice == 'espresso':
        return espresso_price
    elif drink_choice == 'latte':
        return latte_price
    elif drink_choice == 'cappuccino':
        return cappuccino_price
    elif drink_choice == 'report':
        return print_report()


def insert_coin():
    quarters = float(input("How many quarters?")) * 0.25
    dimes = float(input("How many dimes?")) * 0.1
    nickles = float(input("How many nickles?")) * 0.05
    pennies = float(input("How many pennies?")) * 0.01

    total_coins = quarters + dimes + nickles + pennies

    if total_coins == order_drink():
        print(f"Here is your {drink_choice}. Enjoy!”")

    elif total_coins > order_drink():
        change = round((total_coins - order_drink()), 2)
        print(f'Here is your change: {change}$.')
    elif total_coins < order_drink():
        print("Sorry that's not enough money. Money refunded.")


resource_checker()
