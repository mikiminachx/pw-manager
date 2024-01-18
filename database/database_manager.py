import sqlite3

# Connect to SQLite database
def connect_db():
    conn = sqlite3.connect('password.db')
    return conn

# Create table for storing passwords
def create_table(conn):
    conn.execute('''
    CREATE TABLE IF NOT EXISTS passwords(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                encrypted_password TEXT NOT NULL
    );
    ''')

    conn.commit()

# Inserting password
def insert_password(conn, service, encrypted_password):
    conn.execute(conn.execute("INSERT INTO passwords (service, encrypted_password) VALUES (?, ?)", (service, encrypted_password)))
    conn.commit()

# Retrieving password
def retrieve_password(conn, service):
    cursor = conn.execute("SELECT encrypted_password FROM password WHERE service=?", (service,))
    return cursor.fetchone()

# Testing
if __name__ == "__main__":
    conn = connect_db()
    create_table(conn)
    conn.close()


