from flask import Flask, redirect, render_template, request
from config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from datetime import datetime

# db variable initialization
db = SQLAlchemy()

# Marshmallow initialization
ma = Marshmallow()

# initialize migrate 
migrate = Migrate()

# create flask instance
app = Flask(__name__)

# app configuration
app.config['SECRET_KEY'] = app_config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = app_config['DB']

db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)

class ExtraMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# fruits model
class Fruit(db.Model, ExtraMixin):
    __tablename__ = 'fruits'
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()


# route for home page: http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template('index.html')

# route for hello page: http://127.0.0.1:5000/hello
@app.route('/hello')
def hello():
    return 'you have reached the hello page'


# route for html page: http://localhost:5000/html
@app.route('/html')
def html():
    message = """
    <h1> Welcome to my webpage </h1>
    <p> This is my new webpage, come and check it out </p>
    """
    return message

# /say-hello/john => Hello John
# Dynamic route with a parameter http://localhost:5000/say-hello/john
@app.route('/say-hello/<name>')
def say_hello(name):
    # return f"Hello {name}"
    # return "Hello {}".format(name)
    return render_template('hello.html', name=name)


# /add/2/3 => 2 + 3 = 5
# Dynamic route with two parameters http://localhost:5000/add/2/3
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1 + num2
    }
    return render_template('calc.html', context=context)
    # return render_template('calc.html', num1=num1, num2=num2, result=num1 + num2)


# query string
# /add?num1=1&num2=2 => 1 + 2 = 3
# http://localhost:5000/add?num1=1&num2=2
@app.route('/add')
def add_query():
    num1 = int(request.args['num1'])
    num2 = int(request.args.get('num2'))
    result = num1 + num2
    return f"{num1} + {num2} = {result}"
    # return render_template('calc.html', context=context)
    # return render_template('calc.html', num1=num1, num2=num2, result=num1 + num2)



# /fruits => apple, banana, orange
# http://localhost:5000/fruits
@app.route('/fruits', methods=['GET', 'POST'])
def add_fruits():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        price = request.form['price']
        fruit = Fruit(name=name, color=color, price=price)
        fruit.save()
        return redirect('/fruits')
        

    fruits = Fruit.get_all()
    return render_template('fruits.html', fruits=fruits)
    


# url_for => path to a function
# url_for('add_fruits') => /fruits


# /fruits/1 => apple
# /fruits/banana => banana
# Implement the above two routes



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=3000, debug=True)