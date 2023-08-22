# динамическое программирование

weight = {1: 1,  # вес предметов
          2: 4,
          3: 3}
price = {1: 1500,  # цена предметов
         2: 3000,
         3: 2000}
place = {1: "guitar",  # местоположение предметов в таблицах
         2: "recorder",
         3: "notebook"}

elements = {0: {0: [None],  # предметы, которые мы берем в каждом подрюкзаке
                1: [None],  # нулевая строка и столбец нужны, чтобы не сломать программу
                2: [None],
                3: [None],
                4: [None]},
            1: {},
            2: {},
            3: {}}

table = {0: {0: 0,  # таблица цен в каждом подрюкзаке
             1: 0,
             2: 0,
             3: 0,
             4: 0},
         1: {0: 0,
             1: 0,
             2: 0,
             3: 0,
             4: 0},
         2: {0: 0,
             1: 0,
             2: 0,
             3: 0,
             4: 0},
         3: {0: 0,
             1: 0,
             2: 0,
             3: 0,
             4: 0}}

# заполнение таблицы
for i in range(1, len(table)):  # проходимся по каждому предмету (строка)
    for k in table[i]:  # проходимся по каждому подрюкзаку (столбец)
        el = []  # список взятых элементов
        if k >= weight[i]:  # если предмет влезает
            if table[i - 1][k] < price[i] + table[i - 1][k - weight[i]]:  # если цена предмета + цена оставшегося пространства больше предыдущего максимума
                table[i][k] = price[i] + table[i - 1][k - weight[i]]  # заносим цену пространства в таблицу
                el = [i for i in elements[i-1][k-weight[i]] if i]  # добавляем все взятые предметы в список
                el.append(place[i])
                elements[i][k] = el  # заносим данные в таблицу
                continue  # идем на следующую клетку
        # ИНАЧЕ (сработает, если мы не заходили хотя бы в одно предыдущее условие)
        table[i][k] = table[i - 1][k]  # максимум сохраняется
        elements[i][k] = elements[i - 1][k]  # элементы сохраняются

# выводим данные из последних клеток таблицы
print(f"Нужно украсть: {elements[max(list(elements.keys()))][max(list(elements[i].keys()))]}")
print(f"Стоимость: {table[max(list(table.keys()))][max(list(table[i].keys()))]}")