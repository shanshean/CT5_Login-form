import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Form")
root.geometry("400x350")
root.configure(bg = "#BCCCC1")

title_label = tk.Label(
    root,
    text = "USER LOGIN",
    font = ("Courier", 20, "bold"),
    bg = "#1E5631",
    fg = "#F8C42E"
)
title_label.pack(pady = 5)

username_label = tk.Label(
    root,
    text = "Username",
    font = ("Courier", 11),
    bg = "#D4AF37",
    fg = "#304F27"
)
username_label.pack(pady = 5)

username_entry = tk.Entry(
    root,
    font = ("Courier", 12),
    width = 25,
    bg = "#FCF8EC",
    fg = "#D99201"
)
username_entry.pack(pady = 5)

password_label = tk.Label(
    root,
    text = "Password",
    font = ("Courier", 12),
    bg = "#D4AF37",
    fg = "#304F27"
)
password_label.pack(pady = 5)

password_entry = tk.Entry(
    root,
    font = ("Courier", 12),
    width = 25,
    bg = "#FCF8EC",
    fg = "#D99201",
    show = "*"
)
password_entry.pack(pady = 5)
    
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "12345":
        messagebox.showinfo(
            "LOGIN SUCCESSFULLY!",
            "Welcome Admin!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid Username and Password!"
        )

login_button = tk.Button(
    root,
    text = "LOG IN",
    font = ("Courier", 12, "bold"),
    bg = "#2A7F5E",
    fg = "#FDCA89",
    width = 20,
    command = login
)
login_button.pack(pady = 20)

root.mainloop()