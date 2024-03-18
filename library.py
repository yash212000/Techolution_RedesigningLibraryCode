"""This class defines the book class representing the books of the library and has attributes like title,author,
isbn etc."""


class Book:  # defining the book class
    def __init__(self, title, author, isbn):  # constructor to initialize a book object
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def __repr__(self):  # __repr__() will print the information about book object
        status = 'Available' if not self.checked_out else 'Checked out'
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, status={status})"


'''This class defines User Class representing users of the library with basic information like name and user ID.'''


class User:
    def __init__(self, name, user_id):  # Initializes new user object with name and user ID
        self.name = name
        self.user_id = user_id

    def __repr__(self):  # Provides a string representation of user object, used while printing.
        return f"User(name={self.name}, user_id={self.user_id})"


'''This file defines the model of library management system,including managing books, users, and checkouts. '''


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


'''
This class Manages the check-in and check-out processes for books in the library.
It's used by the Library class(in models.py) to update book statuses and track which books are currently checked out.
Note that: Check-out means issuing the book from library to user.
Check-in means returning the book by user to Library.
'''


class CheckManager:
    def __init__(self, library):
        self.library = library

    def checkout_book(self, user_id, isbn):  # Issues a book(check-out) to a user if it's available
        # next() here retrieves the next item from the iterator(generator), if item is not present is returns None
        user = next((user for user in self.library.users if user.user_id == user_id), None)
        book = next((book for book in self.library.books if book.isbn == isbn), None)
        if user and book and not book.checked_out:  # checking if user and book are present and book has not been
            # checked out
            book.checked_out = True
            self.library.checkouts.append((user, book))
            print(f"Book {book.title} checked out by {user.name}.")
        else:
            print("Checkout failed. Book might be unavailable or already checked out.")

    def checkin_book(self, isbn):  # Checks in a book from user, making it available again
        book = next((book for book in self.library.books if book.isbn == isbn), None)
        if book and book.checked_out:
            book.checked_out = False
            self.library.checkouts = [(user, bk) for user, bk in self.library.checkouts if bk.isbn != isbn]
            print(f"Book {book.title} checked in.")
        else:
            print("Check-in failed. Book might not be checked out or doesn't exist.")


'''This class saves the library data on exiting the program in a JSON file in a dictionary format'''

import json


def save_data(filename, data):  # Saves data (books or users) to a JSON file

    with open(filename, 'w') as f:
        json.dump([obj.__dict__ for obj in data], f)


'''This is the main function, execution starts here
It creates a library object and gives a menu for user to choose from different available operations
It provides a command-line interface for the library management system
'''


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add User")
        print("3. Checkout Book")
        print("4. Check-in Book")
        print("5. List Books")
        print("6. List Users")
        print("7. List Checkouts")
        print("8. Delete Book")
        print("9. Delete User")
        print("10. Exit")
        choice = input("Enter choice: ")
        try:  # Using a try-except block to catch and handle any potential errors
            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN (10 digits): ")
                if not library.is_valid_isbn(isbn):
                    print("Invalid ISBN. Please try again.")
                    continue
                library.add_book(title, author, isbn)
                print("Book added successfully.")

            elif choice == '2':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                library.add_user(name, user_id)
                print("User added successfully.")

            elif choice == '3':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                library.check_manager.checkout_book(user_id, isbn)

            elif choice == '4':
                isbn = input("Enter ISBN of the book to check in: ")
                library.check_manager.checkin_book(isbn)

            elif choice == '5':
                print("Books:")
                for book in library.list_books():
                    print(book)

            elif choice == '6':
                print("Users:")
                for user in library.list_users():
                    print(user)

            elif choice == '7':
                print("Checkouts:")
                for checkout in library.list_checkouts():
                    print(f"User: {checkout[0]}, Book: {checkout[1]}")

            elif choice == '8':
                isbn = input("Enter ISBN of the book to delete: ")
                if not library.is_valid_isbn(isbn):
                    print("Invalid ISBN. Please try again.")
                    continue
                library.delete_book(isbn)

            elif choice == '9':
                user_id = input("Enter user ID of the user to delete: ")
                library.delete_user(user_id)

            elif choice == '10':
                save_data('books.json', library.books)
                save_data('users.json', library.users)
                print("Data saved. Exiting.")
                break

            else:
                print("Invalid choice, please try again.")
        except ValueError as e:  # Catches ValueError exceptions and prints an error message
            print(f"Error: {e}. Please try again.")
        except Exception as e:  # Catches any other exceptions and prints an error message
            print(f"An unexpected error occurred: {e}. Please try again.")


if __name__ == "__main__":
    main()
