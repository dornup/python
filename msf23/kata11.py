slovarik = {0: -5,
        1: 3,
        2: 13,
        3: -2,
        4: -6,
        5: 7,
        7: 1,
        8: -4,
        9: 8}
k = []
for i in slovarik.keys():
    if slovarik[i] < 0:
        k.append(i)
for i in k:
    slovarik.pop(i)
print(slovarik)
