class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # Runtime: 12 ms
        # Memory: 13.2 MB
        if time[0] == "?":
            if time[1] == "?" or time[1] < "4":
                time = "2" + time[1:]
            else:
                time = "1" + time[1:]
        if time[1] == "?":
            if time[0] == "2":
                time = time[0] + "3" + time[2:]
            else:
                time = time[0] + "9" + time[2:]
        if time[3] == "?":
            time = time[:3] + "5" + time[4]
        if time[4] == "?":
            time = time[:4] + "9"
        return time
