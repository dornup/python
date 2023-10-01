from class_user import User, users


def vhod(username, password):
    user = None
    for i in users:
        if i.authorise(username, password):
            print('вы вошли в свой аккаунт')
            user = i
            return user
    print('Пользователь не найден, попробуйте еще раз')
    return user


def registration(username, password):
    user = User(username, password)
    print('Вы успешно зарегистрировались')
    return user


def q():
    print('Вы вышли из приложения')
    quit()


def help_1():
    return '''список команд для пользователя:
    help - вывести список комманд
    log out - выйти из аккаунта
    exit - выйти из приложения
    subscribe *name* - подписаться на пользователя *name*
    unsubscribe *name* - отписаться от *name*
    followers - вывести список папищеков
    following - вывести список подписок
    change password - сменить пароль'''


def log_out():
    print('Вы вышли из аккаунта')
    return None

