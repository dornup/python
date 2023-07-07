# рекурсия

# def counter(i):  # без остановки на нуле это будет бесконечный цикл
#     print(i)
#     # добавляем остановку на нуле
#     if i == 0:  # базовый случай
#         return
#     else:  # рекурсивный случай
#         counter(i - 1)  # рекурсия
#
#
# counter(7)


# стек вызовов
#
# def greet(name):  # первая функция
#     print("Hello,", name, "!")
#     greet2(name)  # вызываем вторую, она "переходит вверх", первая фунция на время останавливается
#     print("getting ready to say bye...")
#     bye(name)  # вызов третьей функции (аналогично вызову второй)
#
#
# def greet2(name):
#     print("How are you,", name, "?")
#
#
# def bye(name):
#     print("Ok, bye,", name)
#
#
# greet("maggie")

# стек вызовов с рекурсией на примере факториала

def factorial(x):
    if x == 1:  # если дошли до 1, то возвращаем 1
        return 1
    else:
        return x * factorial(x-1)  # иначе вызываем функцию факториала предыдущего числа


print(factorial(5))