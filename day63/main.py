from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

##CREATE DATABASE
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
#db = sqlite3.connect("books-collection.db")
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db= SQLAlchemy(model_class=Base)
# initialize the app with the extension
db.init_app(app)

all_books = []
# Define the books1 table
class books1(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False) 
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()
    


@app.route('/')
def home():
    #db = sqlite3.connect("books-collection.db")
    # cursor = db.cursor()
    # cursor.execute("SELECT title, author, rating FROM books")
    # rows = cursor.fetchall()
    
    books = books1.query.all()
    
    return render_template("index.html", books=books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        new_book_entry = books1(title=new_book["title"], author=new_book["author"], rating=float(new_book["rating"]))
        db.session.add(new_book_entry)
        db.session.commit()
        print(all_books)
        return redirect(url_for('home'))
      
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)



#cursor = db.cursor()

#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute ("INSERT INTO books VALUES(2, 'Harry Potter_my head is splitting', 'J. K. Rowling', '9.9')")
# db.commit()
# cursor.execute("INSERT INTO books VALUES(3, 'Harry Potter-Chamber_ of Secrets', 'J. K. Rowling', '9.7')")
# cursor.execute("INSERT INTO books VALUES(4, 'Harry Potter- Prisoner _of Azkaban', 'J. K. Rowling', '8.9')")
# cursor.execute("INSERT INTO books VALUES(5, 'Harry Potter- Goblet_ of Fire', 'J. K. Rowling', '9.0')")
# cursor.execute("INSERT INTO books VALUES(6, 'Harry Potter- Order_ of Phoenix', 'J. K. Rowling', '8.7')")
# cursor.execute("SELECT * FROM books")
# db.commit()
