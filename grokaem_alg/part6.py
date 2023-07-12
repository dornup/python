#  реализация графа и поиска в ширину с помощью словаря и очереди


# функция определения продавца манго (подойдет любая функция, отбирающая по рандомному признаку)
def is_mango(person):
    return person[-1] == "m"


# создаем граф
friends = {}  # взяла граф из книжки, чтобы самой не писать вручную тысячу связей
friends["you"] = ["alice", "bob", "claire"]  # связи между узлами в графе = пары словаря типа "ключ-значение"
friends["bob"] = ["anuj", "peggy"]
friends["alice"] = ["peggy"]
friends["claire"] = ["thom", "jonny"]
friends["anuj"] = []  # от этих узлов дальше связи не идут
friends["peggy"] = []
friends["thom"] = []
friends["jonny"] = []


# реализуем поиск в ширину
def search(graph, name):  # передаем в функцию граф и ключ к массиву связей 1 уровня
    from collections import deque
    queueue = deque()  # очередь для последовательной обработки пользователей
    queueue += graph[name]  # добавляем в очередь узлы первого уровня
    checked = []  # список проверенных людей (избегаем повторов и бесконечных циклов)
    while queueue:
        person = queueue.popleft()  # достаем первый узел из очереди
        if person not in checked:  # сработает, если мы еще не проверяли этого человека
            if is_mango(person):  # это продавец манго?
                print(f"{person} is a mango seller!")  # говорим об этом и выходим
                return True
            else:  # нет?
                queueue += graph[person]  # добавляем в очередь всех друзей этого человека
                checked.append(person)  # добавляем этого человека в список проверенных
    return False  # у нас нет продавца манго

print(search(friends, "you"))
