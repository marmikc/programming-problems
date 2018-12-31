# Find the size of the longest sequence of increasing numbers in a grid of numbers

Source: Problem posed to me in a programming interview

## Problem Description:

Given a grid of numbers, find the size of the longest sequence of strictly increasing numbers. The sequence allows only for numbers that are directly adjacent to each other (in other words, up, down, left or right).

## Thought process 

Any cell on the grid is part of a path, even if it is the only cell in a path. Within the entire grid, there are many maxima, and minima. 

```
1
2
3
4 3 2 1 0
2
1
```

Any of the above numbers is part of a path from a low number, to the maxima of 4.

So, if one were to pick any cell and then iterate to (by following increasing adjacent cells) any maxima, the program can work backwards to all of the minima. 

The path cost of a maxima to itself is 0, from an adjacent cell (that is strictly lower) is 1, and so on until the minima. This information can be put in a dictionary to record the length of a path to its furthest maxima. 

When iterating to the minima, if a cell has already been visited, and if the path from the current maxima is bigger than the size in the dictionary, then that cell should be overwritten along with all the others all the way to the minima.

This way, as all the paths from the maxima to the minima are explored, the longest will be stored.