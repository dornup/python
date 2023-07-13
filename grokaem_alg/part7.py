# алгоритм Дейкстры


def find_lowest(costs):  # функция поиска узла с наименьшей стоимостью
    lowest_cost = float("inf")  # наименьшая стоимость (по умолчанию бесконечность)
    lowest_cost_node = None  # узел с наименьшей стоимостью (пока никакой)
    for i in costs:  # перебираем словарь узлов и их стоимостей
        cost = costs[i]  # стоимость узла
        if cost < lowest_cost and i not in checked:  # если стоимость меньше предыдущей и узел не обработан
            # обновляем данные
            lowest_cost = cost
            lowest_cost_node = i
    return lowest_cost_node


# граф, который будем обрабатывать
graph = {"start": {"a": 6,
                   "b": 2},
         "a": {"end": 1},
         "b": {"a": 3,
               "end": 5},
         "end": {}}

# цены узлов (будут изменяться)
costs = {"a": 6,
          "b": 2,
          "end": float("inf")}

# родители (тоже будут меняться, как ни странно)
parents = {"a": "start",
           "b": "start",
           "end": None}

checked = []  # список проверенных узлов для исключения повторов

node = find_lowest(costs)  # узел с наименьшей стоимостью
while node is not None:  # пока есть узлы
    cost = costs[node]  # сохраняем стоимость обрабатываемого узла
    for i in graph[node].keys():  # перебираем соседей этого узла
        new_cost = cost + graph[node][i]  # стоимость соседя через текущий узел
        if new_cost < costs[i]:  # если через текущий узел стоимость соседя стала меньше
            # обновляем данные
            costs[i] = new_cost
            parents[i] = node
    checked.append(node)  # относим узел к обработанным
    node = find_lowest(costs)  # определяем следующий по стоимости узел


print("Cамый короткий путь имеет вес", costs["end"])
