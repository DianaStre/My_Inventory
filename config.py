import os

"""The os module is a built-in Python library that allows interaction with the operating system.
It helps handle file paths dynamically"""

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) #This helps Flask find the database anywhere the project is stored.

#This class helps store settings for the app
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'inventory.db')
    #This means the database file will be located in the project folder.
    SQLALCHEMY_TRACK_MODIFICATIONS = False #This setting is optional, but setting it to False reduces memory usage.
