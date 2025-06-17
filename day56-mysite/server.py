
from flask import Flask, render_template
import random
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

# @app.route("/about")
# def hello_world():
#     return render_template("ramesh.html")    
if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
