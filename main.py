from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# noinspection PyUnresolvedReferences
class Cafes(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    map_url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(10), nullable=False)
    coffee_price = db.Column(db.String(10), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def get_all_cafes():
    if request.method == 'POST':
        text = request.form['text'].title()
        print(text)
        cafes = Cafes.query.filter_by(location=text)
    else:
        cafes = Cafes.query.all()

    return render_template("index.html", all_cafes=cafes)


@app.route('/cafe/id=<cafe_id>', methods=['GET'])
def get_cafe(cafe_id):

    cafe_ = Cafes.query.get(cafe_id)
    return render_template("cafe.html", cafe=cafe_)


@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
