import tkinter as tk
from tkinter import messagebox, ttk
from src.PasswordManager import PasswordManager

class PasswordManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        # PasswordManager instance
        self.pm = PasswordManager()

        # Layout
        self.setup_layout()

    def setup_layout(self):
        instructions = "To add password fill all the fields and press 'Add Password'.\nTo view password, enter Account Name and press 'Get Password'."
        signature = "Developed by Meko Lau"

        # Centre Frame
        centre_frame = tk.Frame(self.master, bg="#d3d3d3")
        centre_frame.pack(padx=10, pady=10)

        # Instructions Label
        instruction_label = tk.Label(centre_frame, text=instructions, bg="#d3d3d3")
        instruction_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        # Service Entry
        tk.Label(centre_frame, text="Account:", bg="#d3d3d3").grid(row=1, column=0, padx=10, pady=5)
        self.service_entry = tk.Entry(centre_frame)
        self.service_entry.grid(row=1, column=1, padx=10, pady=5)

        # LoginID Entry
        tk.Label(centre_frame, text="Username:", bg="#d3d3d3").grid(row=2, column=0, padx=10, pady=5)
        self.loginid_entry = tk.Entry(centre_frame)
        self.loginid_entry.grid(row=2, column=1, padx=10, pady=5)

        # Password Entry
        tk.Label(centre_frame, text="Password:", bg="#d3d3d3").grid(row=3, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(centre_frame, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        # Add and Get Password Buttons
        tk.Button(centre_frame, text="Add Password", command=self.add_password).grid(row=4, column=0, padx=10, pady=5)
        tk.Button(centre_frame, text="Get Password", command=self.get_password).grid(row=4, column=1, padx=10, pady=5)

        # Show All Passwords Button
        tk.Button(centre_frame, text="Show Passwords", command=self.show_password_table).grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        # Signature Label
        tk.Label(centre_frame, text=signature, bg="#d3d3d3").grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def add_password(self):
        service = self.service_entry.get()
        loginid = self.loginid_entry.get()
        password = self.password_entry.get()
        if service and loginid and password:
            self.pm.add_password(service, loginid, password)
            messagebox.showinfo("Success", "Password added")
        else:
            messagebox.showwarning("Warning", "Please enter service, loginID and password")
    def get_password(self):
        service = self.service_entry.get()
        if service:
            password = self.pm.get_password(service)
            loginid = self.pm.get_loginid(service)
            if password and loginid:
                self.show_password_table(service, loginid, password)
            else:
                messagebox.showerror("Not Found", "Password and LoginID for the specified service not found")
        else:
            messagebox.showwarning("Warning", "Please enter a service to retrieve")

    def populate_password_table(self, table):
        for service in self.pm.get_all_service():
            print(f"Service: {service}")  # For debugging
            password = self.pm.get_password(service)
            loginid = self.pm.get_loginid(service)
            print(f"Login ID: {loginid}, Password: {password}")  # For debugging
            table.insert("", tk.END, values=(service, loginid, password))

    def show_password_table(self, service, loginid, password):
        table_window = tk.Toplevel(self.master)
        table_window.title(f"Password Details for {service}")

        # Setting up the Treeview widget
        columns = ("Service", "LoginID", "Password")
        password_table = ttk.Treeview(table_window, columns=columns, show='headings')
        password_table.heading("Service", text="Service")
        password_table.heading("LoginID", text="LoginID")
        password_table.heading("Password", text="Password")
        password_table.column("Service", width=150)
        password_table.column("LoginID", width=150)
        password_table.column("Password", width=150)

        # Insert the specific service's details
        password_table.insert("", tk.END, values=(service, loginid, password))
        
        password_table.pack(fill=tk.BOTH, expand=True)