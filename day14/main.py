#import game data 
from data import data
import random

score=0
b2=random.choice(data)
game_over=False

# while game is not over
while not game_over:
    #genrate random name from data file
    b1=b2
    b2=random.choice(data)
    
    if b1==b2:
        b2=random.choice(data)


    # format all the data items properly
    def format_data(account):
        account_name = account['name']
        account_follower_count = account['follower_count']
        account_age = account['age']
        account_city = account['city']
        return f"{account_name}, a {account_age}, from {account_city}, follower count: {account_follower_count}"


    print(f"Comapre :{format_data(b1)}")
    print("vs")
    print(f"Against: {format_data(b2)}")
    # ask user to guess
    user_guess=input("Who has more followers? Type 'A' or 'B': ").lower()

    #get follower count , check if user is correct, if user is correct add to correct counter, 
    def check_answer(user_guess, a_f_cnt, b_f_cnt):
        
        a_f_cnt= b1['follower_count']
        b_f_cnt= b2['follower_count']

        if a_f_cnt>b_f_cnt:
         return user_guess =='a'
        else:
            return user_guess =='b'
    is_correct=check_answer(user_guess,b1['follower_count'],b2['follower_count'])
    if is_correct:
        score +=1
        print(f"you are correct, your current score is {score}")
    else:
        game_over=True
        print(f"You are wrong and your game is over, final score is {score}")

    


