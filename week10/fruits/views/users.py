from flask import Blueprint, render_template, request, redirect, url_for, flash
from fruits.models import User

userviews = Blueprint('userviews', __name__, url_prefix='/users')


@userviews.route('/')
def index():
    return render_template('home.html')


@userviews.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.get_user_by_username(username)

        if user and User.verify_password(password, user.password):
            flash('Login successful')
            return redirect(url_for('userviews.index'))
        else:
            flash('Login failed')
            return redirect(url_for('userviews.login'))
    return render_template('login.html')


@userviews.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # check if user already exists
        existing_user = User.get_user_by_email(email)
        if existing_user:
            flash('Email already exists')
            return redirect(url_for('userviews.register'))

        if User.get_user_by_username(username):
            flash('Username already exists')
            return redirect(url_for('userviews.register'))

        # create new user
        user = User(
            username=username,
            email=email,
            password=User.hash_password(password)
        )
        user.save()
        flash('Your account has been created, please login')
        return redirect(url_for('userviews.login'))
    return render_template('register.html')



@userviews.route('/logout')
def logout():
    return "logout"