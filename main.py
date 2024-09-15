import tkinter

window = tkinter.Tk()
window.configure(bg="silver")
window.title("Calculator")
window.geometry("300x300")

def add():
    num1 = text_num1.get()
    num2 = text_num2.get()
    result = int(num1) + int(num2)
    text_answer.delete(0, "end")
    text_answer.insert(0, str(result))

def sub():
    num1 = text_num1.get()
    num2 = text_num2.get()
    result = int(num1) - int(num2)
    text_answer.delete(0, "end")
    text_answer.insert(0, str(result))


def mul():
    num1 = text_num1.get()
    num2 = text_num2.get()
    result = int(num1) * int(num2)
    text_answer.delete(0, "end")
    text_answer.insert(0, str(result))

def div():
    num1 = text_num1.get()
    num2 = text_num2.get()
    result = int(num1) / int(num2)
    text_answer.delete(0, "end")
    text_answer.insert(0, str(result))

def clear():
        num1 = text_num1.get()
        num2 = text_num2.get()
        text_answer.delete(0, "end")
        text_num1.delete(0, "end")
        text_num2.delete(0, "end")


def off():
   window.destroy()


button_add = tkinter.Button(window, text = "+", command=add, width = 7, height=2, bg="black", fg="orange")
button_add.place(x = 95, y = 110)

button_sub = tkinter.Button(window, text = "-", command=sub, width=7, height=2, bg="black", fg="orange")
button_sub.place(x = 160, y = 110)

button_mul = tkinter.Button(window, text = "*", command=mul, width=7, height=2, bg="black", fg="orange")
button_mul.place(x = 95, y = 154)
text_num1 = tkinter.Entry(window, bg="black", fg="white")
text_num1.place(x = 95, y = 40)

button_div = tkinter.Button(window, text = "/", command=div, width=7, height=2, bg="black", fg="orange")
button_div.place(x = 160, y = 154)

button_clear = tkinter.Button(window, text = "C", command=clear, width=5, height=2, bg="black", fg="orange")
button_clear.place(x = 230, y = 110)

button_off = tkinter.Button(window, text = "OFF", command=off, width=5, height=2, bg="black", fg="orange")
button_off.place(x = 230, y = 156)

text_num2 = tkinter.Entry(window, bg="black", fg="white")
text_num2.place(x = 95, y = 81)

text_answer = tkinter.Entry(window, width = 20, bg="black", fg="gold")
text_answer.place(x = 95, y = 221)

label_num1 = tkinter.Label(window, text = "Введите первое число:  ", bg="silver")
label_num1.place(x = 95, y = 20)

label_num2 = tkinter.Label(window, text = "Введите второе число: ", bg="silver")
label_num2.place(x = 95, y = 61)

label_answer = tkinter.Label(window, text = "Ответ: ", bg="silver")
label_answer.place(x = 95, y = 200)

window.mainloop()
