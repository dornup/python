# а это я пытаюсь понять что за логгинг...
import logging
# модуль дает нам регистратор для сообщений каждого уровня:

# logging.debug('Это сообщение о дебаге')  # по умолчанию это не будет выводиться
# logging.info('Это информационное сообщение')  # и это тоже
# logging.warning('Это предупреждение')
# logging.error('Это сообщение об ошибке')
# logging.critical('Это сообщение о конце света')


# это должно настраиваться в самом начале и только 1 раз:
logging.basicConfig(
    level=logging.INFO,  # level отвечает за то, сообщения какого уровня (и выше) записываются
    filename='something.txt',  # файл, куда будем сохранять (не все же в консоль выводить)
    filemode='w',  # режим 'r' = чтение, 'w' = очистка и запись и т.д.
    format='%(asctime)s - %(levelname)s - %(message)s',  # формат записи
    datefmt='%d.%m.%y - %X'
    # есть и другие настройки: https://docs.python.org/3/library/logging.html#logging.basicConfig
)


# запись информации в журнал:

logging.info('this will be logged to a file')  # пока пишем на инглише, т.к. я еще не поняла, куда пихать encoding(

name = 'Melany'
logging.error('%s raised an error', name)  # можно записать так
logging.error(f'{name} raised an error')  # можно так

# запись ошибок и исключений с пояснениями:

try:
    c = 1/0
except Exception:
    logging.warning('Exception occurred', exc_info=True)  # так можно делать с регистратором любого уровня
    # то же самое, но всегда на уровне error:
    logging.exception('Exception occured')


# по-хорошему надо заменить регистратор по умолчанию на свой собственный (lego2)
