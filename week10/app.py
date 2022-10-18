from flask import Flask, redirect, render_template, request

myapp = Flask(__name__)

fruits = ['apple', 'banana', 'orange']


@myapp.route('/')
def index():
    return render_template('index.html')


@myapp.route('/hello')
def hello():
    return 'you have reached the hello page'


@myapp.route('/html')
def html():
    message = """
    <h1> Welcome to my webpage </h1>
    <p> This is my new webpage, come and check it out </p>
    """
    return message

# /say-hello/john => Hello John
@myapp.route('/say-hello/<name>')
def say_hello(name):
    # return f"Hello {name}"
    # return "Hello {}".format(name)
    return render_template('hello.html', name=name)


# /add/2/3 => 2 + 3 = 5
@myapp.route('/add/<int:num1>/<int:num2>')
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
@myapp.route('/add')
def add_query():
    num1 = int(request.args['num1'])
    num2 = int(request.args.get('num2'))
    result = num1 + num2
    return f"{num1} + {num2} = {result}"


# /fruits => apple, banana, orange
@myapp.route('/fruits', methods=['GET', 'POST'])
def add_fruits():
    if request.method == 'POST':
        fruit = request.form['fruit']
        
        if not fruit:
            return "Please enter a fruit"

        fruits.append(fruit)
        return redirect('/fruits')

    return render_template('fruits.html', fruits=fruits)


# /fruits/1 => apple
# /fruits/banana => banana
# Implement the above two routes



if __name__ == '__main__':
    myapp.run(debug=True)
    # myapp.run(host='127.0.0.1', port=3000, debug=True)