#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
'''
with open ('/Users/Ramesh/Pgms/python/day24/m/Input/Letters/starting_letter.txt', mode ="r") as file:
     for line in file:
         cont = file.read()
         print(cont)

     
    
with open ('/Users/Ramesh/Pgms/python/day24/m/Input/Names/invited_names.txt', mode ="r") as file:
     for line in file:
         cont1 = file.read()
         print(cont1)'''

PLACEHOLDER = "[name]"


with open('/Users/Ramesh/Pgms/python/day24/m/Input/Names/invited_names.txt') as names_file:
     names= names_file.readlines()
    # print(names)

with open ('/Users/Ramesh/Pgms/python/day24/m/Input/Letters/starting_letter.txt') as letter_file:
   letter = letter_file.read()
   for name in names:
       sn=name.strip() # Remove any leading/trailing whitespace characters
       letter_with_name = letter.replace(PLACEHOLDER, sn)
       with open(f'/Users/Ramesh/Pgms/python/day24/m/Output/ReadyToSend/letter_for_{sn}.txt', mode="w") as completed_letter:
                completed_letter.write(letter_with_name)