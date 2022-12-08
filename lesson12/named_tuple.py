from collections import namedtuple

citizen = namedtuple("Житель", "имя возраст статус какую_группу_ты_уважаешь")
alex = citizen(имя="Лёха Алексеев", возраст=27, статус="Предприниматель", какую_группу_ты_уважаешь="Аля Пугачева")

print(alex.имя)
print(alex.какую_группу_ты_уважаешь)
print(alex)
