# Random Weighted Shuffle

Given a list of items with weights, randomly shuffle the list keeping into account the weights, at each round.

For example, with the weights [2, 1], the item with a weight of 2 would be chosen first 66% of the time, while the item with a weight of 1 would be chosen 33% of the time. 

Example 2, given a list with weights: [2, 1, 1]

Item with a weight of 2 is chosen 50% of the time.
	Given that the item with weight of 2 is chosen first, the two remaining items have a 50/50 chance of being chosen

Given that an item with weight of 1 is chosen first
	The item with a weight of 2 is then chosen second 66% of the time

**Each round of sampling influences the next.**

## Thought Process

Given there are several rounds of sampling, there needs to be at least n samples. For each sample we need to determine which item was chosen. 

A way to do this would be to create a list of sums, where each item is the sum of all numbers before it. Then, generate a random number from 1 to the sum of all weights. Finally, via a binary search, find the interval the corresponds to the generated number and choose that item.

This would make the overall runtime of this algorithm O(nlog(n)).

## Testing this algorithm

### Frequency Analysis

Given that this is a randomized algorithm, analysing the correctness of the algorithm requires a frequency analysis. Wherein, given a list of items with weights, different items should appear with different probabilities, depending on where in the list they appear and what items preceeded them.

For example, given the following testcase:

```python
	testcase1 = [
	        ("Apple", 2),
	        ("Grape", 1),
	        ("Pea", 1),
	]
```
Apple:
- Apple should appear first 50% of the time.
- Given that either Grape or Pea was sampled first, Apple should appear second 66% of the time.

Grape:
- Grape should appear first 25% of the time.
- Given that Apple was sampled first, Grape should appear second 50% of the time.
- Given that Pea was sampled first, Grape should appear second 33% of the time.

Pea:
- Pea has the same probabilites as Grape.

`FrequencyAnalysis.py` tests both algorithms over 100,000 iterations and returns how often each item appears in every scenario.

### Time Analysis

I tried my hand at timing the runtime of both solutions. `TimeAnalysis.py` generates a list with a specified number of elements, and then outputs the average time of both. The following is output from runs with different configurations.

```
$ python TimeAnalysis.py
List size:  5000
Number of Iterations:  5
Binary Tree    | Average Time:  0.09740982055664063
Naive Solution | Average Time:  1.9978332042694091

```

Cranking this up to a list with 100,000 items.

```
$ python TimeAnalysis.py
List size:  100000
Number of Iterations:  1
Binary Tree    | Average Time:  3.1257734298706055
Naive Solution | Average Time:  981.63298869133
```
