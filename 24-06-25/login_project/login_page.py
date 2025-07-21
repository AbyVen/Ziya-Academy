import tkinter as tk
from tkinter import messagebox

# Dummy username and password
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

# Function to validate login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        show_success_page()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to show success page
def show_success_page():
    login_window.destroy()  # close login window

    success_window = tk.Tk()
    success_window.title("Welcome")
    success_window.geometry("500x300")
    success_window.configure(bg="#D1D5DB")

    success_label = tk.Label(success_window, text="✅ Login Successful!",
                              font=("Helvetica", 20, "bold"), bg="#D1D5DB", fg="#1F2937")
    success_label.pack(pady=100)

    success_window.mainloop()

# Create login window
login_window = tk.Tk()
login_window.title("Login Page")
login_window.geometry("400x250")
login_window.configure(bg="#F3F4F6")

# Username
tk.Label(login_window, text="Username", bg="#F3F4F6", font=("Arial", 12)).pack(pady=(20, 5))
entry_username = tk.Entry(login_window, width=30)
entry_username.pack()

# Password
tk.Label(login_window, text="Password", bg="#F3F4F6", font=("Arial", 12)).pack(pady=(10, 5))
entry_password = tk.Entry(login_window, width=30, show="*")
entry_password.pack()

# Login Button
login_button = tk.Button(login_window, text="Login", width=10, command=login)
login_button.pack(pady=20)

# Run the app
login_window.mainloop()
