# create a url shortner using flask and mysql

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import yaml
import random
import string
import re

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['db']['host']
app.config['MYSQL_USER'] = db['db']['user']
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = db['db']['database']

mysql = MySQL(app)

# configure templates in the templates folder
app.config['TEMPLATES_AUTO_RELOAD'] = True

# app features
# 1. create a short url
# 2. redirect to the original url
# 3. display all the urls
# 4. delete a url
# 5. update a url


def generate_short_url():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

# create a short url
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # fetch form data
        long_url = request.form['long_url']

        if long_url == '':
            return render_template('index.html', error='URL Field cannot be blank')

        # check if the url is valid
        if not re.match(r'(http|https)://', long_url):
            return render_template('index.html', error='URL is not valid')

        # check if the url already exists
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM urls WHERE long_url = %s", (long_url,))
        mysql.connection.commit()
        result = cur.fetchone()
        if result:
            return render_template('index.html', error='URL already exists', short_url=result[2])

        short_url = 'http://localhost:5000/' + generate_short_url()
        cur.execute("INSERT INTO urls(long_url, short_url) VALUES(%s, %s)", (long_url, short_url))
        mysql.connection.commit()
        cur.close()
        # show the short url created
        return render_template('index.html', short_url=short_url)       
    return render_template('index.html')

# redirect to the original url
@app.route('/<string:short_url>')
def redirect_to_url(short_url):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM urls WHERE short_url = %s", ['http://localhost:5000/' + short_url])
    if result > 0:
        url = cur.fetchone()
        visits = cur.execute("SELECT visits FROM visits WHERE short_url = %s", [url[0]])
        if visits > 0:
            cur.execute("UPDATE visits SET visits = visits + 1 WHERE short_url = %s", [url[0]])
            mysql.connection.commit()
        else:
            cur.execute("INSERT INTO visits(visits, short_url) VALUES(%s, %s)", (1, url[0]))
            mysql.connection.commit()
        visits = cur.fetchone()
        cur.close()
        return redirect(url[1])
    return 'No url found'

# display all the urls
@app.route('/display')
def display():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM urls")
    if result > 0:
        urls = cur.fetchall()
        return render_template('display.html', urls=urls)
    return 'No url found'

# delete a url
@app.route('/delete/<string:id>', methods=['GET', 'POST'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM urls WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('display'))

# update a url
@app.route('/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = request.form['short_url']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE urls SET long_url = %s, short_url = %s WHERE id = %s", (long_url, short_url, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('display'))
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM urls WHERE id = %s", [id])
    if result > 0:
        url = cur.fetchone()
        return render_template('update.html', url=url)
    return 'No url found'

if __name__ == '__main__':
    app.run(debug=True)

