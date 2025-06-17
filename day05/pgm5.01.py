# This program is for creating hangman game

# step-1 to choose a word from word_list and call it choosen word- Done
# Step-2 Ask the user to guess a letter and assing the answer to a variable called guess. 
#          Make the guess lower case
# Step-3Check if the letter guessed by the user matches the choosen word , if yes yes, great and move to next word, if no the user looses a life.
# # The user has a total of five lives
import random

#step-1
word_list = ["car", "bus", "plane","train", "ship"] 
ch_wr=(random.choice(word_list))
#print (ch_wr)
chars= []
for char in ch_wr:
    chars.append(char)
print(chars)
#print(random.choice(word_list))
#step-2
a=[]
l=len(ch_wr)
lifes =6
guess = input("Please guess an alphabet: ").lower()
ans=""
'''for letter in ch_wr:
    if letter == guess:
        ans+=letter
    else:
        ans+="-"
print(ans)'''
while l>0 :
   
    l-=1
    
    if lifes >0 :
        lifes -=1
        if guess in chars:
            print(f"The letter '{guess}' is in the list.")
            a.append(guess)
        else:
            print(f"The letter '{guess}' is not in the list and one life gone")
    else:
        print("your lifes are over")

print("the word entered by the user is : "+ a)