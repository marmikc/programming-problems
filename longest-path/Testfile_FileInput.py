"""Test longest path with input from a file"""
import LongestPath

# No path
test1 = [
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
]

# One path
test2 = [
    [9, 2, 3],
    [8, 1, 4],
    [7, 6, 5]
]

# One path
test3 = [
        [3, 2, 9],
        [4, 1, 8],
        [5, 6, 7]
]

# 2 merging paths
test4 = [
    [5, 9, 9],
    [3, 4, 5],
    [2, 9, 9]
]

# Same path lengths
test5 = [
    [2, 2, 2],
    [2, 9, 2],
    [2, 2, 2]
]

# One max, multiple minima
test6 = [
        [0, 0, 0, 9, 0, 0],
        [5, 6, 7, 8, 7, 6],
        [0, 0, 0, 7, 0, 0],
        [3, 4, 5, 6, 5, 4],
        [0, 0, 0, 5, 0, 0],
        [1, 2, 3, 4, 3, 2]
]

# One minima, multiple maxima
test7 = [
        [9, 9, 9, 1, 9, 9],
        [5, 4, 3, 2, 3, 4],
        [9, 9, 9, 3, 9, 9],
        [7, 6, 5, 4, 5, 6],
        [9, 9, 9, 5, 9, 9],
        [9, 8, 7, 6, 8, 9]
]

grid = test3
for row in grid:
    print(row)
print(LongestPath.LongestPath(grid).longest_path)
