from flask import Flask
from config import Config
from models import db, InventoryItem
import pandas as pd

"""This file  is responsible for creating the database and importing data from an Excel file into the database.
It ensures that the inventory data is automatically added when setting up the application."""

#This section initializes flask and the database
app = Flask(__name__) #This creates the flask app
app.config.from_object(Config) #This loads the database configuration from config.py
db.init_app(app) #this connects SQLAlchemy to the app

#This section creates the database
def create_database(): #This ensures that the table exists in the database
    with app.app_context():
        db.create_all() #If the database doesn't exist, it creates a new table based on the model InventoryItem
        print("Database created successfully!")

#This section helps read the inventory data from the Excel file
def import_data_from_excel():
    df = pd.read_excel('inventory_data.xlsx') #This loads the spreadsheet as a Pandas DataFrame

#This section adds the data to the database
    with app.app_context():
        for _, row in df.iterrows(): #This loops through each row
            item = InventoryItem(
                id=int(row['Inventoty item no.']),  # Fixing typo or format issues
                item_name=row['inventory item name'],
                type=row['inventory type'], #This reads the item's type
                status=row['inventory status'] #This reads the item's status
            )
            db.session.add(item) #This adds items to the database
        db.session.commit() #This saves the newly added data
        print("Data imported successfully!") #This confirms a successful import

#This section runs the script
if __name__ == "__main__": #This ensures the script only runs when executed directly
    create_database() #This creates the SQLite database
    import_data_from_excel() #This imports the data from the Excel file
