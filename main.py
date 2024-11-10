from random import choice

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink):
    """Check if enough resources are available to make the chosen drink."""
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources.get(ingredient, 0) < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def make_coffee(drink):
    """Deduct resources for the drink that was ordered."""
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {drink}. Enjoy!")

def total_value(total_penny, total_nickel, total_dime, total_quarter):
    total_penny *= 0.01
    total_nickel *= 0.05
    total_dime *= 0.10
    total_quarter *= 0.25

    total_sum = total_penny + total_nickel + total_dime + total_quarter
    return total_sum


def coins(max_price):
    total_pennies = int(input("How many pennies? "))
    total_nickels = int(input("How many nickles? "))
    total_dimes = int(input("How many dimes? "))
    total_quarters = int(input("How many quarters? "))

    total = total_value(total_pennies, total_nickels, total_dimes, total_quarters)

    if total < max_price:
        print("Sorry, that's not enough money.")
        return False
    else:
        change = total - max_price
        print(f"Here is ${change:.2f} in change.")
        return True



machine_on = True


while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    cost_of_coffe = MENU[user_choice]["cost"]
    if user_choice == "off":
        machine_on = False
        print("Turning off the coffee machine. Goodbye!")
    elif user_choice in MENU:
        if check_resources(user_choice):
            print(f"The price of the {user_choice} is {cost_of_coffe}, insert the coins in the machine:")
            if  coins(cost_of_coffe):
                make_coffee(user_choice)
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif user_choice == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
    else:
        print("Invalid input. Please choose from espresso, latte, or cappuccino.")


