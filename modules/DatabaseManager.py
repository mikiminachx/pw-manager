import sqlite3
import logging

class DatabaseManager:
    def __init__(self, db_path='password.db'):
        self.db_path = db_path
        self.conn = None  # Initialize as None
        try:
            self.conn = self.create_connection()  # Attempt connection
        except sqlite3.Error as e:
            logging.error("Database connection error: %s", e)
            raise  # Raise exception to handle error appropriately
        # Connect to SQLite database with error handling

    def create_connection(self):
        try:
            return sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            logging.error("Database connection error: %s", e)
            raise

    # Create table for storing passwords (unchanged)
    def create_table(self):
        with self.conn:  # Use connection established in __init__
            self.conn.execute('''
            CREATE TABLE IF NOT EXISTS passwords(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        service TEXT NOT NULL,
                        loginid TEXT NOT NULL,
                        encrypted_password TEXT NOT NULL
            );
            ''')

    # Inserting password with error handling and cursor closing
    def insert_password(self, service, loginid, encrypted_password):
        try:
            with self.conn:
                cursor = self.conn.cursor()  # Use cursor
                cursor.execute("INSERT INTO passwords (service, loginid, encrypted_password) VALUES (?, ?, ?)", (service, loginid, encrypted_password))
        except sqlite3.Error as e:
            logging.error("Database insertion error: %s", e)
            raise
        finally:
            if cursor:
                cursor.close()  # Explicitly close cursor

    # Retrieving password with error handling and cursor closing
    def retrieve_password(self, service):
        if not self.conn:  # Check for existing connection
            raise Exception("Database connection not established")

        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT encrypted_password FROM passwords WHERE service=?", (service,))
            result = cursor.fetchone()  # Fetch only one row
            if result:
                return result[0]  # Return encrypted password if found
            else:
                return None  # Return None if not found
        except sqlite3.Error as e:
            logging.error("Database retrieval error: %s", e)
            raise
        finally:
            if cursor:
                cursor.close()  # Ensure cursor is closed
        
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