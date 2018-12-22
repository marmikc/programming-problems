class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def nth_last_node(self, n):
        """Return value of nth last node."""
        """Zero indexing from last, i.e. 0th last is the last node."""
        if n < 0:
            return None

        ptr_behind = self
        ptr_ahead = self

        ptr_difference = -1

        while ptr_ahead != None:
            ptr_ahead = ptr_ahead.next

            if ptr_difference < n:
                ptr_difference += 1
            else:
                ptr_behind = ptr_behind.next

        if ptr_difference == n:
            return ptr_behind.value
        else:
            return None
