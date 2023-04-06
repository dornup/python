color1 = input("Введите первый цывет: ").lower().strip()
color2 = input("Введите вторый цывет: ").lower().strip()

colors = ("красный", "синий", "желтый")

if color1 not in colors or color2 not in colors:
    print("аааа звуки не проигрываются, но ты бяка")

# оранжевый
elif (color1 == colors[0] and color2 == colors[2])\
    or (color1 == colors[2] and color2 == colors[0]):
    print("оранжевый")

# фиолетовый
elif (color1 == colors[0] and color2 == colors[1])\
    or (color1 == colors[1] and color2 == colors[0]):
    print("фиолетовый")

# зеленый
elif (color1 == colors[1] and color2 == colors[2])\
    or (color1 == colors[2] and color2 == colors[1]):
    print("зеленый")

else:
    print(color1.capitalize())

    # вторая за дачей))

print(int("08"))

start = input("Начало первого урока (чч:мм): ")
urok = int(input("Длительность урока (мин): "))
peremen = int(input("Длительность перемен (мин): "))
n = int(input("На сколько уроков нужно расписание: "))

splited_start = start.split(":")
hours = int(splited_start[0])
minutes = int(splited_start[1])
vremya = hours * 60 + minutes

for i in range(n):
    print(i + 1, "урок: ", end="")
    print(f"{str(vremya // 60).rjust(2, '0')}:{str(vremya % 60).rjust(2, '0')} - ", end="")
    vremya += urok
    print(f"{str(vremya // 60).rjust(2, '0')}:{str(vremya % 60).rjust(2, '0')}")
    vremya += peremen