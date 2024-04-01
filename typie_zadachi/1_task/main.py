f = open('input.txt')
w = open('output.txt', 'w')
l = [int(i) for i in f.read().split()]
w.write(str(sum(l)))
