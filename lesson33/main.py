# TASKS


# ======== 1 task ===========
# 1)

# slovar = {"key1": "value1",
#           "key2": "value2",
#           "key3": "value3",
#           "key4": "value4",
#           "key5": "value5"}
#
# keys = []
# values = []
#
# for i in slovar:
#     keys.append(i)
#     values.append(slovar[i])
#
# print(keys)
# print(values)

# 2)

# slovar = {"key1": "value1",
#           "key2": "value2",
#           "key3": "value3",
#           "key4": "value4",
#           "key5": "value5"}
#
# keys = list(slovar.keys())
# values = list(slovar.values())
#
# print(keys)
# print(values)


#=========== 2 TASK ==============

# 1)

# x = ["Никита", "Екатерина", "Арсалан", "Наталья", "Григорий", "Евгений", "Анастасия", "Андрей", "Евгения", "Герман",
#      "Тимур", "Ярослава", "Есения", "Даниил", "Данил"]
#
# imya = input("Введи имя: ").capitalize()
# colvo = 0
#
# for i in x:
#     if i == imya:
#         colvo += 1
#
# print(colvo)

# 2)

# x = ["Никита", "Екатерина", "Арсалан", "Наталья", "Григорий", "Евгений", "Анастасия", "Андрей", "Евгения",
#      "Герман", "Тимур", "Ярослава", "Есения", "Даниил", "Данил"]
#
# imya = input("Введи имя: ").capitalize()
# colvo = x.count(imya)
#
# print(colvo)


# =========== 3 TASK =================

# import math
#
# x = math.ceil(float(input("Введи чиселко: ")))
# print(x)


# ========== 4 TASK ===================

# from random import choice
# from string import ascii_uppercase
#
# alphabet = list(ascii_uppercase)
# x = int(input("Введите чиселко: "))
# word = ""
#
# for i in range(x):
#     word += choice(alphabet)
#
# word = set(word)
# orig = ""
#
# for i in word:
#     orig += i
#
# print(word)
# print(orig)


# ============= 5 TASK ==================

# while True:
#     sueta = input("Ну введи суету..:")
#     sueta = sueta.split(" ")
#     if sueta[0] == "Суета":
#         break


# ============= 6 TASK ===================

# x = "abcdefghijklmnopqrstuvw"
# print(x[-1::-2])
# print(x[-1:3:-2])


# ============== 7 TASK ===================

# from random import randint
#
# s = set()
#
# for i in range(10):
#     s.add(randint(0, 15))
#
# s = list(s)
# max = 0
#
# # for i in s:
# #     if i > max:
# #         s.remove(i)
# #         s.insert(0, i)
# #         max = i
#
# s.sort(reverse=True)
#
# print(s)



