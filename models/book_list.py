from models.book import Book

book1 = Book("Long Walk to Freedom", "Nelson Mandela", "Autobiography")
book2 = Book("The Brothers Karamazov", "Fyodor Dostoevsky", "Novel")
book3 = Book("Everything is Illuminated", "Jonathan Safran Foer", "Novel")

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def remove_book_by_title(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break

    books.remove(book_to_delete)