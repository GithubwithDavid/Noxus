from ttkbootstrap import Window, Radiobutton, IntVar
from tkinter import messagebox
from PIL import ImageTk, Image

# Window Sizing and Setting
window = Window(themename='darkly')
window.iconbitmap(r"C:\Users\HP\Downloads\icons8-google-password-240.ico")
window.title('Password Manager')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 500
window_height = 300
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f'{window_width}x{window_height}+{x}+{y}')
window.resizable(False, False)

# Building
r = IntVar()
Radiobutton(window, text='Option 1', variable=r, value=1).pack()
Radiobutton(window, text='Option 2', variable=r, value=2).pack()
window.mainloop()
