''' Designing a new coffee machine
1. Should have 3 flavors of coffee 
2. The falvours , ingredients and price are as follows:
    espresso- 50 ml water+ 18g coffee- price $1.50
    latte-200ml water+24g coffee+150ml milk- price $2.50
    cappuccino- 250ml water+24g coffee+100ml milk- price $3.00
3.Automatic cup dispenser
4.counting the number of cups
5. Should have a display to show the number of cups
6. Should have a display to show the number of coins
'''

Menu = {
        'espresso':{
        'ingredients':{
             'water' : 50 ,
            'coffee':  18 ,
        },
        'price':  1.50
        },
       'latte': {
       'ingredients':{  
        'water' : 200 ,
        'milk': 150 ,
        'coffee': 24 ,
       },
        'price': 2.50
        },
        'cappuccino':{
        'ingredients':{
        'water' : 250 ,
        'coffee': 24,
        'milk': 100,
        },
        'price': 3.00
        }   
}
resources = {
        'water': 300,
        'milk': 200,
        'coffee': 100,
        'money': 0  
    }
total = 0
water =  0
coffee = 0  
milk =  0
money = 0
machine_on = True
def process_coins(): 
    print("Please insert coins")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return total
 
def get_resources(order_coffee):
    for item in order_coffee:
        if order_coffee[item] >= resources[item]:
            print(f"Sorry, Not enough {item}")
            return False
    return True
    
def make_coffee(coffee, order_ingredints):
    for item in order_ingredints:
        resources[item] -= order_ingredints[item]
    print(f"Here is your {coffee}. Enjoy your coffee")
    return
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Milk: {resources['milk']}ml")
    print(f"Money: ${money}")
    return

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global money
        money += drink_cost
        #print(f"Here is your {money}. Enjoy your coffee")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

while machine_on:
    print("Welcome to the coffee machine")
    print("Please select the coffee you want to have, espresso, latte or cappuccino")
    coffee = input("Enter the coffee you want to have: ").lower()
    if coffee == 'off':
            print("Machine is turning off")
            machine_on = False
            exit()
    elif coffee == 'report':
            print_report()
    else:
        drink = Menu[coffee]
        if  get_resources(drink['ingredients']):
            payment= process_coins()
            if is_transaction_successful(payment, drink['price']):
                 make_coffee(coffee, drink['ingredients'])
                 
 