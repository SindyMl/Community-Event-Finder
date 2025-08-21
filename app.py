from flask import Flask, render_template, request, redirect, url_for
from database import init_db, get_events, add_event

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    category = request.args.get('category', 'All')
    events = get_events(category)
    categories = ['All', 'Tech', 'Career', 'Social', 'Academic', 'Cultural', 'Sports']  # Expanded categories
    return render_template('index.html', events=events, categories=categories, selected_category=category)

@app.route('/add', methods=['GET', 'POST'])
def add_event_route():
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        location = request.form['location']
        category = request.form['category']
        description = request.form['description']
        price_type = request.form['price_type']
        price_value = request.form.get('price_value', '')
        ticket_types = request.form.getlist('ticket_types')  # Multi-select
        add_event(title, date, location, category, description, price_type, price_value, ticket_types)
        return redirect(url_for('index'))
    return render_template('add_event.html')

if __name__ == '__main__':
    init_db()  # Initialize database with sample data
    app.run(debug=True)