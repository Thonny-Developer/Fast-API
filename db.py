import sqlite3
import random
import string

def database():
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS keys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        key TEXT NOT NULL
    )
    ''')

    return conn, cursor

def generate_key():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=16))
def NewKey(Email):
    conn, cursor = database()
    
    try:
        Key = generate_key()

        cursor.execute("INSERT INTO keys (email, key) VALUES (?, ?)", (Email, Key))
        conn.commit()
        cursor.close()
        return True, Email, Key
    
    except Exception as Error:
        print("Error NewKey:", Error)
        cursor.close()
        return False, Email, None
    
def GetKey(Key):
    conn, cursor = database()

    cursor.execute("SELECT id, email FROM keys WHERE key = ?", (Key,))
    answer = cursor.fetchall()

    cursor.close()

    if answer:
        return True, answer
    else:
        return False, None
