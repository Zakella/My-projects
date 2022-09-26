import sqlite3

conn = sqlite3.connect('orders.db')


def create_table():
    conn.execute("""CREATE TABLE IF NOT EXISTS users(
       userid INT PRIMARY KEY,
       first_name TEXT,
       last_name TEXT,
       birth_day DATA,
       tel TEXT);
    """)
    conn.commit()
