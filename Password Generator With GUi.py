import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0!")
            return
        
        chars = ""
        if uppercase_var.get():
            chars += string.ascii_uppercase
        if lowercase_var.get():
            chars += string.ascii_lowercase
        if digits_var.get():
            chars += string.digits
        if symbols_var.get():
            chars += string.punctuation
        
        if not chars:
            messagebox.showerror("Error", "Select at least one character type!")
            return
        
        password = ''.join(random.choice(chars) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Invalid password length!")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied!", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Password Length
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Character Types Checkboxes
tk.Label(root, text="Include:").pack(pady=5)

uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Uppercase (A-Z)", variable=uppercase_var).pack(anchor="w", padx=50)

lowercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Lowercase (a-z)", variable=lowercase_var).pack(anchor="w", padx=50)

digits_var = tk.BooleanVar()
tk.Checkbutton(root, text="Digits (0-9)", variable=digits_var).pack(anchor="w", padx=50)

symbols_var = tk.BooleanVar()
tk.Checkbutton(root, text="Symbols (!@#...)", variable=symbols_var).pack(anchor="w", padx=50)

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

# Generated Password
tk.Label(root, text="Generated Password:").pack(pady=5)
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

# Copy Button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=10)

root.mainloop()