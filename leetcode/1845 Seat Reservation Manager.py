from bisect import insort


class SeatManager(object):
    # Runtime: 5204 ms
    # Memory: 44.1 MB
    def __init__(self, n):
        """
        :type n: int
        """
        self.seats = list(range(1, n + 1))

    def reserve(self):
        """
        :rtype: int
        """
        return self.seats.pop(0)

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        # The function insert the value to the list at an appropriate place so that the list is remained sorted.
        insort(self.seats, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
