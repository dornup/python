from  tkinter import *
root = Tk()
root.geometry("550x550")
#===========CANVAS===========

c = Canvas(root, width=500, height=500, bg="lightblue")
c.pack(anchor=CENTER, expand=True)

#===========ТЕКСТ============
# c.create_text(0, 0,
#               text="пельмени пельмени пельмени",
#               font="Arial 15",
#               anchor=NW,
#               fill="green")

#===========ПРЯМОУГОЛЬНИК====
# c.create_rectangle(10,10,
#                    200,150,
#                    fill="red",
#                    width=10,
#                    outline="magenta")

#===========МНОГОУГОЛЬНИК====
# c.create_polygon(10, 10,
#                  50,50,
#                  10, 50,)

#===========ОКРУЖНОСТЬ=======
# c.create_oval(10, 10,
#               50,50,)

#===========ARC==============
# c.create_oval(10, 10,
#               50, 50,
#               fill="silver")
# c.create_arc(10, 10,
#              50, 50,
#              fill="brown",
#              extent=-120,
#              start=45,)
# c.create_arc(10, 10,
#              50, 50,
#              fill="blue",
#              extent=135,
#              start=90,
#              style=CHORD)
# c.create_arc(10, 10,
#              50, 50,
#              outline="magenta",
#              extent=120,
#              start=110,
#              style=ARC,
#              width=10)

#===========ЛИНИИ=============
# c.create_line(10, 10,
#               150, 150,
#               arrow=BOTH,
#               arrowshape=(50, 50, 50),
#               width=20)

#=============================
c.create_rectangle(10,10,
                   200,150,
                   fill="red",
                   width=5,
                   outline="magenta",
                   dash="-",
                   activefill="blue",
                   activewidth=10)

root.mainloop()