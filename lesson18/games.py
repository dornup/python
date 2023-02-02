import easygui
import random


def rock_paper_scissors():
    otvets = {"bumaga": "img/bumaga.png",
              "nojnici": "img/nojnici.png",
              "kamen": "img/kamen.png",
              "ROSSIA": "img/ROSSIA.png"}
    result = easygui.buttonbox(
        msg="Выбери фигурку 👽",
        title="kamen, nojnici, bumaga, rossia",
        images=["img/bumaga.png", "img/nojnici.png", "img/kamen.png", "img/ROSSIA.png"],
        choices=("я ухожу, оставляя горы окурков, километры дней, миллионы придурков",),

    )
    print(otvets.keys())
    #    answer_comp = random.choice(list(otvets.keys()))
    answer_comp = "nojnici"
    print(answer_comp)
    if result == otvets["kamen"] and answer_comp == "nojnici":
        easygui.msgbox(msg="Урааааа 🦑")
    # ДОПИСААААААААААААААААААААААААААААААААААААААААААААТЬ


otvet_compa = random.randint(1,99)
def guess_the_number():
    result = easygui.integerbox(
        msg="Какое чесело, кефиренок?",
        lowerbound=1,
        upperbound=99,
    )
    if result == otvet_compa:
        return # выход из функции
    while result != otvet_compa:
        if result < otvet_compa:
            result = easygui.integerbox(
                msg="Какое чесело, кефиренок?",
                lowerbound=1,
                upperbound=99,
                image= "img/m.png"
        )




games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()