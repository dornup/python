from classiki import User

# Инициализация

u1 = User(fam="Дорн", nam="Мелания", log="dornup", pas="9876o")
u2 = User()

# Авторизация

users = [u1, u2]
l = input("Логин: ")
p = input("Пароль: ")
for u in users:
    if u.log_in(l, p) == True:
        print("Ты вошел в аккаунт")
        current_user = u
