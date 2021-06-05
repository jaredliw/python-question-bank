class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # Runtime: 28 ms
        # Memory: 13.8 MB
        scores = []
        for op in ops:
            if op == "+":
                scores.append(scores[-1] + scores[-2])
            elif op == "D":
                scores.append(scores[-1] * 2)
            elif op == "C":
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)
