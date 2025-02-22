from flask import Flask
from config import Config
from models import db, InventoryItem
import pandas as pd

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def create_database():
    with app.app_context():
        db.create_all()
        print("Database created successfully!")

def import_data_from_excel():
    df = pd.read_excel('inventory_data.xlsx')

    with app.app_context():
        for _, row in df.iterrows():
            item = InventoryItem(
                id=int(row['Inventoty item no.']),  # Fixing typo
                item_name=row['inventory item name'],
                type=row['inventory type'],
                status=row['inventory status']
            )
            db.session.add(item)
        db.session.commit()
        print("Data imported successfully!")

if __name__ == "__main__":
    create_database()
    import_data_from_excel()
