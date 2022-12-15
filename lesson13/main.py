# # МНОЖЕСТВА
# s = set() # пустое множество
# s1 = {1, 2, 3, 3} # дубликаты исключаются. будет - {1, 2, 3}
# print(s1)

# s2 = {"а", "б", "в"} # неупорядоченный тип данных
# print(s2)

# s1 = {1, 2, 3, 4, 5}
# s2 = {3, 4, 5, 6, 7}
# print(s1.union(s2)) # объединение
# print(s1 | s2) # то же, что и сверху
#
# print(s1.intersection(s2)) #пересечение
# print(s1 & s2)
#
# print(s1.difference(s2)) # разность
# print(s1 - s2)
#
# print(s1.symmetric_difference(s2)) # симметрическая разность
# print(s1 ^ s2)


# словарь
# d = {} # пустой словарь
# d1 = {"Пи": 3.14,
#       "Преподаватель": "Антон",
#       "Список дел": ["Выжить", "Ловить балдеж"],
#       "Словарь": {"Вл1": 1}}
#
# print(d1["Преподаватель"]) # Антон
# print(d1["Список дел"][1]) # Ловить балдеж
# print(d1["Словарь"]["Вл1"]) # 1


# from random import  randint
#
# lst = []
#
# for _ in  range(5):
#       lst.append(randint(1, 5))
# print(lst)
#
# unique = set(lst)
#
#
# print(f"{len(unique)} штук: {unique}")


# from random import randint
#
# lst1 = []
# lst2 = []
#
# size = randint(100, 1000)
# r_start = 0
# r_end = 10_000 # _ - декоративный разделитель
#
# for _ in range(size):
#       lst1.append(randint(r_start, r_end))
#       lst2.append(randint(r_start, r_end))
# set1 = set(lst1)
# set2 = set(lst2)
#
# inter = set1.intersection(set2)
# print(f"Общих чисел: {len(inter)}")
# print(f"Кол-во генераций: {size}")
# print(f"Максимальное число: {max(inter)}")
# print(f"Минимальное число: {min(inter)}")
# # Возможное решение, но колхозно
# # inter1 = list(inter)
# # inter1.sort()
# # print(inter1)
# print(sorted(inter)) # Сортирует и преображает в список


# set = set()
# insert = ""
#
# while insert != "end":
#       insert = input("Ввод:")
#       if insert.lstrip("-").isdigit():
#             # .lstrip() убирает слева то, что в скобках
#             if insert not  in set:
#                   print("❌ нет")
#                   set.add(insert)
#             else:
#                   print("✅ да")
#       elif insert == "end":
#             break
#       else:
#             print("оскорбления - бан, читы - бан...")
