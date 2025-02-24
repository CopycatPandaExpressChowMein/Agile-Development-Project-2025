from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, timedelta
from PyQt5.QtWidgets import *
import requests

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('mood_tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mood (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT UNIQUE,
                    mood INTEGER CHECK(mood BETWEEN 1 AND 5))''')
    conn.commit()
    conn.close()

# Insert or update daily mood
def insert_mood(date, mood):
    conn = sqlite3.connect('mood_tracker.db')
    c = conn.cursor()
    c.execute('''INSERT INTO mood (date, mood) VALUES (?, ?) 
                 ON CONFLICT(date) DO UPDATE SET mood=excluded.mood''', (date, mood))
    conn.commit()
    conn.close()

# Fetch last 7 days of mood data
def get_weekly_average():
    conn = sqlite3.connect('mood_tracker.db')
    c = conn.cursor()
    past_week = (datetime.now() - timedelta(days=6)).strftime('%Y-%m-%d')
    c.execute("SELECT AVG(mood) FROM mood WHERE date >= ?", (past_week,))
    avg_mood = c.fetchone()[0]
    conn.close()
    return round(avg_mood, 2) if avg_mood else None

@app.route('/submit_mood', methods=['POST'])
def submit_mood():
    data = request.json
    date = data.get('date', datetime.now().strftime('%Y-%m-%d'))  # Default to today
    mood = data.get('mood')
    if not (1 <= mood <= 5):
        return jsonify({"error": "Mood should be between 1 and 5"}), 400
    insert_mood(date, mood)
    return jsonify({"message": "Mood recorded successfully"})

@app.route('/weekly_average', methods=['GET'])
def weekly_average():
    avg_mood = get_weekly_average()
    return jsonify({"weekly_average": avg_mood if avg_mood else "No data available"})

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("How are you feeling today? (1-5)")
        self.mood_input = QSpinBox()
        self.mood_input.setRange(1, 5)
        self.submit_button = QPushButton("Submit Mood")
        self.submit_button.clicked.connect(self.submit_mood)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.mood_input)
        self.layout.addWidget(self.submit_button)
        self.setLayout(self.layout)

    def submit_mood(self):
        mood_value = self.mood_input.value()
        response = requests.post("http://127.0.0.1:5000/submit_mood", json={"mood": mood_value})
        QMessageBox.information(self, "Response", response.json().get("message", "Error"))

class StatisticsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Weekly Average Mood: ")
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.fetch_weekly_average)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.refresh_button)
        self.setLayout(self.layout)
        self.fetch_weekly_average()

    def fetch_weekly_average(self):
        response = requests.get("http://127.0.0.1:5000/weekly_average")
        avg_mood = response.json().get("weekly_average", "No data available")
        self.label.setText(f"Weekly Average Mood: {avg_mood}")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
