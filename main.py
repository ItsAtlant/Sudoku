import numpy as np
import matplotlib.pyplot as plt

def create_sudoku_grid():
    grid = np.zeros((9, 9), dtype=int)
    
    # Popola la griglia con numeri casuali
    numbers = np.arange(1, 10)
    np.random.shuffle(numbers)
    
    for i in range(3):
        grid[i] = np.roll(numbers, i)
    
    for i in range(3, 6):
        grid[i] = np.roll(numbers, i-1)
    
    for i in range(6, 9):
        grid[i] = np.roll(numbers, i-2)
    
    # Rimuovi alcuni numeri per creare spazi vuoti
    empty_indices = np.random.choice(np.arange(81), size=50, replace=False)
    grid = grid.flatten()
    grid[empty_indices] = 0
    grid = grid.reshape((9, 9))
    
    return grid

def display_sudoku_grid(grid):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(10))
    ax.set_yticks(np.arange(10))
    ax.grid(color='black', linewidth=1.5)
    ax.set_axisbelow(True)
    for i in range(9):
        for j in range(9):
            if grid[i, j] != 0:
                ax.text(j+0.5, i+0.5, str(grid[i, j]), fontsize=16, ha='center', va='center')
    plt.show()
    
def is_valid_move(grid, row, col, value):
    # Controlla la riga
    if value in grid[row, :]:
        return False
    
    # Controlla la colonna
    if value in grid[:, col]:
        return False
    
    # Controlla il quadrante 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    if value in grid[start_row:start_row+3, start_col:start_col+3]:
        return False
    
    return True

# Esempio di utilizzo
sudoku_grid = create_sudoku_grid()
display_sudoku_grid(sudoku_grid)

# Esempio di controllo dell'inserimento di un valore
row = 0
col = 0
value = 5

if is_valid_move(sudoku_grid, row, col, value):
    sudoku_grid[row, col] = value
else:
    print("Mossa non valida!")