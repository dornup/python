from tkinter import *

win = Tk()
win.geometry("400x400")

# ============== ЗАДАЧА 1 =====================
#
# Label(win, text="Логин:").grid(row=0, column=0)
# Label(win, text="Пароль:").grid(row=1, column=0)
#
# Entry(win).grid(row=0, column=1, pady=5)
# Entry(win).grid(row=1, column=1, pady=5)
#
# Button(win, text="Авторизация").grid(row=2, column=0, columnspan=2, sticky=E)

# ============= ЗАДАЧА 2 =============
# from random import randint
#
# def mooove(a):
#     btn.place(x=randint(0,350), y=randint(0,350))
#
# btn = Button(win, text="подкрадули)", bg="red", fg="blue")
# btn.place(x=10, y=10)
# btn.bind("<Enter>", mooove)


# ============= ЗАДАЧА 3 ==============
from random import randint
def eda():
    rb_val.set(randint(1,5))
    win.after(1000, eda)

fr = Frame()
fr.pack(anchor=NW)
rb_val = IntVar()
rb1 = Radiobutton(fr, variable=rb_val, value=1, fg="red")
rb1.pack(side=LEFT)
rb2 = Radiobutton(fr, variable=rb_val, value=2, fg="orange")
rb2.pack(side=LEFT)
rb3 = Radiobutton(fr, variable=rb_val, value=3, fg="yellow")
rb3.pack(side=LEFT)
rb4 = Radiobutton(fr, variable=rb_val, value=4, fg="green")
rb4.pack(side=LEFT)
rb5 = Radiobutton(fr, variable=rb_val, value=5, fg="lightblue")
rb5.pack(side=LEFT)

eda()

win.mainloop()