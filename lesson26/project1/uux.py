from main import MusicBox

pleer = MusicBox()

while True:
    pleer.play()
    guess = input("Что ты heard: ")
    if guess == "":
        break
    pleer.cheeek(guess)
print("Очков:", pleer.get_score())