import tkinter as tk
from .src.gui import PasswordManagerApp

def main():
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
