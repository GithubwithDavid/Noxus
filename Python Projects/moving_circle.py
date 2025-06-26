from ttkbootstrap import Window, Canvas, BOTH
window = Window(themename='darkly')
window.title('Circle')
window.state('zoomed')

canvas = Canvas(window)
canvas.pack(fill=BOTH, expand=True)

circle_id = canvas.create_oval(100, 100, 150, 150, fill='red')

def move_circle(event, x, y):
    canvas.move(circle_id, x, y)

# Use lambda with event passed
window.bind("<Right>", lambda event: move_circle(event, 10, 0))
window.bind("<Left>", lambda event: move_circle(event, -10, 0))
window.bind("<Up>", lambda event: move_circle(event, 0, -10))
window.bind("<Down>", lambda event: move_circle(event, 0, 10))

window.mainloop()
