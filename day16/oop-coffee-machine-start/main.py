''' 
Print report
check resources
process coins
check transaction successful
make coffee
'''

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_on = True
money_maker= MoneyMachine()
coffe_maker= CoffeeMaker()
menu = Menu()




while machine_on:
    options= menu.get_items()
    choice = input(f"What would you like to have? ({options}): ")
    
    if choice == "off":
        print("Machine is turning off")
        machine_on = False
        exit()
    elif choice == "report":    
        coffe_maker.report()
        money_maker.report()
    else:
       drink= menu.find_drink(choice)
       if (coffe_maker.is_resource_sufficient(drink)) and money_maker.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
           
   
   
   
 