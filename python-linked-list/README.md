# Implement a Linked List in Python

Tutorial and Source: https://www.tutorialspoint.com/python/python_linked_lists.htm

I have not much had the opportunity to work with linked lists in python. This folder is my creating and implmenting one.

## Problem Description:

Given a linked list of an unkown size, and an integer n, return the nth element from the end of the linked list.

The solution to this problem is simple. Maintain two pointers to nodes in the linked list. Increment one pointer so that it is n elements ahead of the other pointer, and then increment both until the end is reached. The node pointed to by the pointer that is behind is the nth element fromt the end.