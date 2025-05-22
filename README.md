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

### CLI Version (C++)
- Binary Search to locate elements
- Delete element if found (maintains sorted order)
- Insert element if not found (inserts at correct sorted position)
- User-driven input and loop to perform multiple operations

## How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YashitaaArya/SortedArrayManager_CLI.git
   cd SortedArrayManager_CLI
   ```
2. **Compile the code:**

   Make sure you have a C++ compiler installed.

   ```bash
   g++ -o BinarySearchApp main.cpp
   ```
3. **Run the executable:**
   ```bash
   ./BinarySearchApp      # On Linux/macOS
    BinarySearchApp.exe    # On Windows
   ```
4. **Follow on-screen instructions to search, insert, or delete elements.**

## Code Structure
    main.cpp : Contains the main program logic.
    Functions:
    - binarySearch() : Performs binary search on the array.
    - insert() : Inserts an element into the sorted array.
    - deleteElement() : Deletes an element from the array.

## Example
```bash
Enter the size of array: 5
Enter the elements:
1 3 5 7 9
Enter the element to be searched: 5
Element found at 3 position.
Do you wish to delete the same element? (y/n)
y
Successfully deleted!
1 3 7 9
Continue the search? (yes/no)
no
```

## 🖼️ GUI (Python Tkinter)
Make sure Python is installed (version 3.6+ recommended).
```bash
python sorted_array_manager_gui.py
```
## 📸 Screenshot (for GUI)

![GUI Screenshot](Images/GUI.png)

![CLI Screenshot](Images/CLI.png)

## 📚 Technologies Used
- C++ (CLI)
- Python 3.x (GUI)
- Tkinter for graphical interface
- Git & GitHub for version control

## Requirements
- C++ compiler (g++, clang++, or Visual Studio)
- Basic command-line environment
- Python's Tkinter

## License
  This project is licensed under the MIT License.
  
---

## Author
 Yashitaa Arya
