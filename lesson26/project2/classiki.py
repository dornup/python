import requests
from random import randint

class User:

    def __init__(self, fam="", nam="", log="", pas=""):
        self.__lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.imya = self.__data["FirstName"] if not nam else nam
        self.familiya = self.__data["LastName"] if not fam else fam
        self.login = self.__data["Login"] if not log else log
        self.__parol = self.__data["Password"] if not pas else pas
        self.posts = [self.__lorem[randint(0, 35):randint(36, 70)]]

    def log_in(self, l, p):
        if self.login == l and self.__parol == p:
            return True

# x = "" # False
# x = " " # True
# if x:
#     print(y)