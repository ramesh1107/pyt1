'''code to creata a basic calcualtor'''




def add (n1,n2):
    return n1 + n2

def sub (n1,n2):
    return n1 - n2

def mul (n1,n2):
    return n1 * n2

def div (n1,n2):
    return n1 / n2

calc ={"+": add ,
       "-": sub ,
       "*": mul,
        "/": div   }

def calcr():
    to_cal= True
    curr_res=0
    while to_cal:
        n1= float(input("Plz enter the first number: "))
        oper= input("Enter the mathematical operator '+','-','*'','/'")
        n2= float(input("Plz enter the Second number: "))
        choice= input("Do you want to continue with previous result?  if 'yes' type 'y' if 'no' type 'n' ").lower()

        if choice =="y" :
            result= (calc[oper](n1,n2))
            curr_res = result
            print (f"The result of {n1} {oper} {n2} is : {curr_res}")
        else:
            to_cal= False
            print("\n"*20)
            calcr()
    
calcr()


