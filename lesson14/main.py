# # 1 задача из тысячи)
# phrase = "РОССИЯ, РОССИЯ, РОССИЯ И БОГДАН! ".lower().strip() # жестко опускаем
# symbols = list("~@#$%^&*()1234567890'\",.?!") # \" - экранирование. прикол
# phrase_clear = "" #Ща помоем
# for anton in phrase: # итерироваться по фразе
#     if anton not in symbols:
#         phrase_clear += anton
#
# phrase_list = phrase_clear.split(" ")
# print(phrase_list)
#
# d = {}
# for dom in phrase_list:
#     if dom not in d:  # если ключа нет
#         d[dom] = 1 # обозначение нового элемента {"Россия" : 1}
#     else: # если ключ есть
#         d[dom] += 1 # плюс элемент
# print(d)


# второй задача
# sloj = 0
# d = {"Молоко": 100,
#      "Доширак": 21,
#      "Чипсы": 0.5,
#      "Богдан": 999}
# for i in d.values(): #перебор по значениям
#     sloj += i
# print(sloj)


#Тритий (за дачей)
DIE_SIDES = 6
DIE_COUNT = 2
d = {}

for first in range(1, DIE_SIDES + 1):
    for second in range(1, DIE_SIDES + 1):
        if first + second not in d:
            d[first + second] = [(first, second)]
        else:
            d[first+second].append((first, second))

for Mega_Anton in d:
    print(f"{Mega_Anton}: {d[Mega_Anton]}")
