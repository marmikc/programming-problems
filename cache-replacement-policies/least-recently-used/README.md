# Implement a Least Recently Used (LRU) Cache

Within a cache of a given size, if there is a cache miss, and there are no open spots, the cache should evict the item that was least recently used, i.e. accessed the oldest.

## Thought process

A linked list is a great way of storing the order of items, while also supporting O(1) insertion and deletion, provided I use random access via a dictionary into the list. The front of the list would hold the most recently used item, and the end would hold the least.

When there is a cache miss, the item at the end is deleted, and the relevant data is added to the linked list at the front. Where there is a cache hit on an item that is not the head of the list, the item is made the head and other portions of the list are edited accordingly.

This data structure allows O(1) access for cache hits, and in the event of a miss, O(1) insertion (not including complexity to get the data from memory or whatever the cache is accessing during a cache miss).

## Testing

I have written two test files for this LRU cache. 

### Hardcoded Input

The first runs the cache in verbose mode and tests against a memory I wrote. It doesn't automatically determine whether the output of the cache is right, but it serves as a good way to understand what the cache is doing and how it is change between cache calls. Furthermore, it tests important edge cases that I wanted to go through manually and see how the implementation performs.

The below shows some sample output:

<details>
	<summary>
		<p>
			TestLRU_Hardcoded.py Output
		</p>
	</summary>
<p>
	```

	$ python TestLRU_HardcodedInput.py
	Command: get( Apple )
	Cache miss on:  ('Apple', 2)
	('Apple', 2) ->

	Command: get( Apple )
	Cache hit on:  ('Apple', 2)
	('Apple', 2) ->

	Command: get( Grape )
	Cache miss on:  ('Grape', 5)
	('Grape', 5) -> ('Apple', 2) ->

	Command: get( Pea )
	Cache miss on:  ('Pea', 1)
	('Pea', 1) -> ('Grape', 5) -> ('Apple', 2) ->

	Command: get( Apple )
	Cache hit on:  ('Apple', 2)
	('Apple', 2) -> ('Pea', 1) -> ('Grape', 5) ->

	Command: get( Mango )
	Cache miss on:  ('Mango', 6)
	('Mango', 6) -> ('Apple', 2) -> ('Pea', 1) ->

	Command: get( Kiwi )
	Cache miss on:  ('Kiwi', 4)
	('Kiwi', 4) -> ('Mango', 6) -> ('Apple', 2) ->

	Command: get( Apple )
	Cache hit on:  ('Apple', 2)
	('Apple', 2) -> ('Kiwi', 4) -> ('Mango', 6) ->

	Command: get( Mango )
	Cache hit on:  ('Mango', 6)
	('Mango', 6) -> ('Apple', 2) -> ('Kiwi', 4) ->

	Command: get( Apple )
	Cache hit on:  ('Apple', 2)
	('Apple', 2) -> ('Mango', 6) -> ('Kiwi', 4) ->

	Command: get( Pea )
	Cache miss on:  ('Pea', 1)
	('Pea', 1) -> ('Apple', 2) -> ('Mango', 6) ->

	```

</p>
</details>

### Randomized Input

This test file takes a memory and then randomly generates a call to the cache. It picks a key at random and calls the cache on that. It then checks the cache with a correct cache state that this file also builds and maintains. 

The correct cache state is built by using the last n cache calls, where n is the max size of the cache. In other words, it goes from the most recent call to the least recent call and builds what the cache should look like (ignoring any duplicates).

The below shows some sample output when the script is run in verbose mode.

<details>
	<summary>
		<p>
			TestLRU_RandomizedInput.py Output
		</p>
	</summary>
	```

		$ python TestLRU_RandomizedInput.py
		Command: get( Grape )
		Correct State:   [('Grape', 5)]
		Returned State:  [('Grape', 5)]

		Command: get( Mango )
		Correct State:   [('Mango', 6), ('Grape', 5)]
		Returned State:  [('Mango', 6), ('Grape', 5)]

		Command: get( Starfruit )
		Correct State:   [('Starfruit', 3), ('Mango', 6), ('Grape', 5)]
		Returned State:  [('Starfruit', 3), ('Mango', 6), ('Grape', 5)]

		Command: get( Grape )
		Correct State:   [('Grape', 5), ('Starfruit', 3), ('Mango', 6)]
		Returned State:  [('Grape', 5), ('Starfruit', 3), ('Mango', 6)]

		Command: get( Peach )
		Correct State:   [('Peach', 4), ('Grape', 5), ('Starfruit', 3)]
		Returned State:  [('Peach', 4), ('Grape', 5), ('Starfruit', 3)]

		Command: get( Apple )
		Correct State:   [('Apple', 2), ('Peach', 4), ('Grape', 5)]
		Returned State:  [('Apple', 2), ('Peach', 4), ('Grape', 5)]

		Command: get( Kiwi )
		Correct State:   [('Kiwi', 4), ('Apple', 2), ('Peach', 4)]
		Returned State:  [('Kiwi', 4), ('Apple', 2), ('Peach', 4)]

		Command: get( Apple )
		Correct State:   [('Apple', 2), ('Kiwi', 4), ('Peach', 4)]
		Returned State:  [('Apple', 2), ('Kiwi', 4), ('Peach', 4)]

		Command: get( Orange )
		Correct State:   [('Orange', 5), ('Apple', 2), ('Kiwi', 4)]
		Returned State:  [('Orange', 5), ('Apple', 2), ('Kiwi', 4)]

		Command: get( Starfruit )
		Correct State:   [('Starfruit', 3), ('Orange', 5), ('Apple', 2)]
		Returned State:  [('Starfruit', 3), ('Orange', 5), ('Apple', 2)]

		Passed all randomized tests!

	```
</details>