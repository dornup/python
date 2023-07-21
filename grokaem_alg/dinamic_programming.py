# динамическое программирование

weight = {1: 1,
          2: 4,
          3: 3}
price = {1: 1500,
         2: 3000,
         3: 2000}
place = {1: "guitar",
         2: "recorder",
         3: "notebook"}

elements = {0: {0: "nothing",
                1: "nothing",
                2: "nothing",
                3: "nothing",
                4: "nothing"},
            1: {},
            2: {},
            3: {}}

table = {0: {0: 0,
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

stolen = set()

for i in range(1, len(table)):
    for k in table[i]:
        if k >= weight[i]:
            print(k - weight[i])
            if table[i - 1][k] < price[i] + table[i - 1][k - weight[i]]:
                table[i][k] = price[i] + table[i - 1][k - weight[i]]
                elements[i][k] = [place[i], elements[i - 1][k - weight[i]]]
                continue
        table[i][k] = table[i - 1][k]
        elements[i][k] = elements[i - 1][k]
    print(table)
    print(elements)
