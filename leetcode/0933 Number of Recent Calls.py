class RecentCounter(object):
    # Runtime: 276 ms
    # Memory: 18.1 MB

    # Implement queue using list
    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        # Since t is increasing every time, the values on the very first of the list won't be useful once
        # they < t - 3000
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


from collections import deque


class RecentCounter(object):
    # Runtime: 264 ms
    # Memory: 18.5 MB

    # Implement queue using double ended queue
    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Python 3 only
from queue import Queue


class RecentCounter:
    # Runtime: 612 ms
    # Memory: 19 MB

    # Implement queue using double ended queue.Queue
    def __init__(self):
        self.queue = Queue()

    def ping(self, t: int) -> int:
        self.queue.put(t)
        # Queue object has an attribute "queue", which is the underlying data structure (collection.deque) of Queue
        # you can't call Queue.get without remove the item from the queue
        while self.queue.queue[0] < t - 3000:
            self.queue.get()
        # Error -- len(self.queue)
        # Note: Queue is not iterable
        return self.queue.qsize()

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
