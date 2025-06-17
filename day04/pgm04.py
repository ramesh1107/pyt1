#Random number generator

import random
r_list = [0,1,21]
r_p=random.choice(r_list)
print(r_p)

us_in= int(input("What do you choose? Type 0 for Rock,  for Paper, 2 for Scissors "))
print(us_in)
if r_p >us_in:
    print("COmputer won")
else:
    print("you won")
'''if r_int == 1:
    print("Heads")
else:
    print("Tails")

#randm_nm_0_1= random.random()*10
#print(randm_nm_0_1)
#r_float= random.uniform(1,3)
print(r_float)'''