from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB

class Base(DeclarativeBase):
  pass
#db = sqlite3.connect("books-collection.db")
#
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db= SQLAlchemy(model_class=Base)
# initialize the app with the extension
db.init_app(app)


# Define the books1 table
class Movie(db.Model):
    __tablename__ = "movies1"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False) 
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    reviews: Mapped[str] = mapped_column(String(500), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    trailer_youtube: Mapped[str] = mapped_column(String(250), nullable=False)
     
    def __repr__(self):
        return f"<Movie {self.title}>"    
# CREATE TABLE -  Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


@app.route("/")

def home():
    movies1 = db.session.execute(db.select(Movie).order_by(Movie.ranking.desc())).scalars().all()
    return render_template("index.html", movies1=movies1)

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    # logic to update movie
    movie = db.session.get(Movie, movie_id)
    if request.method == "POST":
        movie.title = request.form["title"]
        movie.year = int(request.form["year"])
        movie.description = request.form["description"]
        movie.rating = float(request.form["rating"])
        movie.ranking = int(request.form["ranking"])
        movie.reviews = request.form["reviews"]
        movie.img_url = request.form["img_url"]
        movie.trailer_youtube = request.form["trailer_youtube"]
        
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie)

@app.route("/delete/<int:movie_id>", methods=["GET","POST"])
def delete(movie_id):
    # logic to delete movie
    movie = db.session.get(Movie, movie_id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_movie = Movie(
            title=request.form["title"],
            year=int(request.form["year"]),
            description=request.form["description"],
            rating=float(request.form["rating"]),
            ranking=int(request.form["ranking"]),
            reviews=request.form["reviews"],
            img_url=request.form["img_url"],
            trailer_youtube=request.form["trailer_youtube"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("add.html")
      

if __name__ == '__main__':
    app.run(debug=True)
