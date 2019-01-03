"""Randomly shuffle or sample a set of items with weights."""
import random


class WeightedShuffler:

    def __init__(self, items):
        self.all_items = []
        self.total_weight = 0
        for item, weight in items:
            self.total_weight += weight
            self.all_items.append((item, weight))

    def shuffle(self):
        return self.sample_items(len(self.all_items))

    def sample_items(self, num_samples):
        """Return list of num_samples weighted samples"""
        weight_sum = self.total_weight
        item_list = self.all_items.copy()

        sample_list = []
        for i in range(0, num_samples):
            rand = -1
            if weight_sum != 1:
                rand = random.randint(1, weight_sum)
            else:
                rand = 1

            sample_sum = 0
            for j in range(len(item_list)):
                sample_sum += item_list[j][1]

                if rand <= sample_sum:
                    sample_list.append(item_list[j])
                    weight_sum -= item_list[j][1]
                    item_list[j] = (item_list[j][0], 0)
                    break

        return sample_list
