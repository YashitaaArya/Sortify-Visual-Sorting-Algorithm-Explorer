from tkinter import Canvas

canvas_width = 800
canvas_height = 400

def draw_data(canvas: Canvas, data, color_array):
    canvas.delete("all")
    n = len(data)
    if n == 0:
        return

    bar_width = max(15, canvas_width // n)
    spacing = 2

    for i, val in enumerate(data):
        x0 = i * (bar_width + spacing)
        y0 = canvas_height - val
        x1 = x0 + bar_width
        y1 = canvas_height

        # Draw bar
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])

        # Draw centered value
        text_x = (x0 + x1) / 2
        canvas.create_text(text_x, y0 - 10, text=str(val), anchor='s', font=("Helvetica", 10, "bold"))

    canvas.update_idletasks()
