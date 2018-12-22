"""Test with random numbers"""

import BinaryIndexTree
import NaiveSolution
import random
import sys

array_size = 3
max_elem = 10
test_iterations = 2
verbose = True


def main():
    # Basic command line parsing
    if len(sys.argv) > 2:
        print("Invalid command line arguments")
    elif len(sys.argv) == 2:
        # No error checking
        if sys.argv[1] == "-q":
            global verbose
            verbose = False

    for i in range(0, test_iterations):
        run_test()


def test_sum(BIT, naive):
    sum_idx = random.randint(0, array_size - 1)
    function_call = "Function call: Sum from index 0 to index " + str(sum_idx)

    naive_add = naive.sum_to_index(sum_idx)
    BIT_add = BIT.sum_to_index(sum_idx)

    return evaluate("BIT", naive_add,
                    "Naive", naive_add, function_call)


def test_update(BIT, naive):
    update_idx = random.randint(0, array_size - 1)
    update_value = random.randint(-max_elem, max_elem)
    function_call = "Function call: update index " + \
        str(update_idx) + " by adding " + str(update_value)

    naive.update_value(update_idx, update_value)
    BIT.update_value(update_idx, update_value)

    naive_idx_value = naive.sum_range(update_idx, update_idx)
    BIT_idx_value = BIT.sum_range(update_idx, update_idx)

    return evaluate("BIT", BIT_idx_value,
                    "Naive", naive_idx_value, function_call)


def evaluate(label1, value1, label2, value2, function_call):
    test_result = "TEST FAILED\n"
    result = False

    if value1 == value2:
        test_result = "TEST PASSED\n"
        result = True

    output = ""
    output += test_result + function_call

    if verbose:
        output += '\n' \
            + label1 + " " + str(value1) + '\n' \
            + label2 + " " + str(value2) \

    print(output)
    return result


def run_test():
    array = []
    for j in range(0, array_size):
        array.append(random.randint(1, max_elem))
    print("Array: ", array)

    BIT = BinaryIndexTree.BinaryIndexTree(array)
    naive = NaiveSolution.NaiveSolution(array)

    sum1_result = test_sum(BIT, naive)
    update_result = test_update(BIT, naive)
    sum2_result = test_sum(BIT, naive)

    all_tests_passed = sum1_result & sum2_result & update_result
    if all_tests_passed:
        print("Passed all tests this round")

    print('\n')
    return


if __name__ == "__main__":
    main()
