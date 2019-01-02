"""Analyse performance of both solutions"""

import NaiveSolution as NS
import RandomWeightedShuffle as RWS

NUM_ITERATIONS = 10000

testcase1 = [
    ("Apple", 2),
    ("Grape", 1),
    ("Pea", 1),
]

naive = NS.WeightedShuffler(testcase1)
print(naive.shuffle())

solution = RWS.WeightedShuffler(testcase1)
print(solution.shuffle())
