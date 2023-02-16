# f = open("восьмой бэ сегодня дежурка лох.txt", "w", encoding="utf-8")
# f.write("hellow orld\n")
# f.write("Movavi")
#
# f.close()

# f = open("восьмой бэ сегодня дежурка лох.txt", "r", encoding="utf-8")
# #content = f.read() # чтение одной строкой
# content = f.readlines() # чтение в несколько строк
# print(content)
# print(f"Первая лайн: {content[0]}")
#
# for line in content:
#     print(line.rstrip()) # убирает перенос строки(\n) в конце
# f.close()

# задачечка уан:

# file_name = input("Введи имя файла:")
# file_text = input(">>>")
# file = open(file_name, "w", encoding="utf-8")
# file.write(file_text + "\n")
# while True:
#     if file_text == "":
#         print("Файл записан")
#         break
#     else:
#         file_text = input(">>>")
#         file.write(file_text + "\n")
# file.close()

# 2 задача
# f = open("пипипу.txt", "r", encoding="utf-8")
# content = f.readlines()
# f.close()
# f = open("zad2.txt", "w", encoding="utf-8")
# count = 1
# for line in content:
#     result = f"{count}) {line}"
#     f.write(result)
#     count+=1
# print(content)