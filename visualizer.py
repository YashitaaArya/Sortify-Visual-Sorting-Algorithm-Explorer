# visualizer.py

def draw_data(canvas, data, color_array):
    canvas.delete("all")
    canvas_width = int(canvas['width'])
    canvas_height = int(canvas['height'])
    
    bar_width = max(15, canvas_width // len(data))
    spacing = 4
    offset = 30

    for i, val in enumerate(data):
        x0 = i * (bar_width + spacing) + spacing
        y0 = canvas_height - val
        x1 = x0 + bar_width
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i], outline="")
        canvas.create_text((x0 + x1) / 2, y0 - 12, text=str(val),
                           fill="black", font=("Helvetica", 10, "bold"),
                           anchor='s', justify='center')

    canvas.update_idletasks()
