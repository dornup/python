#  попытка реализовать связанные списки

class Element:  # класс, содержащий в себе элемент и ссылку на следующий
    def __init__(self, thing):
        self.thing = thing  # то, что хранится в элементе
        self.next = None  # ссылка на следующий

    # функция добавления элемента в конец
    def append(self, val):
        n = self  # сохраняем первый элемент в отдельную переменную
        while n.next:  # пока имеем ссылку на следующий элемент (пока не доходим до конца по ссылкам)
            n = n.next  # переходим к следующему элементу
        n.next = Element(val)  # добавляем к последнему элементу списка ссылку на добавленный

    # функция вставки после определенного элемента
    def after(self, early, val):
        added = Element(val)  # создаем добавляемый объект
        n = self  # сохраняем первый элемент
        while n.thing != early:  # пока не дошли до элемента, после которого нужно добавить новый
            n = n.next  # переходим к следующему
        added.next = n.next  # добавляем ссылку на следующий после вставляемого объект
        n.next = added  # добавляем ссылку от предыдущего объекта на добавленный

    # функция вставки по индексу
    def insert(self, val, ind=int):
        added = Element(val)  # создаем новый объект
        n = self  # сохраняем первый элемент
        if ind > 0:  # если индекс положительный
            for i in range(ind - 1):
                n = n.next
            added.next = n.next
            n.next = added
        elif ind < 0:  # если индекс отрицательный
            counter = 1
            while n.next:
                n = n.next
                counter += 1
            n = self
            for i in range(counter + ind):
                n = n.next
            added.next = n.next
            n.next = added
        else:  # вставить в начало (индекс 0)
            added.next = n


linked_list = Element(1)
linked_list.append(2)
linked_list.append(3)
linked_list.after(2, 6)
linked_list.insert(2, 2)

element = linked_list
print(element.thing)
while element.next:
    element = element.next
    print(element.thing)
