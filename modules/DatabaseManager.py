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
                        loginid TEXT NOT NULL,
                        encrypted_password TEXT NOT NULL
            );
            ''')

    # Inserting password
    def insert_password(self, service, loginid, encrypted_password):
        with self.conn:
            cursor = self.conn.execute("INSERT INTO passwords (service, loginid, encrypted_password) VALUES (?, ?, ?)", (service, loginid, encrypted_password))

    # Retrieving password
    def retrieve_password(self, service):
        cursor = self.conn.execute("SELECT encrypted_password FROM passwords WHERE service=?", (service,))
        return cursor.fetchall()
    
    # Retrieving loginid
    def retrieve_loginid(self, service):
        cursor = self.conn.execute("SELECT loginid FROM passwords WHERE service=?", (service,))
        return cursor.fetchall()

    # Retrieving all services
    def retrieve_all_details(self):
        with self.conn:
            cursor = self.conn.execute("SELECT service, loginid, encrypted_password FROM passwords")
            return cursor.fetchall()

# Testing
if __name__ == "__main__":
    db_manager = DatabaseManager()
    db_manager.insert_password("example_service", "example_loginid", "encrypted_example_password")

    print("Password for 'example_service':", db_manager.retrieve_password("example_service"))
    print("Login ID for 'example_service':", db_manager.retrieve_loginid("example_service"))

    print("All services:", db_manager.retrieve_all_details())