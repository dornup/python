# # классы. повторение
#
# class Nazvanie:
#     def __init__(self): # magic метод
#         self.money = 1_000 # public
#         self.__zarplata = 3 # private
#
#     def bar(self): # public метод
#         if self.__zarplata > 4: # используем private
#             return True
#         else:
#             self.__sad()
#             return False
#     def __sad(self): # private метод
#         print("*Сане грустнехонько*")
#
# sanya = Nazvanie()
# print(sanya.money) # public можно выводить
# sanya.money += 100 # public можно менять
#
# # print(sanya.__zarplata) # нельзя выводить private
# # sanya.__zarplata = 10 # private можно менять?.. Нет, это public
# #sanya.__zarplata += 10
# print(sanya.bar())
#
# sanya._Nazvanie__zarplata = 1_000_000 # меняем private

# Первый задача
# class Avtomobil:
#     def zapusk(self):
#         return "Автомобиль заведен"
#
#     def vikl(self):
#         return "Автомобиль заглушен"
#
#     def cvet (self, color):
#         self.avto_color = color
#
#     def god(self, year):
#         self.avto_year = year
#
#     def tip(self, type):
#         self.avto_type = type
#
# nissan = Avtomobil()
# print(nissan.zapusk())
# print(nissan.vikl())
# nissan.cvet("goluboi")
# print(nissan.avto_color)
# nissan.tip("sedan")
# print(nissan.avto_type)
# nissan.god("2017")
# print(nissan.avto_year)


# # Вторая задача
# import string
#
# class Alphabet:
#     def __init__(self, language, letters):
#         self.__language = language
#         self.__letters = string.ascii_lowercase
#     def print(self):
#         print(self.__letters)
#     def l(self):
#         print(len(self.__letters))
#
# ala = Alphabet("eng", "abcdefghijklmnopqrstuvwxyz")
# ala.print()
# ala.l()


# задача тритий
# import datetime
# class Clock:
#     def __init__(self):
#         self.__time = datetime.datetime.now().strftime("%H:%M:%S")
#         self.__h, self.__m, self.__s = self.__time.split(":")
#         self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)
#
#     def hours(self):
#         self.__h += 1
#
#     def minutes(self):
#         self.__m += 1
#
#     def seconds(self):
#         self.__s += 1
#
#     def test_h(self):
#         if self.__h > 23:
#             self.__h = 0
#
#     def test_m(self):
#         if self.__m > 59:
#             self.__m = 0
#             self.__h += 1
#
#     def vivod(self):
#         print(f"{str(self.__h).rjust(2, '0')}:{str(self.__m).rjust(2, '0')}:{str(self.__s).rjust(2, '0')}")
#
#
# time_0 = Clock()
# time_0.minutes()
# # time_0.test_m()
# time_0.vivod()
