# TIP calculator
print("Welcome to Tip calcualtor.")

tbl=float( input("What is the total bill amount:$"))
tip=int(input("How much tip would you like to give:"))

Splt=int(input("how many people to split the bill:"))

total=tbl+ tbl*tip/100
print (total)
eps=total/Splt
epsf= round(eps,2)
print(f"Each person should pay: ${epsf}")
