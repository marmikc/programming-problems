# Clock Page Replacement Algorithm

Implement a clock page replacement algorithm. Each line in the cache contains the page, and a reference bit. 

If the reference bit is True, and there is a request for that page, there is no page fault.

If the reference bit is False, but the page is present, then upon a request, there is a page fault and the reference bit is set to true.

If the page is not present in the table, then the clock increments, setting all pages with reference bit True, to False along the way, until it finds a page with the reference bit as False. This page is then repalced, the reference bit set to true, and the clock is incremented to the next page.

## Tought Process

Using a list with a value that serves as the clock hand, pointing to an index in the list should accomplish the behavior we need.

If the hand ever increments to the end of the list we can make it wrap back around to 0 to maintain the illusion of a "clock". 

## Testing

### Hardcoded Input

I created a test file with hardcoded commands to test the behavior of the clock and to see how it behaves under simple edge cases that I designed. The below shows the output from running the file. 

<details><summary>TestClock.py Output</summary>
<p>

```
$ python TestClock.py
Command: get( Apple )
Page fault on:  ('Apple', 2)
Found:  ('Apple', 2)
Clock State:  -> (('Apple', 2), True) -> **((None, None), False)** -> ((None, None), False) ->

Command: get( Apple )
Found:  ('Apple', 2)
Clock State:  -> (('Apple', 2), True) -> **((None, None), False)** -> ((None, None), False) ->

Command: get( Grape )
Page fault on:  ('Grape', 5)
Found:  ('Grape', 5)
Clock State:  -> (('Apple', 2), True) -> (('Grape', 5), True) -> **((None, None), False)** ->

Command: get( Pea )
Page fault on:  ('Pea', 1)
Found:  ('Pea', 1)
Clock State:  -> **(('Apple', 2), True)** -> (('Grape', 5), True) -> (('Pea', 1), True) ->

Command: get( Apple )
Found:  ('Apple', 2)
Clock State:  -> **(('Apple', 2), True)** -> (('Grape', 5), True) -> (('Pea', 1), True) ->

Command: get( Mango )
Page fault on:  ('Mango', 6)
Evicting:  ('Apple', 2)
Found:  ('Mango', 6)
Clock State:  -> (('Mango', 6), True) -> **(('Grape', 5), False)** -> (('Pea', 1), False) ->

Command: get( Pea )
Found:  ('Pea', 1)
Clock State:  -> (('Mango', 6), True) -> **(('Grape', 5), False)** -> (('Pea', 1), True) ->

Command: get( Apple )
Page fault on:  ('Apple', 2)
Evicting:  ('Grape', 5)
Found:  ('Apple', 2)
Clock State:  -> (('Mango', 6), True) -> (('Apple', 2), True) -> **(('Pea', 1), True)** ->

Command: get( Mango )
Found:  ('Mango', 6)
Clock State:  -> (('Mango', 6), True) -> (('Apple', 2), True) -> **(('Pea', 1), True)** ->

Command: get( Fish )
Page fault on:  ('Fish', 0)
Evicting:  ('Pea', 1)
Found:  ('Fish', 0)
Clock State:  -> **(('Mango', 6), False)** -> (('Apple', 2), False) -> (('Fish', 0), True) ->

Command: get( Pea )
Page fault on:  ('Pea', 1)
Evicting:  ('Mango', 6)
Found:  ('Pea', 1)
Clock State:  -> (('Pea', 1), True) -> **(('Apple', 2), False)** -> (('Fish', 0), True) ->

Final clock state:  -> (('Pea', 1), True) -> **(('Apple', 2), False)** -> (('Fish', 0), True) ->
```

</p>
</details>