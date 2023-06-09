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