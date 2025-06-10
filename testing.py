import tkinter as tk

window = tk.Tk()
window.title("Password Manager")
window.configure(bg='#819A91')

window_width = 800
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2) + 10) 
y = int((screen_height / 2) - (window_height / 2) - 40)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.resizable(False, False)

window.mainloop()
