"""Analyse performance of both solutions"""

import NaiveSolution as NS
import RandomWeightedShuffle as RWS

NUM_ITERATIONS = 100000


def main():
    testcase1 = [
        ("Apple", 2),
        ("Grape", 1),
        ("Pea", 1),
    ]

    print("Testcase: ", testcase1)

    naive = NS.WeightedShuffler(testcase1)
    # print(naive.shuffle())

    rws = RWS.WeightedShuffler(testcase1)
    # print(rws.shuffle())

    print("Performing analysis on NAIVE SOLUTION")
    perform_frequency_analysis(naive)

    print("")

    print("Performing analysis on BINARY TREE SOLUTION")
    perform_frequency_analysis(rws)


def perform_frequency_analysis(shuffler):
    list_permutation_counts = {}
    for count in range(0, NUM_ITERATIONS):
        shuffled = shuffler.shuffle()

        preceeding_items = []
        for item in shuffled:
            if tuple(preceeding_items) not in list_permutation_counts:
                list_permutation_counts[tuple(preceeding_items)] = 0
            else:
                list_permutation_counts[tuple(preceeding_items)] += 1

            preceeding_items.append(item)

    for key in list_permutation_counts:
        # Probabilty of appearance
        if key == ():
            continue

        prob = list_permutation_counts[key] / list_permutation_counts[key[:-1]]
        print("Given: ", key[:-1], " | ", key[-1], " appears with prob ", prob)

if __name__ == "__main__":
    main()
