# 1 task

number = input()
n = len(number)
summa = 1
end = 0
bef = 0
for i in range(n):
    summa = summa * 2
    end += summa
    if i == n-2:
        bef = end

for o in number:
    a = end - bef
    if o == '4':
        end -= a*0.5
    elif o == '7':
        bef += a*0.5

print(round(end))