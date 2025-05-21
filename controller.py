# controller.py
import random
import time
from tkinter import Canvas
from algorithms import bubble_sort, selection_sort, insertion_sort

array = []

canvas_width = 800
canvas_height = 400

speed_map = {
    "Fast": 0.001,
    "Medium": 0.1,
    "Slow": 0.3
}

def draw_data(canvas: Canvas, data, color_array):
    canvas.delete("all")
    bar_width = max(15, canvas_width // len(data))
    spacing = 4
    offset = 30
    for i, val in enumerate(data):
        x0 = i * (bar_width + spacing) + spacing
        y0 = canvas_height - val
        x1 = x0 + bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i], outline="")
        canvas.create_text((x0 + x1) / 2, y0 - 12, text=str(val), anchor='s', font=("Helvetica", 10, "bold"))
    canvas.update_idletasks()

def generate_data(canvas, show_sort_button_callback):
    global array
    array = [random.randint(10, 300) for _ in range(20)]
    draw_data(canvas, array, ["#3498db"] * len(array))
    show_sort_button_callback()

def on_sort_click(canvas, algorithm, speed, root):
    if not array:
        return

    speed_map_ms = {
        "Fast": 10,    # 10 ms delay
        "Medium": 100, # 100 ms delay
        "Slow": 300    # 300 ms delay
    }
    speed_ms = speed_map_ms.get(speed, 10)

    if algorithm == "Bubble Sort":
        bubble_sort(array, lambda d, c: draw_data(canvas, d, c), speed_ms, root)
    elif algorithm == "Selection Sort":
        selection_sort(array, lambda d, c: draw_data(canvas, d, c), speed_ms, root)
    elif algorithm == "Insertion Sort":
        insertion_sort(array, lambda d, c: draw_data(canvas, d, c), speed_ms, root)

# def on_sort_click(canvas, algorithm, speed):
#     if not array:
#         return
#     delay = lambda: time.sleep(speed_map[speed])
#     if algorithm == "Bubble Sort":
#         bubble_sort(array, lambda d, c: draw_data(canvas, d, c), delay)
#     elif algorithm == "Selection Sort":
#         selection_sort(array, lambda d, c: draw_data(canvas, d, c), delay)
#     elif algorithm == "Insertion Sort":
#         insertion_sort(array, lambda d, c: draw_data(canvas, d, c), delay)
