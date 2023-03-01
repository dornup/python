import random
import math
while True:
    print("Угадай число")
    mini = 0
    try:
        maxi = int(input("Введи максимум: "))
    except ValueError:
        maxi = int(input("Антон, здесь нужно ввести число, чтобы не сломать"
                         "ни программу, ни мои нервы), максимум: "))
    while True:
        if maxi < 1:
            maxi = int(input("Кстати, Антон, это число должно быть "
                             "положительным. Спасибо за понимание, введите максимум:"))
        else:
            break
        
    computer_number = random.randint(mini, maxi)
    life = round(math.log2(maxi))
    
    while life > 0:
        try:
            user_number = int(input("Введи число: "))
        except ValueError:
            print("Антон, тут есть except, который не даст вам сломать программу")
        else:
            if user_number < mini or user_number > maxi:
                print(f"Введи число от {mini} до {maxi}")
                continue
            if computer_number == user_number:
                print("Вы победили!")
                break
            elif computer_number < user_number:
                print("Нужно меньше.")
                maxi = user_number
            else:
                print("Нужно больше.")
                mini = user_number
            print(f">>> Интервал: {mini} – {maxi}")
            life = life - 1
            print("❤️:", life)
    answer = input("Хочешь продолжить?")
    if answer == "Да":
        continue
    else:
        break
