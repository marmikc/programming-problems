import BinaryIndexTree
import NaiveSolution
import random
import sys

# Arrays of Size 4
for i in range(0, 2):
    array = []
    arraySize = 30
    for j in range(0, arraySize):
        array.append(random.randint(1, 10))

    print("Array: ", array)

    BIT = BinaryIndexTree.BinaryIndexTree(array)
    naive = NaiveSolution.NaiveSolution(array)

    sum_idx = random.randint(0, arraySize - 1)
    print("Function call: sum_to(" + str(sum_idx) + ")")

    naive_add = naive.sum_to_index(sum_idx)
    BIT_add = BIT.sum_to_index(sum_idx)

    if naive_add != BIT_add:
        print("Inconsistent answers")
        print("Naive Result: ", naive_add)
        print("BIT Result: ", BIT_add)
    else:
        print("Consistent answers! ", BIT_add)
