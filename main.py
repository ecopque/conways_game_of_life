# FILE: /main.py

# CONWAYs GAME OF LIFE:

import random, time, copy

WIDTH = 60 # column (x) / largura
HEIGHT = 20 # lines (y) / altura

# RANDOM MATRIX CREATION:
next_cells = []
for x in WIDTH:
    column = 0
    for y in HEIGHT:
        if (random.randint(0, 1) == 0):
            column.append("#")
        else:
            column.append(" ")
    next_cells.append(column)

# PRINT THE GRID TO THE SCREEN:
while True:
    print("\n\n\n\n\n\n")
    current_cells = copy.deepcopy(next_cells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end="")
        print()

    # NEXT GENERATION CALCULATION:
    for x in range(WIDTH):
        for y in range(HEIGHT):
        
        # DEFINES THE POSITIONS OF THE NEIGHBORS:
        # Take the neighbor on the left. If it is in the 1st column, go back to the last column.
        left_coord = (x - 1) % WIDTH
        # Take the neighbor on the right. If it is in the last column, it goes back to the first
        # column.
        right_coord = (x + 1) % WIDTH
        # Neighbor above. If it is on the 1st line, it goes back do the last line.
        above_coord = (y - 1) % HEIGHT
        # Neighbot below. If it is on the last line, it goes back to the first line.
        below_coord = (y + 1) % HEIGHT




