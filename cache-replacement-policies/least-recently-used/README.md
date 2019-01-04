# Implement a Least Recently Used (LRU) Cache

Within a cache of a given size, if there is a cache miss, and there are no open spots, the cache should evict the item that was least recently used, i.e. accessed the oldest.

## Thought process

A linked list is a great way of storing the order of items, while also supporting O(1) insertion and deletion, provided I use random access via a dictionary into the list. The front of the list would hold the most recently used item, and the end would hold the least.

When there is a cache miss, the item at the end is deleted, and the relevant data is added to the linked list at the front. Where there is a cache hit on an item that is not the head of the list, the item is made the head and other portions of the list are edited accordingly.

This data structure allows O(1) access for cache hits, and in the event of missed O(1) insertion (not including complexity to get the data from memory or whatever the cache is accessing during a cache miss).