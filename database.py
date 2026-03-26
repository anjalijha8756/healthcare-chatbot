import sqlite3
import os

DB_NAME = 'healthcare.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Create tables for storing chats and alerts
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            symptoms TEXT,
            severity TEXT,
            suggested_action TEXT,
            is_sos BOOLEAN,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_message(sender, message):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO messages (sender, message) VALUES (?, ?)', (sender, message))
    conn.commit()
    conn.close()

def save_alert(patient_id, symptoms, severity, suggested_action, is_sos):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO alerts (patient_id, symptoms, severity, suggested_action, is_sos) 
        VALUES (?, ?, ?, ?, ?)
    ''', (patient_id, symptoms, severity, suggested_action, is_sos))
    conn.commit()
    conn.close()
