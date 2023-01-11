n = input(">>> N:")
if not n.isdigit():
    print("аааа можно число?")
    n = input(">>> N:")
n = int(n)
tree = {}
for _ in range(n):
    vvod = input(">>> ")
    svyaz = vvod.split(" ")
    if svyaz[1] not in tree:
        tree[svyaz[1]] = [svyaz[0]]
    else:
        tree[svyaz[1]] += [svyaz[0]]

print(tree)
        
