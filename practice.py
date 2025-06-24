from ttkbootstrap import Window, Entry, Label, Frame, Button, font, Style
from tkinter import messagebox
from PIL import ImageTk, Image

# Window Setup
window = Window(themename='darkly')
window.iconbitmap(r"C:\Users\HP\Downloads\icons8-google-password-240.ico")
window.title('Password Manager')

# Center the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 500
window_height = 200
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f'{window_width}x{window_height}+{x}+{y}')
window.resizable(False, False)

my_font = font.Font(family='Helvetica', size=12)
style = Style()
style.configure('Custom.TButton', font=my_font)

# Frame for form
center_frame = Frame(window)
center_frame.place(relx=0.5, rely=0.4, anchor='center')

# Username
Label(center_frame, text='Username:', font=('Helvetica', 12)).grid(row=0, column=0, padx=10, pady=10, sticky='e')
username = Entry(center_frame, width=30)
username.grid(row=0, column=1, padx=10, pady=10)

# Password
Label(center_frame, text='Password:', font=('Helvetica', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
password = Entry(center_frame, width=30)
password.grid(row=1, column=1, padx=10, pady=10)

# Login Button (centered)
login_button = Button(center_frame, text='Login', style='Custom.TButton')
login_button.grid(row=2, column=0, columnspan=2, pady=10)  # ✅ centered

window.mainloop()
