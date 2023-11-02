# input:
n = int(input('Кол-во оценок: '))
end = float(input('Необходимый рейтинг: '))
rate = float(input('Рейтинг сейчас: '))
min_sum_rates = round((rate-0.05)*n, 1)
max_sum_rates = round((rate+0.04)*n, 1)
max_five, min_five = 0, 0
print(min_sum_rates, max_sum_rates)

while rate < end:
    if max_sum_rates/n < end:
        max_sum_rates += 5
        max_five += 1
    n += 1
    min_sum_rates += 5
    min_five += 1
    rate = round(min_sum_rates/n, 1)

print(f'Нужно от {min_five} до {max_five} пятерок c какой-то погрешностью')