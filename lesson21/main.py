# try:
#     number = int(input("Введи чиселко: "))
# except (ValueError, IndexError):
#     print("понял")
# except IndexError:
#     print("эээ")
# else:
#     print("понял")
# finally:
#     print("пооон")
#
#
# name = input("введи имя подружечки: ").title()
# try:
#     if name == "Антон":
#         raise ValueError("Атайди сабака!")
# except ValueError as pelemeny:
#     print(pelemeny, "Фу, бяка")
#
# def masha(content):
#     s = 0
#     k = 0
#     for chiselko in content:
#         try:
#             s += int(chiselko)
#         except ValueError:
#             print("Найдено не число")
#         else:
#             k += 1
#         if k == 0:
#             print("чисел нету, покусики")
#             return "Пустоты"
#     return round(s / k, 3)
#
# try:
#     g = open("23-02.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("Файлик не найден, покусик!")
#     quit()
# content = g.read().split()
# g.close()
# print(masha(content))
#
#
# try:
#     g = open("23-02.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("Файлик не найден, покусик!")
#     quit()
# content = g.readlines()
# g.close()
#
# for i, student in enumerate(content):
#     content[i] = student.split()
#
# maxi = -1
# for student in content:
#     try:
#         if int(student[3]) > maxi:
#             maxi = int(student[3])
#     except ValueError:
#         print("неверно указаны баллы", student)
#     except IndexError:
#         print("баллы отсутствуют", student)
#
# if maxi == -1:
#     print("записи об участниках не найдены")
# else:
#     print(maxi)
#
#
# try:
#     g = open("23-02.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("Файлик не найден, покусик!")
#     quit()
#
# content = g.read()
# word = input("Какое словечко мы ищем: ")
# print(content.count(word))
