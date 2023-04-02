## 18 урок
## Функции
##def function(x): ## объявление функции
##    return x + 1
##print(function(5))
##
##f = lambda x2: x2 + 1 ## объявили лямбда функцию
##print(f(5))
## куча фасоли
##fasol = 20
##def schot(x):
##    global fasol
##    fasol -= x
##while fasol > 0:
##    while True:
##        f = int(input("number one, 1, 2 или 3 фосольки:"))
##        if f < 4 and f > 0:
##            break
##    schot(f)
##    print(f"осталось", fasol, "фосолей")
##    if fasol <= 0:
##        print("number one - loser")
##        break
##    while True:
##        s = int(input("number two, 1, 2 или 3 фосольки:"))
##        if s < 4 and s > 0:
##            break
##    schot(s)
##    print(f"осталось", fasol, "фосолей")
##    if fasol <= 0:
##        print("number two - loser")
##        break

## strelba
##from random import randint
##import time
##
##print("Время проверить твою ловкость и скорость и понять, кто самый быстрый стрелок на западе! Когда увидишь 'СТРЕЛЯЙ', у тебя будет 0.3 секунды чтобы нажать Enter. Но если ты нажмёшь Enter раньше, то ты проиграл.")
##
##input("нажмите enter чтобы умереть:")
##print("Время пострелять!")
##time.sleep(randint(2, 5))
##start = time.time()
##input("ПУЛЯЙ!")
##end = time.time()
##cenok = end - start
##if cenok < 0.3 and cenok > 0:
##    print(f"твоя реакция произошла за", cenok , "секунд. Хорошая работа, Олег")
##elif cenok > 0.3:
##    print(" я тебе сейчас скандал учиню, чирипака! ")
##else:
##    print("А вот это уже не моя проблема")

## dies
##from random import randint
##
##colvo = int(input("Cколько косточек?"))
##d = {}
##
##for i in range(colvo, 6*colvo+1):
##    d[i] = 0
##for b in range(1_000_000):
##    total = 0
##    for _ in range(colvo):
##        brooosok = randint(1, 6)
##        total +=brooosok
##    d[total] += 1
##print(d)
    

