# тот же логгинг, только со своим логгером, хэндлерами и т.д.
import logging


# создаем Карла Логгерфельда
logger = logging.getLogger(__name__)  # __name__ - встроенная переменная, которая хранит имя текущего модуля

# создаем обработчики
c_handler = logging.StreamHandler()  # этот отвечает за консоль
f_handler = logging.FileHandler('something2.txt', 'w', 'utf-8')  # этот за файл (кстати, тут есть encoding)
c_handler.setLevel('WARNING')  # на консоль выводится все, начиная с WARNING
f_handler.setLevel('ERROR')  # в файл выносится все, начиная с ERROR

# настраиваем формат вывода и соединяем его с хэндлерами
c_format = logging.Formatter('%(name)s - %(levelname)s: %(message)s')  # в консоли только самое важное
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')  # в файле нужно время для ориентации
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# добавляем обработчики в логгер
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# проверяем
logger.warning('This is a warning')  # это выведется в консоль
logger.error('This is an error')  # это выведется в консоль и в файл


# также можно настроить ведение журнала через файл конфигурации, но, как мне кажется, через классы удобнее)
