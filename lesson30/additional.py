import tkinter as tk
root = tk.Tk()
root.geometry("500x500")
const = (("Сложение", "+"),("Вычитание", "-"),("Умножение", "*"),("Степень", "**"),("Деление", "/"),("Деление(целая часть)", "//"),("Деление(остаток)", "%"))
lambda1 = lambda x,y: int(x)+int(y) if type(x) != "<class 'method'>" and type(y) != "<class 'method'>" else " "
lambda2 = lambda x,y: int(x)-int(y) if x != "" and y != "" else ""
lambda3 = lambda x,y: int(x)*int(y) if x != "" and y != "" else ""
lambda4 = lambda x,y: pow(int(x), int(y)) if x != "" and y != "" else ""
lambda5 = lambda x,y: int(x)/int(y) if x != "" and y != "" and y != "0" else ""
lambda6 = lambda x,y: int(x)//int(y) if x != "" and y != "" and y != "0" else ""
lambda7 = lambda x,y: int(x)%int(y) if x != "" and y != "" and y != "0" else ""
def chek(a):
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
    for element in lst:
        if element in a:
            return False
        else:
            return True
for i in range(7):
    exec(f"fanc = lambda a, b: ' ' if chek(str(a)) == False or chek(str(b)) == False else lambda{i+1}(str(a),str(b)) ")
    exec(f"def func(x): "
         f"     ans{i+1}.insert(0, fanc(a, b))")
    exec(f"lf{i+1} = tk.LabelFrame(root, text=const[i][0])")
    exec(f"lf{i+1}.pack()")
    exec(f"en{i+1} = tk.Entry(lf{i+1})")
    exec(f"a = en{i+1}.get")
    exec(f"en{i+1}.pack(side='left')")
    exec(f"tk.Label(lf{i+1}, text=const[i][1]).pack(side='left')")
    exec(f"enn{i+1} = tk.Entry(lf{i+1})")
    exec(f"b = enn{i+1}.get")
    exec("print(b)")
    exec(f"enn{i+1}.pack(side='left')")
    exec(f"btn{i+1} = tk.Button(lf{i+1}, text='=')")
    exec(f"btn{i+1}.pack(side='left')")
    exec(f"btn{i+1}.bind('<Button-1>', func)")
    exec(f"ans{i+1} = tk.Entry(lf{i+1})")
    exec(f"ans{i+1}.pack(side='left')")
root.mainloop()
