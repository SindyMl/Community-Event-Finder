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
                  description TEXT)''')
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

def add_event(title, date, location, category, description):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('INSERT INTO events (title, date, location, category, description) VALUES (?, ?, ?, ?, ?)',
              (title, date, location, category, description))
    conn.commit()
    conn.close()