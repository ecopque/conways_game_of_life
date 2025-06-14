# conways_game_of_life:

import random, time, copy

WIDTH = 60 # column (x) / largura
HEIGHT = 20 # lines (y) / altura

# Random matrix creation:
next_cells = []
for x in WIDTH:
    column = 0
    for y in HEIGHT:
        if (random.randint(0, 1) == 0):
            column.append("#")
        else:
            column.append(" ")
    next_cells.append(column)

while True:
    print("\n\n\n\n")
    current_cells = copy.deepcopy(next_cells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end="")
        print()



