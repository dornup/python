import tkinter as tk


def baget(event):
    print("Я хочу на море")


window = tk.Tk()  # инициализация, создание окна В НАЧАЛЕ

window.geometry("500x400")  # размер окна
window.title("у моего окна черемуха цветет")  # заголовок

btn = tk.Button(window)  # создание кнопки
btn.pack()  # размещение кнопки
btn["text"] = "ы"  # изменение конфигурации
btn["font"] = ("Arial Black",  # шрифт
               15,  # размер
               "bold",  # жирный
               "underline",  # подчеркнутый
               "italic",  # курсив
               "overstrike"  # зачеркнутый
               )

btn["bg"] = "red"  # цвет фона (background)
btn["fg"] = "blue"  # цвет текста (foreground)
btn["width"] = 5  # ширина
btn["height"] = 3  # высота
btn["bd"] = 10  # ширина рамки (borderground)
# btn["command"] = baget  # нажатие левой кнопкой мыши по кнопке
btn.bind("<Double-Button-1>", baget)

window.mainloop()  # закрытие окна В КОНЦЕ
