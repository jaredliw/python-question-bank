class MyHashSet(object):
    # Runtime: 140 ms
    # Memory: 18.7 MB
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashset.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        try:
            self.hashset.remove(key)
        except KeyError:
            pass

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hashset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
