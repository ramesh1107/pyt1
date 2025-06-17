#treasure island

print("Welcome to treasure island!!!S")
dir=input('Do you choose "left" or "right" : ').lower()



if dir =="left":
    trv=input("Do you waana swim or wait for boat: ").lower()
    if trv =="wait":
          door=input("Which door do you wanna open- red, Blue, or yellow: ").lower()
        if door== "yellow":
                print("you won baby")
        elif door == "blue":
                print("sorry game over")
        elif door == "red":
                print("sorry game over")
    elif trv == "swim":
                print("sorry game over")
              
else :
      print("sorry game over")
