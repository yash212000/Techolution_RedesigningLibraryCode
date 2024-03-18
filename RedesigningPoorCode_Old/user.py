'''This file defines User Class representing users of the library with basic information like name and user ID.'''

class User:
    def __init__(self, name, user_id): # Initializes new user object with name and user ID
        self.name = name
        self.user_id = user_id

    def __repr__(self): # Provides a string representation of user object, used while printing.
        return f"User(name={self.name}, user_id={self.user_id})"
