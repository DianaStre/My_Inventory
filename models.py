from flask_sqlalchemy import SQLAlchemy

"""SQLAlchemy is a Python library that allows us to work with a database using Python 
classes instead of raw SQL queries."""
db = SQLAlchemy()

class InventoryItem(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # Ok, Damaged, Sent for maintenance
    status = db.Column(db.String(50), nullable=False)  # Free, In use

    def __repr__(self):
        return f'<Item {self.id}: {self.item_name}, {self.type}, {self.status}>'
