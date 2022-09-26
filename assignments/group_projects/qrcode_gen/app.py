from flask import Flask, render_template, request, redirect, url_for

from qrcode_gen import QRCodeGenerator



app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form["data"]
        qr = QRCodeGenerator()
        img = qr.generate(data)
        img.save("static/qr.png")
        return redirect(url_for("index"))
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)