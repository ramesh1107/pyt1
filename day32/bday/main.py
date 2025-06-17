import smtplib
import datetime as dt
import pandas as pd
import random

my_email="testingpytester1@gmail.com"
my_password="lvhk zqpw ttqt eaee"
my_email1="testingpytester1@yahoo.com" 
nw=dt.datetime.now()
my_date= nw.weekday() # getting the current date
print(my_date)
if my_date == 3:
    with open("day32/bday/quotes.txt") as data_file:
        d = data_file.readlines()  # reading all the quotes
        rl=random.choice(d)    #picking a random quote
        print(f"ramdaom qute is{rl}")  # printing the random quote
    
# Gmail email
with smtplib.SMTP("smtp.gmail.com") as connection: #setting up email connection
    connection.starttls()# secute connection
    connection.login(my_email, my_password)# loggign in to the email
    print("i m logged in")
    connection.sendmail(from_addr=my_email, to_addrs=my_email1,
                   msg=f"Subject:Hello\n\n{rl}")

