from flask import Flask, render_template, request
from currency_converter import CurrencyConverter

app = Flask(__name__)
c = CurrencyConverter()
symbols = c.get_symbols()


@app.route('/')
def index():
    return render_template('index.html', symbols=symbols)

@app.route('/convert', methods=['POST', 'GET'],)
def convert():
    if request.method == 'GET':
        return render_template('index.html', symbols=symbols)
    amount = request.form['amount']

    if not amount or not amount.isnumeric():
        return render_template('index.html', error='Please enter a valid amount', symbols=symbols)

    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    result = c.convert(amount, from_currency, to_currency)
    message = f'{amount} {from_currency} is equal to {result} {to_currency}'
    return render_template('index.html', result=result, message=message, symbols=symbols)

if __name__ == '__main__':
    app.run(debug=True)