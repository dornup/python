import tkinter as tk

root = tk.Tk()  # Создали окно

root.geometry("400x400")


# CHECKBUTTON
#
# def check():
#     print(val_cb.get())
#
#
# val_cb = tk.BooleanVar()  # Переменная для хранения значения True/False
# cb = tk.Checkbutton(root,
#                     text="Subscribe?",
#                     font=15,
#                     bg="red",
#                     variable=val_cb,  # Хранение значения в переменной
#                     onvalue=True,
#                     offvalue=False,
#                     command=check,
#                     )  # Создали переключатель
# cb.pack()

# RADIOBUTTON

# def rodion():
#     print(val_rb.get())
#
#
# val_rb = tk.IntVar()
#
# rb1 = tk.Radiobutton(root,
#                      text="Радио дача)",
#                      variable=val_rb,
#                      value=123,
#                      command=rodion)
# rb1.pack()
# rb2 = tk.Radiobutton(root,
#                      text="Радио BusinessFM)",
#                      variable=val_rb,
#                      value=696,
#                      command=rodion)
# rb2.pack()

# SKALE
#
# def get_skala(eeeooo):
#     print(skala.get())
#     print(eeeooo)
#
# skala = tk.Scale(root,
#                  from_=500,
#                  to=1000,
#                  width = 50,
#                  length=600,
#                  orient=tk.HORIZONTAL,
#                  tickinterval=100,
#                  resolution=10,
#                  command=get_skala)
# skala.pack()

#  IMAGES

# img = tk.PhotoImage(file="ruka.png")  # Создали обжект изображения
# img = img.subsample(3, 3)  # Уменьшили
# img = img.zoom(2, 2) # Увеличили
# lab = tk.Label(root,
#                image=img,)
#
# lab.pack()

#  СОСТОЯНИЯ

# def switch():
#     if btn1["state"] == "disabled":  # Если кнопка неактивна
#         btn1["state"] = "normal"
#     else:
#         btn1["state"] = "disabled"
#
# btn1 = tk.Button(root,
#                  text="Включи меняяя",
#                  state=tk.DISABLED,
#                  fg="red",
#                  disabledforeground="blue",
#                  width=20)
# btn1.pack(pady=30, ipady=20)
# btn2 = tk.Button(root,
#                  text="активатар",
#                  command=switch,
#                  width=20)
# btn2.pack()

#  ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ В ENTRY

ent = tk.Entry(root,
               )
ent.pack()
ent.insert(tk.END, "я люблю людей")

root.mainloop()  # Запустили окно