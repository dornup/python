import random
import datetime

while True:
    number = input("Сколько дршек мы генерируем? (до 70):")
    if not number.isdigit() or int(number) < 2 or int(number) > 70:
        print("Это по твоему шютка какая то?! (")
        print("-" * 5)
    else:
        number = int(number)
        break

birthdays = []
startOfYear = datetime.date(2009, 1, 1)
for _ in range(number):
    sdvig = random.randint(0, 364)
    randomDay = datetime.timedelta(sdvig)
    birthday = startOfYear + randomDay
    birthdays.append(birthday)

for superanton in range(number):
    print(f"{superanton + 1}) {birthdays[superanton].strftime('%d.%m.%y')}") #string format time поменять формат

print("=" * 10)
for i in set(birthdays):  #список -> множество чтобы исключить повторения
    if birthdays.count(i) > 1:
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)} раза")