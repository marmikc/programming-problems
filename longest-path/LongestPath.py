"""My solution to the Longest Path Problem as defined in the README."""


class Queue:
    """Stores nodes to traverse"""

    def __init__(self):
        self.queue = []

    def push(self, item):
        """Push item into the front of the queue"""
        self.queue.insert(0, item)

    def pop(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0


class LongestPath():
    """Class to hold setup and solution to the problem"""

    def __init__(self, grid):
        """Initialize member variables"""
        # Coordinates of visited cells to path length to maxima
        self.cells = {}
        self.grid = grid
        self.longest_path = 0
        self.find_longest_path()

    def find_longest_path(self):
        """Finds the longest path of increasing integers"""
        for row_num in range(0, len(self.grid)):
            for col_num in range(0, len(self.grid[0])):
                if (row_num, col_num) in self.cells:
                    continue

                maxima = self.find_local_max(row_num, col_num)
                self.iterate_to_minima(maxima)

        return self.longest_path

    def iterate_to_minima(self, maxima_list):
        """Iterate to all minima from the list of maxima"""
        queue = Queue()
        for maxima in maxima_list:
            count = 0
            queue.push((maxima[0], maxima[1], 0))

            while not queue.is_empty():
                top_element = queue.pop()
                count = top_element[2]
                coord = (top_element[0], top_element[1])

                current_value = self.grid[coord[0]][coord[1]]

                if coord in self.cells and self.cells[coord] >= count:
                    continue
                else:
                    self.cells[coord] = count

                    if self.cells[coord] > self.longest_path:
                        self.longest_path = self.cells[coord]

                count += 1

                if coord[0] - 1 >= 0:
                    if self.grid[coord[0] - 1][coord[1]] < current_value:
                        queue.push((coord[0] - 1, coord[1], count))

                if coord[0] + 1 < len(self.grid):
                    if self.grid[coord[0] + 1][coord[1]] < current_value:
                        queue.push((coord[0] + 1, coord[1], count))

                if coord[1] - 1 >= 0:
                    if self.grid[coord[0]][coord[1] - 1] < current_value:
                        queue.push((coord[0], coord[1] - 1, count))

                if coord[1] + 1 < len(self.grid[0]):
                    if self.grid[coord[0]][coord[1] + 1] < current_value:
                        queue.push((coord[0], coord[1] + 1, count))

    def find_local_max(self, row_num, col_num):
        """Iterate to all maxima from the given cell"""
        maxima_list = []

        queue = Queue()
        queue.push((row_num, col_num))

        while not queue.is_empty():
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
