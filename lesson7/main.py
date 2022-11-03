# # #ZeroDivisionError
# # #x = 5/0
# # #TypeError:
# # #x = "a" + 15
# # IndexError:
# # x=[0, -15, "Aнтон"]
# # x[3]
# SyntaxError:
# x = "Привет, я Антон
# NameError:
# x = "Я строчка"
# print(x2)
# # assert --> AssertionError
# def summa (numbers)
#     return sum(numbers)
#
# print(summa([3,4]))
#
# assert summa([1,2]) == 3
# assert summa([1,2]) == 4
# # try - пытаться
# # except - ловить ошибку
# #finally - в конце
# try:
#     number = int(input())
#     x = 5/ number
# except ZeroDivisionError:
#     print("Слышь, нельзя на ноль делитб!")
# except ZeroDivisionError:
#     print("Хочу кифир")
# except Exception:
#     print("Не трай((")
# else: #когда все чикипуки
#     print("Я поделив)")
# finally:
#     print("всьо")
#
#
# print("я закончил работать")
# # PASS
# try:
#     number = int(input())
#     x = 5/number
# except Exception:
#     pass # ЗАВАЛИСЬ
# if 5 == 5:
#     pass #TODO:
# try:
#     x = input("Введи имя:")
#     if x == "Антон":
#         raise Exception ("Не отдаем Антона!")# Вызвать исключение
# except Exception as error_message:
#     print("ЗАПРЕЩЕНКА", error_message)


ints = []
try:
    f = open("text.txt")
except FileNotFoundError:
    print("ну, я попытався, не получилосб")
else:
    try:
        for line in f:
            ints.append(int(line))
    except ValueError:
        print("Тут не число, а мне цифырки нужны")
    else: #если нет ошибак
        print(ints)
    finally: # ВСЕГДА
        f.close()
        print("я всьо")

