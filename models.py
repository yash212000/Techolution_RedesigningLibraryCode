'''This file defines the model of library management system,including managing books, users, and checkouts. '''


# importing necessary classes
from check import CheckManager
from book import Book
from user import User


class Library:
    def __init__(self):
        self.books = []  # to store list of book objects
        self.users = []  # to store list of user objects
        self.checkouts = []  # Will store tuples of (User, Book)
        self.check_manager = CheckManager(self)  # passing library's instance to check manager

    def add_book(self, title, author, isbn):  # adds a new book (object) to the library
        book = Book(title, author, isbn)
        self.books.append(book)
        return book

    def add_user(self, name, user_id):  # Adds a new user to the library.
        if not user_id.isdigit():
            print("Invalid user ID. User ID must be numeric.")
            return None

            # Check for uniqueness of the user_id
        if any(user.user_id == user_id for user in self.users):
            print(f"User ID {user_id} is already in use. Please choose a different User ID.")
            return None

        user = User(name, user_id)
        self.users.append(user)
        return user
        # user = User(name, user_id)
        # self.users.append(user)
        # return user

    def list_books(self):  # Returns a list of all books in the library.
        return self.books

    def list_users(self):  # Returns a list of all users in the library.
        return self.users

    def list_checkouts(self):  # Returns a list of all checkouts, with each entry showing the user name and book title.
        return [(user.name, book.title) for user, book in self.checkouts]

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.checked_out:
                    print(f"Cannot delete {book.title}. It is currently checked out.")
                    return
                self.books.remove(book)
                print(f"Book {book.title} deleted successfully.")
                return
        print("Book not found.")

    def delete_user(self, user_id):  # Deletes a user from the library if they have no books currently checked out.
        for user in self.users:
            if user.user_id == user_id:
                # Check if the user has any checked-out books
                if any(checkout[0].user_id == user_id for checkout in self.checkouts):
                    print(f"Cannot delete user {user.name}. They have checked out books.")
                    return
                self.users.remove(user)
                print(f"User {user.name} deleted successfully.")
                return
        print("User not found.")

    # Static method to check is number is ISBN
    @staticmethod
    def is_valid_isbn(isbn):
        if len(isbn) != 10 or not isbn.isdigit():
            return False
        total = sum((10 - i) * int(digit) for i, digit in enumerate(isbn))
        return total % 11 == 0
