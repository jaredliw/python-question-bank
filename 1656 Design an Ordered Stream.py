class OrderedStream(object):
    # Runtime: 200 ms
    # Memory: 13.9 MB
    def __init__(self, n):
        """
        :type n: int
        """
        self.stream = [None] * n
        self.pointer = 0

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey - 1] = value

        data = []
        while self.pointer < len(self.stream) and self.stream[self.pointer] is not None:
            data.append(self.stream[self.pointer])
            self.pointer += 1
        return data

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
