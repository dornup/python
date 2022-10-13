# # # # print("тыкаем папочку")
# # # familia = input("Фамилия:").capitalize()
# # # imya = input("Имя:").capitalize()
# # # otchestvo = input("Отчество:").capitalize()
# # # print(familia, imya[0] + ".", otchestvo[0] + ".")
# # # print(f"{familia} {imya[0]}. {otchestvo[0]}." )
# # # word = input("введи фразочку:")
# # # print("a:", word.count("a"))
# # # print("ab:" , word.count("ab"))
# # strochka = input("Введи в меня фразу, разделенную пробелами:").strip()
# # lst = strochka.split(" ")
# # lst.pop(0) #удалить по значению
# # print(lst)
# phrase = input("введи пхразу")
# find = input("Что меняем:")
# replace = input("На что меняем:")
# print(phrase.replace(find, replace)) # репласе замена одного на другое
# x = input()
# print(x.replace("йо", "ё"))
alphabet = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "j",
}
phrase = input("Введи фразу:")
translate = ""
for bukva in phrase:
    translate = translate + alphabet[bukva]
print(translate)

