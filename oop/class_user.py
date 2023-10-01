from random import choice, randint
from string import ascii_letters, ascii_lowercase

users = []


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.following = []
        self.followers = []
        users.append(self)

    def change_password(self):
        password = input('Введите старый пароль: ')
        if self.password == password:
            new_password_1 = 0
            new_password_2 = 1
            while new_password_1 != new_password_2:
                new_password_1 = input('Введите новый пароль: ')
                new_password_2 = input('Повторите новый пароль: ')
                if new_password_1 != new_password_2:
                    print('Пароли не совпадают, попробуйте еще раз')
            self.password = new_password_1
            print('Вы успешно сменили пароль')
        else:
            print('Неверный пароль, попробуйте еще раз')

    def authorise(self, username: str, password: str) -> bool:
        if self.username == username and self.password == password:
            return True

    def subscribe(self, name: str) -> str:
        for i in users:
            if i.username == name:
                if self.following.count(i) == 0:
                    self.following.append(i)
                    i.followers.append(self)
                    return f'Вы подписались на {i.username}'
                else:
                    return 'Вы уже подписаны на этого пользователя'
        return 'Пользователь с таким именем не найден, попробуйте еще раз'

    def unsubscribe(self, name: str) -> str:
        for i in self.following:
            if i.username == name:
                self.following.remove(i)
                i.followers.remove(self)
                return f'вы отписались от {i.username}'
        return 'вы не подписаны на данного пользователя'


def make_people(x: int) -> None:
    for i in range(x):
        username = ''.join([choice([i for i in ascii_lowercase]) for _ in range(randint(4, 10))])
        password = ''.join([choice([i for i in ascii_letters] + [str(i) for i in range(10)]) for _ in range(randint(6, 12))])
        User(username, password)


u1 = User('smir-ant', "123")
u2 = User('max_dorn', "456")
u3 = User('dornarra', "789")
u4 = User('yulia_dorn', "101")
make_people(10)
