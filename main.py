import tkinter as tk
from .src.gui import PasswordManagerApp  # Import your GUI class
# from password_manager import PasswordManager  # If needed
# from database_manager import DatabaseManager  # If needed
# from encryption_manager import EncryptionManager  # If needed

def main():
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
