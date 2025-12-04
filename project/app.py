from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize database (creates table if not exists)
def init_db():
    conn = sqlite3.connect('visitors.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            visit_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # Initialize database when app starts

# Homepage
@app.route('/')
def home():
    # Log visitor with dummy data (you can replace with real form later)
    conn = sqlite3.connect('visitors.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO visitors (name, email, phone, visit_time) VALUES (?, ?, ?, ?)",
                   ("Guest", "guest@example.com", "0000000000", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
    return render_template('index.html')

# Courses page
@app.route('/courses')
def courses():
    course_data = [
        {"name": "CSE", "placement": "95%"},
        {"name": "ECE", "placement": "90%"},
        {"name": "MECH", "placement": "85%"},
        {"name": "CIVIL", "placement": "80%"}
    ]
    return render_template('courses.html', courses=course_data)

# Show visitor data
@app.route('/show-data')
def show_data():
    conn = sqlite3.connect('visitors.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM visitors")
    data = cursor.fetchall()
    conn.close()
    return render_template('show_data.html', visitors=data)

if __name__ == "__main__":
    app.run(debug=True)
