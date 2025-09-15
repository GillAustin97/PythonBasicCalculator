🧮 Python Calculator
A simple, beginner-friendly calculator built in Python.
This project demonstrates modular programming by splitting each operation (addition, subtraction, multiplication, division) into separate files and then importing them into the main program.


✨ Features

Four basic math operations:
  ➕ Addition
  ➖ Subtraction
  ✖️ Multiplication
  ➗ Division (with error handling for divide by zero)

Uses f-strings for clean, formatted output
Organized with separate Python files for each function
Beginner-friendly structure to learn about functions, imports, and program entry points (if __name__ == "__main__":)


📂 Project Structure

pythonCalculator/
│
├── addition.py        # defines add(a, b)
├── subtraction.py     # defines subtract(a, b)
├── multiplication.py  # defines multiply(a, b)
├── division.py        # defines divide(a, b)
└── pythonCalculatorMain.py   # main program (user interface)

🐍 Requirements

Python 3.10 or newer (tested on Python 3.13)
Works on Windows, macOS, and Linux

⚙️ Install Python

Go to the official download page: python.org/downloads
Download the latest version for your operating system.

On Windows: check the box that says "Add Python to PATH" during installation.
On macOS/Linux: Python 3 usually comes pre-installed, but you can update if needed.

Verify installation by running in your terminal:

python --version

or (on some systems):

python3 --version

▶️ How to Run

Clone or download this repository.
Open a terminal and navigate into the project folder:

cd pythonCalculator

Run the program:

python pythonCalculatorMain.py








