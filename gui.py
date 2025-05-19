import tkinter as tk
from tkinter import ttk
from controller import generate_data, on_sort_click

def run_app():
    root = tk.Tk()
    root.title("Sortify - Sorting Visualizer")
    root.maxsize(900, 600)
    root.config(bg="white")

    # Variables
    selected_algo = tk.StringVar(value="Bubble Sort")
    speed = tk.StringVar(value="Medium")

    # UI Frame
    ui_frame = tk.Frame(root, width=900, height=200, bg="white")
    ui_frame.grid(row=0, column=0, padx=10, pady=5)

    # Dropdown for Algorithm
    tk.Label(ui_frame, text="Algorithm:", bg="white").grid(row=0, column=0, padx=5, pady=5)
    algo_menu = ttk.Combobox(ui_frame, textvariable=selected_algo, values=["Bubble Sort", "Selection Sort", "Insertion Sort"], state="readonly", width=15)
    algo_menu.grid(row=0, column=1, padx=5, pady=5)

    # Speed selection
    tk.Label(ui_frame, text="Speed:", bg="white").grid(row=0, column=2, padx=5, pady=5)
    speed_menu = ttk.Combobox(ui_frame, textvariable=speed, values=["Fast", "Medium", "Slow"], state="readonly", width=10)
    speed_menu.grid(row=0, column=3, padx=5, pady=5)

    # Buttons
    canvas = tk.Canvas(root, width=800, height=400, bg="white")
    canvas.grid(row=1, column=0, padx=10, pady=5)

    tk.Button(ui_frame, text="Generate", command=lambda: generate_data(canvas), bg="#28a745", fg="white", padx=10).grid(row=0, column=4, padx=5, pady=5)
    tk.Button(ui_frame, text="Start Sorting", command=lambda: on_sort_click(canvas, selected_algo.get(), speed.get()), bg="#007bff", fg="white", padx=10).grid(row=0, column=5, padx=5, pady=5)

    root.mainloop()
