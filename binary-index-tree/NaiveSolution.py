"""Naive solution class."""


class NaiveSolution():
    """Naive solution for the Binary Index Tree Problem"""

    def __init__(self, array):
        self.array = array

    def sum_to_index(self, index):
        total_sum = 0
        for i in range(0, index + 1):
            total_sum += self.array[i]

        return total_sum

    def sum_range(from_idx, to_idx):
        total_sum = 0
        for i in range(from_idx, to_idx + 1):
            total_sum += self.array[i]

        return total_sum

    def update(self, index, value):
        self.array[index] = value
