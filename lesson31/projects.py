from tkinter import *
root = Tk()
root.geometry("500x500")
c = Canvas(root, width=300, height=300, bg="pink")
c.pack(anchor=CENTER, expand=True)
# -------- ЗАДАЧА 1 ---------
# def schetchik():
#     global timer
#     timer += 1
#     c.delete(ALL)
#     c.create_text(150, 150, text=timer)
#     c.create_image(150, 150, image=img)
#     root.after(1000, schetchik)
#     if timer == 16:
#         root.destroy()
#
# img = PhotoImage(file="tumer.png").subsample(2, 2)
# c.create_image(150, 150, image=img)
# timer = 0
# c.create_text(150, 150, text=timer)
# schetchik()

# -------- ЗАДАЧА 2 -----------
c.create_text(10, 10, anchor=NW, text="Школа", font="Arial 20")
c.create_line(150, 25, 250, 25, arrow=LAST)
c.create_text(300, 10, anchor=NW, text="Туда-сюда", font="Arial 20")
c.create_line(500, 25, 600, 25, arrow=LAST)
c.create_text(650, 10, anchor=NW, text="Успешный успех", font="Arial 20")

root.mainloop()