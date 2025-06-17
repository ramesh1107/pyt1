

print("Welcome tp pizza delivery")
size= input("Please enter your size  S , M or L:")
pprn= input("Please enter if you want pepporoni  Y or N:")
ec= input("Please enter if you want Extra cheese  Y or N:")
bill = 0
if size =='S':  
       bill = 15 
       print(f"pizza size bill is $ : {bill}")
elif size=='M':
       bill =20
       print(f"pizza size bill is $ : {bill}")
elif size=='L':
       bill =25 
       print(f"pizza size bill is $ : {bill}")

if pprn =='Y':
    if size =='S':
        bill += 2
        print(f"pizza size & pepp bill is $ : {bill}")
    else:
        bill += 3
        print(f"pizza size & pepp bill is $ : {bill}")
if ec =='Y':
    bill += 1
    print(f"pizza size & pepp & cheese bill is $ : {bill}")

print(f"Your final bill is $ : {bill}")

