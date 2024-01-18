import sqlite3

class DatabaseManager:
    def __init__(self, db_path='password.db'):
        self.db_path = db_path
        self.conn = self.create_connection()
        self.create_table()

    # Connect to SQLite database
    def create_connection(self):
        return sqlite3.connect(self.db_path)

    # Create table for storing passwords
    def create_table(self):
        with self.conn:
            self.conn.execute('''
            CREATE TABLE IF NOT EXISTS passwords(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        service TEXT NOT NULL,
                        encrypted_password TEXT NOT NULL
            );
            ''')

    # Inserting password
    def insert_password(self, service, encrypted_password):
        with self.conn:
            cursor = self.conn.execute("INSERT INTO passwords (service, encrypted_password) VALUES (?, ?)", (service, encrypted_password))

    # Retrieving password
    def retrieve_password(self, service):
        cursor = self.conn.execute("SELECT encrypted_password FROM passwords WHERE service=?", (service,))
        row = cursor.fetchone()
        return row[0] if row else None

# Testing
if __name__ == "__main__":
    db_manager = DatabaseManager()
    db_manager.insert_password("example_password", "encrypted_example_password")
    print(db_manager.retrieve_password("example_service"))


