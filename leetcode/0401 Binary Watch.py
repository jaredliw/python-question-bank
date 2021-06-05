class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # Runtime: 20 ms
        # Memory: 13.4 MB
        ans = []
        for hour in range(12):
            for minute in range(60):
                on_leds = (bin(hour) + bin(minute)).count("1")
                if on_leds == num:
                    ans.append("{}:{:0>2}".format(hour, minute))
        return ans
