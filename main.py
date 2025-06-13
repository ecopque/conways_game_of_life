# conways_game_of_life:

import random

WIDTH = 60 # column
HEIGHT = 20 # lines

# Random matrix creation:
next_cells = []
for i1 in WIDTH:
    column = 0
    for i2 in HEIGHT:
        if (random.randint(0, 1) == 0):
            column.append("#")
        else:
            column.append(" ")
    next_cells.append(column)




