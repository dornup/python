# сортировка выбором

def find_smallest(arr):
    smallest = arr[0]
    smallest_ind = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_ind = i
    return smallest_ind


def sorting(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


# это необязательно, просто я добавила генерацию списка пользователем


x = int(input("Сколько чисел в списке: "))
lst = [int(input("Введите число: ")) for _ in range(x)]

print("Несортированный список:", lst)
print("Сортированный список:", sorting(lst))
