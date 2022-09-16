from models.book import Book
from datetime import datetime, timedelta

dt = datetime.now()
td = timedelta(days=28)
return_date = dt + td

book1 = Book("Long Walk to Freedom", "Nelson Mandela", "Autobiography", False, None, "nelson_mandela")
book2 = Book("The Brothers Karamazov", "Fyodor Dostoevsky", "Novel", True, return_date, "Fyodor_Dostoevsky")
book3 = Book("Everything is Illuminated", "Jonathan Safran Foer", "Novel", False, None, "jonathan_safran_foer")
book4 = Book("Harry Potter", "JK Rowling", "Childrens", True, return_date, "jk_rowling")

books = [book1, book2, book3, book4]

books.sort(key=lambda x: x.genre, reverse=False)


def add_new_book(book):
    books.append(book)

def remove_book_by_title(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break
    books.remove(book_to_delete)

def checkout_book_by_title(book_title):
    book_to_checkout = None
    for book in books:
        if book.title == book_title:
            book_to_checkout = book
            break
    book.checked_out=True
    book.return_date=return_date

def return_book_by_title(book_title):
    book_to_return = None
    for book in books:
        if book.title == book_title:
            book_to_return = book
            break
    book.checked_out=False
    book.return_date=None