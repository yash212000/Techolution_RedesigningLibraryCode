'''This is the main file, execution starts here
It creates a library object and gives a menu for user to choose from different available operations
It provides a command-line interface for the library management system
'''
from book import Book
from user import User
from models import Library
from storage import save_data


def main():
    library = Library()  # creating a library object, by this we can even create multiple libraries
    # by creating multiple library objects and handle them with this program.

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
        try: # Using a try-except block to catch and handle any potential errors
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
        except ValueError as e: # Catches ValueError exceptions and prints an error message
            print(f"Error: {e}. Please try again.")
        except Exception as e: # Catches any other exceptions and prints an error message
            print(f"An unexpected error occurred: {e}. Please try again.")


if __name__ == "__main__":
    main()
