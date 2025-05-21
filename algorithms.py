# algorithms.py

def bubble_sort(data, draw_callback, speed_ms, root):
    n = len(data)
    
    def sort_step(i, j):
        if i < n:
            if j < n - i - 1:
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                colors = ['#e74c3c' if x == j or x == j + 1 else '#3498db' for x in range(n)]
                draw_callback(data, colors)
                root.after(speed_ms, sort_step, i, j + 1)
            else:
                root.after(speed_ms, sort_step, i + 1, 0)
        else:
            draw_callback(data, ['#2ecc71'] * n)  # Sorted color
    
    sort_step(0, 0)

def selection_sort(data, draw_callback, speed_ms, root):
    n = len(data)
    
    def sort_step(i, j, min_index):
        if i < n - 1:
            if j < n:
                if data[j] < data[min_index]:
                    min_index = j
                colors = ['#e74c3c' if x == min_index or x == j else '#3498db' for x in range(n)]
                draw_callback(data, colors)
                root.after(speed_ms, sort_step, i, j + 1, min_index)
            else:
                data[i], data[min_index] = data[min_index], data[i]
                root.after(speed_ms, sort_step, i + 1, i + 2, i + 1)
        else:
            draw_callback(data, ['#2ecc71'] * n)  # Sorted color
    
    sort_step(0, 1, 0)

def insertion_sort(data, draw_callback, speed_ms, root):
    n = len(data)
    
    def sort_step(i, j, key):
        if i < n:
            if j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                colors = ['#e74c3c' if x == j or x == j + 1 else '#3498db' for x in range(n)]
                draw_callback(data, colors)
                root.after(speed_ms, sort_step, i, j - 1, key)
            else:
                data[j + 1] = key
                i += 1
                if i < n:
                    key = data[i]
                    j = i - 1
                    colors = ['#e74c3c' if x == i else '#3498db' for x in range(n)]
                    draw_callback(data, colors)
                    root.after(speed_ms, sort_step, i, j, key)
                else:
                    draw_callback(data, ['#2ecc71'] * n)
        else:
            draw_callback(data, ['#2ecc71'] * n)
    
    if n > 0:
        sort_step(1, 0, data[1])
    else:
        draw_callback(data, ['#2ecc71'] * n)
