import tkinter as tk
from tkinter import messagebox
from PasswordManager import PasswordManager  # Your integrated password manager class

class PasswordManagerApp:
    def __init__(self, root):
        self.pm = PasswordManager()
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Password Manager")

        tk.Label(self.root, text="Service:").pack(pady=(10, 0))
        self.service_entry = tk.Entry(self.root)
        self.service_entry.pack(pady=(0, 10))

        tk.Label(self.root, text="Password:").pack(pady=(10, 0))
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=(0, 10))

        tk.Button(self.root, text="Add Password", command=self.add_password).pack(pady=(0, 5))
        tk.Button(self.root, text="Get Password", command=self.get_password).pack(pady=(5, 10))

    def add_password(self):
        service = self.service_entry.get()
        password = self.password_entry.get()
        if service and password:  # Check if the fields are not empty
            self.pm.add_password(service, password)
            messagebox.showinfo("Success", "Password added")
            self.service_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Service and password fields cannot be empty")

    def get_password(self):
        service = self.service_entry.get()
        retrieved_password = self.pm.get_password(service)
        if retrieved_password:
            messagebox.showinfo("Password Retrieved", f"Password: {retrieved_password}")
        else:
            messagebox.showerror("Error", "Service not found")