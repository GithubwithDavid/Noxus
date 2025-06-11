from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Calculator')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (500 / 2))
y = int((screen_height / 2) - (500 / 2) - 40)
window.geometry(f'500x500+{x}+{y}')
window.resizable(False, False)
window.config(bg='#1e1e1e')

def on_enter(event):  # must accept 'event'
    user_input = c_entry.get()
    try:
        result = eval(user_input)
        messagebox.showinfo("Result", f"Result: {result}")
    except Exception as e:
        messagebox.showerror("Error: Invalid expression")

c_entry = Entry(window, font=('Helvetica', 20), bg='#2e2e2e', fg='white', bd=0, justify='right')
c_entry.pack(fill='x', ipady=20)
c_entry.bind('<Return>', on_enter)
window.mainloop()
