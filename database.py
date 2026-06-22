import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "records.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT NOT NULL,
            attempts INTEGER NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    conn.commit()
    conn.close()


def save_record(nickname, attempts):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO records (nickname, attempts) VALUES (?, ?)",
        (nickname, attempts),
    )
    conn.commit()
    conn.close()


def get_top_records(limit=10):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM records ORDER BY attempts ASC, date ASC LIMIT ?",
        (limit,),
    )
    rows = cur.fetchall()
    conn.close()
    return [list(row) for row in rows]
