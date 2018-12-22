"""Binary Index Tree Class."""


class BinaryIndexTree():
    """Implementing Binary Index Tree"""

    def __init__(self, array):
        """Initialize the Tree with the input list"""
        # 1-indexed array
        self.array = [0] + array

        for index in range(1, len(self.array)):
            next_binary_index = index + (index & -index)
            if next_binary_index < len(self.array):
                self.array[next_binary_index] += self.array[index]

    def sum_to_index(self, index):
        """Finds the sums of all integers from 1,index inclusive"""
        index += 1
        total_sum = 0
        while index:
            total_sum += self.array[index]
            index -= index & -index

        return total_sum

    def sum_range(self, from_idx, to_idx):
        """Sum between ranges, both inclusive"""
        to_sum = sum_to_index(to_idx)
        from_sum = sum_to_index(from_sum - 1)

        return to_sum - from_sum

    def update_value(self, index, value):
        """Add the value to the array[index] element"""
        index += 1
        while index < len(self.array):
            self.array[index] += value
            index += index & -index
