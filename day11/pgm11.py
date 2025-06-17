# create blackjack game

import random
#cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,10]
#inti_player=0
#inti_dealer=0

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,10]
    card= random.choice(cards)
    return card
def cal_score(cards):
   if sum(cards)==21 and len(cards) ==2:
    return 0
   
   if 11 in cards and sum(cards) >21:
      cards.remove(11)
      cards.append(1)
      
   return sum(cards)
def compare_score(u_scr, comp_scr):
    if u_scr == comp_scr:
        return "its a draw"
    elif comp_scr ==21 or u_scr>21:
        return "Computer is winner"
    elif u_scr ==21 or comp_scr>21:
        return"user is winner"
    elif u_scr > comp_scr:
        return "User wins"
    else:
        return "you loose"

def play_game():
    user_cards =[]
    comp_cards =[]
    comp_scr =-1
    u_scr =-1
    is_game_over= False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
    while not is_game_over:
        u_scr= cal_score(user_cards)
        comp_scr= cal_score(comp_cards)
        print(f"your cards : {user_cards}, current score: {u_scr}")
        print(f"Computer cards : {comp_cards}, current score: {comp_scr}")

        if u_scr == 0 or comp_scr ==0  or u_scr >21 :
            is_game_over =True
        else:
            user_should_deal =input("Tyep 'Y' to get another card or 'n' to pass ")
            if user_should_deal =="y":
                user_cards.append(deal_card())
            else:
                is_game_over =True

    while comp_scr !=0 and comp_scr <17:
        comp_cards.append(deal_card())
        comp_scr =cal_score(comp_cards)
    print(comp_scr(u_scr, comp_scr))

while input("Do you want to play a gamr of blackjack ") =="y":
    print("\n" *20)
    play_game()