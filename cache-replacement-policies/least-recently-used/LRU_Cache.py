"""My implementation of an LRU cache"""


class _Node:

    def __init__(self, node_key=None, node_value=None, next_node=None, previous_node=None):
        self.key = node_key
        self.value = node_value
        self.next = next_node
        self.previous = previous_node


class LRU_Cache:

    def __init__(self, memory, max_size):
        self.memory = memory

        self.node_dict = {}
        self.head_node = None
        self.tail_node = None
        self.size_limit = max_size
        self.size = 0

    def get(self, key):
        # Cache hit
        if key in self.node_dict:
            self.__update_queue(key)
            return (key, self.node_dict[key])

        # Cache miss
        value = self.memory[key]

        self.__insert(key, value):

        return (key, value)

    def print(self):
        current_node = self.head_node
        output = ""
        while current_node != None:
            output += str((self.head_node.key, self.head_node.value))
            output += " -> "
            current_node = current_node.next

        print(output)

    def __insert(self, key, value):
        new_node = _Node(key, value)
        self.node_dict[key] = new_node

        if self.size == 0:
            self.head_node = new_node
            self.tail_node = self.head_node

            self.size += 1
        elif self.size > 0 and self.size < self.size_limit:
            new_node.next = self.head_node
            self.head_node.previous = new_node

            self.head_node = new_node
            self.size += 1
        else:
            second_last = self.tail_node.previous
            second_last.next = None

            new_node.next = self.head_node
            self.head_node.previous = new_node

            self.head_node = new_node
            # LRU node should be deleted by garbage collection

    def __update_queue(self, key):
        to_update = node_dict[key]

        to_update.next = old_next
        to_update.previous = old_previous

        # Remove node from old position
        old_previous.next = old_next
        old_next.previous = old_previous

        self.head_node.previous = to_update
        to_update.next = self.head_node

        self.head_node = to_update
