import numpy as np
import matplotlib.pyplot as plt
import random

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


def suggerimento(sudoku_grid, row, col, value):

    numeri_suggeriti = []
    numeri_possibili = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Rimuovi i numeri già presenti nella stessa riga
    for num in sudoku_grid[row]:
        if num in numeri_possibili:
            numeri_possibili.remove(num)

    # Rimuovi i numeri già presenti nella stessa colonna
    for i in range(9):
        num = sudoku_grid[i][col]
        if num in numeri_possibili:
            numeri_possibili.remove(num)

    # Calcola la posizione iniziale della regione 3x3
    start_riga = (row // 3) * 3
    start_colonna = (col // 3) * 3

    # Rimuovi i numeri già presenti nella stessa regione 3x3
    for i in range(start_riga, start_riga + 3):
        for j in range(start_colonna, start_colonna + 3):
            num = sudoku_grid[i][j]
            if num in numeri_possibili:
                numeri_possibili.remove(num)

    # Scegli casualmente due numeri dalla lista dei numeri possibili
    numeri_suggeriti = random.sample(numeri_possibili, 2)
            
    print(f"Uhm, sembra che {value}, non sia il numero giusto!,\
            Perchè non provi con uno di questi: {numeri_suggeriti}?")

def check(sudoku_grid):

    # Controllo se tutte le celle sono state riempite
    num_nonzero = np.count_nonzero(sudoku_grid)
    if num_nonzero == 81:
        # Tutte le celle sono state riempite
        return True
    else:
        # Ci sono ancora celle vuote
        return False


while(check):
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
        suggerimento(sudoku_grid, row, col, value)