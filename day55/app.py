from flask import Flask

app = Flask(__name__)

# Decorators
def make_bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper

def make_emphasis(fn):
    def wrapper():
        return "<em>" + fn() + "</em>"
    return wrapper

def make_underlined(fn):
    def wrapper():
        return "<u>" + fn() + "</u>"
    return wrapper

@app.route("/")
def hello_world():
    return (
        '<p>Hello, World!</p>'
        '<p>As soon as Bailey gets up he wants this </p>'
        '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnp0em04NHF3Z2dtMGh3YmVqZmtldmxyYzBkaWFscXJra2Vhazg1cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6UvJeCtn366Hu/giphy.gif">'
        '<p>After Bailey eats food this is what he does </p>'
        '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXRiZHljMGRtOWlpaWF5M2UybXNiNm9ta3ZrNzZrbG1zdDgxbmhzMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6Umkh0GwRYhfG/giphy.gif">'
    )

@app.route("/about")
def about():
    return "<p>This is the about page.</p>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "<p>Goodbye!</p>"

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)