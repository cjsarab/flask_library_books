from flask import render_template, request
from app import app
from models.book import Book
from models.book_list import *

@app.route('/books')
def index():
    return render_template('index.html', books=books)

@app.route('/books/<index>')
def book(index):
    book = books[int(index)]
    return render_template('book.html', book=book)
