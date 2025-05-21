# gui.py
import tkinter as tk
from tkinter import ttk

def create_gui(root, on_algorithm_select, on_speed_select, on_generate_click, on_sort_click):
    root.title("Sortify - Sorting Algorithm Visualizer")
    root.maxsize(1000, 700)
    root.config(bg="#2c3e50")

    heading = tk.Label(
        root, text="SORTIFY", font=("Helvetica", 28, "bold"),
        bg="#2c3e50", fg="white", pady=10
    )
    heading.pack()

    container = tk.Frame(root, bg="#34495e", padx=20, pady=20)
    container.pack(pady=20)

    # Step 1: Algorithm selection
    algo_frame = tk.Frame(container, bg="#34495e")
    algo_frame.pack()
    algo_label = tk.Label(algo_frame, text="Choose Sorting Algorithm:", font=("Helvetica", 14), bg="#34495e", fg="white")
    algo_label.pack(side=tk.LEFT, padx=(0, 10))
    algo_menu = ttk.Combobox(algo_frame, values=["Bubble Sort", "Selection Sort", "Insertion Sort"], state="readonly")
    algo_menu.pack(side=tk.LEFT)
    algo_menu.bind("<<ComboboxSelected>>", lambda e: on_algorithm_select())

    # Step 2: Speed selection (initially hidden)
    speed_frame = tk.Frame(container, bg="#34495e")
    speed_label = tk.Label(speed_frame, text="Choose Speed:", font=("Helvetica", 14), bg="#34495e", fg="white")
    speed_label.pack(side=tk.LEFT, padx=(0, 10))
    speed_menu = ttk.Combobox(speed_frame, values=["Fast", "Medium", "Slow"], state="readonly")
    speed_menu.pack(side=tk.LEFT)
    speed_menu.bind("<<ComboboxSelected>>", lambda e: on_speed_select())

    # Step 3: Generate button (shown after speed selection)
    generate_btn = tk.Button(
        container, text="Generate Data", font=("Helvetica", 12, "bold"),
        bg="#1abc9c", fg="white", padx=10, pady=5,
        command=lambda: on_generate_click()
    )

    # Step 4: Sort button (enabled only after generate)
    sort_btn = tk.Button(
        container, text="SORTIFY", font=("Helvetica", 12, "bold"),
        bg="#e67e22", fg="white", padx=10, pady=5,
        command=lambda: on_sort_click()
    )
    sort_btn.config(state=tk.DISABLED)

    canvas = tk.Canvas(root, width=800, height=400, bg="white")
    canvas.pack(pady=20)
    canvas.pack_forget()  # Initially hidden

    # Provide access for controller to show/hide
    def show_speed():
        speed_frame.pack(pady=10)

    def show_generate():
        generate_btn.pack(pady=10)

    def show_canvas():
        canvas.pack()

    def enable_sort():
        sort_btn.config(state=tk.NORMAL)
        sort_btn.pack(pady=10)

    return {
        "algo_menu": algo_menu,
        "speed_menu": speed_menu,
        "show_speed": show_speed,
        "show_generate": show_generate,
        "show_canvas": show_canvas,
        "enable_sort": enable_sort,
        "canvas": canvas,
    }
