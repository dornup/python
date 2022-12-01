alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
symbols = ['.', ',', ':', ';', '"', '«', '»']
phrasa = input("Введи фразу:")
rus_bukvi = 0
other = 0
for letter in phrasa:
    if letter in symbols:
        other += 1
    elif letter in alphabet:
        rus_bukvi += 1

print("русских букв:", rus_bukvi)


