from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffeemaker = CoffeeMaker()
my_moneymachine = MoneyMachine()
while True:
    order_name = input(f"What would you like?({my_menu.get_items()}):")
    if order_name == "off":
        break

    elif order_name == "report":
        my_coffeemaker .report()
        my_moneymachine.report()
    else:
        # get_coffee_info
        coffee_items = my_menu.find_drink(order_name)
        if coffee_items:
            # check resource is enough
            if my_coffeemaker.is_resource_sufficient(coffee_items):
                # if true ,money is enough
                if my_moneymachine.make_payment(coffee_items.cost):
                    my_coffeemaker.make_coffee(coffee_items)

        else:
            break