def bubble_sort(data, draw_func, delay_func):
    n = len(data)
    for i in range(n):
        flag = 0
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = 1
            draw_func(data, ["green" if x == j or x == j+1 else "blue" for x in range(n)])
            delay_func()
        if flag == 0:
            break

def selection_sort(data, draw_func, delay_func):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
            draw_func(data, ["yellow" if x == j or x == min_idx else "blue" for x in range(n)])
            delay_func()
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_func(data, ["green" if x == i or x == min_idx else "blue" for x in range(n)])
        delay_func()

def insertion_sort(data, draw_func, delay_func):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            draw_func(data, ["red" if x == j or x == i else "blue" for x in range(n)])
            delay_func()
        data[j + 1] = key
        draw_func(data, ["green" if x == j + 1 or x == i else "blue" for x in range(n)])
        delay_func()
