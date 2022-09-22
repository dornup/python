# a =int(input("a:"))
#
# print("последняя цифра:",a % 10)
# print("первая цифра:", a // 100)
# print("вторая цифра:", )
# a = int(input("a:"))
# first = a // 100
# second = a //10 % 10
# third = a % 10
# print("Произведение цифр:",first * second * third)
# a = int(input("a:"))
# if a % 2 == 1:
#     a = a + 1
# else:
#     a = a + 2
# print ("Следущее четное число:",a)
# d = int(input("d:"))
# print("длина:",d*3.14)
# r = d / 2
# print ("площадь:",3.14 * r ** 2)
a = int(input("секундочки:"))
h = a // 3600
m = a % 3600 // 60
s = a % 60
if h < 10:
    h = "0" + str(h)
if m < 10:
    m = "0" + str(m)
if s < 10:
    s = "0" + str(s)


print(f"{h}:{m}:{s}")
