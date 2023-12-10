import sqlite3

def get_db_connection():
    conn = sqlite3.connect('periodic_table_app/database/periodic_table.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_elements():
    conn = get_db_connection()
    elements = conn.execute('SELECT * FROM elements').fetchall()
    conn.close()
    return elements
