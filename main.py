import tkinter as tk
from tkinter import messagebox
from src.PasswordManager import PasswordManager  # Adjust this import as per your project structure

class PasswordManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        # PasswordManager instance
        self.pm = PasswordManager()

        # Layout
        self.setup_layout()

    def setup_layout(self):
        # Service label and entry
        tk.Label(self.master, text="Service:").pack()
        self.service_entry = tk.Entry(self.master)
        self.service_entry.pack()

        # Password label and entry
        tk.Label(self.master, text="Password:").pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        # Add password button
        tk.Button(self.master, text="Add Password", command=self.add_password).pack()

        # Get password button
        tk.Button(self.master, text="Get Password", command=self.get_password).pack()

    def add_password(self):
        service = self.service_entry.get()
        password = self.password_entry.get()
        if service and password:
            self.pm.add_password(service, password)
            messagebox.showinfo("Success", "Password added")
        else:
            messagebox.showwarning("Warning", "Please enter both service and password")

    def get_password(self):
        service = self.service_entry.get()
        if service:
            password = self.pm.get_password(service)
            if password:
                messagebox.showinfo("Password", f"Password for {service} is {password}")
            else:
                messagebox.showerror("Not Found", "Password for the specified service not found")
        else:
            messagebox.showwarning("Warning", "Please enter a service to retrieve")

def main():
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
