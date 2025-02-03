import sqlite3

DB_PATH = "/data/data.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS booking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_id TEXT UNIQUE,
            hotel TEXT,
            check_in TEXT,
            check_out TEXT,
            adults INTEGER,
            children INTEGER
        )
    """)

    conn.commit()
    conn.close()
    print("Database initialized and table created (if it didn't exist).")