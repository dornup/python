import easygui
#
# result = easygui.msgbox(
#     msg= "hellowo rld",
#     title="Я рюкзак я рюкзак",
#     ok_button="жёсткий пон",
#     image="img/lyaguha.png"
# )
# if result == None:
#     print("Пака пака пупсик 🍭")
# elif result == "img/lyaguha.png":
#     print("Моя ты лягушечка")
# elif result == "жёсткий пон":
#     print("Спасибо за понимание")
#
#
# easygui.buttonbox(
#     msg="Выбери, какой сегодня ты",
#     choices=("Лягушонка", "Солнышко", "Булочка", "Испанец"),
#     images=["img/lyaguha.png", "img/ficus.png"],
#     title="имагес"
# )
#
#
# easygui.integerbox(
#     msg="Сколько раз?",
#     title="Чиселкии",
#     lowerbound=1,
#     upperbound=100,
#     image="img/ficus.png",
#     default=30
# )


# easygui.enterbox(
#     msg="Маия и, маия а, маия а, маия а а",
#     title= "dragonstea",
#     image="img/lyaguha.png"
# )

func = easygui.buttonbox(
    msg = "Чего делать будем?",
    choices = ("зарабатывать", "покупать дом")
)
if func == "зарабатывать":
    answer = easygui.msgbox(
        msg = "ты заработал 100 монеток",
        ok_button = "пон"
    )