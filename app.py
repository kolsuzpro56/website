from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Ana sayfa"

@app.route("/secret")
def secret():
    return "Gizli sayfa"

@app.route("/yazitura")
def yazi_tura():
    return random.choice(["Yazi", "Tura"])

@app.route("/sifre")
def sifre():
    karakterler = "abc123"
    sifre = ""

    for i in range(5):
        sifre += random.choice(karakterler)

    return sifre

if __name__ == "__main__":
    app.run(debug=True)
