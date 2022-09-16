from flask import render_template, request, redirect
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

@app.route('/books', methods = ['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']

    new_book = Book(book_title, book_author, book_genre)

    add_new_book(new_book)

    return render_template('index.html', books = books)

@app.route('/books/delete/<title>', methods = ['POST'])
def remove_book(title):
    remove_book_by_title(title)
    return redirect('/books')