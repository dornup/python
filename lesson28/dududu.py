import tkinter as tk
#
# def gaga(a):
#     message = ent.get()
#     ent.delete(0, "end")
#     print(message)
#
#     message2 = txt.get(1.0, "end")
#     txt.delete(0.0, "end")
#     print(message2)
#
# window = tk.Tk()
# window.geometry("500x500")
# window.title("dududu")
#
# lab1 = tk.Label(window, text="Ваш адрес:", font="Verdana 10 bold", bg="yellow", fg="green")
# lab1.pack()
#
# ent = tk.Entry(window, bd=5, width=20, bg="yellow")
# ent.pack()
#
# lab2 = tk.Label(window, text="Комметарий:", font="Verdana 10 bold", fg="green")
# lab2.pack()
#
# txt = tk.Text(window, width=25, height=10)
# txt.pack()
#
# btn = tk.Button(window, text="Отправить", width=20, height=2, bg="lightblue", fg="green")
# btn.pack()
# btn.bind("<Button-1>", gaga)
#
# window.configure(background='wheat')
#
# window.mainloop()

window = tk.Tk()
window.geometry("500x500")
window.title("rainbow")

red = tk.Button(window, width=20, height=2, bg="red")
red.pack()

orange = tk.Button(window, width=20, height=2, bg="orange")
orange.pack()

yellow = tk.Button(window, width=20, height=2, bg="yellow")
yellow.pack()

green = tk.Button(window, width=20, height=2, bg="green")
green.pack()

lightblue = tk.Button(window, width=20, height=2, bg="lightblue")
lightblue.pack()

blue = tk.Button(window, width=20, height=2, bg="blue")
blue.pack()

purple = tk.Button(window, width=20, height=2, bg="purple")
purple.pack()

window.mainloop()