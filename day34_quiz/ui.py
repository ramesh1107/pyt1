THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizUI:
    def __init__(self, quiz_brain:QuizBrain):
        self.question =quiz_brain
        self.window= Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, 
            text="Question",
            width=280, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_imgae=PhotoImage(file="day34/images/true.png")
        self.true_button=Button(image=true_imgae, highlightthickness=0, command=self.display_right_answer)
        self.true_button.grid(row=2, column=0)
        false_image=PhotoImage(file="day34/images/false.png")
        self.false_button=Button(image=false_image, highlightthickness=0, command=self.display_wrong_answer)    
        self.false_button.grid(row=2, column=1)
        self.display_question()
        #self.canvas.grid(row=1, column=0, columnspan=2)
        #self.question = question
        #self.score = score
        self.window.mainloop()


    def display_question(self):
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
         

    '''def display_score(self):
        print(f"Your current score is: {self.score}")
    def display_final_score(self):
        print(f"Your final score is: {self.score}")
    def display_correct_answer(self, correct_answer):
        print(f"The correct answer is: {correct_answer}")
    def display_wrong_answer(self):
        print("That's wrong.")
    def display_right_answer(self):     
        print("You got it right!")
    def display_next_question(self):
        print("Next question...")
    def display_game_over(self):
        print("Game Over")
    def display_score_summary(self):    
        print(f"Your final score is: {self.score}")
    def display_question_number(self, question_number):
        print(f"Question number: {question_number}")
    def display_question_text(self, question_text):
        print(f"Question text: {question_text}")
    def display_answer(self, answer):
        print(f"Answer: {answer}")
    def display_answer_summary(self, answer_summary):
        print(f"Answer summary: {answer_summary}")
    def display_answer_summary(self, answer_summary):
        print(f"Answer summary: {answer_summary}")'''
