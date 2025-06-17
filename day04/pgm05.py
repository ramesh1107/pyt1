# prgoram to try loops

import random 
''' 
studnet_scores = [100,78,79,75,65,44,39,75,99]

print (max(studnet_scores))
max_score =0
for score in studnet_scores:
    if score > max_score:
        print (f"the score is {score}")
        max_score = score

print (f"the maximum marks are {max_score} ")
#numbers divisable by 15, 5 & 3
for number in range(1,101):
    
    if number % 15 == 0:
        print("Fizz Buzz- divisable by 15")
    elif number % 5 == 0:
        print("Buzz- Divisable by 5")
    elif number %3 ==0 :
        print("Fizz- Divisable by 3")
    else:
        print(number)''' 

letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','+']

print("Welcome to random passowrd generator ")
nr_letters= int(input("How many leeters would you like in the your password?\n"))
nr_numbers= int(input("How many numbers would you like in the your password?\n"))
nr_symbols= int(input("How many symbols would you like in the your password?\n"))
new_password=" "
for char in range (0,nr_letters):
    new_password +=random.choice(letters)
    
for char in range (0,nr_numbers):
    new_password +=random.choice(numbers)

for sym in range (0,nr_symbols):
        new_password +=random.choice(symbols)
#new_password=new_password_lt+new_password_nm+new_password_sym
new_p= random.sample(new_password,len(new_password))
new_pw =  " "
for char in new_p:
     new_pw+=char
print (f"the new randaom password is {new_pw}")