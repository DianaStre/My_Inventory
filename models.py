from flask_sqlalchemy import SQLAlchemy

"""SQLAlchemy is a Python library that allows us to work with a database using Python 
classes instead of raw SQL queries. The SQLAlchemy instance helps create and manage database tables."""

db = SQLAlchemy() #This initializes the database

# This defines a database model for inventory items.
# The class represents a single table in the database.
class InventoryItem(db.Model):
    __tablename__ = 'inventory' #This sets the table's name to "inventory" to ensure consistency.
#Here, we define each of the table columns
    id = db.Column(db.Integer, primary_key=True) #this defines an integer column in the database
    item_name = db.Column(db.String(100), nullable=False) #This defines a string column with a maximum of 100 characters.
    type = db.Column(db.String(50), nullable=False)  # Ok, Damaged, Sent for maintenance
    status = db.Column(db.String(50), nullable=False)  # Free, In use

#This helps with representing the Object as a String
#It helps debugging by making it easy to inspect objects.
    def __repr__(self): #This is a method that controls how objects appear when printed.
        return f'<Item {self.id}: {self.item_name}, {self.type}, {self.status}>'
