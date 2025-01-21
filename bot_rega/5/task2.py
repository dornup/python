n, m = map(int, input().split())
set_foo = {}
foo_trainer = {range(1, m + 1)}
for i in range(n):
    command = frozenset(map(int, input().split()))
    if set_foo.get(command) == None:
        set_foo[command] = False
    elif set_foo.get(command) == False:
        set_foo[command] = True



