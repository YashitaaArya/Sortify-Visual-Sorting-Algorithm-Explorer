# Sortify – The Visual Sorting Algorithm Explorer

Sortify is an interactive, GUI-based tool that visually demonstrates the step-by-step process of popular sorting algorithms. Built using Python and Tkinter, it is designed for students, educators, and developers to understand sorting logic through dynamic visual feedback.

## Features
- Graphical User Interface using Tkinter
- Visual representation of sorting algorithms:
  1. Bubble Sort
  2. Selection Sort
  3. Insertion Sort
- Adjustable sorting speeds: Fast, Medium, Slow
- Random array generation
- Real-time visualization with color-coded transitions:
  1. Blue – Unsorted bars
  2. Red – Bars being compared or swapped
  3. Green – Sorted bars

## Technologies Used: 
- Python 3
- Tkinter for GUI
- Object-Oriented Programming principles
- Modular design using multiple files for separation of concerns

## Project Structure
```bash
Sortify/
│
├── main.py              # Entry point of the application
├── algorithms.py        # Sorting algorithm implementations
├── controller.py        # Controls data flow and user actions
├── gui.py               # GUI layout and component setup
├── visualizer.py        # Drawing and animation logic
├── assets/              # Optional: screenshots, GIFs
└── README.md            # Project documentation
```

## How it Works?
1. Launch the application using **main.py**.
2. Select a sorting algorithm from the dropdown.
3. Choose a speed for the visualization.
4. Click "Generate Array" to create a new dataset.
5. Click "Sortify" to begin the sorting visualization.
   
Each step of the algorithm is animated in real-time, allowing users to observe how values are compared and swapped.

1. **Clone the repository:**

   ```bash
    git clone https://github.com/your-username/sortify.git
    cd sortify
   ```
2. **Run the application:**
   
   ```bash
   python main.cpp
   ```
   
## License
  This project is licensed under the MIT License.
  
---

## Author
 Yashitaa Arya
 CSE | NIT Hamirpur
