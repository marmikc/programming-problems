# Clock Page Replacement Algorithm

Implement a clock page replacement algorithm. Each line in the cache contains the page, and a reference bit. 

If the reference bit is True, and there is a request for that page, there is no page fault.

If the reference bit is False, but the page is present, then upon a request, there is a page fault and the reference bit is set to true.

If the page is not present in the table, then the clock increments, setting all pages with reference bit True, to False along the way, until it finds a page with the reference bit as False. This page is then repalced, the reference bit set to true, and the clock is incremented to the next page.

