from tkinter import *
from tkinter import messagebox

# def get_list(gfjhf):
#     indx = lstbox.curselection()[0]
#     print(lst[indx])

win = Tk()
win.geometry("500x500")


# lst = ["Первый", "Второй", "Третий"]
# lsttk = StringVar(value=lst)
# lstbox = Listbox(win, listvariable=lsttk, selectmode=SINGLE)
# lstbox.pack()
# lstbox.bind("<<ListboxSelect>>", get_list)
# lstbox["selectbackground"] = "pink"
# lstbox["selectforeground"] = "white"
# lstbox["selectborderwidth"] = 10


# 1 путь
# for el in lst:
#     lstbox.insert(END, el)

# labelframe

# ===== Верхний блок =====
# root = Tk()
# root.geometry("500x500")
# frame_top = LabelFrame(root, text="Верх")
# frame_top.pack()
# Label(frame_top, width=7, height=4, bg='yellow', text="1").pack()
# Label(frame_top, width=7, height=4, bg='orange', text="2").pack()
#
# # ===== Нижний блок =====
# frame_bottom = LabelFrame(root, text="Низ")
# frame_bottom.pack()
# Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3").pack()
# Label(frame_bottom, width=7, height=4, bg='lightblue', text="4").pack()

# message box
#
# messagebox.showerror("Заголовок", "щщщщ не шуми")
# messagebox.showinfo()
# messagebox.showwarning()

# pack
#
# btn = Button(win, text="пельмени пельмени пельмени")
# btn.pack(anchor=SW, expand=True)
# btn.pack(fill=BOTH, expand=True)

# fr = Frame(win)
# fr.pack(anchor=NW)
# btn1 = Button(fr, text="1")
# btn1.pack(side=LEFT)
# btn2 = Button(fr, text="2")
# btn2.pack(side=LEFT)

# greed

# btn1 = Button(win, text="1")
# btn1.grid(row=0, column=0)  #отсчет с 0
# btn2 = Button(win, text="2")
# btn2.grid(row=0, column=1)
# btn3 = Button(win, text="3")
# btn3.grid(row=0, column=2)
# btn4 = Button(win, text="4")
# btn4.grid(row=1, column=0, columnspan=3, sticky=E)

# place
#
# btn1 = Button(win, text="1")
# btn1.place(x=10,y=300)
#

# after
#
# def hello():
#     print("print")
#     win.after(3000, hello)
#
#
# btn1 = Button(win, text="1")
# btn1.pack()
# def color():
#     # sleep(3)
#     btn1["bg"] = "green"
# win.after(3000, hello)

# from time import sleep

# bind

def func(e):
    print("print")

btn = Button(win, text="zuhsks")
btn.pack()
btn.focus_set()
btn.bind("<u>", func)

# set

rb_val = IntVar()
print(rb_val.get())
rb_val.set(5)
print(rb_val.get())


win.mainloop()
