from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/category')
def category():
    return render_template("category.html")

if __name__ == '__main__':
    app.run(debug=True)
