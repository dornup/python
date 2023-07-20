# динамическое программирование

weight = {"guitar": 1,
          "recorder": 4,
          "notebook": 3}
price = {"guitar": 1500,
         "recorder": 3000,
         "notebook": 2000}
place = {1: "guitar",
         2: "recorder",
         3: "notebook"}

elements = {0: {0: None,
                1: None,
                2: None,
                3: None,
                4: None},
            1: {0: None,
                1: None,
                2: None,
                3: None,
                4: None},
            2: {0: None,
                1: None,
                2: None,
                3: None,
                4: None},
            3: {0: None,
                1: None,
                2: None,
                3: None,
                4: None},
            4: {0: None,
                1: None,
                2: None,
                3: None,
                4: None}}

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
    for k, l in table[i].keys(), table[i].values():
        if k >= weight[place[i]]:
            choice = {elements[i-1][k]: table[i-1][k], [place[i], elements[i-1][k - weight[place[i]]]]: price[place[i]] + table[i-1][k - weight[place[i]]]}
            table[i][k] = max([table[i-1][k], price[place[i]] + table[i-1][k - weight[place[i]]]])
#            best_elements =