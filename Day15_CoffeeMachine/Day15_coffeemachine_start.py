import menu

# initialise the resource and money
water_amount = menu.resources["water"]
milk_amount = menu.resources["milk"]
coffee_amount = menu.resources["coffee"]
money_amount = 0

water_cost = 0
milk_cost = 0
coffee_cost = 0
coffee_price = 0
money_inchange = 0


def insert_coins():
    # TODO: ask user to insert coins
    print("Please insert coins.")
    quarter_amount = int(input("how many quarters?: "))
    dime_amount = int(input("how many dimes?: "))
    nickles_amount = int(input("how many nickles?: "))
    pennies_amount = int(input("how many pennies?: "))

    # get total input money
    total_money = quarter_amount * 0.25 + dime_amount * 0.1 + nickles_amount * 0.05 + pennies_amount * 0.01
    return total_money


while True:
    # ask user to choose a coffee
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    '''
    type coffee type to get coffee
    type off to stop the program
    type report to print the report: water/milk/coffee remain ; money earned
    and keep asking 
    '''
    if user_choice == "off":
        break

        # TODO: print report
    if user_choice == "report":
        print(f"Water: {water_amount}ml")
        print(f"Milk: {milk_amount}ml")
        print(f"Coffee: {coffee_amount}g")
        print(f"Money:${money_amount}")

    else:

        # initialise coffee information
        for e in menu.MENU:
            if user_choice == e:
                if user_choice != "espresso":
                    water_cost = menu.MENU[e]["ingredients"]["water"]
                    milk_cost = menu.MENU[e]["ingredients"]["milk"]
                    coffee_cost = menu.MENU[e]["ingredients"]["coffee"]
                    coffee_price = menu.MENU[e]["cost"]
                else:
                    water_cost = menu.MENU[e]["ingredients"]["water"]
                    milk_cost = 0
                    coffee_cost = menu.MENU[e]["ingredients"]["coffee"]
                    coffee_price = menu.MENU[e]["cost"]
        # for test
        print(water_cost, milk_cost, coffee_cost, coffee_price)
        # TODO: check the resource enough or not , if not print sorry ....
        if water_cost > water_amount:
            print("Sorry there is not enough water.")
        elif milk_cost > milk_amount:
            print("Sorry there is not enough milk.")
        elif coffee_cost > coffee_amount:
            print("Sorry there is not enough coffee.")
        else:
            total_money = insert_coins()
            print(f"You have inserted {total_money}")

            if total_money < coffee_price:

                print("Sorry that's not enough money.Money refunded.")
            else:
                # TODO: get change
                money_inchange = total_money - coffee_price
                money_amount += coffee_price
                print(f"Here is ${money_inchange} in change.")
                # TODO: resource calculate
                water_amount -= water_cost
                milk_amount -= milk_cost
                coffee_amount -= coffee_cost
                print(f"Here is your {user_choice} ☕. Enjoy!")
