from flask import Blueprint, request, redirect, render_template
from fruits.models import Fruit

views = Blueprint('views', __name__)

# route for home page: http://127.0.0.1:5000/
@views.route('/')
def index():
    return render_template('index.html')

# route for hello page: http://127.0.0.1:5000/hello
@views.route('/hello')
def hello():
    return 'you have reached the hello page'


# route for html page: http://localhost:5000/html
@views.route('/html')
def html():
    message = """
    <h1> Welcome to my webpage </h1>
    <p> This is my new webpage, come and check it out </p>
    """
    return message

# /say-hello/john => Hello John
# Dynamic route with a parameter http://localhost:5000/say-hello/john
@views.route('/say-hello/<name>')
def say_hello(name):
    # return f"Hello {name}"
    # return "Hello {}".format(name)
    return render_template('hello.html', name=name)


# /add/2/3 => 2 + 3 = 5
# Dynamic route with two parameters http://localhost:5000/add/2/3
@views.route('/add/<int:num1>/<int:num2>')
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
@views.route('/add')
def add_query():
    num1 = int(request.args['num1'])
    num2 = int(request.args.get('num2'))
    result = num1 + num2
    return f"{num1} + {num2} = {result}"
    # return render_template('calc.html', context=context)
    # return render_template('calc.html', num1=num1, num2=num2, result=num1 + num2)



# /fruits => viewsle, banana, orange
# http://localhost:5000/fruits
@views.route('/fruits', methods=['GET', 'POST'])
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


# /fruits/1 => viewsle
# /fruits/banana => banana
# Implement the above two routes