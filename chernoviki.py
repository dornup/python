import random
s = set()
s2 = set()

while True:
    lst = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
    element = ""
    for i in range(random.randint(1, len(lst))):
        a = random.choice(lst)
        element += str(a)
        lst.remove(a)
    if element in s:
        s2.add(element)
    else:
        s.add(element)
        print(s)
    if s==s2:
        break

print(s)

