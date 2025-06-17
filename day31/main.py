from tkinter import *

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("day31/data/words_to_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv("day31/data/french_words.csv")
    to_learn = data.to_dict(orient="records")
    data = pandas.DataFrame(to_learn)
else:
    data = data.to_dict(orient="records")
#finally:
    

data_dict = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_fnt)
    flip_timer=window.after(2000, func=flip_card)

  
def flip_card():
    
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_bck)
def remove_word():
    data_dict.remove(current_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("day31/data/words_to_learn.csv", index=False)
    next_card()



# ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer=window.after(1000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_fnt=PhotoImage(file="day31/images/card_front.png")
card_bck=PhotoImage(file="day31/images/card_back.png") 
card_bg=canvas.create_image(400, 263, image=card_fnt)
card_title=canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic")) 
card_word=canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold")) 
canvas.grid(row= 0, column=0, columnspan=2)
# ---------------------------- Buttons ------------------------------- #
right_img = PhotoImage(file="day31/images/right.png")
wrong_img = PhotoImage(file="day31/images/wrong.png")

wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_img, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

# 
#canvas.create_text(400, 363, text="Word", font=("Ariel", 60, "bold"), fill="black")    
#canvas.create_image(400, 263, image=card_bck)
#canvas.create_text(400, 263, text="", font=("Ariel", 40, "italic"), fill="black")
#canvas.create_text(400, 363, text="", font=("Ariel", 60, "bold"), fill="black")
#canvas.create_image(400, 263, image=card_bck)
#canvas.create_image(400, 263, image=right_img)
#canvas.grid(column=1, row=0)
 
#canvas.grid(column=1, row=0)
#window.config(bg="white")
#window.config(padx=50, pady=50)
#canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)    
#canvas.grid(column=1, row=0)
#logo_img = PhotoImage(file="day29/logo.png")
#canvas.create_image(100, 100, image=logo_img)'''
  




next_card()
window.mainloop()