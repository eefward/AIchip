import sqlite3

def create_db():
  con = sqlite3.connect("downlaod.db", check_same_thread=False)
  cur = con.cursor()

  cur.execute('''
        CREATE TABLE IF NOT EXISTS downloads (
            id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')