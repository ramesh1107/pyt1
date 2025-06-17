from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean




app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafers(db.Model):
     __tablename__ = "cafers"
    # Define the columns of the Cafe table
     id: Mapped[int] = mapped_column(Integer, primary_key=True)
     name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
     map_url: Mapped[str] = mapped_column(String(500), nullable=False)
     img_url: Mapped[str] = mapped_column(String(500), nullable=False)
     location: Mapped[str] = mapped_column(String(250), nullable=False)
     seats: Mapped[str] = mapped_column(String(250), nullable=False)
     has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
     has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
     has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
     can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
     coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
     def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()



@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/all", methods=["GET"])
def get_all_cafe():
    cafes = db.session.execute(db.select(Cafers)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes]), 200

@app.route("/random", methods=["GET"])
def get_random():
    cafes = db.session.execute(db.select(Cafers)).order_by(Cafers.name).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes]), 200 
 
@app.route("/search", methods=["GET"])
def get_all_cafes():
    query = request.args.get("loc")
    if not query:
        return jsonify({"error": "Location query parameter is required"}), 400
    
    cafe = db.session.execute(db.select(Cafers).where(Cafers.location.ilike(f"%{query}%"))).scalar_one_or_none()
    
    if cafe:
        return jsonify({
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        }), 200
    else:
        return jsonify({"error": "Cafe not found"}), 404

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    data = request.get_json()

    new_cafe = Cafers(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data["seats"],
        has_toilet=data["has_toilet"],
        has_wifi=data["has_wifi"],
        has_sockets=data["has_sockets"],
        can_take_calls=data["can_take_calls"],
        coffee_price=data["coffee_price"]
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify({"message": "Cafe added successfully"}), 201# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
