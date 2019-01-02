"""My solution to the Longest Path Problem as defined in the README."""


class _Queue:
    """Stores nodes to traverse"""

    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.insert(0, item)

    def pop(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0


def _iterate_to_minima(maxima_list, grid, cells, longest_path):
    """Iterate to all minima from the list of maxima"""
    queue = _Queue()
    for maxima in maxima_list:
        count = 0
        queue.push((maxima[0], maxima[1], 0))

        while not queue.is_empty():
            top_element = queue.pop()
            count = top_element[2]
            coord = (top_element[0], top_element[1])

            current_value = grid[coord[0]][coord[1]]

            if coord in cells and cells[coord] >= count:
                continue
            else:
                cells[coord] = count

                if cells[coord] > longest_path:
                    longest_path = cells[coord]

            count += 1

            if coord[0] - 1 >= 0:
                if grid[coord[0] - 1][coord[1]] < current_value:
                    queue.push((coord[0] - 1, coord[1], count))

            if coord[0] + 1 < len(grid):
                if grid[coord[0] + 1][coord[1]] < current_value:
                    queue.push((coord[0] + 1, coord[1], count))

            if coord[1] - 1 >= 0:
                if grid[coord[0]][coord[1] - 1] < current_value:
                    queue.push((coord[0], coord[1] - 1, count))

            if coord[1] + 1 < len(grid[0]):
                if grid[coord[0]][coord[1] + 1] < current_value:
                    queue.push((coord[0], coord[1] + 1, count))

        return cells, longest_path


def _find_local_max(row_num, col_num, grid):
    """Iterate to all maxima from the given cell"""
    maxima_list = []

    queue = _Queue()
    queue.push((row_num, col_num))

    while not queue.is_empty():
        coord = queue.pop()
        current_value = grid[coord[0]][coord[1]]
        is_max = 0

        if coord[0] - 1 >= 0 and grid[coord[0] - 1][coord[1]] > current_value:
            queue.push((coord[0] - 1, coord[1]))
        else:
            is_max += 1

        if coord[0] + 1 < len(grid) and grid[coord[0] + 1][coord[1]] > current_value:
            queue.push((coord[0] + 1, coord[1]))
        else:
            is_max += 1

        if coord[1] - 1 >= 0 and grid[coord[0]][coord[1] - 1] > current_value:
            queue.push((coord[0], coord[1] - 1))
        else:
            is_max += 1

        if coord[1] + 1 < len(grid[0]) and grid[coord[0]][coord[1] + 1] > current_value:
            queue.push((coord[0], coord[1] + 1))
        else:
            is_max += 1

        if is_max == 4:
            maxima_list.append(coord)

    return maxima_list


def find_longest_path(grid):
    """Find and return longest path"""
    cells = {}
    grid = grid
    longest_path = 0

    """Finds the longest path of increasing integers"""
    for row_num in range(0, len(grid)):
        for col_num in range(0, len(grid[0])):
            if (row_num, col_num) in cells:
                continue

            maxima = _find_local_max(row_num, col_num, grid)
            cells, longest_path = _iterate_to_minima(
                maxima, grid, cells, longest_path)

    return longest_path
