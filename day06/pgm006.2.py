# Prgoram to identify true love

def calc_tru_lov(name1, name2 ):
    text1="true"
    text2="love"

    c1=0
    c2=0
    c3=0
    c4=0
    for l1,l2 in zip(name1,text1):
        if l1 ==l2:
            c1+=1

    for l3,l4 in zip(name1,text2):
         if l3 ==l4:
            c2+=1
    for l4,l5 in zip(name2,text1):
        if l4 ==l5:
            c3+=1

    for l5,l6 in zip(name2,text2):
         if l3 ==l4:
            c4+=1
    c= c1+c2+c3+c4
    print (f"Your love score is : {c}")

calc_tru_lov("ramesh", " love")