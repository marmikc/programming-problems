"""My implementation of an LRU cache"""


class _Node:

    def __init__(self, node_key=None, node_value=None, next_node=None, previous_node=None):
        self.key = node_key
        self.value = node_value
        self.next = next_node
        self.previous = previous_node


class LRU_Cache:

    def __init__(self, memory, max_size, verbose=False):
        self.verbose = verbose
        self.memory = memory

        self.node_dict = {}
        self.head_node = None
        self.tail_node = None
        self.size_limit = max_size
        self.size = 0

    def get(self, key):
        if self.verbose:
            print("Command: get(", key, ")")

        # Cache hit
        if key in self.node_dict:
            self.__update_queue(key)
            if self.verbose:
                print("Cache hit on: ", (key, self.node_dict[key].value))
                self.print_cache()
            return (key, self.node_dict[key].value)

        # Cache miss
        value = self.memory[key]
        self.__insert(key, value)

        if self.verbose:
            print("Cache miss on: ", (key, value))
            self.print_cache()

        return (key, value)

    def print_cache(self):
        current_node = self.head_node
        output = ""
        while current_node != None:
            output += str((current_node.key, current_node.value))
            output += " -> "
            current_node = current_node.next

        print(output, "\n")

    def get_cache_as_list(self):
        current_node = self.head_node
        cache_as_list = []
        while current_node != None:
            cache_as_list.append((current_node.key, current_node.value))
            current_node = current_node.next

        return cache_as_list

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
            self.node_dict.pop(self.tail_node.key, None)

            second_last = self.tail_node.previous
            second_last.next = None

            new_node.next = self.head_node
            self.head_node.previous = new_node

            self.head_node = new_node
            self.tail_node = second_last
            # LRU node should be deleted by garbage collection

    def __update_queue(self, key):
        to_update = self.node_dict[key]

        if to_update != self.head_node:
            old_next = to_update.next
            old_previous = to_update.previous

            if to_update == self.tail_node:
                self.tail_node = old_previous

            # Remove node from old position
            old_previous.next = old_next
            if old_next != None:
                old_next.previous = old_previous

            self.head_node.previous = to_update
            to_update.next = self.head_node

            self.head_node = to_update
