import pyshorteners
import tkinter as tk
from tkinter import ttk
import pyperclip  # For copying to clipboard

def shorten_url():
    long_url = entry.get()
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    short_url_entry.delete(0, tk.END)  # Clear previous text
    short_url_entry.insert(0, short_url)

def copy_to_clipboard():
    short_url = short_url_entry.get()
    if short_url:
        pyperclip.copy(short_url)

def clear_text_fields():
    entry.delete(0, tk.END)
    short_url_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x200")  # Set initial window size

# Create and configure a title label
title_label = ttk.Label(root, text="URL Shortener by Kartik Gadhave")
title_label.config(font=("Arial", 16))
title_label.pack(pady=10)  # Add some padding

# Create and configure input label and entry
input_label = ttk.Label(root, text="Enter your long URL:")
input_label.pack()
entry = ttk.Entry(root, width=40)
entry.pack()

# Create and configure a button to shorten the URL
shorten_button = ttk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack()

# Create and configure a text entry field to display the result
short_url_entry = ttk.Entry(root, width=40)
short_url_entry.pack(pady=10)  # Add padding

# Create and configure the copy button
copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack()

# Create and configure the clear button
clear_button = ttk.Button(root, text="Clear", command=clear_text_fields)
clear_button.pack()

# Start the tkinter main loop
root.mainloop()
