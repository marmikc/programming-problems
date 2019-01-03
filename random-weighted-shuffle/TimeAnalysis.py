"""Analyse performance of both solutions"""

import random
import time
import NaiveSolution as NS
import RandomWeightedShuffle as RWS

LIST_SIZE = 5000
MAX_WEIGHT = 1000
NUM_ITERATIONS = 5


def main():
    generated_test_case = generate_random_list()

    # print(generated_test_case)
    print("List size: ", LIST_SIZE)
    print("Number of Iterations: ", NUM_ITERATIONS)

    naive = NS.WeightedShuffler(generated_test_case)
    rws = RWS.WeightedShuffler(generated_test_case)

    average_rws_time = perform_timing_analysis(rws)

    print("Binary Tree    | Average Time: ", average_rws_time)

    average_naive_time = perform_timing_analysis(naive)

    print("Naive Solution | Average Time: ", average_naive_time)


def perform_timing_analysis(shuffler):
    total_time = 0
    for iteration in range(0, NUM_ITERATIONS):
        start = time.time()

        shuffler.shuffle()

        end = time.time()
        total_time += (end - start)

    return(total_time / NUM_ITERATIONS)


def generate_random_list():
    generated_list = []
    for count in range(0, LIST_SIZE):
        key = count
        value = random.randint(1, MAX_WEIGHT)

        item = (key, value)

        generated_list.append(item)

    return generated_list

if __name__ == "__main__":
    main()
