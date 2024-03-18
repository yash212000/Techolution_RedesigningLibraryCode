'''This file defines the book class representing the books of the library and has attributes like title,author,isbn etc.'''
class Book:  # defining the book class
    def __init__(self, title, author, isbn):  # constructor to initialize a book object
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def __repr__(self):  # __repr__() will print the information about book object
        status = 'Available' if not self.checked_out else 'Checked out'
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, status={status})"
