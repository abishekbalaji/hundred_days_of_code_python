from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def main():
    choice = input(f"What do you like to have: ({menu.get_items()}): ")
    print(choice)
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        return
    else:
        item = menu.find_drink(choice)
        if item is not None:
            if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)
    main()


if __name__ == '__main__':
    main()
