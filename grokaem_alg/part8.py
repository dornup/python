# задача на покрытие множества с помощью жадного алгоритма


states = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}  # штаты, которые нужно покрыть

stations = {"kone": {"id", "nv", "ut"},  # словарь станций и городов, в которых они работают
            "ktwo": {"wa", "mt", "id"},
            "ktree": {"or", "nv", "ca"},
            "kfour": {"nv", "ut"},
            "kfive": {"ca", "az"}}

final_stations = set()  # будущий словарь необходимых станций

# жадный алгоритм
while states:  # пока есть непокрытые города
    best_station = None  # наиболее эффективная станция
    states_covered = set()  # сколько городов она покрывает
    for station, states_for_station in stations.items():  # проходимся по ключам и значениям словаря
        covered = states & states_for_station  # пересечение городов станции и необходимых городов
        if len(covered) > len(states_covered):  # если станция покрывает больше городов, чем предыдущая
            # обновляем данные
            best_station = station
            states_covered = covered
    states -= states_covered  # исключаем покрытые города
    final_stations.add(best_station)  # добавляем станцию в множество


print(final_stations)
