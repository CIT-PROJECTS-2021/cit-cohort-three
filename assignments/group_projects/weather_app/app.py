# Weather Forecast App using OpenWeatherMap API and Flask

from flask import Flask, render_template, request
import requests
import json
from keys import API_KEY

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']

        if city == '':
            return render_template('index.html', error='Please enter a city name')

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format(city, API_KEY)
        r = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': f"http://openweathermap.org/img/w/{r['weather'][0]['icon']}.png"
        }
        return render_template('weather.html', weather=weather)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)