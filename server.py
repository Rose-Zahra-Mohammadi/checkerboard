from cmath import phase
from os import times
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def four():
    return render_template("4.html")

@app.route('/<int:x>/<int:y>')
def ixy(x,y):
    return render_template("xy.html", x = x, y =y)

@app.route('/10/10')
def tenten():
    return render_template("1010.html")

if __name__ == "__main__":
    app.run(debug=True)
