# Goal is to create a basic cipher


'''
text=("ramesh")
n=int(input("type the shidt number:2"))
nt =text[n:]
print(nt)
'''
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction= input("Type e 'encode' to encrypt  and d'decode' to decrypt\n").lower()
text = input("Type your message\n").lower()
st =int(input("Type the shift number\n"))

def ceaser(dir,otext, shift):
    nt =""
    dt=""
    if dir =="e":
        for ltr in otext:
            sp= letters.index(ltr) +shift
            sp%=len(letters)
            nt +=letters[sp]
            #if sp .len(letters)-1:
            #    sp =sp -len(letters)
            #   nt +=letters[sp]
        print(f"the ciphered value of the given letter is  : {nt}")
    elif dir =="d":
        for l in otext:
            kv=letters.index(l) - shift
            kv%=len(letters)
            dt+=letters[kv]     
        print(f"the deciphered value of the given letter is  : {dt}")
    else:
        print("You have entered in the wrong direction")
ceaser(dir= direction,otext =text ,shift=st)

'''def decrpty (ot, sht):
    dt=""
    for l in ot:
         kv=letters.index(l) - sht
         dt+=letters[kv]     
    print(f"the deciphered value of the given letter is  : {dt}")
decrpty(ot=nt,sht=st )'''