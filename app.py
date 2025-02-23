from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, InventoryItem

"""This app manages inventory for a small company with only one employee.
This is the main entry point of my Flask application. It handles routing, 
rendering templates, database interactions, and updating inventory items."""

#This section initializes flask and the database
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

#This section creates the database if it doesn't already exist
with app.app_context():
    db.create_all()

#This section defines the homepage route ("/")
@app.route('/')
def index():
    items = InventoryItem.query.all() #This retrieves the inventory items from the database
    return render_template('index.html', items=items)

#This section helps book an inventory item
@app.route('/book_item/<int:item_id>', methods=['POST'])
def book_item(item_id):
    item = InventoryItem.query.get_or_404(item_id) #id is passed dynamically
    item.status = "In use" #This updates the status of the item
    db.session.commit() #This saves the changes to the database
    return redirect(url_for('index')) #Redirects the user back to the homepage

#This is the admin panel route
@app.route('/admin')
def admin():
    items = InventoryItem.query.all() #This fetches all the items from the database
    return render_template('admin.html', items=items)

#This allows editing of inventory items
@app.route('/edit_item/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)

    if request.method == 'POST':
        item.type = request.form['type'] #This updates the item's type
        item.status = request.form['status'] #This updates the item's status
        db.session.commit()
        return redirect(url_for('admin')) #This redirects the user back to the homepage

    return render_template('edit_item.html', item=item)

if __name__ == '__main__': #This helps run the app, ensures the app is only run when executed directly
    app.run(debug=True)
