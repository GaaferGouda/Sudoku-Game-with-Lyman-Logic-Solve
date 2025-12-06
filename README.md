# Sudoku Game with Lyman Logic Solver (Python)

This project provides a complete Sudoku game implemented in Python. It supports:

- Playing Sudoku manually in the terminal.
- Solving puzzles using a Lyman-style logical elimination algorithm.
- Automatically solving any remaining cells using a backtracking solver.
- Displaying the board in a clear, readable format.

The code is simple, clean, and fully self-contained.

---

## Features

### 1. Interactive Console Gameplay
You can enter moves using the following format:

```
row col num
```

Example:

```
1 3 8
```

Additional commands:

- `solve` – Solves the puzzle using logic and backtracking.
- `quit` – Exits the game.

---

### 2. Lyman-Style Logical Solver
The logical solver performs candidate elimination.  
If a cell has only one possible number, it automatically fills it.  
This process repeats until no more logical moves can be made.

---

### 3. Backtracking Solver
If the logical solver cannot fully solve the puzzle, the backtracking solver completes the remaining cells. This guarantees that any valid Sudoku puzzle can be solved.

---

## How to Run

1. Install Python on your system.
2. Save the script as `sudoku_game.py`.
3. Run the script using:

```
python sudoku_game.py
```

---

## Example Puzzle
A default Sudoku puzzle is included in the script.  
You can replace it with your own by modifying the `puzzle` list at the bottom of the file.

---

## Project Structure

```
sudoku_game.py      # Main game and solvers
README.md           # Documentation
```

---

## License
This project is free to use and modify.  
Credit is appreciated but not required.

---

## Author
This project was developed to demonstrate Sudoku solving logic in Python in a clear and educational way.
