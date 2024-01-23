import tkinter as tk
from tkinter import messagebox
from app.app import PasswordManagerApp

class start_application:
    def main():
        root = tk.Tk()
        app = PasswordManagerApp(root)
        root.mainloop()
