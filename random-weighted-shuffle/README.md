# Random Weighted Shuffle

Given a list of items with weights, randomly shuffle the list keeping into account the weights, at each round.

For example, with the weights [2, 1], the item with a weight of 2 would be chosen first 66% of the time, while the item with a weight of 1 would be chosen 33% of the time. 

Example 2, given a list with weights: [2, 1, 1]

Item with a weight of 2 is chosen 50% of the time.
	Given that the item with weight of 2 is chosen first, the remaining two item have a 50/50 chance of being chosen

Given that an item with weight of 1 is chosen first
	The item with a weight of 2 is then chosen second 66% of the time

**Each round of sampling influences the next.**

## Thought Process

Given there are several rounds of sampling, there needs to be at least n samples. For each sample we need to determine which item was chosen. 

A way to do this would be to create a list of sums, where each item is the sum of all numbers before it. Then, generate a random number from 1 to the sum of all weights. Finally, via a binary search, find the interval the corresponds to the generated number and choose that item.
