

 
#BMI Caluclator with Interpreations

print ("welcome to BMI calculator with interpretations")
height =float(input("what is your height?"))
weight =float(input("what is your weight?"))
h2=height*2;
bmi=weight/h2
print (h2)
print (bmi)
if bmi <18.5:
    print("you are lucky , you are underweight")
elif bmi>=18.5 and bmi<=24.9:
    print ("You are fine and Normal")
else:
    print("you are overweight")'''