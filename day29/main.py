from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
     
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    #messagebox.showinfo(title="Password Generated", message=f"Your password is: {password}")
    pyperclip.copy(password)  # Copy password to clipboard
# ---------------------------- Search PASSWORD ------------------------------- #
# Search Passowrd
def search_password():
    website = website_entry.get()
    try:
        with open("day29/data.JSON", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the website {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Save password to a file

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data= {
        website: {
                "email": email,
                "password": password,
               }
                } 

    #if len(website) == 0 or len(password) == 0:
     #     messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
     
    #else:
    try:
        with open("day29/data.JSON", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("day29/data.JSON", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
            data.update(new_data)  # updating

            with open("day29/data.JSON", "w") as data_file:  
                json.dump(data, data_file, indent=4)# write
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
     
       
 
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.config(bg="white")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)    
canvas.grid(column=1, row=0)
logo_img = PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=logo_img)

# Labels

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"a.ramesh73@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
password_entry.focus()

# Buttons
search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(column=2, row=1)
generate_password = Button(text="Generate Password", command=generate_password) 
generate_password.grid(column=2, row=3)
add_button = Button(text="Add", width= 36,command=save_password)
add_button.grid(column=1, row=4,columnspan=2)


   







window.mainloop()