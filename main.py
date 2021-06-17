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


machine_on = True

def if_enough_resources(ingredients):
    for item in ingredients:
        if resources[item] <= ingredients[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


def if_enough_money(type_of_drink,total_money_inserted):
    if type_of_drink['cost'] > total_money_inserted:
        print("Sorry that's not enough money. Money refunded.")
        return False

    return True

def deduct_resources(drink, ingredients):
    for resource in ingredients:
        resources[resource] -= ingredients[resource]

    print("dispensing drink ......")
    print(f"Here is your {drink}, enjoy....")

profit=0
while machine_on:

    user_input = input('What would you like? (espresso, latte, cappuccino)\n')

    if user_input == 'off':
        machine_on = False
    elif user_input == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} ml")
        print("Profit: $",profit)
    else:
      drink = MENU[user_input]
      if if_enough_resources(drink['ingredients']):
          num_quarters= float(input('Enter Quarters: ')) *.25
          num_dimes = float(input('Enter Dimes: ')) *.10
          num_nickles = float(input('Enter Nickles: ')) *.05
          num_pennies = float(input('Enter Pennies: ')) * .01

          num_total = num_quarters + num_nickles + num_dimes + num_pennies

          if if_enough_money(drink,num_total):

              total_change = round(num_total - drink['cost'],2)
              deduct_resources(user_input,drink['ingredients'])

              print('Your change is $',total_change,"....")



              profit += drink['cost']

















