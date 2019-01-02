import LongestPath
import random

MAX_INT_SIZE = 9
MIN_INT_SIZE = 0
NUM_ROWS = 4
NUM_COLUMNS = 4

# Generate Grid
grid = []
for row in range(0, NUM_ROWS):
    row = []
    for column in range(0, NUM_COLUMNS):
        cell_value = random.randint(MIN_INT_SIZE, MAX_INT_SIZE)
        row.append(cell_value)

    grid.append(row)
    print(row)

print(LongestPath.find_longest_path(grid))
