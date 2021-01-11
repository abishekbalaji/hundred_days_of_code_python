import menu

items = menu.MENU
resources = menu.resources
money = 0


def report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}")


def is_sufficient(req):
    return req['water'] <= resources['water'] and req['milk'] <= resources['milk'] and req['coffee'] <= resources[
        'coffee']


def get_money():
    return {
        "quarters": int(input("Enter no. of quarters: ")),
        "dimes": int(input("Enter the no. of dimes: ")),
        "nickles": int(input("Enter the no. nickles: ")),
        "pennies": int(input("Enter the no. pennies: "))
    }


def process_payment(cost, paid):
    global money
    denominations = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    amount = 0
    for x in paid:
        amount += paid[x] * denominations[x]
    if amount < cost:
        return None
    elif amount == cost:
        return 0
    money += cost
    return amount - cost


def make_coffee(req):
    global resources
    for x in resources:
        resources[x] -= req[x]


def machine():
    served = False
    choice = input("What would you like: (espresso/latte/cappuccino): ")
    if choice == "report":
        report()
    elif choice in ("espresso", "latte", "cappuccino"):
        if is_sufficient(items[choice]["ingredients"]):
            print("Payment time!")
            paid = get_money()
            cost = items[choice]["cost"]
            payment = process_payment(cost, paid)
            if payment is None:
                print("Sorry that's not enough money. Money refunded.")
            elif payment == 0:
                print(f"Enjoy your {choice}")
                served = True
            else:
                print(f"Here is your ${round(payment, 2)} in change.\nEnjoy your {choice}")
                served = True
        else:
            print(f"Sorry. We are out of ingredients for {choice}.\nTry something else.")
        if served:
            make_coffee(items[choice]["ingredients"])
    elif choice == "off":
        print("Bye!")
        return
    else:
        print("Check your input.")
    machine()


machine()
