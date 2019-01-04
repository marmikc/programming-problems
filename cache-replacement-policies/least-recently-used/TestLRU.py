import LRU_Cache as lru

memory = {
    "Apple": 2,
    "Grape": 5,
    "Pea": 1,
    "Mango": 6,
    "Kiwi": 4
}

cache = lru.LRU_Cache(memory, 3, True)

# Cache hit on a partially filled cache
# Cache hit on head node
cache.get("Apple")
cache.get("Apple")

# Cache misses on a partially filled cache
cache.get("Grape")
cache.get("Pea")

# Cache hit on full cache
# Cache hit on LRU node
cache.get("Apple")

# Cache misses on a full cache
cache.get("Mango")
cache.get("Kiwi")

# Cache hits on a full cache
cache.get("Apple")
cache.get("Mango")
cache.get("Apple")

# Cache miss
cache.get("Pea")
