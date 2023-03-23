# class Chelovek:
#     pi = 3.14 # public статический
#     __city = "Новосибирск" # private статический
#     def __init__(self):
#         self.hi = 888 # public динамический
#         self.__vozrast = 40 # private динамический
#
# obj = Chelovek()
# print(obj.hi)
# # print(Chelovek.pi)

# class Chelovek:
#     def __init__(self, height = 200): # значение по умолчанию
#         self.hi = height
#
# obj = Chelovek() # не передал -> значение по умолчанию
# print(obj.hi)
#
# obj2 = Chelovek(300) # передал -> переданное значение
# print(obj2.hi)


# sims 10
import easygui
from random import randint

class Human:
    default_name = "Антон"
    default_age = 37
    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 5
        self.__house = False
    def info(self):
        return f"Имя:{self.name}, возраст:{self.age}, место проживания:{self.__house}, капитал:{self.__money}"
    def earn_money(self):
        self.__money += 100
        return self.__money
    def default_info(self):
        return Human.default_name, Human.default_age
    def __make_deal(self, dom):
        if self.__money >= dom.final_price():
            self.__money -= dom.final_price()
            return True
        else:
            return False
    def buy_house(self, dom):
        if self.__make_deal(dom) == True:
            dom.owner = self.name
            self.__house = dom
            return "Cделка прошла успешно"
        else:
            return f"Денег мало. Тебе нужно еще {dom.final_price() - self.__money}"

class House:
    def __init__(self, area, price):
        self.__area = area
        self.__price = price
        self.__skidka = randint(5, 25) / 100
    def final_price(self):
        return self.__price - self.__price * self.__skidka

imya = easygui.enterbox(
    msg = "Введите имя игрока:"
)
vozrast = easygui.integerbox(
    msg = "Введите возраст игрока"
)
chel = Human(imya, vozrast)

while True:
    func = easygui.buttonbox(
        msg = "Чего делать будем?",
        choices = ("зарабатывать", "покупать дом", "кто я?")
    )
    if func == "зарабатывать":
        answer = easygui.msgbox(
            msg = "ты заработал 100 монеток",
            ok_button = "пон"
        )
        chel.earn_money()
        if answer ==  "пон":
            continue
        else:
            break
    elif func == None:
        break
    elif func == "покупать дом":
        pass
    elif func == "кто я?":
        answer = easygui.msgbox(
            msg = chel.info()
        )


domik1 = House("Улица пушкина, дом колотушкина", 200)
domik2 = House("Замок Дракулы", 500)
domik3 = House("квартира в культурном центре Петербурга", 400)

# print(artem.info())
# print(artem.earn_money())
# print(artem.default_info())
# print(domik1.final_price())
# print(artem.buy_house(domik1))



