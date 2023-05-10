import tkinter as tk
from tkinter import font
import pyperclip
import re

def shorten_url():
    original_url = url_entry.get().strip()

    # Validate the URL using a regular expression
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https:// or ftp:// or ftps://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if not re.match(url_regex, original_url):
        error_label.config(text="Please enter a valid URL", fg="red")
        return

    # Shorten the URL using a custom algorithm
    base_url = "https://tiny.com/"
    shortened_url = base_url + str(hash(original_url))[1:7]

    # Display the shortened URL and copy it to the clipboard
    result_label.config(text=shortened_url, fg="green")
    pyperclip.copy(shortened_url)

# Create the main window
root = tk.Tk()
root.geometry("400x200")
root.title("URL Shortener")

# Create the UI elements
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=(10, 5))

url_entry = tk.Entry(root, width=30, font=font.Font(size=14))
url_entry.pack(pady=5)

shorten_button = tk.Button(root, text="Shorten", command=shorten_url, font=font.Font(size=14))
shorten_button.pack(pady=10)

result_label = tk.Label(root, text="", font=font.Font(size=14))
result_label.pack()

error_label = tk.Label(root, text="", font=font.Font(size=14))
error_label.pack(pady=(5, 0))

# Start the main event loop
root.mainloop()
