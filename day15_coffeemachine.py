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
    "coffee": 100
}

def drinkcost(choice):
    return MENU[choice]["cost"]

def paymentvalue(quarters, dimes, nickels, pennies):
    total = (quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)
    return total

def calculatechange(payment, cost):
    change = float(payment - cost)
    return change

def calcResources(choice):
    for ingredient, amount in MENU[choice]["ingredients"].items():
        if resources.get(ingredient, 0) < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    for ingredient, amount in MENU[choice]["ingredients"].items():
        resources[ingredient] -= amount

    return True


money = 0

ableToMakeDrinks = True

while ableToMakeDrinks:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "off":
        ableToMakeDrinks = False

    elif drink == "report":
        print(f"Coffee: {resources['coffee']}g")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: ${money}")

    elif drink in ("espresso", "latte", "cappuccino"):
        if not calcResources(drink):
            continue

        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        cost = drinkcost(drink)
        pay = paymentvalue(quarters, dimes, nickels, pennies)

        if pay >= cost:
            change = calculatechange(pay, cost)
            print(f"Here is ${change:.2f} in change.")
            money += cost
        else:
            print("Not enough money.")
            for ingredient, amount in MENU[drink]["ingredients"].items():
                resources[ingredient] += amount

    else:
        print("Please choose one of the drinks.")    