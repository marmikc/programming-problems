"""My solution to the Longest Path Problem as defined in the README."""
import util


class LongestPath():
    """Class to hold setup and solution to the problem"""

    def __init__(self, grid):
        """Initialize member variables"""
        # Coordinates of visited cells to path length to maxima
        self.cells = {}
        self.grid = grid
        self.longest_path

    def find_longest_path(self):
        """Finds the longest path of increasing integers"""
        for row_num in len(self.grid):
            for col_num in len(self.grid[0]):
                if cell in self.cells:
                    continue

                maxima = self.find_local_max(row_num, col_num)
                self.iterate_to_minima(maxima)

        return self.longest_path

    def iterate_to_minima(self, maxima_list):
        queue = util.Queue()
        for maxima in maxima_list:
            count = 0
            queue.push(maxima)

            while not queue.isEmpty():
                coord = queue.pop()

                current_value = self.grid[coord[0]][coord[1]]

                if coord in cells and cells[coord] >= count:
                    break
                else:
                    cells[coord] = count

                    if cells[coord] > self.longest_path:
                        self.longest_path = cells[coord]

                if coord[0] - 1 >= 0:
                    if self.grid[coord[0] - 1][coord[1]] < current_value:
                        queue.push((coord[0] - 1, coord[1]))

                if coord[0] + 1 < len(self.grid):
                    if self.grid[coord[0] + 1][coord[1]] < current_value:
                        queue.push((coord[0] + 1, coord[1]))

                if coord[1] - 1 >= 0:
                    if self.grid[coord[0]][coord[1] - 1] < current_value:
                        queue.push((coord[0], coord[1] - 1))

                if coord[1] + 1 < len(self.grid[0]):
                    if self.grid[coord[0]][coord[1] + 1] < current_value:
                        queue.push((coord[0], coord[1] + 1))

                count += 1

    def find_local_max(self, row_num, col_num):
        maxima_list = []

        queue = util.Queue()
        queue.push((row_num, col_num))

        while not queue.isEmpty():
            coord = queue.pop()
            current_value = self.grid[coord[0]][coord[1]]
            is_max = 0

            if coord[0] - 1 >= 0 and self.grid[coord[0] - 1][coord[1]] > current_value:
                queue.push((coord[0] - 1, coord[1]))
            else:
                is_max += 1

            if coord[0] + 1 < len(self.grid) and self.grid[coord[0] + 1][coord[1]] > current_value:
                queue.push((coord[0] + 1, coord[1]))
            else:
                is_max += 1

            if coord[1] - 1 >= 0 and self.grid[coord[0]][coord[1] - 1] > current_value:
                queue.push((coord[0], coord[1] - 1))
            else:
                is_max += 1

            if coord[1] + 1 < len(self.grid[0]) and self.grid[coord[0]][coord[1] + 1] > current_value:
                queue.push((coord[0], coord[1] + 1))
            else:
                is_max += 1

            if is_max == 4:
                maxima_list.append(coord)

        return maxima_list
