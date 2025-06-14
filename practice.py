from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import messagebox

window = Window(themename='darkly')
window.title('Calculator')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (500 / 2))
y = int((screen_height / 2) - (500 / 2) - 40)
window.geometry(f'500x500+{x}+{y}')
window.resizable(False, False)
window.config(bg='#1e1e1e')

def on_enter(event):
    user_input = c_entry.get()
    try:
        result = eval(user_input)
        messagebox.showinfo("Result", f"Result: {result}")
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression")

def pressed(c):
    c_entry.insert(END, c)

# ✅ Use only supported options for ttk.Entry
c_entry = Entry(window, font=('Helvetica', 20), justify='right')
c_entry.pack(fill='x', ipady=20)
c_entry.bind('<Return>', on_enter)

# ✅ Styled buttons using ttkbootstrap
plus = Button(window, text='+', command=lambda: pressed('+'), bootstyle='info-outline')
plus.pack(side='left', anchor='n', ipadx=10, ipady=5)

minus = Button(window, text='-', command=lambda: pressed('-'), bootstyle='success-outline')
minus.pack(anchor='n', side='left', ipadx=15, ipady=5)

window.mainloop()
