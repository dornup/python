import tkinter as tk

root = tk.Tk()

# первый задач

# def cho_hochesh():
#     if btn["state"] == "disabled":
#         btn["state"] = "normal"
#         btn["text"] = "Активен"
#     else:
#         btn["state"] = "disabled"
#         btn["text"] = "Не активен"
#
# cb = tk.Checkbutton(root,
#                     text="Активировать",
#                     command=cho_hochesh)
# cb.pack()
# cb.select()
#
# btn = tk.Button(root,
#                 text="Не активен")
# btn.pack()

# второй задач

def bold():
    if var_cb1.get():
        lb["font"] += " bold"
    else:
        lb["font"] = lb["font"].replace(" bold", " ")

def italic():
    if var_cb2.get():
        lb["font"] += " italic"
    else:
        lb["font"] = lb["font"].replace(" italic", " ")
def overstrike():
    if var_cb3.get():
        lb["font"] += " overstrike"
    else:
        lb["font"] = lb["font"].replace(" overstrike", " ")
def underline():
    if var_cb4.get():
        lb["font"] += " underline"
    else:
        lb["font"] = lb["font"].replace(" underline", " ")

var_cb1 = tk.BooleanVar()
var_cb2 = tk.BooleanVar()
var_cb3 = tk.BooleanVar()
var_cb4 = tk.BooleanVar()

lb = tk.Label(root,
              text="Я текст, а чего добился ты?!",
              font="Arial 15")
lb.pack()
cb1 = tk.Checkbutton(root,
                    text="жирный",
                    variable=var_cb1,
                    onvalue=True,
                    offvalue=False,
                    command=bold)
cb1.pack()
cb2 = tk.Checkbutton(root,
                    text="курсив",
                    variable=var_cb2,
                    onvalue=True,
                    offvalue=False,
                    command=italic)
cb2.pack()
cb3 = tk.Checkbutton(root,
                    text="зачеркнутый",
                    variable=var_cb3,
                    onvalue=True,
                    offvalue=False,
                    command=overstrike)
cb3.pack()
cb4 = tk.Checkbutton(root,
                    text="подчеркнутый",
                    variable=var_cb4,
                    onvalue=True,
                    offvalue=False,
                    command=underline)
cb4.pack()



root.mainloop()