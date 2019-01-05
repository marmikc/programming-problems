"""My implementation of the clock page replacement algorithm"""


class _Memory_Element:

    def __init__(self, index):
        self.referenced = False
        self.value = None
        self.page = None
        self.index = index


class Clock:

    def __init__(self, all_pages, max_size, verbose=False):
        self.all_pages = all_pages
        self.max_size = max_size
        self.verbose = verbose

        self.page_dict = {}
        self.clock_hand = 0
        self.memory = [_Memory_Element(count) for count in range(0, max_size)]

    def print_clock(self):
        output = "-> "
        count = 0
        for item in self.memory:
            if self.clock_hand == count:
                output += "**"

            output += str(((item.page, item.value), item.referenced))

            if self.clock_hand == count:
                output += "**"

            output += " -> "
            count += 1

        return output

    def get(self, page):
        if self.verbose:
            print("Command: get(", page, ")")

        # No fault
        if page in self.page_dict:
            value = self.page_dict[page].value

            self.page_dict[page].referenced = True
        else:
            # Page fault
            value = self.all_pages[page]

            if self.verbose:
                print("Page fault on: ", (page, value))

            found_unreferenced_page = False
            while not found_unreferenced_page:
                if self.memory[self.clock_hand].referenced == False:
                    if self.verbose:
                        if self.memory[self.clock_hand].page != None:
                            evicted_page = self.memory[self.clock_hand].page
                            evicted_value = self.memory[self.clock_hand].value
                            self.page_dict.pop(evicted_page, None)
                            print("Evicting: ", (evicted_page, evicted_value))

                    self.memory[self.clock_hand].page = page
                    self.memory[self.clock_hand].value = value
                    self.memory[self.clock_hand].referenced = True
                    self.page_dict[page] = self.memory[self.clock_hand]

                    found_unreferenced_page = True
                else:
                    self.memory[self.clock_hand].referenced = False

                # Increment clock_hand
                self.clock_hand = (self.clock_hand + 1) % (self.max_size)

        if self.verbose:
            print("Found: ", (page, value))
            print("Clock State: ", self.print_clock(), "\n")

        return (page, value)
