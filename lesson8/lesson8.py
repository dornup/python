import turtle


screen = turtle.Screen()
t = turtle.Turtle()


try:
    stupenka_igrok = int(input("Cколько ступенек:"))
    
except ValueError:
    stupenka_igrok = int(input("\n"
                               "мне число нужно:"))
    
stupenka_t = 0

if stupenka_igrok < stupenka_t:
    stupenka_igrok = int(input("\n"
                               "не может быть отрицательного кол-ва ступенек..\
( Введи положительное число:"))


try:
    color_1 = input("\n"
                    "Выбери первый цвет(контур)\n"
               "[red, orange, yellow, green, light blue, blue, purple,\
pink, black, white...]\n"
                    "Фууух... больше не вспомню. выбирай:")
    
    color_2 = input("\n"
                    "Выбери второй цвет(заливка)\n"
               "[red, orange, yellow, green, light blue, blue, purple,\
pink, black, white...]\n"
                    "Фууух... больше не вспомню. выбирай:")

    t.color(color_1, color_2)
    
except Exception:
    color_1 = input("\n"
                    "Введи, пожалуйста, правильно цвет для контура из \
верхнего списка, а то получится, что я зря старалась( :")
    
    color_2 = input("\n"
                    "Введи, пожалуйста, правильно цвет заливки из \
верхнего списка, а то получится, что я зря старалась(( :")
    
finally:
    t.color(color_1, color_2)
    
    
try:
    speed = int(input("\n"
                      "Введи скорость(число от 1 до 10):"))
    
except ValueError:
    speed = int(input("\n"
                      "Мне нужны только цифарки):"))
    
if speed > 10:
    speed = int(input("\n"
                      "Если скорость будет такой высокой, мы не заметим работу \
черепашки(( Введи число поменьше: "))
    
t.speed(speed)


t.begin_fill()
while stupenka_t < stupenka_igrok:
    t.lt(90)
    t.fd(20)
    t.rt(90)
    t.fd(20)
    stupenka_t = stupenka_t + 1
if stupenka_t == stupenka_igrok:
    a = stupenka_t * 20
    t.rt(90)
    t.fd(a)
    t.rt(90)
    t.fd(a)

t.end_fill()


screen.exitonclick()



