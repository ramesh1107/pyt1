
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comicsans"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    print("Timer reset")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():   
    global reps 
    reps += 1
    print (reps)
    work_sec = WORK_MIN *5# 60
    short_break_sec = SHORT_BREAK_MIN * 5# 60
    long_break_sec = LONG_BREAK_MIN * 5# 60
    # If reps is odd, it's time for work
    if reps % 8 == 0:
        # Long break
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # Short break
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        # Work
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)

    #countdown(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    # Calculate minutes and seconds
    minutes = math.floor (count / 60)
    seconds = count % 60

    # Update the timer text to display minutes and seconds
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
   # canvas.itemconfig(timer_text, text=f"{count:02}")
    print (count)
    if count >0:
         global timer
         timer = window.after(1000, countdown,count -1 ) 
    else:
        # When the timer reaches zero, update the checkmarks label
        mark =""
        for _ in range (math.floor(reps / 2)):
            mark += "✔️"
        checkmarks_label.config(text=mark)
        # Start the next timer
        start_timer()
   
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

def say (a,b,c):
    print(a)
    print(b)
    print(c)
    # You can also use the after method to schedule a function to be called after a certain amount of time
    # For example, to call the say function after 1 second (1000 milliseconds):
    #

 # Example of using after method

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

#title  Labels
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)
# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)  
# Checkmarks
text="✔️" 
checkmarks_label = Label(fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)
# Entry
'''entry = Entry(width=10, font=(FONT_NAME, 35, "bold"))
entry.grid(column=1, row=4)
entry.insert(0, "00:00")
# Entry button
def entry_button_clicked():
    # Get the value from the entry field
    entry_value = entry.get()
    # Update the timer text with the value from the entry field
    canvas.itemconfig(timer_text, text=entry_value)
    # Optionally, you can also start the timer with this value
    # start_timer(entry_value)
entry_button = Button(text="Set Timer", command=entry_button_clicked)
entry_button.grid(column=1, row=5)
# Entry button to start the timer with the value from the entry field
def countdown(count):   
    # Calculate minutes and seconds
    minutes = count // 60
    seconds = count % 60
    # Update the timer text
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    # Stop the timer when it reaches zero
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        checkmarks_label.config(text="✔️") '''







window.mainloop()
