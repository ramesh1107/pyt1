#name= input("pleease enter your name:")
#price= input("please enter your your bid proce $:")
bid={}

#bid[name] =price

def compare_rates(bd):
    winner =" "
    hb=0
    for bidder in bd :
        bdamt =bd[bidder]
        if bdamt>hb:
            hb=bdamt
            winner= bidder
    print(f"The winner of the bid  is: {winner} and the winning bid is {hb}")

cb= True
while cb:
    name= input("pleease enter your name:")
    price= int(input("please enter your bid price $:"))
    bid[name] =price
    chk=input("Are there any other bidders if 'yes' type y or if 'no' type n ?").lower()
    if  chk =="n":
        cb =False
        compare_rates(bid)
    elif chk =="y":
        print("\n"*10)

