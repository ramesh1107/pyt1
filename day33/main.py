from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    if response.status_code == 200:
        data = response.json()
        quote = data["quote"]
        canvas.itemconfig(quote_text, text=quote)
        print(quote)
    elif response.status_code == 404:
        print("Error:", response.status_code)
    elif response.status_code == 401:
        print("Error:", response.status_code)
    #Write your code here.



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="day33/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="day33/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()