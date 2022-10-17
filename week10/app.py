from flask import Flask

app = Flask(__name__)


# Routes
@app.route('/hello')
def index():
    return "Hello world"



if __name__ == "__main__":
    app.run(debug=True)