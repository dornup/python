import easygui
def atbash(text):
    engin="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_eng = engin[::-1]
    rusya="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    reversed_rus = rusya[::-1]
    itog=""
    for letter in text:
        if letter not in rusya and letter not in engin:
            itog += letter
        elif letter in rusya:
            indecs =rusya.index(letter)
            bukva =reversed_rus[indecs]
            itog=itog+bukva
        else:
            indecs = engin.index(letter)
            bukva = reversed_eng[indecs]
            itog = itog + bukva
    easygui.msgbox(
        msg=itog
    )
#    print(itog)
shifr = easygui.enterbox(
    msg="Введи сообщение, буба").upper()
#shifr=input("Введи сообщение:").upper()
atbash(shifr)

