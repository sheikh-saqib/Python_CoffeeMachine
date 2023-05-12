from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_items = menu.get_items()

print(coffee_maker.report())
user_choice = input(f"Select a drink {menu_items}: ")
drink = menu.find_drink(user_choice)
if drink is not None:
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
