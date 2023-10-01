import time

# input here

start = time.perf_counter()

# code here

a = int(input())
b = int(input())
for i in str(b):
    if int(i) >= a:
        print('НЕТ')
        quit()
print('ДА')

end = time.perf_counter()
print(f"time = {end - start:0.4f}")

# output here
