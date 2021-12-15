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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns resources left for coffee"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item} for your coffee")
            return False
    return True


def process_coins():
    '''Returns the total calculated coins inserted'''
    print('Please Insert Coins.')
    total = int(input('How many AED 1 coins: ')) * 1
    total += int(input('How many AED 0.50 coins: ')) * 0.50
    total += int(input('How many AED 0.25 coins: ')) * 0.25
    total += int(input('How many AED 0.05 coins: ')) * 0.05
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is AED {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money Refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_machine_on = True

while is_machine_on:
    user_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_drink == "off":
        is_machine_on = False
    elif user_drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: AED {profit}")

    else:
        drink = MENU[user_drink]
        print(f"The drink cost is AED {drink['cost']}")
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_drink, drink['ingredients'])
