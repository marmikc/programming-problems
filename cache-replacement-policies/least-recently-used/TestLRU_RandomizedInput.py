"""Test the LRU implementation with randomized cache calls"""

import random
import LRU_Cache as LRU

MEMORY = {
    "Apple": 2,
    "Grape": 5,
    "Pea": 1,
    "Mango": 6,
    "Kiwi": 4,
    "Starfruit": 3,
    "Peach": 4,
    "Fish": 0,
    "Potato": 1,
    "Orange": 5
}

MEMORY_SIZE = len(MEMORY)
NUM_CACHE_CALLS = 1000
CACHE_SIZE = 5
VERBOSE = False


def main():
    cache = LRU.LRU_Cache(MEMORY, CACHE_SIZE)

    memory_as_list = process_memory_into_list(MEMORY)

    previous_calls = []

    error = False

    for count in range(0, NUM_CACHE_CALLS):
        random_key_index = random.randint(0, MEMORY_SIZE - 1)
        random_key = memory_as_list[random_key_index][0]

        cache.get(random_key)
        previous_calls.append(memory_as_list[random_key_index])

        cache_state = cache.get_cache_as_list()
        correct_cache = build_correct_cache_state(previous_calls)

        if cache_state != correct_cache:
            print("ERROR")
            error = True
        if VERBOSE == True or cache_state != correct_cache:
            print("Command: get(", random_key, ")")
            print("Correct State:  ", correct_cache)
            print("Returned State: ", cache_state)

    if not error:
        print("Passed all randomized tests!")
    else:
        print("Some tests failed!")


def build_correct_cache_state(previous_calls):
    """The correct cache state is the last CACHE_SIZE calls, no duplicates"""
    correct_cache = []
    count = 0
    while len(correct_cache) < CACHE_SIZE:
        index = len(previous_calls) - 1 - count
        if index < 0:
            break

        item = previous_calls[index]

        if item not in correct_cache:
            correct_cache.append(item)

        count += 1

    return correct_cache


def process_memory_into_list(memory):
    memory_as_list = []
    for key, value in memory.items():
        memory_as_list.append((key, value))

    return memory_as_list

if __name__ == "__main__":
    main()
