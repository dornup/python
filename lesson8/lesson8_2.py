import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(3)
t.color("green", "purple")


t.begin_fill()

try:
    ugol_i = int(input("Введи количество углов (>2):"))
    
except Exception:
    ugol_i = int(input("\n"
                     "Ты что-то ввел не так(( Мне нужно целое положительное число БОЛЬШЕ 2!:"))
if ugol_i == 2:
    ugol_i = int(input("\n"
                     "Ты что-то ввел не так(( Мне нужно целое положительное число БОЛЬШЕ 2!:"))
    
ugol_t = 0

while ugol_t < ugol_i:
   t.fd(40)
   t.rt(360/ugol_i)
   ugol_t = ugol_t + 1

t.end_fill()


screen.exitonclick()
    
