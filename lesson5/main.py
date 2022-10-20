# x = int(input("Введи число:"))
# if 5 < x < 10:
#     print("урааа")
# if x < 10 and x > 5: # оба условия обязательны
#     pass # заткнись
# if x < 10 or x > 5: # или то или то
#     pass
# списки
# name_1 = "Тоха"
# name_2 = "Антон"
# name_3 = "Антуан"
# mega_anton = [name_1, name_2, name_3]
# # операции со списками :
# mega_anton.append("Тоша") # добавить
# print(mega_anton)
# mega_anton.pop(2) #удалить по индексу
# mega_anton.remove("Тоха") #удалить по значению
# print(mega_anton)
# # двойная индексация (индексация несколько раз)
# man = [["Антон", "Гриша"] , ["Компуктеры" , "Настолки"] , "Мама"]
# print(man[0][0]) #Выводим Антона
# number = float(input("Введите число: "))
# if number < 0 :
#     print("отрицательное")
# elif number > 0:
#     print("положительное") # else: if = elif
# else:
#     print("нуль")
# year = int(input("Введи год:"))
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print("Високосненько )")
# else:
#     print(" Не високосненько ( ")
# number_1 = int(input( "Введи первое число!!! :"))
# operation = input("Введи операцию (+, -, /, *, **, |) :").strip()
# number_2 = int(input ("Введи второе число!!! :"))
# lst = ["+", "-", "/", "*" , "**" , "|"]
# if operation in lst:
#     if operation == "+":
#         print(number_1 + number_2)
#     elif operation == "-":
#         print(number_1 - number_2)
#     elif operation == "/":
#         print(number_1/number_2)
#     elif operation == "*":
#         print(number_1*number_2)
#     elif operation == "**":
#         print(number_1**number_2)
#     elif operation == "|":
#         print(abs(number_1), abs(number_2))
# number_1 = int(input("Первое число"))
# number_2 = int(input("Второе число"))
# number_3 = int(input("Третье число"))
# lst = [number_1, number_2, number_3]
# print("Максимальное число:" , max(lst))
# print("Минимальное число:", min(lst))
# # мин - минимальный макс - максимальный
# ticket = input("Введи номер билета:")
# if len(ticket) == 6 and ticket.isdigit(): # 6 цифр в билете
#     first_half = ticket[:3] # три первых числа
#     last_half = ticket[-3:] # три последних числа
#     first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
#     last_sum = int(last_half[0]) + int(last_half[1]) + int(last_half[2])
#     if first_sum == last_sum:
#         print("счастливенький)))❤")
#     else:
#         print("ты лошарик(((💔")
# else:
#     print("ну але...")