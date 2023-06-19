first = input()
second = input()
third = input()
ans = ""
for i in range(len(first)):
    if first[i] == second[i] == third[i]:
        ans += first[i]
print(ans)