# оказывается, мне нужно освоить (или хотя бы попытаться это сделать)
# асинхронное программирование

import asyncio
import time


# Нужно сделать так, чтобы все функции выполнились как можно быстрее.
# В них есть 'Быстрые' и 'Медленные' операции

# Решение без asincio:

# def fun1(x):
#     print(x**2)
#     time.sleep(3)
#     print('fun1 завершена')
#
#
# def fun2(x):
#     print(x**0.5)
#     time.sleep(3)
#     print('fun2 завершена')
#
#
# def main():
#     fun1(4)
#     fun2(4)
#
#
# print(time.strftime('%X'))  # Это мы выводим время начала выполнения
#
# main()  # Тут мы сделали все свои дела
#
# print(time.strftime('%X'))  # А это время конца

# Это решение занимает ровно 6 секунд - 3 на fun1 и 3 на fun2
# Может быть, можно быстрее?

# решение с asincio:

async def fun1(x):  # приставка async показывает, что функция асинхронная
    print(x ** 2)
    await asyncio.sleep(3)  # await говорит: 'Я посплю 3 секундочки, но вы делайте свои дела'
    print('fun1 завершена')


async def fun2(x):  # все точно так же, как и в fun1
    print(x ** 0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    task1 = asyncio.create_task(fun1(4))  # создаем задачу
    task2 = asyncio.create_task(fun2(4))  # и еще одну такую же

    await task1  # опять await говорит, что если task затупит, то мы продолжаем работу
    await task2


print(time.strftime('%X'))  # время старта

asyncio.run(main())  # запуск всех функций

print(time.strftime('%X'))  # время конца

# ШОК КОНТЕНТ: функции выполняются одновременно(нет), время выполнения программы - 3 секунды...
