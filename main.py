from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_running = True

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while machine_is_running:
    options = menu.get_items()
    choice = input(f"What do you want to order?{options}:")
    if choice == "off":
        machine_is_running = False
    elif choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            coffee_maker.make_coffee(drink)
