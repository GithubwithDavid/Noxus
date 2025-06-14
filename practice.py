from ttkbootstrap import *
from tkinter import messagebox
from ttkbootstrap.constants import *
from PIL import ImageTk, Image

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
icon = ImageTk.PhotoImage(Image.open(r'C:\Users\HP\Downloads\icons8-google-password-240.png'))
Label(image=icon).pack()
Quit_Button = Button(window, text='Exit Program', command=window.quit, bootstyle='success-outline')
Quit_Button.pack()
window.mainloop()
