import requests

class User:

    def __init__(self, fam="", nam="", log="", pas=""):
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.imya = self.__data["FirstName"] if not nam else nam
        self.familiya = self.__data["LastName"] if not fam else fam
        self.login = self.__data["Login"] if not log else log
        self.__parol = self.__data["Password"] if not pas else pas

    def log_in(self, l, p):
        if self.login == l and self.__parol == p:
            return True