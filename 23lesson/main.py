# # классы
# class Person: # объявление класса
#     def __init__(self, imya, vozrast): # метод инициализации
#         self.age = vozrast # установка значений атрибутов
#         self.name = imya
#     def __str__(self):
#         return "Я Кристина"
#
#
# eugenii = Person("Юджин Фицхерберт", 40)
# anna = Person(vozrast=0, imya="Кристина")
#
# print(anna.name)
# print(eugenii.age)
# print(anna)


# class HelloWorld:
#     def __getitem__(self, key):
#         print("hello world", key)
#
# hi = HelloWorld()
#
# # !!! обрати внимания, что здесь нет print(), просто обращение по ключу
# hi[42]
# hi['Movavi']


# # задача 1
# class Person:
#     def __init__(self, imya, vozrast, familia):
#         self.name = imya
#         self.age = vozrast
#         self.secondname = familia
#         self.grades = [randint(2, 5) for n in range(randint(5, 10))]
#         self.sa = sum(self.grades) / len(self.grades)
#     def __str__(self):
#         return f"{self.name} {self.age} {self.secondname}"
#     def greet(self):
#         return f"Привет! Меня зовут {self.secondname} {self.name}, и мне {self.age} лет"
#
#
# anna = Person("Аня", 20, "Пупкина")
# print("Имя: ", anna.name)
# print("Фамилия: ", anna.secondname)
# print("Возраст: ", anna.age)
# print(anna)
# print(anna.greet())
# # print(anna.grades)
# # print(anna.sa)
# melanya = Person("Мелаша", 13, "Дорн")
# vladislav = Person("Владюша", 14, "Пупочкин")
# anton = Person("Антоша", 20, "Смирнов")
# studen = [anna, melanya, vladislav, anton]
#
# dnevnik = {}
# for item in studen:
#     dnevnik[item.name] = item.sa
#
# sorted_dnevnik = dict(reversed(sorted(dnevnik.items(), key=lambda item: item[1])))
#
# schetchik = 0
# for item in sorted_dnevnik:
#     schetchik += 1
#     print(f"{schetchik}. {item} - {sorted_dnevnik[item]}")


# задача 3

class Rectangle:
    def __init__(self, d1, d2):
        self.dot1 = d1
        self.dot2 = d2
    def ploshad(self):
        a = self.dot2.y - self.dot1.y
        b = self.dot2.x - self.dot1.x
        return a * b

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

dot1 = Point(1, 152)
dot2 = Point(2, 250)
pryamoug = Rectangle(dot1, dot2)
print(pryamoug.ploshad())