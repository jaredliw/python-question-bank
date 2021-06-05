class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        # Runtime: 3808 ms
        # Memory: 13.7 MB

        # Get indices of non-empty boxes
        with_ball = []
        for idx, box in enumerate(boxes):
            if box == "1":
                with_ball.append(idx)

        # For each box, calculate sum(absolute distance between current box and every non-empty box)
        results = []
        for idx in range(len(boxes)):
            results.append(sum(map(lambda x: abs(x - idx), with_ball)))

        return results
