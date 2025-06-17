# Roller coaster
print ("welcome to roller coaster")
height =int(input("what is your height?"))
age =int(input("what is your age?"))
wantphoto=(input("Do you eant a photot- Y or n-"))
tb=0

if height >120:
    print ("You can ride roller coaster ")
    if age <= 12:
        print ("Child tickets are $5 for the ride")
        tb= 5
    elif age>12 and age <18:
         print ("Teen tickets are $7 for the ride ")
         tb=7
    elif age>45 and age <45:
        print ("You get a free ridee ")
    else:
         print ("you get a free ridee ")
         tb=12
    if wantphoto =="y":
        tb+=3
    print(f"Totla bill is pay $ {tb}")
else:
    print ("You cannot ride the roller coaster now")