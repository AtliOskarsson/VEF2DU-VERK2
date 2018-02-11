from flask import Flask, render_template
from application import app
from application import model

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", booklist = model.booklist)

app.route("/book/<theBook>")
def book(theBook = None):
    return render_template("books.html", book = model.urlCheck(model.booklist, theBook).check())