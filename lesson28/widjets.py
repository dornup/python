import tkinter as tk


def batone(text):
    # прием значения из entry:

    message = ent.get()
    print(message)  # получить значение из окна ввода
    ent.delete(0, "end")
    lab["text"] = message
    print(message)

    # прием значения из text:

    message2 = txt.get(1.0, "end") # отсчет от 1.0
    txt.delete(1.0, "end")
    print(message2)


window = tk.Tk()
window.geometry("300x400")
window.title("Не бублики")

lab = tk.Label(window, text="Бублики", font="Verdana 18 bold", bg="orange", fg="purple")  # Надпись
lab.pack()

ent = tk.Entry(window, bd=7, width=10)
ent.pack()

btn = tk.Button(window, text="Отправить", font="Verdana 18 bold", bg="orange", fg="purple")
btn.pack()
btn.bind("<Button-1>", batone)

txt = tk.Text(window, width=20, height=5)  # многострочный ввод
txt.pack()

window.mainloop()
