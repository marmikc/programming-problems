"""Randomly shuffle or sample a set of items with weights."""
import random


class _Node:

    def __init__(self, weight, item, right_weight, left_weight):
        self.weight = weight
        self.item = item
        self.right_weight = right_weight
        self.left_weight = left_weight
        self.sampled = False


class _BinaryTree:
    """Each node contains its weight and sum of all weights in nodes below"""

    def __init__(self, all_items):
        self.all_items = all_items
        self.num_items = len(all_items)
        self.tree = [None for _ in range(0, self.num_items)]

    def left_index(self, index):
        return (2 * index) + 1

    def right_index(self, index):
        return (2 * index) + 2

    def construct_tree(self, index=0):
        if index < self.num_items:
            item = self.all_items[index][0]
            weight = self.all_items[index][1]
            right_weight = self.construct_tree(self.right_index(index))
            left_index = self.construct_tree(self.left_index(index))

            self.tree[index] = _Node(weight, item, right_weight, left_weight)
            return weight + right_weight + left_weight
        else:
            return 0

    def sample_tree(value, index=0):
        node_weight = 0
        if self.tree[index].sampled:
            node_weight = 0
        else:
            node_weight = self.tree[index].weight

        right_weight = self.tree[index].right_weight
        left_weight = self.tree[index].left_weight

        sampled_node = -1
        sampled_weight = -1
        if value < node_weight + left_weight and value > left_weight:
            sampled_node = index
            sampled_weight = self.tree[sampled_node].weight
        elif value < node_weight + left_weight:
            sampled_node, sampled_weight = self.sample_tree(
                self.left_index(value, index))
        else:
            new_value = value - (node_weight + left_weight)
            sampled_node, sampled_weight = self.sample_tree(
                self.right_index(new_value, index))

        return (sampled_node, sampled_weight)

    def reset_tree(self, index=0):
        """Mark all nodes as unsampled"""
        if index < self.num_items:
            self.tree[index].sampled = False
            self.reset_tree(self.right_index(index))
            self.reset_tree(self.left_index(index))


class WeightedShuffler:

    def __init__(self, items):
        self.all_items = []
        self.total_weight = 0
        for item, weight in items:
            self.total_weight += weight
            self.all_items.append((item, weight))

        self.tree = _BinaryTree(all_items)

    def shuffle(self):
        return self.sample_items(len(self.all_items))

    def sample_items(self, num_samples):
        """Return list of num_samples weighted samples"""
        weight_sum = self.total_weight
        sampled_list = []
        for sample_num in range(0, num_samples):
            rand = random.randint(1, weight_sum)

            sampled_item = self.tree.sample_tree(rand)
            weight_sum -= sampled_item[1]

            sampled_list.append(sampled_item)

        self.tree.reset_tree()
        return sampled_list
