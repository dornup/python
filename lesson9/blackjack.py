import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
hand_player = [random.choice(cards)]
hand_computer = [random.choice(cards)]
score_player = 0
score_computer = 0
get_card = "y"
while get_card == "y":
    hand_player.append(random.choice(cards))
    if sum(hand_player) > 21 and 11 in hand_player:
        for i in range(0, len(hand_player)): # перебираем карты
            if hand_player[i] == 11: # ищем туза
                hand_player[i] = 1 # меняем 11 на 1
                break
    score_player = sum(hand_player)
    print(f"Твоя рука: {hand_player}. Очков: {score_player}")
    print(f"Первая карта компутора: {hand_computer[0]}")

    if score_player > 21:
        get_card = "n"
    else:
        get_card = input("Берем карту? y - да, х - нет")


