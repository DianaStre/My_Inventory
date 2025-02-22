from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, InventoryItem

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    items = InventoryItem.query.all()
    return render_template('index.html', items=items)

@app.route('/book_item/<int:item_id>', methods=['POST'])
def book_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    item.status = "In use"
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    items = InventoryItem.query.all()
    return render_template('admin.html', items=items)

@app.route('/edit_item/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)

    if request.method == 'POST':
        item.type = request.form['type']
        item.status = request.form['status']
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('edit_item.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)
