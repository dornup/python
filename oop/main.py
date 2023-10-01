from commands import *

while True:
    func = input('Войти или зарегистрироваться: ').lower()
    user = None
    if func == 'войти':
        username = input('введите имя пользователя: ')
        password = input('введите пароль: ')
        user = vhod(username, password)

    elif func == 'зарегистрироваться':
        username = input('введите имя пользователя: ')
        password = input('введите пароль: ')
        user = registration(username, password)

    elif func == 'выйти' or func == 'exit':
        q()

    else:
        print('Вы ввели что-то неправильно, попробуйте еще раз')

    while user:
        command = input('Чтобы увидеть список команд, введите help\n'
                        'Введите команду: ').split()
        if len(command) < 2:
            if command[0] == 'help':
                print(help_1())
            elif command[0] == 'exit':
                q()
            elif command[0] == 'followers':
                print(','.join([i.username for i in user.followers]))
            elif command[0] == 'following':
                print(','.join([i.username for i in user.following]))
        else:
            if command[0] == 'subscribe':
                print(user.subscribe(command[1]))
            elif command[0] == 'unsubscribe':
                print(user.unsubscribe(command[1]))
            elif command[0] == 'log':
                user = log_out()
            elif command[0] == 'change':
                user.change_password()



