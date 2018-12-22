import BinaryIndexTree
import NaiveSolution
import random
import sys

array_size = 4
max_elem = 10
test_iterations = 2
verbose = False


def main():
    # Basic command line parsing
    if len(sys.argv) > 2:
        print("Invalid command line arguments")
    elif len(sys.argv) == 2:
        verbose = (sys.argv[1] == "-v")

    for i in range(0, test_iterations):
        run_test()


def test_sum(BIT, naive):
    sum_idx = random.randint(0, array_size - 1)
    print("Function call: Sum from 0 to " + str(sum_idx))

    naive_add = naive.sum_to_index(sum_idx)
    BIT_add = BIT.sum_to_index(sum_idx)


def test_update(BIT, naive):
    update_idx = random.randint(0, array_size - 1)
    update_value = random.randint(-max_elem, max_elem)
    print("Function call: update " + str(update_idx) +
          " by adding " + str(update_value))

    naive.update_value(update_idx, update_value)
    BIT.update_value(update_idx, update_value)

    naive_idx_value = naive.sum_range(update_idx, update_idx)
    BIT_idx_value = BIT.sum_range(update_idx, update_idx)


def evaluate(pair1, pair2, function_call):
    label1, value1 = pair1
    label2, value2 = pair2

    if value1 != value2:
        print("INCONSISTENCY")
        print(label1, value1)
        print(label2, value2)


def run_test():
    array = []
    for j in range(0, array_size):
        array.append(random.randint(1, max_elem))

    print("Array: ", array)

    BIT = BinaryIndexTree.BinaryIndexTree(array)
    naive = NaiveSolution.NaiveSolution(array)

    test_sum(BIT, naive)

    test_update(BIT, naive)

    test_sum(BIT, naive)


if __name__ == "__main__":
    main()
