# This program is for creating hangman game

# step-1 to choose a word from word_list and call it choosen word- Done
# Step-2 Ask the user to guess a letter and assing the answer to a variable called guess. 
#          Make the guess lower case
# Step-3Check if the letter guessed by the user matches the choosen word , if yes yes, great and move to next word, if no the user looses a life.
# # The user has a total of five lives
import random

#step-1
word_list = [ "busveni", "planes","trains", "shipkris"] 
ch_wr=(random.choice(word_list))

chars= []
for char in ch_wr:
    chars.append(char)


#step-2
a=[]
l=len(ch_wr)
lifes =6
game_over = False
final=[]
while not game_over:
    guess = input("Please guess an alphabet: ").lower()
ans=""
for letter in ch_wr:
    if letter == guess:
        ans+=letter
        final.append(guess)
    elif letter in final:
        ans+=letter
    else:
        ans+="-"
print(ans)
if guess not in ch_wr:
    lifes-=1
    if lifes ==0:
        game_over = True
        print("You loose")

if "_" not in ans:
    game_over = True
    print("you win")







'''while l>0 :
   
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

print("the word entered by the user is : "+ a)'''