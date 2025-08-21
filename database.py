import sqlite3

def init_db():
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS events
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  date TEXT NOT NULL,
                  location TEXT NOT NULL,
                  category TEXT NOT NULL,
                  description TEXT,
                  price_type TEXT NOT NULL,
                  price_value TEXT,
                  ticket_types TEXT)''')
    # Add sample events
    sample_events = [
        ("Wits Tech Summit", "2025-09-10", "Wits Main Campus", "Tech", "Annual tech conference", "Paid", "150", "General,VIP"),
        ("Career Fair 2025", "2025-10-05", "Wits Great Hall", "Career", "Meet top employers", "Free", "", "General"),
        ("Wits Music Festival", "2025-11-20", "Johannesburg Park", "Social", "Live music and food", "Paid", "200", "Early Bird,VIP,VVIP")
    ]
    c.executemany('INSERT OR IGNORE INTO events (title, date, location, category, description, price_type, price_value, ticket_types) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', sample_events)
    conn.commit()
    conn.close()

def get_events(category):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    if category == 'All':
        c.execute('SELECT * FROM events')
    else:
        c.execute('SELECT * FROM events WHERE category = ?', (category,))
    events = c.fetchall()
    conn.close()
    return events

def add_event(title, date, location, category, description, price_type, price_value, ticket_types):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    ticket_types_str = ','.join(ticket_types) if ticket_types else ''
    c.execute('INSERT INTO events (title, date, location, category, description, price_type, price_value, ticket_types) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
              (title, date, location, category, description, price_type, price_value, ticket_types_str))
    conn.commit()
    conn.close()