class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        # Runtime: 204 ms
        # Memory: 14.8 MB
        plain = [first]
        for idx, n in enumerate(encoded):
            # c = a ^ b
            # a = b ^ c
            plain.append(n ^ plain[idx])
        return plain
