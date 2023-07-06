# бинарный поиск

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low < high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(lst, 6))
