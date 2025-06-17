'''def format_name (fname, lname):
    name= fname.title() + lname.title()
    return (name)

print (format_name("ramesh", "akkanapragada"))'''

#code to find if the year is leap year

def is_leap_year(year):
    
    if year % 4 ==0:
        print("The entered year is a leap year ")
    else:
        print("The entered year is not a leap year ")

is_leap_year(2020)