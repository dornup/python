from random import choice
import playsound

class MusicBox:

    def __init__(self):
        self.__score = 0
        self.__variants = "dorn"
        self.__sequence = choice(self.__variants)

    def play(self):
        for letter in self.__sequence:
            playsound.playsound(f"zvuki/{letter}.mp3")

    def __next(self):
        __dlina = len(self.__sequence) + 1
        self.__sequence = ""
        for _ in range(__dlina):
            self.__sequence += choice(self.__variants)

    def cheeek(self, predpolojenie:str):
        if self.__sequence == predpolojenie.lower().strip():
            self.__score += 1
            self.__next()
            playsound.playsound("zvuki/correct.wav")
        else:
            self.__score -= 0.5
            playsound.playsound("zvuki/incorrect.wav")

    def get_score(self):
        return self.__score

