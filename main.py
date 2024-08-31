import tkinter

window = tkinter.Tk()
window.title("Calculator")
window.geometry("300x300")

button_add = tkinter.Button(window, text = "+")
button_add.place(x = 95, y = 110)

button_sub = tkinter.Button(window, text = "-")
button_sub.place(x = 160, y = 110)

window.mainloop()
