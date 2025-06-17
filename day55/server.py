from flask import Flask
import random
from flask import render_template

app = Flask(__name__)

# Decorators
# def make_bold(fn):
#     def wrapper():
#         return "<b>" + fn() + "</b>"
#     return wrapper

# def make_emphasis(fn):
#     def wrapper():
#         return "<em>" + fn() + "</em>"
#     return wrapper

# def make_underlined(fn):
#     def wrapper():
#         return "<u>" + fn() + "</u>"
#     return wrapper

@app.route("/")
def hello_world():
    return (
        '<h1>Guess a number between 0 and 9</h1>'
       
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
        
    )
number = random.randint(0, 9)
print("Random number is:", number)
@app.route("/<int:guess>")
def guess(guess):
    if guess < number:
        return ("<h1 style='color:blue'>Too low, try again!</h1>"
                "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjY5NzJsZGh5dG1lNDU1M3QwZDdlaGlrM3prdXltM2FkbzluNmZjdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wodRGe3IkEkQpV5LIv/giphy.gif'>"
                )
            
    elif guess > number:
        return ("<h1 style='color:red'>Too high, try again!</h1>"
                "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGNjOWE2M3Y1anhveWpieWhtMGt5b3hqd2JxN3ZyNHRqYnZ1bTB6dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EYJjKIDi5FKEg/giphy.gif'>"
        )
    else:
        return ("<h1 style='color:green'>You found me!</h1>"
                "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjUwbmlraWQ2bTh6ajRwbnE0MTF1NHhpMjdlanJxeHFvMmtncjdyNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3tTg6UVj3mV6QmgURz/giphy.gif'>"
        )
# @app.route("/about")
# def about():
#     return "<p>This is the about page.</p>"

# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
# def bye():
#     return "<p>Goodbye!</p>"

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)