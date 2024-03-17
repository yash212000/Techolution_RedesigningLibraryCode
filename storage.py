'''This file saves the library data on exitting the program in a JSON file in a dictionary format'''
import json

def save_data(filename, data): # Saves data (books or users) to a JSON file

    with open(filename, 'w') as f:
        json.dump([obj.__dict__ for obj in data], f)

