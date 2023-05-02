import tkinter as tk
root = tk.Tk()
root.geometry("500x500")
const = (("Сложение", "+"),
         ("Вычитание", "-"),
         ("Умножение", "*"),
         ("Степень", "**"),
         ("Деление", "/"),
         ("Деление(целая часть)", "//"),
         ("Деление(остаток)", "%"))

lambda1 = lambda x,y: x+y if x != "" and y != "" else ""
lambda2 = lambda x,y: x-y if x != "" and y != "" else ""
lambda3 = lambda x,y: x*y if x != "" and y != "" else ""
lambda4 = lambda x,y: pow(x, y) if x != "" and y != "" else ""
lambda5 = lambda x,y: x/y if x != "" and y != "" and y != "0" else ""
lambda6 = lambda x,y: x//y if x != "" and y != "" and y != "0" else ""
lambda7 = lambda x,y: x%y if x != "" and y != "" and y != "0" else ""

for i in range(7):
    exec(f"lf{i+1} = tk.LabelFrame(root, text=const[i][0])")
    exec(f"lf{i+1}.pack()")
    exec(f"en{i+1} = tk.Entry(lf{i+1})")
    exec(f"en{i+1}.pack(side='left')")
    exec(f"tk.Label(lf{i+1}, text=const[i][1]).pack(side='left')")
    exec(f"enn{i + 1} = tk.Entry(lf{i + 1})")
    exec(f"enn{i + 1}.pack(side='left')")
    exec(f"btn{i+1} = tk.Button(lf{i+1}, text='=')")
    exec(f"btn{i+1}.pack(side='left')")
    exec(f"ans{i+1} = tk.Entry(lf{i+1})")
    exec(f"ans{i+1}.pack(side='left')")

root.mainloop()
