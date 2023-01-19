# def plus_one(a,b): # вызов функции с 2 аргументами
#     return a + b + 1
#
# print(plus_one(5, 4))
#
#
# # Лямбда (lambda) функции
#
# plus_one2 = lambda a, b: a + b + 1
# print(plus_one2(5,4))
#
# # if-else v lambda
# result = lambda answer: True if answer == "Д" else False

# List comprehension (генератор списка)
# spisok = []
# for i in range(1, 6): # от 1 до 5
#     spisok.append(i)
# print(spisok)
#
# spisok2 = [n for n in range(1, 6)]
# # 1. list comprehension всегда пишется в []
# # for n in range(1, 6) обычный цикл for -> сколько будет элементов в списке
# # все что слева от for -> элемент списка
# print(spisok2)

# Первый зада чей

# c2f = lambda c: 9/5 * c + 32
# f2c = lambda f: 5/9 * (f - 32)
# c2k = lambda c: 273.15 + c
# k2c = lambda k: k - 273.15
# f2k = lambda f: c2k(f2c(f))
# print(f2k(203))


# второй зада чей
#
# from random import randint as rand
#
# vvud = lambda exit : True if exit == "Д" else False
#
# while True:
#     vvod = int(input("Эээ чорт, сколько кубов?  --->"))
#     dies = [rand(1, 6) for n in range (vvod)]
#     print(dies)
#     grusha = input("Выходи! (д/н)").upper()
#     vvud(grusha)
#     if vvud(grusha):# если ты тупой
#         break

# Третий зада чей
# from random import choice
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")
#          ]
#
# cot = [choice(choice(chars)) for n in range(6)]
# cotik = "".join(cot)
# dictionaryy = {"https://www.google.com":"y86oЯх"}
# ssylka_na_kavkaz = "https://www.google.com"
# if ssylka_na_kavkaz in dictionaryy:
#     print("Ссылка уже есть в базе, вот ее кот:")
#     print(dictionaryy[ssylka_na_kavkaz]) # выводим код ссылки
# else:
#     print("Ссылка доваблена, держи кота:", cotik)
#     dictionaryy[ssylka_na_kavkaz] = cotik
#
#
# # 4
#
# delenie = lambda a, b: a / b
# print(delenie(4,2))
# delenie1 = lambda a, b: a % b
# print(delenie1(4, 2))
# delenie2 = lambda a, b: a // b
# print(delenie2(4,2))
# stepen = lambda a, b: a**b
# print(stepen(4, 2))
# modula = lambda a: -a if a < 0 else a
# print(modula(2))

