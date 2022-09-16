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
    book_checked_out = False
    book_return_date = None

    book_author_list = book_author.split()
    author_first = str(book_author_list[0])
    author_second = str(book_author_list[1])

    if len(book_author_list) == 3:
        author_third = str(book_author_list[2])
        book_author_link = author_first + "_" + author_second + "_" + author_third 

    elif len(book_author_list) == 4:
        author_fourth = str(book_author_list[3])
        book_author_link = author_first + "_" + author_second + "_" + author_third + "_" + author_fourth

    else:
        book_author_link = author_first + "_" + author_second
        
    new_book = Book(book_title, book_author, book_genre, book_checked_out, book_return_date, book_author_link)

    add_new_book(new_book)

    return render_template('index.html', books = books)

@app.route('/books/delete/<title>', methods = ['POST'])
def remove_book(title):
    remove_book_by_title(title)
    return redirect('/books')

@app.route('/books/checkout/<title>', methods = ['POST'])
def checkout_book(title):
    checkout_book_by_title(title)
    return redirect('/books')

@app.route('/books/return/<title>', methods = ['POST'])
def return_book(title):
    return_book_by_title(title)
    return redirect('/books')