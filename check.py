'''Manages the check-in and check-out processes for books in the library.
It's used by the Library class(in models.py) to update book statuses and track which books are currently checked out.
Note that: Check-out means issuing the book from library to user.
Check-in means returning the book by user to Library.
'''
class CheckManager:
    def __init__(self, library):
        self.library = library

    def checkout_book(self, user_id, isbn): # Issues a book(check-out) to a user if it's available
        # next() here retrieves the next item from the iterator(generator), if item is not present is returns None
        user = next((user for user in self.library.users if user.user_id == user_id), None)
        book = next((book for book in self.library.books if book.isbn == isbn), None)
        if user and book and not book.checked_out: #checking if user and book are present and book has not been checked out
            book.checked_out = True
            self.library.checkouts.append((user, book))
            print(f"Book {book.title} checked out by {user.name}.")
        else:
            print("Checkout failed. Book might be unavailable or already checked out.")

    def checkin_book(self, isbn): # Checks in a book from user, making it available again
        book = next((book for book in self.library.books if book.isbn == isbn), None)
        if book and book.checked_out:
            book.checked_out = False
            self.library.checkouts = [(user, bk) for user, bk in self.library.checkouts if bk.isbn != isbn]
            print(f"Book {book.title} checked in.")
        else:
            print("Check-in failed. Book might not be checked out or doesn't exist.")

