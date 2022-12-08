# a = int(input("Число:"))
# b = int(input("Число:"))
# lst = []
#
# for mega_anton in range(a + 1, b):
#     lst.append(mega_anton ** 2)
#
# print(lst)

lst = [-5, 14, 2, -8, 1]
mini = min(lst)
maxi = max(lst)

lst[lst.index(mini)], lst[lst.index(maxi)] = lst[lst.index(maxi)], lst[lst.index(mini)]

print(lst)


