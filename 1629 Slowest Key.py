class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        # Runtime: 48 ms
        # Memory: 13.5 MB
        durations = map(lambda idx, x: x if idx == 0 else x - releaseTimes[idx - 1], range(len(releaseTimes)),
                        releaseTimes)
        return max(zip(durations, keysPressed))[1]
