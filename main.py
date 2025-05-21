# main.py
import tkinter as tk
from tkinter import ttk
from controller import generate_data, on_sort_click

# Initialize main window
root = tk.Tk()
root.title("Sortify - Sorting Visualizer")
root.geometry("900x600")
root.config(bg="#f0f0f0")

selected_algorithm = tk.StringVar()
selected_speed = tk.StringVar()

# Title
title = tk.Label(root, text="Sortify - Sorting Algorithm Visualizer", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#2c3e50")
title.pack(pady=20)

# Algorithm Selection
algo_frame = tk.Frame(root, bg="#f0f0f0")
algo_label = tk.Label(algo_frame, text="Choose Sorting Algorithm:", font=("Helvetica", 14), bg="#f0f0f0")
algo_label.pack(side=tk.LEFT, padx=10)
algo_menu = ttk.Combobox(algo_frame, textvariable=selected_algorithm, values=["Bubble Sort", "Selection Sort", "Insertion Sort"], state="readonly", width=20)
algo_menu.pack(side=tk.LEFT, padx=10)
algo_frame.pack(pady=10)

# Speed Selection (Initially hidden)
speed_frame = tk.Frame(root, bg="#f0f0f0")
speed_label = tk.Label(speed_frame, text="Select Speed:", font=("Helvetica", 14), bg="#f0f0f0")
speed_label.pack(side=tk.LEFT, padx=10)
speed_menu = ttk.Combobox(speed_frame, textvariable=selected_speed, values=["Fast", "Medium", "Slow"], state="readonly", width=20)
speed_menu.pack(side=tk.LEFT, padx=10)

# Generate Button (Initially hidden)
generate_button = ttk.Button(root, text="Generate Array")

# Sort Button (Initially hidden)
sort_button = ttk.Button(root, text="Sortify")

# Canvas for Visualization
canvas = tk.Canvas(root, width=800, height=400, bg="white", bd=2, relief="groove")
canvas.pack(pady=20)

# Control Functions
def show_speed_selection():
    if selected_algorithm.get():
        speed_frame.pack(pady=10)
        generate_button.pack(pady=10)

def show_sort_button():
    sort_button.pack(pady=10)

def on_generate_click():
    if selected_speed.get():
        generate_data(canvas, show_sort_button)

def on_sort_click_handler():
    on_sort_click(canvas, selected_algorithm.get(), selected_speed.get(), root)


# Binding buttons
algo_menu.bind("<<ComboboxSelected>>", lambda e: show_speed_selection())
generate_button.config(command=on_generate_click)
sort_button.config(command=on_sort_click_handler)

# Start app
root.mainloop()
