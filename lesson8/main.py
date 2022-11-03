# import random
# number = random.randint(0, 100)  # случайное целое чиселко

# import random as r
# number = r.randint(0, 100)

# from random import randint
# number = randint(0, 100)

# from random import * # фу, бяка
# number = randint(0, 100)
#
# import turtle
#
# screen = turtle.Screen()
# t = turtle.Turtle()
# hor = 200
# ver = 100
# t.width(5)
# t.pensize(5)
# t.color("orange", "red")
# t.speed(9)
# # 1-минимум
# #10 - максимум
# #0 = всемогущество
#
# t.begin_fill()
#  # forward = вперед
# t.fd(hor)
# t.right(90)
# t.fd(ver) # fd = forward
# t.rt(90)
# t.fd(hor)
# t.rt(90)
# t.fd(ver)
# t.rt(90)
# t.end_fill()
#
# t.penup()
# t.goto(120, -30)
# t.pendown()
# t.fd(50)
# t.shape()
#
# t.color("green", "red")
# t.begin_fill()
# t.circle(50)
# t.end_fill()
#
# t. pencolor("yellow")
# t.write("Movavi", font=("Arial Black", 50, "italic"), align = "center")
#
# colors = ["red", "orange", "yellow", "green", "light blue", "blue", "purple"]
# angle = 360/7
#
# for i in range(0, 7):
#     t.color(colors[i])
#     t.fd(80)
#     t.rt(angle)
#
#
#
# screen.exitonclick()

import random
import time

print("Время пострелять")
is_game = True
while is_game:
    print("Заряжаем патрон")
    time.sleep(3)
    print("Крутим барабан")
    time.sleep(2)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print("*Выстрел*")

    slots = [1, 2, 3, 4, 5, 6,]
    patron = random.choice(slots)
    our = random.choice(slots)
    if patron == our:
        print("ЕСТЬ ПРОБИТИЕ 💀")
        is_game = False
    else:
        print("УРА ПОБЕДА")
        a = input("Играем дальше? да/нет:")
        if a == "нет":
            is_game = False

