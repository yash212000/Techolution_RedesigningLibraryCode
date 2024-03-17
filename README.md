The Library Management System is designed to facilitate the management of a library's inventory, including books and users, as well as the process of checking books in and out. 
The system provides a command-line interface (CLI) to perform various operations such as adding, deleting, and listing books and users, and managing book loans.

Object-Oriented Approach
The system is built using OOPs principles. Key entities like books, users, and checkouts are represented as classes, encapsulating related data and behaviors.

Classes used in  the code:
Book: Represents a book in the library, with attributes such as title, author, ISBN, and a checked-out status.
User: Represents a library user, with a name and a unique numeric user ID.
Library: Acts as the central management class, containing lists of books and users, and methods to add, delete, list, and manage these entities.
Also, since Library is a class, we can scale this program to include multiple libraries.
CheckManager: Handles the checking in and out of books, ensuring updates to book availability and tracking current loans.

