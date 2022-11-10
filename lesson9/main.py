# print("ай, дайте паесть!")
#
# # ЦиклЫ
# # while (пока)
# x = 10
# while x != 0:
#     print(x)
#     x -= 1

# while True: # срабатывает каждый раз
#     break # выйти из while
#
# # for
# lst = ["А", "Б", "В", "Г", "Д"] # букавы - итерации
# for letter in lst: # проитерироваться по списку
#     print(letter)
#
# for i in range(0, 3):
#     print(i)


# word = input("введи словечко:")
# while word: # пока слово не пустое
#     print(word, end=" ")
#     word = word[:-1]


# x = int(input("Введите число:"))
# while x: # while x != 0
#     x -= 1
#     if x % 2 == 0:
#         print(x)


x = input("введи чиселко:").strip()
if not x.isdigit() or int(x) <= 1:  # если не число
    print("ПАШОЛ ВОН")
    quit()
else:
    x = int(x)


step = 0
while x != 1:
    step += 1
    if x % 2 == 0:
        print(f"{step})", end=" ")
        print(x, "/ 2 =", end =" ")
        x = x // 2
    else:
        print(f"{step})", end=" ")
        print(x, "* 3 + 1 =", end=" ")
        x = x * 3 + 1
    print(x)
print("Шагов:", step)

