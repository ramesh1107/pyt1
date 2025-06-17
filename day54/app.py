from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p>Hello, World!</p>'\
        '<p>As soon as bailey gets up he wants this </p>'\
        '<img src=https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnp0em04NHF3Z2dtMGh3YmVqZmtldmxyYzBkaWFscXJra2Vhazg1cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6UvJeCtn366Hu/giphy.gif>'\
        '<p>after Bailey eats food this is what he does </p>'\
        '<img src=https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXRiZHljMGRtOWlpaWF5M2UybXNiNm9ta3ZrNzZrbG1zdDgxbmhzMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6Umkh0GwRYhfG/giphy.gif>'  
        


print("Starting Flask app...")
@app.route("/about")
def about():
    return "<p>This is the about page.</p>"

if __name__ == "__main__":
    print("Inside main block")
    app.run(debug=True)
    
