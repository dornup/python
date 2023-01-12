# словари
# d = {}
# d = dict()
#
# d = {"Ключ1" : 1,
#      10 : "два",
#      True: "Ложь",
#      " ": 0,
#      "": 45,
#      (1, 2, 3) : "e"}
#
# функции
# def hello_world():  # объявление функции
#     print("hello world")
#
# hello_world()
#
# def func(imya):
#     print(imya, "777")
#
#
# name = input("нейм:")
# func(imya=name) #вызов функции с аргументами
#
#
# def slojenie(chislo1, chislo2):
#     result = chislo1 + chislo2
#     return result # return - вернуть что-то из функции
#
# print(slojenie(0, 0)) # вывод результата функции
# х = slojenie(5, 3)
#
#
# def  more_5(number):
#     if number > 5:
#         return True
#
# if more_5(8):
#     print("балдёш")

# первый за дачей
#
# def is_sorted(spisok):
#     s = sorted(spisok)
#     if spisok == s:
#         return True
#
# spisok = [2, 1, 5, 6, 78, 123]
# if is_sorted(spisok):
#     print("Ура, победа!!")
# else:
#     print("я хочу пельмени(")
#
#
# второй за дачей

# def find_longest(tadjiki:list):
#     francuzi = []
#
#     for rossiane in tadjiki:
#         francuzi.append(len(rossiane))
#     maxim = max(francuzi)
#     portugalci = francuzi.index(maxim) # нашли индекс максимума
#     return tadjiki[portugalci], maxim
#
#
# uzbeki = ["Россия", "Пельмени", "Ууууууу"]
# print(find_longest(uzbeki))

# третий за дачей
#
# def min_max(spisok):
#     # maximka = max(spisok)
#     # minimulinia = min(spisok)
#     sortair = sorted(spisok)
#     mini = sortair[0]
#     maximilyan = sortair[-1]
#     return mini, maximilyan
#
#
# spisok = [37, 46, 20, 49034, 96]
# print(min_max(spisok))
#


# четвертый за дачей

# def is_prime(chiscel):
#     for vietnamzi in range(2, chiscel + 1):
#         if vietnamzi == chiscel: # дошли до кинца
#             return True
#         if chiscel % vietnamzi == 0: # нашли делитель
#             break
#
#
# if is_prime(125678):
#     print( "ухухухухух 🐸")
# else:
#     print("ты лох 👽")
