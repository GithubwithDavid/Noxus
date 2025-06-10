import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Password Manager')
window.geometry('300x200')

def show_text():
    username = entry.get()
    messagebox.showinfo('Hi', username)

def clear_text():
    entry.delete(0, tk.END)

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

show_button = tk.Button(window, text='Show Text', command=show_text)
show_button.pack(pady=5)
clear_button = tk.Button(window, text='Clear Text', command=clear_text)
clear_button.pack(pady=5)
window.mainloop()