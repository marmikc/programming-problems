# Implement a Least Recently Used (LRU) Cache

Within a cache of a given size, if there is a cache miss, and there are no open spots, the cache should evict the item that was least recently used, i.e. accessed the oldest.

## Thought process

I linked list is a great way of storing the order of items, while also supporting O(1) insertion and deletion, provided I use random access via a dictionary into the list. The front of the list would be good to hold 